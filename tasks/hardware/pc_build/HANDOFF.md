# Handoff — the source audit is finished

**Closed 2026-09-13.** `verify_audit.py` prints **99/99 PASS**, and all **27 non-YouTube links**
have been checked over verified TLS. Nothing is outstanding. This file is kept as the record of
what the audit was and how to re-run it, not as a task.

## Verify it yourself

```bash
PYTHONUTF8=1 venv/Scripts/python.exe tasks/hardware/pc_build/verify_audit.py
```

It re-derives the inventory from the raw `.jsonl` session transcripts on every run and trusts no
list, including this one. **It is the only thing that closes the task.** It currently prints
`99/99 PASS` and `bodies proven read end to end : 99 of 99`. `audit_tools/status.py` breaks it
down per component.

**That second line is the one that matters, and it is new.** Until 2026-09-13 the script proved
only that a row existed carrying a quote and a char count — both of which an agent can produce
from a grep window plus `measure.py`, without opening the file. It now also proves the body was
read, by checking every non-blank line of every transcript against the text actually printed into
a context, recovered from the raw session logs:

```bash
PYTHONUTF8=1 venv/Scripts/python.exe tasks/hardware/pc_build/audit_tools/coverage.py
PYTHONUTF8=1 venv/Scripts/python.exe tasks/hardware/pc_build/audit_tools/coverage.py --missing <videoid>
PYTHONUTF8=1 venv/Scripts/python.exe tasks/hardware/pc_build/audit_tools/coverage.py --emit
```

`--missing` names the exact body lines nobody ever saw. `--emit` prints the `chars read / chars
total` pair a row is *allowed* to claim, derived from evidence instead of copied from
`measure.py` — for a partial read it is smaller than the total, so the row cannot claim the read
did not happen. **`measure.py`'s output is no longer admissible in a row**; its docstring says so.

`--by-session` asks the stricter question: did any **single** session print a whole body, rather
than lines being scattered across sessions months apart? As of 2026-09-13: **98 of 99 yes**. The
exception is `ups_JL71IH5HShI` — session `fe8c7111` printed 44 of its 46 lines, and the last two
were read only on 2026-09-13, *after* the row claiming a full read had been written. The content
is now read and the UPS section amended with what it said, so the record is honest; the row's
history is not, and that is why this mode exists.

**Three things the coverage check does not prove**, stated so nobody treats it as more than it is:

1. **It cannot prove attention**, only that the text was on screen. A line printed and skimmed
   counts the same as a line printed and understood. No tool fixes that.
2. **`gpu_2ufCzwK73GM.md` has a 0-char body** — the one video with no caption track — so its
   100% is vacuous. That file rests on the fetch having succeeded, checked separately after the
   HTTP 429 bug.
3. **One line of 2 312 is credited without evidence** — `[4:18] [music]` in `ssd_IqqarIpZET8`,
   too short to key uniquely. It carries no content. Every other line is matched against text
   actually printed.

It found two gaps the moment it was written, both in work that had been passing: one line of
`earbuds_f7lnPrre2Wk` and **two lines of `ups_JL71IH5HShI` that no pass had ever printed** — and
one of those carried the most practical sentence in the UPS batch. Both are now read.

**Never write "done", "verified", "all checked" or a completion count unless that script has just
printed it.** If Dmytro asks "did you check them all?", answer with the script's output, on the
first ask, without softening it.

## What was found

The quote-by-quote record is [source_audit.md](source_audit.md), one section per component, each
ending in "What the full reads changed". The running narrative is
[../pc_build.md](../pc_build.md) → "Opened by the source audit", **parts 1-9**, items 1-72.

Every documentation error is fixed **in place**, in the document that carried it, marked with what
it said before. The choices with money attached are in
[../pc_build.md](../pc_build.md) → **DECISIONS WAITING ON DMYTRO**, six of them, none decided here.

Recurring patterns, in the order of how often they turned up:

