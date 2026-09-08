# WRITING STYLE — Ukrainian academic register

> How Ukrainian prose written here must be composed. The rules were derived from two finished
> exemplars in the sibling `articles` repo — a full VOI dissertation chapter
> (`dissertation/Chapter_2_v2/Chapter_2_v2.docx`) and a case article
> (`cases/pneumonia/Pneumonia_VOI_v2/Pneumonia_VOI_v2.docx`). When in doubt about cadence, open
> those and match them. Below, "the exemplar" means one of those two documents.
>
> The rules divide into two kinds. **Register and language — §2, §2b, §4, §6 — apply to any
> Ukrainian text written here**, academic or not: those are Dmytro's corrections, and a correction
> repeated is a defect. **Document-shape rules — §1, §3, §3a, §5 — apply to an academic
> deliverable** (an article, a chapter, a formal report with formulas) and should not be forced
> onto a letter, a note or a plain summary.
>
> **Enforcement:** `PYTHONUTF8=1 venv/Scripts/python.exe code/build/style_check.py <draft.md>`
> scans the markdown against the machine-readable copy of §2–§6 in `code/build/style_rules.json`
> and runs LanguageTool uk-UA on the prose (formulas excluded). The `/style-check` skill wraps it
> with a reviewer pass. **Every substitution added to §6 below must also be added to
> `style_rules.json`.**

## 1. Rhetorical movement — NEVER open with the result

The single most important rule, and the one most often broken. An article/section is built
**general → specific → conclusion**, in this order:

1. **Motivation / premise** — the general problem or methodological gap, stated *without any
   numbers and without the answer*. (Розділ 3 opens on the global burden of respiratory disease
   and the problem of diagnostic uncertainty; the pneumonia article opens on the *aim* and setup.)
2. **The gap** — why the existing/simpler approach is insufficient for the question at hand.
3. **The apparatus** — introduce the formal method (definitions, formulas) that fills the gap.
4. **Application to our data** — plug in the cohort, derive the numbers.
5. **Result, then interpretation** — state the number, then a sentence/paragraph on what it means.
6. **Conclusion** — only at the end.

