"""Measure transcript body length for sources/ files matching a glob.

    PYTHONUTF8=1 venv/Scripts/python.exe measure.py "tasks/.../sources/ssd_*.md"

DO NOT PASTE THESE NUMBERS INTO AN AUDIT ROW.
-------------------------------------------
This prints how long a body IS.  It says nothing about whether anyone read it, and on
2026-09-13 four rows were built by copying this output next to a quote lifted from a grep
window - a full-read claim for a file that had only been sampled.  `verify_audit.py` passed
all four, because a char count is evidence of measurement, not of reading.

The pair a row is allowed to claim comes from evidence instead:

    PYTHONUTF8=1 venv/Scripts/python.exe audit_tools/coverage.py --emit

which derives "chars read" from the lines actually printed into a context, recorded in the
raw .jsonl session logs.  For a full read it equals the body length; for a partial read it
is smaller, and the row cannot claim what did not happen.  Use this script for sizing a
file before opening it, and for nothing that ends up in the audit.
"""
import glob
import io
import os
import sys

MARK = "\n## Transcript\n\n"

for pattern in sys.argv[1:]:
    for path in sorted(glob.glob(pattern)):
        text = io.open(path, encoding="utf-8").read()
        i = text.find(MARK)
        body = 0 if i < 0 else len(text[i + len(MARK):].strip())
        print("%-34s %7d" % (os.path.basename(path), body))
