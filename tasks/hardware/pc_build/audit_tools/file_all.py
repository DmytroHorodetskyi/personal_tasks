"""Copy every staged transcript into sources/ under its GROUPS.tsv prefix.

    PYTHONUTF8=1 venv/Scripts/python.exe file_all.py <rawdir>

Idempotent: skips an id that already has a file in sources/.
"""
import glob
import io
import os
import shutil
import sys

ROOT = r"C:\Users\Dmitriy\Documents\GitHub\personal_tasks\tasks\hardware\pc_build"
SOURCES = os.path.join(ROOT, "sources")
GROUPS = os.path.join(SOURCES, "GROUPS.tsv")

prefix = {}
for line in io.open(GROUPS, encoding="utf-8"):
    if line.startswith("#") or not line.strip():
        continue
    parts = line.rstrip("\n").split("\t")
    if len(parts) >= 2:
        prefix[parts[1]] = parts[0]

raw = sys.argv[1]
copied = skipped = missing = 0
for vid, pre in sorted(prefix.items()):
    if glob.glob(os.path.join(SOURCES, "*%s*.md" % vid)):
        skipped += 1
        continue
    src = os.path.join(raw, vid + ".md")
    if not os.path.isfile(src):
        print("MISSING staged transcript: %s" % vid)
        missing += 1
        continue
    shutil.copyfile(src, os.path.join(SOURCES, "%s_%s.md" % (pre, vid)))
    copied += 1

print("copied %d, already present %d, missing %d" % (copied, skipped, missing))
print("sources/ now holds %d transcripts"
      % len([p for p in glob.glob(os.path.join(SOURCES, "*.md"))]))