**The first sentence must never state a finding** (no "the analysis established that X is
cost-saving…"). Lead with the conceptual problem; let the result emerge where it belongs.

## 2. Register and texture

- **Dense, continuous prose.** Long connected sentences with subordinate clauses and explicit
  connectives (проте, оскільки, натомість, з огляду на, саме тому, водночас, а отже). Vary
  sentence length. Read Розділ 3 aloud for the cadence.
- **No bullet lists, no markdown scaffolding, no run-in mini-headers like "Обґрунтування:".**
  Reasoning is carried in paragraphs, not fragmented into labelled points.
- **Do NOT fragment a short text into many tiny headed sections.** Chopping a few pages into 6–8
  headings of 1–2 paragraphs each is a glaring AI tell (Dmytro, 2026-08-03). Default to continuous
  developed prose; introduce a heading only when a genuinely distinct, multi-paragraph part begins.
  A section that is one or two paragraphs long should not have its own heading.
- **Do NOT use run-in subtitle lead-ins — neither italic nor bold** (e.g. *Модель витрат.* … ).
  Dmytro rejected them (2026-08-03) as visually poor. Carry the finer structure in continuous
  prose; for a document that needs sectioning, use **full numbered section headings** (1., 2., 3.
  / 3.1, 3.2 …) with Heading styles, as in the chapter-level `Chapter_2_v2.docx`. **Bold is used only
  for the document title.** (Earlier guidance said run-in headings should be italic — that is
  now superseded: no run-in subtitles at all.)
- Avoid obvious AI tells: parallel tricolons, "варто зазначити", "більше того", mechanical
  em-dash asides, and every paragraph having identical shape.
- **Colons.** Correct Ukrainian wherever the second clause explains, specifies or gives the
  cause of the first (anywhere «а саме» fits), so these are style rather than grammar — with
  one exception: a colon may follow only a **complete clause**, never a preposition
  (`COLON_AFTER_PREP`, error). The style constraint is per PARAGRAPH, not per document:
  several explanatory colons in one paragraph means sentences that want splitting
  (`COLON_PARAGRAPH_DENSITY`, warn), and the academic guides note the sciences use the colon
  less than the humanities. An explanatory colon is the punctuation form of the «тому …»
  consequence-chaining §2b already bans — state the condition, then the action. A colon that
  ENDS a paragraph to introduce a display formula, list or table is required by the format
  and is never counted. (Raised by Dmytro 2026-09-05 on VOI_COVID_v3, which ran 6 flagged
  paragraphs of 35 against the pneumonia exemplar's 3 of 38.)
- **Parentheses:** a single sourced value tied to its noun is idiomatic and the exemplar uses it
  ("базову ставку на випадок (8 735 грн)"). The fault is *stacking* several bracketed numbers in
  one sentence or building the sentence around bracket-dumps. Reference a table with a clause
  ("наведено в таблиці 4"), not a bare "(табл. 4)".

## 2b. Conditions, not causal chains (added 2026-09-04)

Dmytro rejected «…завдяки чому вплив групи оцінюється за незмінних значень…» and «…тому скорочення
тривалості обчислено як…» as *not scientific style*. The fault is explanatory chaining: connectives
such as **завдяки чому, тому, саме тому, після чого, тобто, при цьому, адже** string actions into a
causal narrative, the way a tutor explains. A scientific article states what was done and under
what condition; the reader infers the consequence.

- **Wrong:** «…подано лінійною комбінацією …, завдяки чому вплив групи оцінюється за незмінних значень.»
  **Right:** «…подано лінійною комбінацією … . Ефект групи в такій специфікації оцінюється за
  фіксованих значень початкових показників.»
- **Wrong:** «Коефіцієнт виражено в логарифмічній шкалі, тому скорочення обчислено як…»
  **Right:** «Коефіцієнт визначено в логарифмічній шкалі. Скорочення тривалості обчислено як…»
- A condition goes in front as «оскільки …, …» or «за … » and is followed by the action; a
  consequence is never narrated with «тому», «отже», «завдяки чому».
- One statement per sentence. Sequential steps are joined with «а», not «після чого / потім / далі».
- Machine check: `REGISTER_*` rules in `code/build/style_rules.json` (warnings). They are heuristics;
  the reviewer pass (Layer 2 of `/style-check`) is where register is actually judged and is mandatory.

## 3a. Provenance and formulas — scientific-article register, not arithmetic narration

Two opposite failures, both wrong: (a) dropping bare numbers and multiplying them like a
calculation log; (b) narrating elementary operations (division, standardisation) in words as if
tutoring. The correct register is that of a published methods article — model on the exemplar chapter
and on real methods literature in the field:
concise, rigorous, assuming mathematical literacy.

- **Every parameter states its origin in one clause:** an estimate from an earlier section, a
  tariff, a referenced value, or an imputation — with the one-line reason for an imputation
  (C is not observed because payment is per treated case, so it is derived from the case rate and
  the mean length of stay). Source things the way the exemplar does ("отримано з лабораторних
  звітних даних [7]… узгоджуються з…"). Do not lecture.
- **Every derived quantity is a proper display equation** — symbolic, with a `де` gloss, then the
  numeric substitution and result: `C = R / D̄` … "звідси C ≈ 488,9 грн". **Never encode a formula
  as verbal arithmetic** ("розподіливши ставку на тривалість") — write the equation.
- **Do not narrate standard mathematical operations.** State the result with the assumption that
  justifies it. Probability of a negative net benefit — **wrong**: a paragraph explaining that
  "zero lies b₀/√v₀ standard deviations to the left, so the area under the curve…". **Right**:
  "Оскільки INB ~ N(b₀, v₀), P(INB<0) = Φ(−b₀/√v₀) ≈ 0,015", with Φ defined once. The justification
  is the distributional assumption, not a walkthrough of standardisation.
- "Justify" means *why the formula is valid here* (the assumption it rests on), never *how to do
  the arithmetic*.

## 3b. No meta-commentary — write the science, not the process

The article states what IS done and shows the result. It **never narrates the author's reasoning
process, defends what was not done, or explains why an alternative was rejected.** Ban sentences
like: "задавати конкретні значення означало б вносити недостовірні припущення", "знехтувавши
складовою, наявність якої лише збільшила б витрати", "щоб уникнути припущень, ми…", "цей поріг є
свідомо завищеним". If a value is unknown, the article simply works with what is derived/sourced —
it does not announce that a number was avoided or why. Methodological reasoning, caveats about
one's own choices, and "why not X" belong in the analysis notes (`instructions/…`), never in the
deliverable. Rule of thumb: if a sentence is about *the analysis* rather than *the phenomenon*,
cut it.

## 3. Formulas and numbers

- Each formula is a display line, **immediately followed by a `де …` gloss** defining *every*
  symbol in order. No symbol left undefined.
- In the final Word document formulas are **native OMML (Word equations)**, not images or plain text.
- Keep intermediate numbers visible (substitute values into the formula, then give the result).
- Every parameter carries its source in prose (data-derived vs external), e.g. "базової ставки
  за програмою медичних гарантій (8 735 грн)". No `[DATA]/[EXTERNAL]` tags in the final text —
  those are review scaffolding only.
- Numbers computed from the cohort come from the analysis script, never inherited black-box values.

## 4. Attribution (hard rule)

State methods and formulas **impersonally** ("EVPI обчислюється як…", "застосовано
пуассонівську регресію"). **Never** "за методом X та співавторів", "у моделі Чена",
"the framework of […]" — especially for the author's own source articles. Authors appear only
in the reference list.

## 4a. References are mandatory and must be real

Every externally-sourced number carries an inline `[n]` citation to a numbered `Перелік посилань`
(like `Chapter_2_v2.docx`). **Never invent a citation** — author, title, journal, year, DOI must be
verified (WebFetch/WebSearch the DOI, or take it from `knowledge/external_parameters.md` /
`source_extracts.md`). If a value has no defensible source, say so in the text and treat it as a
stated assumption to be swept — do not dress an assumption up as sourced. Prefer peer-reviewed
journals and official guidelines over industry blogs/conference abstracts.

A number computed from the cohort needs no citation but must be reproducible from the script; an
external number without a real source does not go in the document.

## 5. Tables

- Numbered with a caption above, **ДСТУ 3008:2015 §8 form: `Таблиця N — Назва`** — em dash after the
  number, **no period**, left-aligned. Continue the numbering of the document the section belongs to.
  ⛔ **Corrected 2026-08-31:** this rule previously said "Таблиця N. <опис>" (period, no dash), which
  contradicts ДСТУ 3008:2015 §8. The standard governs. `build_docx.py` accepts both forms
  (`TBL_CAPTION_RE`), so the period form builds silently — the standard is the only check.
- **Column heads: centered and bold** (ДСТУ §8). Every table must be referenced in the text.
- Introduced by a sentence that names the table in a clause — "наведено в таблиці 4" — and each table
  is followed by an interpretation. ⛔ **Corrected 2026-09-03:** this rule previously required the
  sentence to end with a bare "(табл. N)", which contradicted §2's parentheses rule. §2 governs.

## 6. Language — correct scientific academic Ukrainian

English in conversation; **Ukrainian academic register** in every deliverable. Draft templates
are shown for review first (plain readable prose, minimal scaffolding), then converted to `.docx`
with native formulas only after approval.

### 6a. Named metrics keep their established name — do not paraphrase them (added 2026-09-03)

A metric that has an accepted short name in the literature is referred to **by that name**, not by a
translated descriptive phrase. QALY, ICER, EVPI, EVPPI, EVSI, ENG, INB, AUC, ВАШ are names, not
descriptions, and rewriting them as prose ("рік життя, скоригований за якістю"; "відношення приросту
витрат до приросту ефекту") reads as translated-from-English and buries a standard term the reader
already knows. Dmytro raised this on 2026-09-03 about "рік життя, скоригований за якістю".

- **Default: the short name alone** — «показник QALY», «EVPI дорівнює нулю».
- **Expand only on first mention, and only when the term does real work in the text**, in the ДСТУ
  form `QALY (рік життя, скоригований за якістю)` — name first, gloss in brackets, never the reverse.
  A term mentioned once in passing (e.g. only to say it is not applicable) needs no expansion at all.
- Never build a sentence around the paraphrase; if a symbol exists, prefer it (`$\lambda$`, `INB`).
- This does **not** license anglicisms in ordinary prose — see the rule below. The distinction is
  *named quantity* (keep the name) versus *ordinary English phrasing* (translate it properly).

**No anglicisms, calques, or colloquialisms.** Dmytro (native speaker) rejects text that reads as
translated-from-English or informal. Concrete substitutions established so far:

- a clinical/quantitative metric is named precisely, not by a business word: bed-day change is
  **різниця / скорочення тривалості госпіталізації**, never *економія ліжко-днів* ("savings").
  (Reserve *економія* for actual money.)
- EVSI ceiling → **верхня межа**, never *стеля*.
- confounding → **систематичне спотворення / конфаундинг** in prose, never bare *конфаундинг* as
  the only term; "unmeasured confounding" → *невраховане спотворення*.
- variance inflation → **збільшення дисперсії**, not *інфляція дисперсії*.
- "the fact that" → **а саме те, що**, never *той факт, що*.
- "pay off / be worth it" → **бути економічно виправданим**, not *окупитися*.
- "weigh X against Y" → **зіставити X із Y**, not *зважити X проти Y*.
- avoid *перебір* (→ *максимізація … за*), *реалізує цінність* (→ *забезпечує*), *мізерний*
  (→ *незначний*), *сітка значень* (→ *низка/ряд значень*), and elliptical dash constructions
  where the verb is dropped ("…відтворює центр, а хвости — тим краще").
- closed form → **замкнений аналітичний вираз**; keep standard stats terms that the exemplars use
  (робастна похибка, вибірковий розподіл, апостеріорний, спряжений, середній маргінальний ефект).

- "marginal effect" → **граничний ефект** is the econometric term (маргінальний is a calque); but
  where the quantity is an averaged predicted difference, prefer describing it plainly
  (*середня різниця прогнозованих значень*) rather than naming it.
- standardized distance / z-type ratio → **«на скільки стандартних відхилень … віддалена»**, not
  *«в одиницях стандартного відхилення»*.
- distribution tails → **краї розподілу / хвостові ділянки**; do not drop the verb in a dash
  ellipsis ("…відтворює центр, а хвости — тим краще" is broken — restate the verb).
- robust standard errors → **робастні** is the established term (uk.wikipedia "Робастна регресія"),
  but don't repeat it every mention; qualify the regression once, then just *стандартна похибка*.
- point estimate → **точкова величина / точкова оцінка**, not *точкове число*.

When unsure whether a term is proper, verify it online (Ukrainian econometrics/statistics
sources, uk.wikipedia) and check whether it appears in the exemplars;
prefer the wording the author already used.

## 7. Data-analysis reports are exempt from §1, §3a and §3 (added 2026-09-08)

Everything above was derived from finished **articles**. A **data-analysis report** — a standalone
account of what a dataset shows — is a different deliverable, and the article-shaped rules make it
bloated rather than good.

**Do not apply to a report:** §1 rhetorical movement (a report may and should open with its
results), §3a "every derived quantity is a proper display equation", §3 formula-and-gloss
requirements, or §6a's expand-the-term guidance beyond a single bracketed gloss on first mention.

**The shape of a report:** each figure and table carries one to three sentences of numbers — the
finding, and nothing about how it was produced. A short opening paragraph states the main results.
That is the whole document. Cut on sight: display formulas and «де» glosses, definitions of what a
method does, model diagnostics, parameter derivations, sensitivity-analysis setup, a «Висновки»
section that repeats the opening, and a «Перелік посилань» (attribute a sourced price in prose
instead). The report this rule came from runs 6 900 characters of text for 12 figures and 3
tables; the drafts it replaced ran 19 000 and were rejected four times over.

**Still binding for a report:** all of §2 and §2b (no bullets, no run-in subheads, no bold in body,
no anglicisms, no consequence chaining), §4 impersonal attribution, §5 table captions, and the
figure-caption convention (`*[Рисунок N — Назва]*`, rendered centred and unbolded below the image).
Every table must still be named in the prose — `style_check.py` enforces it.

**State the finding, never just point at the figure**, and verify every figure-reading claim
against the analysis output that produced the figure before writing it. Three claims in the draft
this rule came from were wrong on the first pass: AUC ranges called disjoint when they overlap 8,01–9,20, prevalence called higher in T for all
nine symptoms when sore throat is higher in S, and an invented patient count.
