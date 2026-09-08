# ВОС-999 and the "missing" звання in Резерв+ — closed 2026-09-08

## Outcome: there was no defect

Резерв+ showed **ВОС 999** and an **empty військове звання**. Profile: never served, no навчальні
збори, no військовий квиток, no ВЛК (holds a live відстрочка), automatically moved from призовник to
військовозобов'язаний on turning 25.

Both entries turned out to be fine.

- **ВОС 999** is a real code in the Перелік approved by наказом МОУ від 07.09.2020 № 317 (registered
  as z0927-20), розд. 10.14 «Без військової підготовки»: «Потребує проходження базової
  загальновійськової підготовки». Nothing to correct.
- **The звання is in the register.** Generating the військово-обліковий документ в електронній формі
  from Резерв+ and opening the downloaded file shows **«Солдат»**. What was blank was the app's
  screen, not «Оберіг».

**Nothing was filed.** `rank_and_vos/Zaiava_zvannia.docx` remains as a drafted, unfiled заява in
case something similar recurs; it is gitignored, along with the filled-in copy.

## The two lessons

1. **The app's screen is not the register.** The generated document is. Pull the eВОД — or the
   register extract under ст. 9 ч. 1 п. 1 Закону № 1951-VIII — *before* concluding data is missing.
   That would have answered the whole question in five minutes.
2. **«Солдат» without «запасу» is not worth chasing.** Ч. 4 ст. 5 Закону «Про військовий обов'язок і
   військову службу» does require the addition — «До військових звань громадян України, які
   перебувають у запасі … додаються слова відповідно "запасу"» — so the display is technically
   incomplete. But the eВОД carries «категорія обліку» as its own field (п. 8 п/п 11 Порядку № 559),
   so the reserve status is already stated. Convention, not missing data.

---

## The legal position, if this ever recurs

All acts below were read from `zakon.rada.gov.ua` on 2026-09-08 in the editions noted. **Re-check
before relying on any of it** — Порядок № 1487 alone was amended fourteen times between 2024 and
mid-2026.

### The obligation

**Абзац дев'ятнадцятий пункту 79** Порядку організації та ведення військового обліку призовників,
військовозобов'язаних та резервістів, затв. постановою КМУ від 30.12.2022 № 1487 — text as amended
through постанову № 812 від 10.06.2026. П. 79 opens «Районні (міські) територіальні центри
комплектування та соціальної підтримки:», and the абзац reads:

> «організовують внесення інформації до Єдиного державного реєстру призовників,
> військовозобов'язаних та резервістів у тридцятиденний строк після досягнення призовниками
> 25-річного віку **без їх виклику** до районних (міських) територіальних центрів комплектування та
> соціальної підтримки про зняття їх з військового обліку призовників та взяття на облік
> військовозобов'язаних **з одночасним присвоєнням військового звання “солдат (матрос) запасу” та
> зазначенням другої категорії запасу**;»

Added by постановою КМУ № 916 від 30.07.2025. The абзац number is rada's own arithmetic: the
paragraph before is annotated «Абзац вісімнадцятий», the one after «Абзац двадцятий … виключено».

Three consequences: the transfer and the rank are **one composite act** («з одночасним
присвоєнням»), so a moved status with a blank rank is half-performance; **no visit, ВЛК, військовий
квиток or БЗВП is a precondition** («без їх виклику»); and there is a **thirty-day term** running
from the 25th birthday. Turchyn's characterisation is the right one — «Це НЕ ПРАВО ТЦК, а ОБОВ'ЯЗОК».