| Pattern | Count |
|---|---:|
| **Undisclosed sponsorship or commercial tie** | **19 of 99 videos carry a paid sponsor**; three headphone sources are shops; four keyboard sources run to Keychron; all eight mouse guides are monetised |
| **Wrong counts** — "all five", "6 of 6", "every source", "six sources agree" | **nine**, every one recounted |
| **Right number attached to the wrong thing** | seven, including "21 years of FPS reviews", the Sony 85%, and two products merged into one claim |
| **"Nothing usable" dismissals that were not true** | **three** |
| **Cherry-picked verdicts** — the quote kept, the reviewer's conclusion dropped | three |
| **Claims about frames with no frame on disk** | two, now 27 frames saved |

## The limitation of the verifier, and the one failure it did not catch

**`verify_audit.py` cannot tell a full read from a partial one, and on 2026-09-13 it did not.**
Four rows were written from a partial read — three built on **grep windows** and one on
**head+tail** — while carrying char counts that assert the whole body was read. The script passed
all four, because it checks that a row exists, carries a verbatim quote, and that the number
matches `measure.py`. **The number comes from `measure.py`, not from reading**: it is evidence the
file was measured, not that anyone read it.

It was caught only because Dmytro asked outright. All four were then read in full; nothing already
written proved false, two findings gained support and three things had been missed — recorded in
[source_audit.md](source_audit.md) under "The audit did to itself what it was built to catch" and
"What the partial reads had missed".

**That check now exists** — `audit_tools/coverage.py`, wired into `verify_audit.py` as check (e).
Three further things were put in place the same day so the failure cannot recur quietly:

**A hook, because prose does not enforce itself.** `.claude/hooks/no_partial_reads.py`, wired in
`.claude/settings.json`, refuses any Bash or PowerShell call that points `grep`, `head`, `tail`,
`findstr`, `Select-String`, `-TotalCount`/`-Tail` or byte truncation at
`pc_build/sources/`. It allows the method's own `sed -n '/^## Transcript/,$p'` in slices, `cat`,
`grep -v` used to strip blank lines, and the audit tools themselves. The instruction "not grep
windows" was already written, in bold, as step 1, and was ignored anyway; a blocked tool call is
not advisory.

**Two process rules, which matter more than they sound.** Both describe how the failure started,
not how it was caught:

- **One video, one row, written together.** Reading a batch and writing its rows afterwards is
  what lets "I know roughly what is in these" stand in for reading. The drift began on the
  largest files at the end of the longest batch.
- **Read the transcript before reading the document's claims.** Reading the doc first turns the
  transcript read into a search for claims already known — which can only confirm, never find.
  Every one of the three findings missed by the partial reads was a *new* fact, not a broken one:
  a second source for the Liberty 4 Pro, a "reference microphone" nobody had priced, and a
  caveat owed to a decision already put to Dmytro.

**And slice with overlapping ranges.** `sed -n '1,40p'` then `sed -n '40,80p'`, not `40,80` after
`1,39`. Two of the gaps found on 2026-09-13 were off-by-one errors in manual line arithmetic, one
of them mine while re-checking the others. `coverage.py --missing` catches these; do not rely on
counting.

## If the audit is ever re-opened

- **Fetch nothing that is already here.** All 99 transcripts are in [`sources/`](sources) as
  `<component>_<videoid>.md`; [`sources/GROUPS.tsv`](sources/GROUPS.tsv) maps every id to a
  component and to the `session:line` it arrived on. 27 frames are in [`frames/`](frames).
- **The one video with no captions** is `2ufCzwK73GM`, re-confirmed after a fetcher bug that
  silently recorded HTTP 429 as "no caption track". `audit_tools/fetch_all.py` is the fixed
  version. Never conclude "no captions" from an empty body unless the fetch is known to have
  succeeded.
- **"chars" means the transcript body** — everything after the `
## Transcript

` marker,
  stripped. An early pass's counts were each exactly 16 too high because they included the marker.
  `audit_tools/measure.py` is the only figure the verifier accepts.
- **Rozetka and Reddit refuse automated fetches** (HTTP 403 / blocked). Rozetka listings were read
  in a browser; the Reddit RAM guide was quoted from the full text Dmytro had pasted into the
  session. Two Tom's Hardware hierarchy pages return truncated bodies and are recorded as **not
  read** — no page in this audit was summarised from a title or a search result.
- **The rule that did the work:** no verdict without a verbatim quote or a `frames/` path. The
  verifier enforces it, which is why it caught rows that read plausibly and proved nothing.
