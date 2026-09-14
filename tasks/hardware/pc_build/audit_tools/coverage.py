"""Prove a transcript was READ, not merely measured.

    PYTHONUTF8=1 venv/Scripts/python.exe tasks/hardware/pc_build/audit_tools/coverage.py
    ...                                                                   --missing <videoid>
    ...                                                                   --emit

Why this exists
---------------
`measure.py` prints how long a transcript body is.  That number can be pasted into an audit
row by an agent that never opened the file, which is exactly what happened on 2026-09-13:
four rows carried "31 598 / 31 598" and similar after the body had only been sampled with
grep windows and head+tail.  `verify_audit.py` passed all four, because a char count is
evidence that a file was *measured*, not that it was *read*.

This module derives the other half from evidence the agent cannot fabricate without doing
the work: **the raw .jsonl session transcripts record every tool result, so they record
every line of every file that was ever actually printed into the context.**  A line the
agent never printed is a line the agent never saw.

Method
------
1. Walk every `*.jsonl` in the project's session directory and collect the text of every
   **tool result** - and only tool results.  Assistant prose and tool *inputs* are ignored
   on purpose: text the agent wrote must never count as evidence that the agent read it.
2. Split that text into lines and index each one under a normalised key: whitespace
   collapsed, any `123|` / `123->` line-number gutter stripped, truncated to KEY_LEN chars.
   KEY_LEN is short enough to survive output truncation and long enough to be unique across
   prose lines that begin with a `[mm:ss]` timestamp.
3. For each transcript under `sources/`, take the body after the `## Transcript` marker and
   look up every non-blank line.  Lines found in the index were printed at some point;
   lines not found were never on screen.
4. `chars_read` is the summed length of the lines that were actually printed.  For a full
   read it equals the body length; for a grep window it is a fraction of it.

False negatives are possible (a line re-wrapped by some tool would not match) and are the
safe direction - they under-report coverage and fail loudly.  False positives are not
reachable without the content having been printed.
"""

import glob
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SOURCES = os.path.join(ROOT, "sources")
TRANSCRIPTS = os.path.expanduser(
    r"~\.claude\projects\C--Users-Dmitriy-Documents-GitHub-personal-tasks"
)

BODY_MARK = "\n## Transcript\n\n"
KEY_LEN = 60
GUTTER = re.compile(r"^\s*\d+(?:\||→|->|\t)")
WS = re.compile(r"\s+")


def key(line):
    """Normalised lookup key for one line, or None if it is too short to identify."""
    line = GUTTER.sub("", line)
    line = WS.sub(" ", line).strip()
    if len(line) < 20:
        return None
    return line[:KEY_LEN]


def _texts(rec):
    """Yield every tool-result text in one .jsonl record. Tool results only."""
    msg = rec.get("message") or {}
    content = msg.get("content")
    if isinstance(content, list):
        for block in content:
            if not isinstance(block, dict) or block.get("type") != "tool_result":
                continue
            inner = block.get("content")
            if isinstance(inner, str):
                yield inner
            elif isinstance(inner, list):
                for sub in inner:
                    if isinstance(sub, dict) and sub.get("type") == "text":
                        yield sub.get("text", "")
    # Claude Code also parks structured tool output here; still tool output, never authored
    # by the agent, so it counts.
    extra = rec.get("toolUseResult")
    if isinstance(extra, str):
        yield extra
    elif isinstance(extra, dict):
        for field in ("stdout", "content", "text", "output", "file"):
            val = extra.get(field)
            if isinstance(val, str):
                yield val
            elif isinstance(val, dict) and isinstance(val.get("content"), str):
                yield val["content"]


def printed_keys():
    """Every line ever printed into the context by a tool, as a set of normalised keys."""
    if not os.path.isdir(TRANSCRIPTS):
        sys.exit("2: transcript directory not found: %s" % TRANSCRIPTS)
    seen = set()
    for path in sorted(glob.glob(os.path.join(TRANSCRIPTS, "*.jsonl"))):
        with io.open(path, encoding="utf-8", errors="replace") as fh:
            for raw in fh:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    rec = json.loads(raw)
                except ValueError:
                    continue
                for text in _texts(rec):
                    if not text:
                        continue
                    for line in text.split("\n"):
                        k = key(line)
                        if k:
                            seen.add(k)
    return seen


def body_lines(path):
    """The non-blank lines of one transcript's body, with the body's full char length."""
    text = io.open(path, encoding="utf-8").read()
    i = text.find(BODY_MARK)
    body = "" if i < 0 else text[i + len(BODY_MARK):].strip()
    lines = [ln for ln in body.split("\n") if ln.strip()]
    return lines, len(body)