«Категорія запасу» (ст. 27 Закону про військовий обов'язок — by service; second = did not serve) is
not «розряд запасу» (ст. 28 — by age). Practitioners conflate them.

### The instrument

No official form exists. **Ст. 9 ч. 1 п. 2 Закону № 1951-VIII** (редакція від 07.01.2026) gives the
right to apply «з мотивованою заявою», and **п. 43 Порядку, затв. постановою КМУ від 29.07.2026
№ 981** provides that corrections follow «за результатами розгляду відповідної мотивованої заяви».
Neither prescribes a form or an attachment list, so a free-form заява is correct — but it must be
*мотивована*, which is why the statutory quotations belong in it.

Small seam: ст. 9 conditions the application on the order set by the Реєстр's **адміністратор**,
while п. 43 sits in a Cabinet-approved Порядок. No administrator's procedure appears to be
published, which supports a free-form application rather than undermining it.

The addressee is the district/city ТЦК та СП — **ч. 8 ст. 5 Закону № 1951-VIII** lists the органи
ведення Реєстру (Міноборони, районні/міські ТЦК та СП, центри рекрутингу ЗСУ, СБУ, розвідувальні
органи). Not the regional centre.

**П. 8 Порядку, затв. постановою КМУ від 16.05.2024 № 559** is worth citing alongside: it lists what
the eВОД must contain — п/п 6 the окремий номер запису в Реєстрі, п/п 8 відстрочка/бронювання, п/п 9
військове звання, п/п 11 категорія обліку. It converts "my record is incomplete" into "the document
the State issues me fails its own required fields".

### Deadlines

- **Thirty days** from the 25th birthday for the entry itself (п. 79). Practitioners read it as time
  the ТЦК is *entitled* to take, so it only bites once expired.
- **Ст. 20 Закону «Про звернення громадян» № 393/96-ВР** for the reply: a month; «невідкладно, але
  не пізніше п'ятнадцяти днів» where no additional study is needed; forty-five days as the hard cap
  on an extended review.

### Filing, and the risk of it

Ст. 5 Закону № 393/96-ВР requires ПІБ, місце проживання, the substance, the request, and the
**signature with the date**; an e-mail address if filed electronically (a КЕП is not required).
Three channels — in person, post, e-mail. **By post**: рекомендованим листом з описом вкладення та
повідомленням про вручення. In person means two copies with the вхідний stamp on the second.

**Do not go in person.** Two lawyers on [uristy.ua № 145014](https://uristy.ua/ua/question/145014)
and [№ 147444](https://uristy.ua/ua/question/147444) warn that a заява «приверне до Вас зайву увагу»
and that turning up «закінчиться направленням Вас на ВЛК та подальшою можливою мобілізацією»; one
describes a повістка timed to pre-empt a бронювання. Weigh that against the fact that a blank or odd
звання blocks nothing: the Генштаб (letter 14.04.2026 № 300/301/121/ВихЗПІ) confirms ВОС 999 and
«солдат резерву» «не перешкоджає ні бронюванню, ні отриманню відстрочки», and п. 3 Порядку № 76
makes бронювання independent of звання, age and ВОС. What blocks бронювання is the status
«призовник».

If ignored: адвокатський запит, then an адміністративний позов. Courts hold that a ТЦК must not
merely decide but **also enter the data**, that the burden cannot be shifted onto the citizen, and
that technical problems in the register do not excuse inaction.

### One contrary opinion, for completeness

Кирда (№ 145014) holds that «зміна статусу з призовника на військовозобов'язаного вимагає особистої
присутності в ТЦК та СП … необхідністю проходження ВЛК». He cites no norm, two colleagues contradict
him, and п. 79 says the opposite — but it is the answer a ТЦК may give.

### Addressee used here

**Шевченківський районний ТЦК та СП**, вул. Батуринська, 2, м. Львів, 79058 (shared with
Галицько-Франківський and Личаківсько-Залізничний), `she@post.mil.gov.ua`, (066) 814-34-79 — from
the Ministry's own [Довідник](https://mod.gov.ua/assets/Dodatok_04_11_25_d9eb4cdb59.pdf) of
04.11.2025, entry № 289. Unresolved: ArmyInform gives the landline (032) 255-39-80 and index 79007
against the building's 79058. Easy to conclude this centre does not exist — it is filed at № 289,
after Червоноградський, rather than among the other Lviv entries.

---

## How the заява document is produced

`rank_and_vos/Zaiava_zvannia.docx` is `rank_and_vos/source/Заява.docx` — Dmytro's own template —
with the wording replaced by `rank_and_vos/rewrite_zaiava.py` (paragraph index → new text, each
paragraph keeping its own `w:pPr` and the `w:rPr` of its first run). Body set to Times New Roman
12 pt, 1.5 spacing, justified; the addressee/applicant block left untouched.

**Do not regenerate it through `code/build/build_docx.py`** — that was tried and it imposed the
builder's own layout, destroying the addressee block, the centred title and the spacing.

Two words in it must not be "corrected" by `/style-check`: «присвоєння» (LanguageTool wants
«надання») and «недостовірних». Both are quoted verbatim from the statutes.

## Sources

- [Порядок № 1487](https://zakon.rada.gov.ua/laws/show/1487-2022-%D0%BF) — абз. 19 п. 79
- [Закон № 1951-VIII](https://zakon.rada.gov.ua/laws/show/1951-19) — ч. 8 ст. 5, ст. 9
- [Порядок № 981](https://zakon.rada.gov.ua/laws/show/981-2026-%D0%BF) — п. 43
- [Порядок № 559](https://zakon.rada.gov.ua/laws/show/559-2024-%D0%BF) — п. 4, п. 7, п. 8
- [Закон «Про звернення громадян» № 393/96-ВР](https://zakon.rada.gov.ua/laws/show/393/96-%D0%B2%D1%80) — ст. 5, ст. 20
- [Закон «Про військовий обов'язок і військову службу» № 2232-XII](https://zakon.rada.gov.ua/laws/show/2232-12) — ч. 4 ст. 5, ст. 27, ст. 28
- [Наказ МОУ від 07.09.2020 № 317 — Перелік ВОС (z0927-20)](https://zakon.rada.gov.ua/laws/show/z0927-20) — розд. 10.14, код 999
- [Порядок бронювання № 76](https://zakon.rada.gov.ua/laws/show/76-2023-%D0%BF) — п. 3
- [uristy.ua № 145014](https://uristy.ua/ua/question/145014) · [№ 147444](https://uristy.ua/ua/question/147444) — nine practitioner answers on the same fact pattern
- [Роз'яснення Генштабу про «солдат резерву» / ВОС 999](https://kadroland.com/news/9618-soldat-rezervu-u-rezerv-kogo-ce-stosujetsya-i-ci-vplivaje)
- [Судова практика — примусити ТЦК оновити «Оберіг» (НААУ)](https://unba.org.ua/publications/10491-yak-zmusiti-tck-onoviti-dani-v-reestri-oberig-sudova-praktika.html)
- [Довідник телефонів та е-адрес ТЦК та СП, 04.11.2025 (PDF)](https://mod.gov.ua/assets/Dodatok_04_11_25_d9eb4cdb59.pdf)
