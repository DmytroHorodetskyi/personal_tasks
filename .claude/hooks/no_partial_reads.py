"""PreToolUse guard: refuse search-shaped reads of audit transcripts.

Wired into .claude/settings.json for the Bash and PowerShell tools.

The source audit's method says, as step 1: "Read the transcript body end to end.  Not
head+tail, not grep windows, not the chapter list."  On 2026-09-13 that instruction was
followed for 94 of 99 transcripts and ignored for the rest - three grep windows and one
head+tail - and the rows written from them claimed a full read.  Prose cannot enforce
itself; this can.

Blocked, when the command touches tasks/hardware/pc_build/sources/:

    grep/rg/findstr/Select-String with a positive pattern   - a window, not a read
    head / tail / -TotalCount / -Tail                       - the ends, not the middle
    head -c / any byte truncation                           - silently drops the tail

Allowed, because none of them can substitute for reading:

    sed -n '/^## Transcript/,$p' [| sed -n 'A,Bp']   the method's own command, in slices
    cat, Get-Content with no line limit
    grep -v / Select-String -NotMatch                a blank-line filter prints everything
    audit_tools/coverage.py, audit_tools/measure.py  they glob sources, never print bodies
    anything whose output is counted (wc, ls, find)

Exit 2 tells Claude Code to block the call and show stderr to the agent.
"""

import json
import re
import sys

SOURCES = re.compile(r"pc_build[/\\]sources[/\\]|sources[/\\][a-z]+_[\w-]{11}\.md")

# Tools that are fine even though they name sources/.
EXEMPT = re.compile(r"coverage\.py|measure\.py|fetch_all\.py|derive\.py|file_all\.py"
                    r"|\bwc\b|\bls\b|\bfind\b|Get-ChildItem|Measure-Object")

SEARCH = [
    (re.compile(r"(?<![\w-])(?:grep|egrep|fgrep|rg)\b(?![^|;&]*\s-v\b)"),
     "grep prints only the lines that match; the rest of the body is never read"),
    (re.compile(r"Select-String\b(?![^|;&]*-NotMatch)"),
     "Select-String is a grep window"),
    (re.compile(r"(?<![\w-])findstr\b"), "findstr is a grep window"),
    (re.compile(r"(?<![\w-])head\b"), "head reads the start and stops"),
    (re.compile(r"(?<![\w-])tail\b"), "tail reads the end and skips the middle"),
    (re.compile(r"-TotalCount\b|(?<![\w-])-Tail\b"),
     "-TotalCount/-Tail read one end only"),
]

ADVICE = """
Read it end to end instead:

  sed -n '/^## Transcript/,$p' <file>

in slices if it is long, with OVERLAPPING sed ranges so nothing falls between them:

  sed -n '/^## Transcript/,$p' <file> | sed -n '1,40p'
  sed -n '/^## Transcript/,$p' <file> | sed -n '40,80p'

Then prove it, rather than asserting it:

  PYTHONUTF8=1 venv/Scripts/python.exe tasks/hardware/pc_build/audit_tools/coverage.py
  ... --missing <videoid>     shows exactly which body lines were never printed

A grep window can produce a quote and measure.py can produce a char count, and together
they look like a finished audit row for a file nobody opened. That is the failure this
hook exists to prevent."""


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    tool = payload.get("tool_name") or ""
    if tool not in ("Bash", "PowerShell"):
        return 0
    command = (payload.get("tool_input") or {}).get("command") or ""
    if not SOURCES.search(command):
        return 0
    if EXEMPT.search(command):
        return 0
    for pattern, why in SEARCH:
        if pattern.search(command):
            sys.stderr.write(
                "BLOCKED by .claude/hooks/no_partial_reads.py\n\n"
                "This command searches an audit transcript instead of reading it: %s.\n"
                "%s\n" % (why, ADVICE))
            return 2
    # head -c and friends truncate mid-line and silently drop the rest.
    if re.search(r"(?<![\w-])head\s+-c|\|\s*head\b|\btruncate\b", command):
        sys.stderr.write(
            "BLOCKED by .claude/hooks/no_partial_reads.py\n\n"
            "Byte truncation drops the tail of the file without saying so.\n%s\n" % ADVICE)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
