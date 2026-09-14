"""Verify that the source audit actually covers every video Dmytro ever sent.

This is the only thing that closes the audit task.  It takes no arguments and trusts no
list written by hand - it re-derives the video inventory from the raw session transcripts
every time it runs.

    PYTHONUTF8=1 venv/Scripts/python.exe tasks/hardware/pc_build/verify_audit.py

For each video id it checks, in order:

  a. the id is one of the ids derived from the .jsonl session transcripts (user turns only)
  b. a transcript file for it exists under sources/, and its body is measured here - not
     taken from anything the audit claims
  c. source_audit.md carries at least one row for the id whose "chars read" equals the
     measured "chars total" (a body of 0 is allowed only when the row says so explicitly)
  d. every row for that id has a non-empty evidence cell - a quote or a frames/ path
  e. THE BODY WAS ACTUALLY READ - every non-blank line of the transcript appears in some
     tool result in the raw .jsonl session logs.  See audit_tools/coverage.py.
  f. one line per video is printed: ID  PASS|FAIL  reason
  g. totals are printed and the process exits non-zero if any video fails

Why (e) exists
--------------
Checks (c) and (d) can both be satisfied by an agent that never opened the file: the char
count comes from measure.py and a quote comes from a grep window.  That happened on
2026-09-13 - four rows claimed a full read after the body had only been sampled - and this
script passed all four.  A char count is evidence that a file was measured, not read.
Check (e) closes that hole with evidence the agent cannot fabricate without doing the work.

    --no-coverage   skip (e).  Only for running this where the session logs are absent;
                    it downgrades the script to what it was before, which was not enough.

Exit codes: 0 = every video passes, 1 = at least one fails, 2 = the audit file or the
transcript directory is missing.
"""

import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCES = os.path.join(HERE, "sources")
FRAMES = os.path.join(HERE, "frames")
AUDIT = os.path.join(HERE, "source_audit.md")
TRANSCRIPTS = os.path.expanduser(
    r"~\.claude\projects\C--Users-Dmitriy-Documents-GitHub-personal-tasks"
)

YT = re.compile(
    r"(?:youtube\.com/(?:watch\?(?:[^\s\"'<>]*&)?v=|embed/|shorts/|live/)|youtu\.be/)"
    r"([A-Za-z0-9_-]{11})"
)
URL = re.compile(r"https?://[^\s\)\]\"'<>,]+")
BODY_MARK = "\n## Transcript\n\n"

# "12 345 / 12 345", "0 / 0", "**16 871 / 16 871**" - thousands separated by spaces.
PAIR = re.compile(r"(\d[\d\s ]*)\s*/\s*(\d[\d\s ]*)")
NO_TRACK = re.compile(r"no caption track|0 chars|no captions", re.I)
FRAME_PATH = re.compile(r"frames/[\w.\-]+\.png")


def num(text):
    return int(re.sub(r"[\s ]", "", text))


def derive_ids():
    """Re-derive every YouTube id the user sent, from the raw session transcripts."""
    if not os.path.isdir(TRANSCRIPTS):
        sys.exit("2: transcript directory not found: %s" % TRANSCRIPTS)
    ids, order = set(), []
    for path in sorted(glob.glob(os.path.join(TRANSCRIPTS, "*.jsonl"))):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue
                if rec.get("type") != "user" or rec.get("toolUseResult") is not None:
                    continue
                msg = rec.get("message") or {}
                if msg.get("role") != "user":
                    continue
                content = msg.get("content")
                if isinstance(content, str):
                    text = content
                elif isinstance(content, list):
                    text = "\n".join(
                        b.get("text", "")
                        for b in content
                        if isinstance(b, dict) and b.get("type") == "text"
                    )
                else:
                    continue
                for url in URL.findall(text):
                    match = YT.search(url.rstrip(".,;:"))
                    if match and match.group(1) not in ids:
                        ids.add(match.group(1))
                        order.append(match.group(1))
    return order


def transcript_body(vid):
    """(path, body_chars) for the id's transcript under sources/, or (None, None)."""
    hits = sorted(glob.glob(os.path.join(SOURCES, "*%s*.md" % vid)))
    if not hits:
        return None, None
    text = open(hits[0], encoding="utf-8").read()
    i = text.find(BODY_MARK)
    body = "" if i < 0 else text[i + len(BODY_MARK):].strip()
    return os.path.basename(hits[0]), len(body)


