---
name: component-research
description: Research, price and present PC components for the build sheet in tasks/hardware/. Use when Dmytro asks about a component or compares options ("what about the CPU", "is X worth it", "why this one"), when a price or a build total is quoted, when a review or YouTube link has to be folded into a decision, or when the three-build table or any components/*.md is edited. Enforces the answer contract — plain specs, one column per build, stock-checked prices — and the rule that a settled decision is not reopened.
---

# Component research for the build sheet

Every rule here was written after Dmytro had to ask for the same thing twice. The docs are in
`tasks/hardware/pc_build/`: one `components/*.md` per part, `pc_build.md` for the three-build
table, `tools.md` for which sources are trusted.

## 1. Before answering

- Read the part's `components/*.md` **and** the three-build table in `pc_build.md`. The answer
  usually already exists and has a date on it.
- Check whether the question is already settled. §4 governs what to do if it is.

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

- The script reads Telemart, Brain, ITbox and Foxtrot direct and uses hotline only as a
  directory of who stocks what. It contacts no other host, verifies certificates and follows no
  redirects — see its header for why all three matter.
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
