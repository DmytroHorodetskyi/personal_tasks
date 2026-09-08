# ВОС-999 and the missing звання in Резерв+

## The matter

Резерв+ (mirroring «Оберіг») shows **ВОС 999** and an **empty військове звання**. Profile: never
served, no навчальні збори or specialised training, no військовий квиток, no ВЛК (holds a
відстрочка), automatically moved from призовник to військовозобов'язаний on turning 25.

## Position established (see `RESEARCH.md`)

- **ВОС 999 is correct and needs nothing.** Confirmed from the primary source: it is a real code in
  the Перелік approved by наказом МОУ від 07.09.2020 № 317, розд. 10.14 «Без військової
  підготовки» — «Потребує проходження базової загальновійськової підготовки».
- **The empty звання is the defect.** П. 79 Порядку № 1487 transfers to військовозобов'язаний at 25
  «без їх виклику» and **«з одночасним присвоєнням військового звання "солдат (матрос) запасу"»**,
  within **thirty days** of the birthday. Transfer and rank are one act; a flipped status with a
  blank rank is half-performance.
- No військовий квиток, ВЛК or БЗВП is a precondition for it.

## State

- `RESEARCH.md` — the legal position as of 2026-09-08, both open items from the earlier session
  closed.
- Nothing filed yet.

## Next steps

1. Try Резерв+ → «…» → «Виправити дані онлайн»; screenshot whatever it returns.
2. Screenshot the eВОД screen showing status = військовозобов'язаний with звання blank, **dated**.
3. Consider an inquiry under ст. 9 ч. 1 п. 1 Закону № 1951-VIII for one's own register data, to
   confirm the blank is in the register and not just in the app (`RESEARCH.md` §5).
4. Then the мотивована заява to the **district / city** ТЦК та СП.

## How the заява is produced — edit Dmytro's file, do not rebuild it

`Zaiava_zvannia.docx` is **`../registry_application/source/Заява.docx` with the wording replaced**,
produced by `rewrite_zaiava.py` (paragraph index → new text; each paragraph keeps its own `w:pPr`
and the `w:rPr` of its first run). Layout, fonts, indents and spacing are Dmytro's.

**Do not regenerate this document through `code/build/build_docx.py`.** That was tried first and
was wrong: the builder imposes its own layout and destroyed the right-aligned addressee block, the
centred title and the spacing. The markdown template it was built from has been deleted. `/style-check`
therefore does not apply here either — the prose lives in the `.docx`, and its register was read by
eye against `knowledge/WRITING_STYLE.md` §2, §2b.

Two things the scan flagged on the earlier markdown version that must **not** be "corrected" if it
is ever run on this text: «присвоєння» (LT wants «надання») and «недостовірних» — both are quoted
verbatim from п. 79 Порядку № 1487 and ст. 9 Закону № 1951-VIII. Paraphrasing a statute you are
quoting is a defect, not a fix.

## ДОДАТКИ — deliberately left empty

The heading stays, the list does not, as in Dmytro's original. Nothing in ст. 5 Закону № 393/96-ВР
or п. 43 Порядку № 981 requires attachments or a list of them, and п. 79 obliges the ТЦК to act
«без їх виклику» — on data it already holds, with nothing supplied by the applicant. An earlier
draft carried a four-item ДОДАТКИ list; it was invented from a secondary article and general
practice, not from any rule, and Dmytro removed it. Hand documents over at the counter if asked.

## Open questions for Dmytro

1. **Is this the matter the `Заява.docx` template is actually for?** The template as transferred is
   written for a бронювання missing from the Реєстр (see `../registry_application/`). If the rank is
   the live problem, say so and the template gets repurposed for this instead — the instrument and
   the formal requirements are the same, only the facts, the legal grounds and the ПРОШУ change.
2. Date of the 25th birthday — it sets the thirty-day term.
3. Which district/city ТЦК та СП he is on accounting at.
4. What Резерв+ shows in the **розряд запасу** field, if it shows one at all.