def audit_rows():
    """{video id: [ (chars_read, chars_total, evidence_cell, whole_row), ... ]}"""
    if not os.path.isfile(AUDIT):
        sys.exit("2: audit file not found: %s" % AUDIT)
    rows = {}
    for line in open(AUDIT, encoding="utf-8"):
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 4:
            continue
        found = re.findall(r"`([A-Za-z0-9_-]{11})`", cells[0])
        if not found:
            continue
        pair = PAIR.search(cells[1])
        if not pair:
            continue
        read, total = num(pair.group(1)), num(pair.group(2))
        rows.setdefault(found[0], []).append((read, total, cells[2], line.strip()))
    return rows


def load_coverage():
    """{vid: info} from audit_tools/coverage.py, or None if it is unavailable."""
    sys.path.insert(0, os.path.join(HERE, "audit_tools"))
    try:
        import coverage
    except ImportError:
        return None
    return coverage.coverage()


def main():
    ids = derive_ids()
    rows = audit_rows()
    want_cov = "--no-coverage" not in sys.argv
    cov = load_coverage() if want_cov else None
    if want_cov and cov is None:
        sys.exit("2: audit_tools/coverage.py not importable; run with --no-coverage to skip"
                 " the read check, knowing that it is the check that matters")

    results = []
    for vid in ids:
        fname, body = transcript_body(vid)
        if fname is None:
            results.append((vid, False, "no transcript in sources/"))
            continue

        mine = rows.get(vid)
        if not mine:
            results.append((vid, False, "no row in source_audit.md (%d chars on disk)" % body))
            continue

        # (d) every row for this id must carry evidence: a quote or a frames/ path.
        blank = [r for r in mine if not r[2] or len(r[2]) < 3]
        if blank:
            results.append((vid, False, "%d row(s) with an empty evidence cell" % len(blank)))
            continue
        for read, total, cell, raw in mine:
            has_quote = '"' in cell or "*" in cell or "«" in cell
            has_frame = FRAME_PATH.search(cell) or FRAME_PATH.search(raw)
            if not (has_quote or has_frame):
                results.append((vid, False, "row with neither a quote nor a frames/ path"))
                break
        else:
            # (e) the body must actually have been printed into a context at some point.
            # This runs before (c) because a row's char count is worthless if the file was
            # never read - that is the whole reason this check exists.
            if cov is not None and body > 0:
                info = cov.get(vid)
                if info is None:
                    results.append((vid, False, "no coverage record for the transcript"))
                    continue
                if info["hit"] < info["lines"]:
                    gap = info["lines"] - info["hit"]
                    results.append((vid, False,
                                    "NOT READ: %d of %d body lines never printed "
                                    "(%d/%d chars) - coverage.py --missing %s"
                                    % (gap, info["lines"], info["read_chars"],
                                       info["total_chars"], vid)))
                    continue

            # (c) at least one row must claim the full body, measured against disk.
            full = [r for r in mine if r[0] == r[1] == body]
            if full:
                if body == 0:
                    explicit = any(NO_TRACK.search(r[3]) for r in mine)
                    if not explicit:
                        results.append((vid, False,
                                        "0 chars but no explicit 'no caption track' note"))
                        continue
                    results.append((vid, True, "0 chars, no caption track (%s)" % fname))
                else:
                    results.append((vid, True, "%d/%d chars read (%s)" % (body, body, fname)))
            else:
                claimed = ", ".join("%d/%d" % (r[0], r[1]) for r in mine[:3])
                results.append((vid, False,
                                "audit says %s, transcript on disk is %d chars"
                                % (claimed, body)))

    width = max(len(v) for v in ids)
    for vid, ok, why in results:
        print("%-*s  %-4s  %s" % (width, vid, "PASS" if ok else "FAIL", why))

    passed = sum(1 for _, ok, _ in results if ok)
    total = len(results)
    print("")
    print("videos derived from transcripts : %d" % len(ids))
    print("transcripts present in sources/ : %d"
          % sum(1 for v in ids if transcript_body(v)[0]))
    print("frames on disk                  : %d"
          % len(glob.glob(os.path.join(FRAMES, "*.png"))))
    if cov is None:
        print("read-coverage check            : SKIPPED (--no-coverage)")
    else:
        gaps = sum(1 for c in cov.values() if c["hit"] < c["lines"])
        print("bodies proven read end to end  : %d of %d"
              % (len(cov) - gaps, len(cov)))
    print("")
    print("%d/%d PASS" % (passed, total))
    if passed != total:
        print("AUDIT NOT FINISHED - %d video(s) failing" % (total - passed))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
