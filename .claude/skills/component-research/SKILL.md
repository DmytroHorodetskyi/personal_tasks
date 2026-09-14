---
name: component-research
description: Research, price and present hardware Dmytro is buying — PC components, peripherals, monitors, earbuds, a UPS — for any matter under tasks/hardware/, not only the pc_build sheet. Use when he asks about a part or compares options ("what about the CPU", "is X worth it", "which one"), when a price or a build total is quoted, when he sends links or videos to check, when a review has to be folded into a decision, when any tasks/hardware/**/*.md is edited, and equally on the verification half of the same work — auditing sources, re-checking what a doc claims, "are the docs up to date", "did you check them all", or continuing a source audit. Enforces the answer contract — plain specs with units, one column per option, stock-checked prices — the source rule that every supplied link is read in full and no verdict is written without a verbatim quote, and the rule that a settled decision is not reopened.
---

# Component research for a purchase in tasks/hardware/

Every rule here was written after Dmytro had to ask for the same thing twice. The docs are in
`tasks/hardware/pc_build/`: one `components/*.md` per part, `pc_build.md` for the three-build
table, `tools.md` for which sources are trusted.

## 1. Before answering

- Read the part's `components/*.md` **and** the three-build table in `pc_build.md`. The answer
  usually already exists and has a date on it.
- Check whether the question is already settled. §4 governs what to do if it is.

## 1b. Sources he hands you

When Dmytro supplies N sources, **every one is read end to end before anything is reported.**

**The rule that makes this checkable: no verdict without a quote.** Each source gets a row
carrying a verbatim quote from it. A row with a conclusion and no quote is not a finding - it is
a guess, and it must say "not read" instead. This is the only part of the rule that does not
rest on self-assessment, which is why it is the rule.

Write the coverage table into the task file and show it in the reply:

| Source | Chars read / total | Verbatim quote | Bearing on the decision |

- **Grepping a source for the models already on the shortlist is not reading it.** It can only
  confirm what is already there; it can never find what was missed, which is the whole reason he
  sent it. On 2026-09-13 a grep-only sweep of nine videos missed the model that won its price
  class in two of them.
- **A title and an upload date are not content.** Never infer "older, nothing applicable" from
  metadata - that inference produced three fabricated verdicts in the same session.
- Transcripts go in the task's `sources/` folder and frames in `frames/`, not the scratchpad, so
  the quote and the number behind it stay checkable after the session ends.
- **These hosts return HTTP 403 to WebFetch every time: hwbusters.com, techpowerup.com,
  tomshardware.com, rtings.com, kitguru.net, pcpartpicker.com, bequiet.com, cclonline.com.**
  Go straight to `mcp__Claude_Browser__navigate` + `get_page_text` for them — that works. Eight
  403s were spent on this in one 2026-09-11 session and more in another on 2026-09-13.
- **On a review site, fetch the page that holds the number** (hwbusters' noise page is `/9/`, its
  verdict `/11/`, its protections `/8/`), not the landing page, and read the vendor's own
  specification page before concluding a figure does not exist.
- Say what the method cannot reach. Microphone or audio samples inside a video cannot be judged
  from a transcript, and frames do not help. Name the gap rather than letting silence imply
  coverage.
- **Every number taken from a video carries its video ID and timestamp** - `(Testing Games,
  4UqYr3nAj90 @ 3:59)`, never a bare channel name. A figure he cannot re-check in one click is a
  figure he has to take on trust.

Never write "all N checked", "verified" or "read in full" into a file or a reply unless every one
was. Answer "did you check them all?" honestly on the **first** ask — on 2026-09-12 the answer to
"IN FULL? ALL 10?" was "NO. 7 of 10", and it should not have taken the question. **Before writing
any count, print it**: `ls sources/ | wc -l`, or the row count of the coverage table. A number you
did not just compute is a guess.

## 1c. Running Python in this repo

CLAUDE.md's rules are not advisory; they were broken in four of nine sampled sessions.

- **Write the script to the scratchpad and run the file.** Never `python - <<'PY'`, never
  `python -c` for anything multi-line. A backslash inside a heredoc silently mangles a regex -
  that cost a turn on 2026-09-13 and in earlier sessions.
- Run it as `PYTHONUTF8=1 venv/Scripts/python.exe <file>`. Bare `python` with no UTF-8 mode
  writing Cyrillic is how content gets corrupted on this cp1251 console.