def coverage(seen=None):
    """{video id: dict(file, total_chars, read_chars, lines, hit, missing)}"""
    if seen is None:
        seen = printed_keys()
    out = {}
    for path in sorted(glob.glob(os.path.join(SOURCES, "*.md"))):
        name = os.path.basename(path)
        stem = os.path.splitext(name)[0]
        if "_" not in stem:
            continue
        # Files are <component>_<videoid>.md and no component prefix contains an
        # underscore, but plenty of video ids do ("7_xjpBYwm5g", "-8LMML_EiMg"), so this
        # must split on the FIRST underscore, not the last.
        vid = stem.split("_", 1)[1]
        if len(vid) != 11:
            continue
        lines, total = body_lines(path)
        hit, read_chars, missing = 0, 0, []
        for n, line in enumerate(lines, 1):
            k = key(line)
            if k is None or k in seen:
                # A line too short to key is counted as covered: it carries no evidence
                # either way and refusing it would punish a genuine read.
                hit += 1
                read_chars += len(line)
            else:
                missing.append(n)
        # the body length includes the newlines between lines; fold them in proportionally
        if lines and hit == len(lines):
            read_chars = total
        out[vid] = dict(file=name, total_chars=total, read_chars=read_chars,
                        lines=len(lines), hit=hit, missing=missing)
    return out


def per_session():
    """{session id: set of keys} - one index per .jsonl, to ask a stricter question.

    The union check ("was this line ever printed?") can be satisfied by lines scattered
    across sessions months apart, which is not the same as one agent reading one file.
    This lets the caller ask whether any SINGLE session printed a whole body.
    """
    out = {}
    for path in sorted(glob.glob(os.path.join(TRANSCRIPTS, "*.jsonl"))):
        keys = set()
        with io.open(path, encoding="utf-8", errors="replace") as fh:
            for raw in fh:
                raw = raw.strip()
                if not raw:
                    continue
                try:
                    rec = json.loads(raw)
                except ValueError:
                    continue
                for text in _texts(rec):
                    if not text:
                        continue
                    for line in text.split("\n"):
                        k = key(line)
                        if k:
                            keys.add(k)
        out[os.path.basename(path)[:8]] = keys
    return out


def main(argv):
    if "--by-session" in argv:
        sess = per_session()
        split = 0
        for path in sorted(glob.glob(os.path.join(SOURCES, "*.md"))):
            base = os.path.basename(path)
            lines, _ = body_lines(path)
            keys = [key(l) for l in lines]
            best, best_hit = None, -1
            for name, sk in sess.items():
                hit = sum(1 for k in keys if k is None or k in sk)
                if hit > best_hit:
                    best, best_hit = name, hit
            whole = best_hit == len(lines)
            if not whole:
                split += 1
            print("%s %-34s %s %d/%d lines"
                  % ("ONE " if whole else "SPLIT", base, best, best_hit, len(lines)))
        print("")
        print("%d transcripts; %d read whole inside a single session, %d only across sessions"
              % (len(glob.glob(os.path.join(SOURCES, "*.md"))),
                 len(glob.glob(os.path.join(SOURCES, "*.md"))) - split, split))
        return 0

    if "--missing" in argv:
        vid = argv[argv.index("--missing") + 1]
        info = coverage().get(vid)
        if not info:
            sys.exit("no transcript for %s" % vid)
        print("%s  %s" % (vid, info["file"]))
        print("lines %d/%d covered, %d chars of %d"
              % (info["hit"], info["lines"], info["read_chars"], info["total_chars"]))
        if info["missing"]:
            print("never printed, body line numbers: %s"
                  % ", ".join(str(n) for n in info["missing"]))
            print("read them with:")
            print("  sed -n '/^## Transcript/,$p' %s | sed -n '%d,%dp'"
                  % (os.path.join("tasks/hardware/pc_build/sources", info["file"]),
                     info["missing"][0], info["missing"][-1]))
        else:
            print("fully covered")
        return 0

    cov = coverage()
    if "--emit" in argv:
        # The pair an audit row is allowed to claim, derived from evidence rather than
        # copied from measure.py.
        for vid in sorted(cov, key=lambda v: cov[v]["file"]):
            c = cov[vid]
            print("%-12s %-34s %s / %s"
                  % (vid, c["file"], "{:,}".format(c["read_chars"]).replace(",", " "),
                     "{:,}".format(c["total_chars"]).replace(",", " ")))
        return 0

    bad = 0
    for vid in sorted(cov, key=lambda v: cov[v]["file"]):
        c = cov[vid]
        pct = 100.0 if not c["lines"] else 100.0 * c["hit"] / c["lines"]
        flag = "OK  " if pct >= 100.0 else "GAP "
        if pct < 100.0:
            bad += 1
        print("%s%-12s %-34s %5.1f%%  %d/%d lines  %d/%d chars"
              % (flag, vid, c["file"], pct, c["hit"], c["lines"],
                 c["read_chars"], c["total_chars"]))
    print("")
    print("%d transcripts, %d with unread lines" % (len(cov), bad))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
