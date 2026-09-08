---
name: build-docx
description: Rebuild a Word deliverable from its markdown template with code/build/build_docx.py and verify the output structurally before handing it over. Use whenever the user says "rebuild the docx / now do doc / build the document", after any template edit that has to reach a .docx, or when the user reports formulas, captions or lists rendering wrongly in Word.
---

# Build a .docx deliverable and verify it before delivery

Deliveries have reached Dmytro with defects he found himself: figure captions above their
figures, one list's numbering running on into the next, display formulas left unconverted — and
once a reported "0 display equations" defect that did not exist, because the session's ad-hoc
checker keyed on the wrong thing. Every one of those sessions wrote a fresh inspection script
from scratch. This skill fixes the check once.

## 1. Preflight

- Ukrainian prose: the template has passed `/style-check` (exit 0) since its last edit.
- Word locks the file. If `~$<name>.docx` exists next to the target, build to a scratchpad path
  and tell Dmytro to close Word before the final build.
- Wide equations: `venv/Scripts/python.exe code/build/linebreak_eqs.py <template.md>` (dry run).
  If it reports rows, re-run with `--apply`, then re-run the dry run until it reports nothing.

## 2. Build

```bash
PYTHONUTF8=1 venv/Scripts/python.exe code/build/build_docx.py <template.md> <out.docx>
```

Run it from the repo root. The venv carries `pypandoc_binary`, so pandoc needs no separate
install; the system interpreter also works if the venv is missing.

Read the summary line (`N unique equations, N display slots, N tables, N lists, N images`) and
compare with the template: display slots must equal the number of `$$…$$` lines, images the
number of `![](…)` lines. A mismatch is a defect in the template (a `$$` line with trailing
punctuation, a multi-line `$$`), not in the builder.

## 3. Verify structurally — Word is the only renderer, never LibreOffice

Write this once per session to the scratchpad and run it with `PYTHONUTF8=1`; do not eyeball
`document.xml` and do not re-derive the checks.

```python
import re, sys, zipfile
x = zipfile.ZipFile(sys.argv[1]).read("word/document.xml").decode("utf-8")
n = zipfile.ZipFile(sys.argv[1]).read("word/numbering.xml").decode("utf-8")
strip = lambda s: re.sub(r"<[^>]+>", "", s)

# (a) slots Word draws as empty dotted boxes
print("empty m:e/m:sub/m:sup :", len(re.findall(r"<m:(e|sub|sup)/>", x)), "(must be 0)")
# (b) eqArr artefacts from line-broken equations
print("literal & in math      :", sum("&amp;" in strip(t) for t in re.findall(r"<m:eqArr>.*?</m:eqArr>", x, re.S)), "(must be 0)")
# (c) every list restarts at 1
print("w:num / startOverride  :", n.count("<w:num "), "/", n.count("startOverride"), "(must be equal)")
# (d) figure captions sit directly under a drawing, regular weight, centred, and were
# recognised as captions at all. A caption whose `*[Рисунок …]*` line is wrapped over
# several lines in the template is NOT matched (FIGURE_RE is single-line) and falls
# through to body text: italic, justified, brackets visible.
paras = re.findall(r"<w:p[ >].*?</w:p>", x, re.S)
bad = []
for i, p in enumerate(paras):
    t = strip(p).strip()
    if "Рисунок" in t[:12]:
        if i == 0 or "<w:drawing>" not in paras[i - 1]:
            bad.append(("not under image", t[:40]))
        if "<w:b/>" in p:
            bad.append(("bold", t[:40]))
        if t.startswith("[") or "<w:i/>" in p or 'w:val="center"' not in p:
            bad.append(("fell through to body text — join the caption onto ONE line", t[:40]))
print("caption problems       :", bad or "none")
# (e) display equations present. An equation's SYMBOLS are text inside <m:t>, so
# stripping tags leaves them behind -- delete the math runs first, then look at what
# is left over. Anything but an equation number means the paragraph is prose.
disp = 0
for p in paras:
    if "<m:oMath" not in p:
        continue
    outside = strip(re.sub(r"<m:oMath[ >].*?</m:oMath>", "", p, flags=re.S)).strip()
    if not re.sub(r"[\s\d.()—-]", "", outside):
        disp += 1
print("oMath blocks           :", x.count("<m:oMath"), "| display-equation paragraphs:", disp)
```

- (a) and (b) must be 0 — fix the template or the equation, rebuild, re-run until they are.
- (c) unequal means a list continues the previous list's numbering.
- (d) any entry means a caption is above its figure, bold, or not recognised as a caption. The
  template convention is `![](media/x.png)`, blank line, `*[Рисунок N.M — Назва]*`. **Regular
  weight, centred, below the figure** — that is the ДСТУ 3008:2015 form and the default here;
  bold is reserved for structural headings and table column heads. A bold-label caption form
  belongs only to a document that follows its own source's typography (e.g. a translation), and
  must never be carried onto anything else. A delivery once went out with every caption bold
  because that exception was applied to the wrong document, and the flag was waved off as a
  false positive.
- (e) compare the display-equation count with the template's `$$` line count. A display equation
  is unnumbered by default (ДСТУ numbers only formulas referenced in the text), so never test for
  tab stops or equation numbers — but a trailing `(N)` is allowed and the check tolerates it.
  **Do not "simplify" this back to stripping tags and testing the leftover text**: an equation's
  symbols live in `<m:t>` text nodes, so they survive tag-stripping and every real equation then
  reads as prose. That version printed 0 for a document holding 16 display equations.
  The count runs slightly ABOVE the `$$` count, because a table cell whose entire content is
  inline math (`$n_1$`, `$B$`, `$U_2/U_1$`) is also a math-only paragraph. Expect
  `count >= $$ lines`; only a count BELOW the `$$` line count is a defect.

## 4. Deliver

Send the file with `SendUserFile` and the five numbers above. Say plainly what this did not
check: the visual look in Word, which only Dmytro can confirm. Nothing is committed.
