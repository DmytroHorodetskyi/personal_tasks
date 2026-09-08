---
name: style-check
description: Verify Ukrainian prose against knowledge/WRITING_STYLE.md before it reaches Dmytro. Cost scales with the size of the text — a proposed sentence or paragraph gets the mechanical scan only; a full document, chapter or article additionally gets one reviewer pass. Use when a draft is about to be delivered, before proposed replacement wording is shown, when the user says "check the text / перевір текст / style check", or after a prose edit larger than a sentence. Reports violations; never rewrites on its own.
---

# Style check — the gate before any prose reaches Dmytro

Every correction Dmytro has had to make is written down in `knowledge/WRITING_STYLE.md` and, in
machine form, in `code/build/style_rules.json`. This skill enforces it at write time.

**The gate is scaled to the size of the text.** Running the full apparatus on a single sentence
burns tens of thousands of tokens for one line of prose; that is what made the gate unusable.
Pick the tier first.

| What is being delivered | Tier |
|---|---|
| A replacement sentence or paragraph proposed in chat or a widget | **A — scan only** |
| A section rewritten, or a prose edit larger than a paragraph | **A — scan only** |
| A full document, chapter or article about to be shown or built | **B — scan + one reviewer pass** |

---

## Tier A — the mechanical scan (always; often the only thing needed)

Save the passage to a `.md` file in the session scratchpad and run, from the repo root:

```bash
PYTHONUTF8=1 venv/Scripts/python.exe code/build/style_check.py <path>.md --fragment
```

Drop `--fragment` when the file is a whole document (it only skips the opening-sentence checks).
The scan costs under a thousand tokens and returns in seconds.

- It parses the markdown the way `build_docx.py` does: `$$…$$ (n)` display formulas, `$…$` inline
  formulas, tables, headings, lists, «Перелік посилань». **Formulas are never spell-checked**;
  inline ones are reduced to their plain symbol (`$C_T$` → `C_T`) so the surrounding grammar
  still parses.
- Repo rules live in `code/build/style_rules.json` — the machine half of WRITING_STYLE.md §2–§6
  (calques, AI tells, meta-commentary, attribution, bare «(табл. N)», paraphrased metric names),
  plus structural checks: result-first opening, «де» gloss after every display formula,
  unglossed symbols, run-in lead-ins, bold in body, lists, tiny sections, decimal points,
  bracket stacking, table captions, citations without reference entries.
- LanguageTool uk-UA runs on the prose via the free public API (`--no-lt` to skip). It catches
  general Ukrainian faults the repo list does not (на протязі, приймати участь, більше того,
  значимий, у/в). A rule that keeps firing falsely goes into `lt_ignore_rules`.
- Exit code 1 means errors remain: fix and re-run until clean. Warnings are read one by one;
  `info` is looked at once.
- Some structural checks assume an academic deliverable (result-first opening, «де» gloss,
  reference list). On a text that is not one — a letter, a note, a plain report — read those
  findings as advisory rather than fixing them into place; the register rules (§2, §2b, §6) apply
  everywhere.

**Then read the passage yourself against §2b before showing it.** The scan cannot judge register,
so check by eye for: explanatory chaining («завдяки чому», «тому … обчислено», «після чого»,
«тобто», «при цьому») — a scientific text states the condition and the action, it does not narrate
why one follows from the other; stacked genitives; «за» + instrumental for "by means of" (a
russism); a named method with no what-it-does / why-here clause. This is a read, not a subagent.

**Whenever Dmytro corrects a word or phrasing, add it to `style_rules.json` in the same turn**
(and the human-readable line to WRITING_STYLE.md §6). The list is the memory of his corrections;
a correction that is not in the list will be repeated. This is the part of the skill that
compounds — a rule added here is a subagent never spawned later.

---

## Tier B — one reviewer pass, for a full document only

For a complete document, chapter or article, after the Tier A scan is clean, spawn **one**
`general-purpose` agent, **once**, on the **final** draft:

> Read `knowledge/WRITING_STYLE.md` in full. If this repo holds a finished Ukrainian deliverable
> of the same kind, read its first 120 lines for cadence. Then read `<draft>` paragraph by
> paragraph. For each paragraph report, by line number, every violation of the style file:
> (a) rhetorical order — does anything state a result before the apparatus that produces it;
> (b) register — anglicism, calque, colloquial word, translated-from-English phrasing, verb
> dropped in a dash ellipsis, sentence built around bracketed numbers; (c) meta-commentary — any
> sentence about *the analysis* rather than *the phenomenon* (defending an omission, explaining
> why an alternative was rejected); (c2) explanatory chaining of consequences («завдяки чому»,
> «тому … обчислено», «після чого», «тобто», «при цьому») (§2b); (d) arithmetic narration — an
> elementary operation described in words instead of a display equation; (e) a named method with
> no what-it-does / why-here clause; (f) every symbol in a formula defined in the «де» gloss, in
> order. Also flag paragraphs whose shape repeats the previous one (same opening construction,
> same length, tricolon endings). Quote the offending words. Do NOT rewrite anything and do NOT
> praise; output only the violation list. If a paragraph is clean say "clean".

**Once means once.** Do not re-spawn the reviewer after applying its fixes, and do not send its
own proposed wordings back through the gate — read them yourself against §2b as in Tier A. The
recursion of doing both is what once made a single deliverable cost six figures in tokens.

---

## Delivery

1. Apply the fixes.
2. Re-run the Tier A scan; it must exit 0.
3. Show the text as one version — the exact wording, no menu of options.

## What this skill does not do

- It does not judge scientific content, numbers or the truth of citations.
- A clean scan of thin, skeletal prose is still a failure: a concept that is introduced gets
  explained, not just named.
- It does not run on the `.docx`; run it on the markdown before `build_docx.py`. A final manual
  pass in Word with the OnlineCorrector add-on is Dmytro's call.
