"""Bulk-fetch transcripts for a list of video IDs, trying en -> uk -> ru.

    PYTHONUTF8=1 venv/Scripts/python.exe fetch_all.py <outdir> <id> [<id> ...]

Writes <outdir>/<id>.md and prints "<id>\t<lang>\t<chars>\t<title>".

A HTTP 429 (rate limit) must NEVER be recorded as "no caption track" - that is the
whole point of the audit this feeds.  On 429 the script backs off and retries, and if
it still cannot tell, it writes nothing and prints RATELIMIT so the id is re-run.
"""
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

CODE = Path(r"C:\Users\Dmitriy\Documents\GitHub\personal_tasks\code")
sys.path.insert(0, str(CODE))
import yt_transcript as yt

PAUSE = 4.0          # polite gap between videos
BACKOFF = [30, 90, 240]


class RateLimited(Exception):
    pass


def ytdlp(args):
    """Like yt_transcript.run_ytdlp but hands back stderr instead of swallowing it."""
    cmd = [sys.executable, "-m", "yt_dlp", "--extractor-args", yt.CLIENT_ARGS] + args
    p = subprocess.run(cmd, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    return p.returncode, p.stdout, p.stderr or ""


def is_429(text):
    return "429" in text or "Too Many Requests" in text


def fetch_vtt_checked(url, lang, workdir):
    """Return vtt text, or None for a genuine absence.  Raise RateLimited on 429."""
    rc, _, err = ytdlp([
        "--skip-download", "--no-warnings",
        "--write-auto-subs", "--write-subs",
        "--sub-langs", "%s.*" % lang, "--sub-format", "vtt/best",
        "-o", str(Path(workdir) / "%(id)s.%(ext)s"),
        url,
    ])
    files = sorted(Path(workdir).glob("*.vtt"))
    if not files:
        if is_429(err):
            raise RateLimited(err.strip().splitlines()[-1:])
        return None
    files.sort(key=lambda p: ("-orig" in p.name, len(p.name)))
    return files[0].read_text(encoding="utf-8")


def meta_checked(url):
    for i, wait in enumerate([0] + BACKOFF):
        if wait:
            time.sleep(wait)
        rc, out, err = ytdlp(["--skip-download", "--dump-single-json", "--no-warnings", url])
        if rc == 0:
            import json
            return json.loads(out)
        if not is_429(err):
            raise RuntimeError(err.strip().splitlines()[-1] if err.strip() else "yt-dlp failed")
    raise RateLimited("metadata")


def body_len(text):
    marker = "\n## Transcript\n\n"
    i = text.find(marker)
    return 0 if i < 0 else len(text[i + len(marker):].strip())


def one(vid, outdir):
    dest = outdir / (vid + ".md")
    if dest.exists() and dest.stat().st_size > 0:
        t = dest.read_text(encoding="utf-8")
        return "%s\tCACHED\t%d\t%s" % (vid, body_len(t), t.splitlines()[0][2:])

    url = "https://www.youtube.com/watch?v=" + vid
    meta = meta_checked(url)

    best, best_lang = "", "none"
    for lang in ("en", "uk", "ru"):
        vtt = None
        for attempt, wait in enumerate([0] + BACKOFF):
            if wait:
                time.sleep(wait)
            try:
                with tempfile.TemporaryDirectory() as tmp:
                    vtt = fetch_vtt_checked(url, lang, tmp)
                break                      # got an answer (text or a genuine None)
            except RateLimited:
                if attempt == len(BACKOFF):
                    raise
        if vtt:
            best, best_lang = yt.render_body(yt.parse_vtt(vtt), 30), lang
            break

    text = yt.render(meta, best)
    dest.write_text(text, encoding="utf-8")
    return "%s\t%s\t%d\t%s" % (vid, best_lang, body_len(text), meta.get("title", "?"))


def main():
    outdir = Path(sys.argv[1])
    outdir.mkdir(parents=True, exist_ok=True)
    for vid in sys.argv[2:]:
        try:
            print(one(vid, outdir))
        except RateLimited as e:
            print("%s\tRATELIMIT\t-1\t%s" % (vid, e))
            time.sleep(BACKOFF[-1])
        except Exception as e:
            print("%s\tERROR\t-1\t%s" % (vid, e))
        sys.stdout.flush()
        time.sleep(PAUSE)


main()
