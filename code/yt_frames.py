"""Pull still frames out of a YouTube video so the numbers on screen can be read.

The companion to yt_transcript.py, and it exists because of that script's stated
limitation: hardware reviewers put their FPS tables in on-screen graphs, so a
commentary-free benchmark video has a transcript containing nothing at all. The
data is in the pixels. This fetches the pixels.

    PYTHONUTF8=1 venv/Scripts/python.exe code/yt_frames.py <url-or-id> -t 10:38 [-t 4:07 ...]

Options:
    -t, --at TIME      timestamp to grab, mm:ss / hh:mm:ss / seconds. Repeatable.
    -o, --out DIR      output directory, default the current one
    --window SECONDS   seconds of video to fetch around each timestamp, default 6
    --height PIXELS    cap the video height, default 1080

Each timestamp yields <out>/<video-id>_<timestamp>.png. Read those with the Read
tool - they are images, and reading a bar chart directly beats OCR on one.

Why it downloads a slice rather than the whole file: yt-dlp's --download-sections
fetches only the requested range, so a 10-second grab off a 16-minute video is
~150KB and takes two seconds. Keep it to the frames actually needed.

Requires imageio-ffmpeg (in requirements.txt) - it ships a static ffmpeg binary,
because ffmpeg is not on PATH on this machine and Windows has no package for it.

Chapter lists from yt_transcript.py are where the useful timestamps come from:
benchmark channels almost always end on an "Average result" chart, and each game
has its own chapter mark. Grab the average first, then individual games only if
the average is ambiguous or the direction of the comparison is unclear.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ID_RE = re.compile(r"(?:v=|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})")

# The default (tv/web) client is unreliable for automated access; the android
# client still serves plain progressive/DASH streams. Same reasoning as
# yt_transcript.py - keep the two in step if one has to change.
CLIENT_ARGS = "youtube:player_client=android"


def video_id(arg):
    """Accept a full URL or a bare 11-character id."""
    match = ID_RE.search(arg)
    if match:
        return match.group(1)
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", arg):
        return arg
    sys.exit(f"not a YouTube URL or video id: {arg}")


def parse_time(text):
    """mm:ss, hh:mm:ss or plain seconds -> seconds."""
    parts = text.split(":")
    if not all(p.strip().isdigit() for p in parts) or len(parts) > 3:
        sys.exit(f"bad timestamp: {text}")
    seconds = 0
    for part in parts:
        seconds = seconds * 60 + int(part)
    return seconds


def ffmpeg_exe():
    try:
        import imageio_ffmpeg
    except ImportError:
        sys.exit(
            "imageio-ffmpeg is not installed in this venv.\n"
            "  venv/Scripts/python.exe -m pip install --trusted-host pypi.org "
            "--trusted-host files.pythonhosted.org imageio-ffmpeg"
        )
    return imageio_ffmpeg.get_ffmpeg_exe()


def stamp_label(seconds):
    return f"{seconds // 60:02d}m{seconds % 60:02d}s"


def grab(vid, seconds, out_dir, ffmpeg, window, height):
    """Download a short slice around `seconds` and write one frame from its middle."""
    clip = out_dir / f".{vid}_{stamp_label(seconds)}.mp4"
    start = max(0, seconds - window // 2)
    end = seconds + window // 2

    fetch = [
        sys.executable, "-m", "yt_dlp",
        "--extractor-args", CLIENT_ARGS,
        "--ffmpeg-location", ffmpeg,
        "-f", f"bv*[height<={height}]",
        "--download-sections", f"*{start}-{end}",
        "-o", str(clip),
        "--quiet", "--no-warnings",
        vid,
    ]
    proc = subprocess.run(fetch, capture_output=True, text=True,
                          encoding="utf-8", errors="replace")
    if proc.returncode != 0 or not clip.exists():
        print(f"  failed at {stamp_label(seconds)}: "
              f"{(proc.stderr or proc.stdout).strip().splitlines()[-1:] or 'no output'}")
        return None

    # Seek to the requested moment inside the slice rather than its first frame:
    # the slice starts early by window//2, and the first frame of a cut stream is
    # often a partial keyframe.
    png = out_dir / f"{vid}_{stamp_label(seconds)}.png"
    extract = [
        ffmpeg, "-y", "-loglevel", "error",
        "-ss", str(seconds - start),
        "-i", str(clip),
        "-frames:v", "1",
        str(png),
    ]
    subprocess.run(extract, capture_output=True, text=True,
                   encoding="utf-8", errors="replace")
    clip.unlink(missing_ok=True)

    if not png.exists():
        print(f"  no frame written at {stamp_label(seconds)}")
        return None
    return png


def main():
    parser = argparse.ArgumentParser(
        description="Grab still frames from a YouTube video at given timestamps.")
    parser.add_argument("video", help="YouTube URL or 11-character video id")
    parser.add_argument("-t", "--at", action="append", required=True, metavar="TIME",
                        help="timestamp to grab (mm:ss, hh:mm:ss or seconds); repeatable")
    parser.add_argument("-o", "--out", default=".", metavar="DIR",
                        help="output directory (default: current)")
    parser.add_argument("--window", type=int, default=6, metavar="SECONDS",
                        help="seconds of video fetched around each timestamp (default: 6)")
    parser.add_argument("--height", type=int, default=1080, metavar="PIXELS",
                        help="cap video height (default: 1080)")
    args = parser.parse_args()

    vid = video_id(args.video)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    ffmpeg = ffmpeg_exe()

    written = []
    for text in args.at:
        seconds = parse_time(text)
        png = grab(vid, seconds, out_dir, ffmpeg, args.window, args.height)
        if png:
            print(f"wrote {png}")
            written.append(png)

    if not written:
        sys.exit("no frames written")


if __name__ == "__main__":
    main()