- **Never set `ssl.CERT_NONE` or `check_hostname=False`.** A scratch scraper did that on
  2026-09-11 and tripped the antivirus; `code/ua_prices.py` exists partly to stop it recurring.
  Use that script instead of writing a new scraper.

## 2. The answer contract

Dmytro asks for a component. Answer in this order, every time:

1. **What it is, in one line.** The category and the plain name — "the processor", "the case
   fan". Do this before any nuance about packaging codes, SKUs or variants. A part number is
   not an answer to "what is this component".
2. **The numbers, with units.** GHz boost, cores, cache, watts, GB, mm, Hz, dB(A), UAH —
   whichever decide *this* part. Never describe a spec you have not printed.
3. **The verdict**, then the cheaper and the better-but-pricier alternative.

**One column per option.** When two or more builds or candidates are compared, every one gets
its own column and every row is filled in. Never collapse them into a "shared platform" column
plus a diff — that has been rejected twice.

Prose after the table, not before it, and only what the table cannot carry.

## 3. Prices

**Never quote hotline's cheapest offer as the price.** It is whichever of ~40 sellers is
momentarily cheapest, usually one with no service department, and it has been wrong in both
directions — 4 598 low on a Windows licence, 3 005 high on a RAM kit.

```bash
PYTHONUTF8=1 venv/Scripts/python.exe code/ua_prices.py tasks/hardware/pc_build/parts.json \
  --cache "$SCRATCH/cache" -o "$SCRATCH/prices.md"
```

- **Dmytro buys at click.ua** (said 2026-09-13, after every table in the project had been
  written around Telemart - because the script contacted four shops and click.ua was not one
  of them). click.ua is now first in `SHOPS`. **Quote its price as the price**; the others are
  a cross-check on whether it is fair, not shops the basket is ordered from. Do not present a
  Telemart basket as the answer again.
- The script reads click.ua, Telemart, Brain, ITbox and Foxtrot direct and uses hotline only as
  a directory of who stocks what. It contacts no other host, verifies certificates and follows no
  redirects — see its header for why all three matter.
- **A premium is only real if both prices come from the same shop.** Never subtract a shop
  price from a hotline floor, or one shop's price from another's, and call the difference a
  premium. On 2026-09-13 that produced a "+1 899" on the Renegade G5 — 11 999 at a shop against
  the 990 PRO's 10 100 hotline floor — while at the one shop that stocked both the G5 was 400
  **cheaper**. The same mistake is recorded in storage.md as one Dmytro had already caught once.
  When only cross-shop numbers exist, print both shops in the row and say the comparison is not
  like-for-like.
- **A price without a stock check is not a price.** Three of the cheapest listings found on
  2026-09-11 were out of stock at the shop advertising them.
- Rozetka and Comfy refuse scripted requests; read those in the browser. КТС and MOYO stock no
  components. **ITbox and Brain are one catalogue** — one source, not two.
- Quote the price *and* the shop. No single shop carries the basket.

## 4. Settled decisions

A decision recorded in the docs with a date is closed. When new evidence appears, say in **one
line** whether it changes the decision, then stop.

Do not restate the case for a closed decision, do not present a fresh source and then withdraw
it, and do not offer the same trade-off again in new words. Re-arguing the 16-vs-32GB choice
across four rounds — each round citing a source that was then disowned — is what "completely
pointless" was aimed at.

If the evidence genuinely overturns something, change the doc and say what changed.

## 5. Touching the three-build table

The tiers must be **different machines**, not one machine with a bigger graphics card. Before
presenting the table, check it:

- No two tiers may share most of their rows. If Max differs from Working only in the GPU and the
  SSD, it is not a tier — say so plainly rather than presenting it as one.
- If the budget ceiling makes a third real tier impossible, say that, and say what the ceiling
  would have to be. Do not pad the table to look tiered.

After any price or part change, recompute the totals from the parts — never adjust an old
total — and update the gaps, the headroom, and the per-build prose totals in the same edit.

## 6. Writing back

`pc_build.md` and the component docs are edited by other sessions too. Re-read the section
immediately before editing it, and make targeted edits — never rewrite a whole section.
Keep the verdict table in `pc_build.md` in step with the component doc it summarises.
