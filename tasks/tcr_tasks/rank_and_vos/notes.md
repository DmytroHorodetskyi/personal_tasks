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

- `RESEARCH.md` — the legal position as of 2026-09-08, verified against practitioner sources
  (§4a) with the two things that verification turned up (§4b).
- `Zaiava_zvannia.docx` — drafted, placeholders unfilled, **not filed**.
- Резерв+ «Виправити дані онлайн» was tried and refused.

## Decide before filing: is anything actually blocked?

The verification pass (`RESEARCH.md` §4b) changed the picture. A blank звання appears to have no
consequence — the Генштаб says ВОС 999 and «солдат резерву» obstruct neither бронювання nor a
відстрочка, п. 3 Порядку № 76 makes бронювання independent of звання, ВОС and age, and what blocks
бронювання is the status «призовник», which has already moved here. Meanwhile two lawyers warn that
a заява «приверне до Вас зайву увагу», and that appearing in person risks a ВЛК referral and
mobilisation.

So: **file it if the blank звання is blocking something concrete**, or if a paper trail is wanted
before escalating. Otherwise the cheap steps are the whole answer. Either way, **by post, never in
person.**

The deferment is live and registered — confirmed by Dmytro 2026-09-08 — so a ВЛК referral, the main
risk of engaging the ТЦК, is much less dangerous while it holds. That is also the reason he was
advised to sort the rank out now rather than later.

## Next steps

1. Log out of Резерв+ and re-verify through BankID — data sometimes fails to refresh and needs
   re-identification (Турчин).
2. Pull the full register extract («повні дані з реєстру Оберіг») — this is also the ст. 9 ч. 1 п. 1
   route, and it settles whether the blank is in the register or only in the app.
3. Screenshot the eВОД screen showing status = військовозобов'язаний with звання blank, **dated**.
4. Read абз. 19 п. 79 in the current редакція of Порядок № 1487 (`RESEARCH.md` §5 — it could not be
   read from rada, only from practitioners quoting it).
5. Only then, if warranted: the заява, рекомендованим листом з описом вкладення.

## How the заява is produced — edit Dmytro's file, do not rebuild it

`Zaiava_zvannia.docx` is **`source/Заява.docx` with the wording replaced**,
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

1. Date of the 25th birthday — it sets the thirty-day term.
2. Which district/city ТЦК та СП he is on accounting at, and its address.
3. What Резерв+ shows in the **розряд запасу** field, if it shows one at all.
4. The rest of the header block: ПІБ, date of birth, РНОКПП, addresses, e-mail, telephone.

The `Заява.docx` in `source/` was originally written for a бронювання missing from the Реєстр.
That matter is not live — the rank is the only problem — so the template was repurposed and the
бронювання research deleted (2026-09-08). The instrument and the formal requirements are the same
either way; only the facts, the legal grounds and the ПРОШУ differ.
