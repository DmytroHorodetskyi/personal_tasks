"""Pull a YouTube video's captions and metadata as plain text.

Written for the pc_build task: hardware reviewers (Hardware Unboxed, Gamers Nexus,
Monitors Unboxed) publish their conclusions in video only, and this makes that text
readable. No API key and no Google account - it reads the same auto-generated caption
track the YouTube player uses.

    PYTHONUTF8=1 venv/Scripts/python.exe code/yt_transcript.py <url-or-id> [...]

Options:
    --lang en          caption language prefix, default en (try uk, de, ...)
    --stamp 30         seconds between [mm:ss] markers in the body, 0 to drop them
    --no-body          metadata, chapters and description only - no transcript
    -o FILE            write to FILE instead of stdout (one file per video if several)

What it does not give you: the numbers on screen. Review videos put their FPS tables in
graphs, so the transcript carries the commentary and the verdict, not the bar charts.
Read the transcript for the reasoning, then confirm figures against the written outlets
listed in tasks/hardware/pc_build/tools.md.
"""

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# The default (tv/web) client no longer serves caption tracks - it fails with
# "The page needs to be reloaded". The android client still does.
CLIENT_ARGS = "youtube:player_client=android"

TAG_RE = re.compile(r"<[^>]*>")
CUE_RE = re.compile(r"^(\d\d:\d\d:\d\d\.\d\d\d)\s+-->\s+(\d\d:\d\d:\d\d\.\d\d\d)")


def run_ytdlp(args):
    cmd = [sys.executable, "-m", "yt_dlp", "--extractor-args", CLIENT_ARGS] + args
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
        raise SystemExit("yt-dlp failed: " + cmd[-1])
    return proc.stdout


def fetch_meta(url):
    out = run_ytdlp(["--skip-download", "--dump-single-json", "--no-warnings", url])
    return json.loads(out)


def fetch_vtt(url, lang, workdir):
    run_ytdlp([
        "--skip-download", "--no-warnings",
        "--write-auto-subs", "--write-subs",
        "--sub-langs", "%s.*" % lang, "--sub-format", "vtt/best",
        "-o", str(Path(workdir) / "%(id)s.%(ext)s"),
        url,
    ])
    files = sorted(Path(workdir).glob("*.vtt"))
    if not files:
        return None
    # Prefer the human track (".en.vtt") over the ASR original (".en-orig.vtt").
    files.sort(key=lambda p: ("-orig" in p.name, len(p.name)))
    return files[0].read_text(encoding="utf-8")


def parse_vtt(text):
    """VTT cues -> [(seconds, line)], with the rolling duplicates dropped.

    Auto-captions repeat the previous line at the top of every cue so the player can
    scroll two lines at a time; keeping them triples the file and breaks sentences.
    """
    out = []
    seen_tail = None
    start = None
    for raw in text.splitlines():
        m = CUE_RE.match(raw.strip())
        if m:
            h, mi, s = m.group(1).split(":")
            start = int(h) * 3600 + int(mi) * 60 + float(s)
            continue
        if start is None or not raw.strip():
            continue
        if raw.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        line = TAG_RE.sub("", raw).strip()
        if not line or line == seen_tail:
            continue
        seen_tail = line
        out.append((start, line))
    return out


def render_body(lines, stamp):
    chunks, buf, mark = [], [], None
    for sec, line in lines:
        if mark is None:
            mark = sec
        buf.append(line)
        if stamp and sec - mark >= stamp:
            chunks.append((mark, " ".join(buf)))
            buf, mark = [], None
    if buf:
        chunks.append((mark or 0, " ".join(buf)))
    if not stamp:
        return "\n\n".join(t for _, t in chunks)
    return "\n\n".join("[%s] %s" % (hhmm(s), t) for s, t in chunks)


def hhmm(sec):
    sec = int(sec)
    return "%d:%02d:%02d" % (sec // 3600, sec % 3600 // 60, sec % 60) if sec >= 3600 \
        else "%d:%02d" % (sec // 60, sec % 60)


def render(meta, body):
    parts = ["# %s" % meta.get("title", "?"), ""]
    parts.append("%s | %s | %s | %s views" % (
        meta.get("uploader", "?"),
        meta.get("upload_date", "?"),
        hhmm(meta.get("duration") or 0),
        meta.get("view_count", "?"),
    ))
    parts.append(meta.get("webpage_url", ""))
    chapters = meta.get("chapters") or []
    if chapters:
        parts += ["", "## Chapters", ""]
        parts += ["- %s %s" % (hhmm(c.get("start_time") or 0), c.get("title", "")) for c in chapters]
    desc = (meta.get("description") or "").strip()
    if desc:
        parts += ["", "## Description", "", desc]
    if body:
        parts += ["", "## Transcript", "", body]
    return "\n".join(parts) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("urls", nargs="+")
    ap.add_argument("--lang", default="en")
    ap.add_argument("--stamp", type=int, default=30)
    ap.add_argument("--no-body", action="store_true")
    ap.add_argument("-o", dest="out")
    a = ap.parse_args()

    for i, url in enumerate(a.urls):
        meta = fetch_meta(url)
        body = ""
        if not a.no_body:
            with tempfile.TemporaryDirectory() as tmp:
                vtt = fetch_vtt(url, a.lang, tmp)
            if vtt is None:
                sys.stderr.write("no %s captions for %s\n" % (a.lang, meta.get("id")))
            else:
                body = render_body(parse_vtt(vtt), a.stamp)
        text = render(meta, body)
        if a.out:
            path = Path(a.out)
            if len(a.urls) > 1:
                path = path.with_name("%s_%d%s" % (path.stem, i + 1, path.suffix))
            path.write_text(text, encoding="utf-8")
            print("wrote %s (%d chars)" % (path, len(text)))
        else:
            sys.stdout.write(text)


if __name__ == "__main__":
    main()
