"""
Generic markdown -> Word (.docx) builder for the translation/deliverable docs.

    python build_docx.py <input.md> <output.docx>

Reuses the layout/packaging engine from docx_engine.py (Times New Roman 14 pt,
1.5 spacing, justified prose, bordered tables, stdlib-only .docx zip). The ONE
thing this file adds is equation handling that scales: display equations are
written in the markdown as LaTeX ($$...$$, with an optional trailing (label)
such as (1.1)) and inline math as $...$; every LaTeX snippet is converted to
native Word OMML in a single pandoc pass and spliced into the document. Because
the equations live in the markdown as data, there is no per-document Python file
to maintain -- any deliverable builds through this one script.

Markdown conventions understood:
  # Title                     -> centered bold document title
  ## Розділ N. ...            -> Heading 1
  ## N.M. ...                 -> Heading 2
  ### N.M.K. ...              -> Heading 3
  Таблиця N. ...              -> table caption (left)
  1. item / 2. item           -> real numbered list (Word auto-numbers; own numId per list)
  - item / * item             -> real bulleted list
  | a | b |                   -> Word table (|---| separator row dropped)
  *[Рисунок N. ...]*          -> italic centered figure placeholder
  <!-- ... -->                -> dropped (translator-note blocks, inline or multi-line)
  $$LaTeX$$  (optional (1.1)) -> display equation centred on the text column, the
                                 number (verbatim) set flush to the right margin
  ...$inline LaTeX$...        -> inline OMML inside a prose paragraph
  &nbsp;                      -> stripped (was only a markdown-preview indent hack)

Requires pandoc (via `pypandoc_binary`, install with the trusted-host recipe):
  python -m pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org pypandoc_binary
"""
from __future__ import annotations

import os
import re
import sys
import zipfile

import pypandoc

from docx_engine import (
    FONT, SZ, LINE, TEXT_W, TEXT_W_LANDSCAPE,
    esc, wrun, wpar, sect_break_par,
    document_xml, CONTENT_TYPES, RELS, DOC_RELS,
)
from omml_prescript import fix_prescripts
from omml_eqarr import clean_eqarr


# ---------------------------------------------------------------------------
# LaTeX -> OMML  (single pandoc pass over the unique snippets)
# ---------------------------------------------------------------------------

def latex_to_omml(snippets):
    """Map each unique LaTeX snippet -> its <m:oMath>...</m:oMath> OMML.

    All snippets are converted in ONE pandoc invocation: each is emitted as its
    own `$$...$$` paragraph, pandoc's docx writer turns every one into exactly
    one <m:oMath> block, and the blocks come back in input order.
    """
    uniq = list(dict.fromkeys(s for s in snippets if s.strip()))
    if not uniq:
        return {}
    blocks = _pandoc_omml("\n\n".join("$$" + s + "$$" for s in uniq))
    if len(blocks) == len(uniq):
        # Rewrite Chen's left-subscript {}_{k} (empty-base subscript -> a dotted box in
        # Word) into proper OMML prescripts. No-op for snippets without one.
        blocks = [fix_prescripts(b) for b in blocks]
        # Clean texmath's <m:eqArr> for line-broken eqs: drop empty-row boxes and the
        # literal '&' alignment runs it leaks. No-op for snippets without an eqArr.
        blocks = [clean_eqarr(b) for b in blocks]
        return dict(zip(uniq, blocks))
    # Count mismatch => at least one snippet failed to parse as a single display
    # equation (pandoc drops it to raw text). Re-run per snippet to name the
    # culprit(s) precisely -- invaluable when transcribing LaTeX by hand.
    bad = [s for s in uniq if len(_pandoc_omml("$$" + s + "$$")) != 1]
    raise RuntimeError(
        "pandoc could not convert %d equation(s) to OMML:\n  %s"
        % (len(bad), "\n  ".join(bad)))


def _pandoc_omml(md):
    tmp = os.path.join(os.environ.get("TEMP", "."), "_build_docx_omml.docx")
    pypandoc.convert_text(md, "docx", format="markdown", outputfile=tmp)
    with zipfile.ZipFile(tmp) as z:
        doc = z.read("word/document.xml").decode("utf-8")
    return re.findall(r"<m:oMath>.*?</m:oMath>", doc, re.S)


# ---------------------------------------------------------------------------
# Inline markdown cleanup (drop code/emphasis markers) for non-math text
# ---------------------------------------------------------------------------

_ESC_STAR = ""          # private-use sentinel guarding an escaped \*


def _clean_inline(s):
    """Plain text for cells/captions/figures: drop code + emphasis markers,
    turn an escaped \\* into a literal asterisk."""
    s = s.replace("\\*", _ESC_STAR)
    s = re.sub(r"`([^`]*)`", r"\1", s)          # drop code backticks, keep text
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)      # **bold** -> text
    s = re.sub(r"\*(.+?)\*", r"\1", s)          # *italic* -> text
    return s.replace(_ESC_STAR, "*")


def _keep_marks(s):
    """Drop code backticks; keep ** / * emphasis markers for the run tokenizer."""
    s = s.replace("\\*", _ESC_STAR)
    s = re.sub(r"`([^`]*)`", r"\1", s)
    return s.replace(_ESC_STAR, "*")


# ---------------------------------------------------------------------------
# Markdown parsing  ->  block list
# ---------------------------------------------------------------------------

NBSP_RE = re.compile(r"(?:&nbsp;)+")
COMMENT_OPEN = "<!--"
COMMENT_CLOSE = "-->"
DISPEQ_RE = re.compile(r"^\$\$(?P<tex>.+?)\$\$\s*(?:\((?P<label>[^()]+)\))?\s*$")
FIGURE_RE = re.compile(r"^\*\[(?P<txt>.+)\]\*$")
IMAGE_RE = re.compile(r"^!\[(?P<alt>[^\]]*)\]\((?P<path>[^)]+)\)$")   # ![alt](media/x.png)
OLITEM_RE = re.compile(r"^(\d+)\.\s+(.*)$")     # "1. text" ordered-list item
ULITEM_RE = re.compile(r"^[-*]\s+(.*)$")        # "- text" / "* text" bullet item
# "Таблиця 5.2 — Назва" (ДСТУ) or the older "Таблиця 5.2. Назва" -- the dash/period
# after the number is what separates a caption from a sentence that merely opens with
# the same words ("Таблиця 5.2 є підсумком усіх…").
TBL_CAPTION_RE = re.compile(r"^Таблиця\s+[\d.]+\s*(?:[—–-]\s|\.\s)")
LANDSCAPE_RE = re.compile(r"^<!--\s*landscape\s*-->$")   # force the next table sideways


def _strip_nbsp(s):
    return NBSP_RE.sub(" ", s).strip()


MATH_SPLIT = re.compile(r"(?<!\\)\$")     # a $ delimiter, but not an escaped \$ (currency)


def _split_math(text):
    """Split on unescaped $ -> [text, math, text, math, ...]. Literal dollar
    amounts are written \\$ and stay inside the text segments."""
    return MATH_SPLIT.split(text)


def _untext(seg):
    """Un-escape \\$ back to a literal $ for a text (non-math) segment."""
    return seg.replace("\\$", "$")


def _inline_math(text):
    """LaTeX snippets (without $) inside a $...$-bearing string, in order."""
    return [seg.strip() for i, seg in enumerate(_split_math(text))
            if i % 2 == 1 and seg.strip()]


def parse_md(path):
    with open(path, encoding="utf-8") as fh:
        lines = fh.read().splitlines()

    blocks = []
    para = []
    table = []
    in_comment = False

    def flush_para():
        if para:
            blocks.append(("par", " ".join(para)))
            para.clear()

    def flush_table():
        if table:
            rows = []
            for r in table:
                cells = [c.strip() for c in r.strip().strip("|").split("|")]
                if cells and all(re.fullmatch(r":?-{2,}:?", c) for c in cells):
                    continue
                # keep cells RAW here -- _cell_runs() strips emphasis after the
                # $...$ split, and cleaning twice would turn an escaped \* into a
                # bare * that the second pass then eats as an italic marker.
                rows.append(list(cells))
            blocks.append(("table", rows))
            table.clear()

    for raw in lines:
        # a directive comment, read before comments are stripped away
        if not in_comment and LANDSCAPE_RE.match(raw.strip()):
            flush_para(); flush_table()
            blocks.append(("landscape", None))
            continue
        # comment blocks (translator notes), inline or spanning many lines
        if in_comment:
            if COMMENT_CLOSE in raw:
                in_comment = False
                raw = raw.split(COMMENT_CLOSE, 1)[1]
                if raw.strip() == "":
                    continue
            else:
                continue
        while COMMENT_OPEN in raw:
            before, rest = raw.split(COMMENT_OPEN, 1)
            if COMMENT_CLOSE in rest:
                raw = before + rest.split(COMMENT_CLOSE, 1)[1]
            else:
                raw = before
                in_comment = True
                break

        s = _strip_nbsp(raw)
        if s == "":
            flush_para(); flush_table()
            continue

        # standalone thematic break (chapter separator) -> drop; not part of the report
        if re.fullmatch(r"-{3,}", s):
            flush_para(); flush_table()
            continue

        if s.startswith("# "):
            flush_para(); flush_table()
            blocks.append(("title", s[2:].strip()))
            continue
        if s.startswith("#### "):
            flush_para(); flush_table()
            blocks.append(("h4", s[5:].strip()))
            continue
        if s.startswith("### "):
            flush_para(); flush_table()
            blocks.append(("h3", s[4:].strip()))
            continue
        if s.startswith("## "):
            flush_para(); flush_table()
            head = s[3:].strip()
            kind = "h1" if head.lower().startswith("розділ") else "h2"
            blocks.append((kind, head))
            continue

        if s.startswith("|") and s.endswith("|"):
            flush_para()
            table.append(s)
            continue
        flush_table()

        mimg = IMAGE_RE.match(s)
        if mimg:
            flush_para()
            blocks.append(("image", (mimg.group("alt"), mimg.group("path"))))
            continue

        mfig = FIGURE_RE.match(s)
        if mfig:
            flush_para()
            blocks.append(("figure", _keep_marks(mfig.group("txt"))))
            continue

        # A caption is "Таблиця N.M — Назва" (ДСТУ) or the older "Таблиця N.M. Назва".
        # The number must be followed by a dash or a period, otherwise a sentence that
        # merely OPENS with the words ("Таблиця 5.2 є підсумком усіх…") is swallowed as
        # a caption and loses its indent.
        if TBL_CAPTION_RE.match(s):
            flush_para()
            blocks.append(("caption", _clean_inline(s)))
            continue

        meq = DISPEQ_RE.match(s)
        if meq:
            flush_para()
            tex = meq.group("tex").strip()
            blocks.append(("dispeq", (tex, meq.group("label"))))
            continue

        para.append(s)

    flush_para(); flush_table()

    # collect EVERY LaTeX snippet (display + inline in prose/caption/figure/cells)
    latex = []
    for kind, data in blocks:
        if kind == "dispeq":
            latex.append(data[0])
        elif kind in ("par", "caption", "figure"):
            latex += _inline_math(data)
        elif kind == "table":
            for row in data:
                for cell in row:
                    latex += _inline_math(cell)
    return blocks, latex


# ---------------------------------------------------------------------------
# Block -> WordprocessingML
# ---------------------------------------------------------------------------

def _text_runs(seg):
    """Plain-text segment with **bold** / *italic* markers -> list of w:r runs.

    An escaped \\* stays parked on _ESC_STAR until AFTER the emphasis split, so a
    literal asterisk (the multiplication sign in a formula written in prose) is
    never mistaken for an italic marker."""
    seg = re.sub(r"`([^`]*)`", r"\1", seg.replace("\\*", _ESC_STAR))
    runs = []
    for tok in re.split(r"(\*\*.+?\*\*|\*[^*]+?\*)", seg):
        if not tok:
            continue
        if tok.startswith("**") and tok.endswith("**"):
            runs.append(wrun(tok[2:-2].replace(_ESC_STAR, "*"), bold=True))
        elif tok.startswith("*") and tok.endswith("*") and len(tok) > 2:
            runs.append(wrun(tok[1:-1].replace(_ESC_STAR, "*"), italic=True))
        else:
            runs.append(wrun(tok.replace(_ESC_STAR, "*")))
    return runs


def build_runs(text, omml):
    """Prose with inline $...$ math -> mix of w:r and inline m:oMath."""
    out = []
    for i, seg in enumerate(_split_math(text)):
        if i % 2 == 0:
            out.extend(_text_runs(_untext(seg)))
        else:
            block = omml.get(seg.strip())      # already a full <m:oMath>...</m:oMath>
            out.append(block if block else wrun(seg))
    return "".join(out)


def heading_par(text, level):
    jc = "center" if level == 1 else "left"
    return ("<w:p><w:pPr><w:pStyle w:val=\"Heading%d\"/><w:jc w:val=\"%s\"/></w:pPr>"
            "<w:r><w:rPr><w:b/></w:rPr><w:t xml:space=\"preserve\">%s</w:t></w:r></w:p>"
            % (level, jc, esc(text)))


def title_par(text):
    return ("<w:p><w:pPr><w:jc w:val=\"center\"/><w:spacing w:after=\"240\"/></w:pPr>"
            "<w:r><w:rPr><w:b/></w:rPr><w:t xml:space=\"preserve\">%s</w:t></w:r></w:p>"
            % esc(text))


def body_par(runs_xml):
    """A prose paragraph: justified, 1.25 cm first-line indent (709 twips), and no
    extra spacing between paragraphs -- the academic-Ukrainian convention. Paragraphs
    are separated by the first-line indent, not by a blank gap."""
    return ("<w:p><w:pPr><w:ind w:firstLine=\"709\"/><w:jc w:val=\"both\"/></w:pPr>%s</w:p>"
            % runs_xml)


def dispeq_par(omml, label):
    """Display equation. `omml` is a full <m:oMath>...</m:oMath> block from pandoc.

    Numbered equations use the standard academic layout: a CENTRE tab (equation
    centred on the text column) followed by a RIGHT tab (the number flush against
    the right margin). Unnumbered equations are simply centred. Tab positions are
    in twips from the left text margin: text width = 11906 - 1701 - 850 = 9355,
    so the centre tab sits at 4677 and the right tab at 9355."""
    # ДСТУ 3008:2015 wants at least one blank line above/below; build_body brackets each
    # formula with a real empty paragraph (blank line), so no per-paragraph spacing here.
    if not label:
        return ("<w:p><w:pPr><w:jc w:val=\"center\"/></w:pPr>%s"
                "<w:r><w:t xml:space=\"preserve\"> </w:t></w:r></w:p>" % omml)
    tabs = ("<w:tabs><w:tab w:val=\"center\" w:pos=\"4677\"/>"
            "<w:tab w:val=\"right\" w:pos=\"9355\"/></w:tabs>")
    return ("<w:p><w:pPr>%s</w:pPr>"
            "<w:r><w:tab/></w:r>%s<w:r><w:tab/></w:r>"
            "<w:r><w:t xml:space=\"preserve\">(%s)</w:t></w:r></w:p>"
            % (tabs, omml, esc(label)))


def figure_par(text, omml):
    """Figure caption: centered, non-italic, honoring **bold**/*italic* markers and
    inline $...$ math (same run tokenizer as prose)."""
    return "<w:p><w:pPr><w:jc w:val=\"center\"/></w:pPr>%s</w:p>" % build_runs(text, omml)


# ---------------------------------------------------------------------------
# Images (embedded PNG/JPEG; stdlib-only, no PIL)
# ---------------------------------------------------------------------------

EMU_PER_TWIP = 635
TEXT_WIDTH_TWIPS = 9355                       # 11906 - 1701 - 850 (cf. dispeq_par)
MAX_IMG_EMU = int(TEXT_WIDTH_TWIPS * EMU_PER_TWIP * 0.65)   # ~65% of the text column
EMU_PER_PX_96 = 9525                          # 914400 EMU/in ÷ 96 px/in


def _png_size(path):
    """(width_px, height_px) read from a PNG IHDR header — stdlib, no PIL."""
    with open(path, "rb") as fh:
        head = fh.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("not a PNG (only PNG sizing is supported): %s" % path)
    return int.from_bytes(head[16:20], "big"), int.from_bytes(head[20:24], "big")


ALT_WIDTH_RE = re.compile(r"\|\s*(\d{1,3})\s*%?\s*$")   # ![Рисунок 1|96](media/x.png)


def _alt_width_frac(alt, default=0.65):
    """Fraction of the text column an image should occupy.

    Defaults to 0.65, which suits the portrait-ish scans in the Chen translation.
    A wide chart is unreadable at that size, so a figure may ask for more with a
    trailing `|NN` in its alt text (NN = per cent of the text column, max 100)."""
    m = ALT_WIDTH_RE.search(alt or "")
    if not m:
        return default
    return max(5, min(100, int(m.group(1)))) / 100.0


def _img_extent_emu(path, frac=0.65):
    """Display size in EMU: native at 96 dpi, scaled to `frac` of the text column."""
    w_px, h_px = _png_size(path)
    cx, cy = w_px * EMU_PER_PX_96, h_px * EMU_PER_PX_96
    cap = int(TEXT_WIDTH_TWIPS * EMU_PER_TWIP * frac)
    if cx > cap:
        cy = int(cy * cap / cx)
        cx = cap
    return cx, cy


def image_par(alt, rid, cx, cy, docpr_id):
    """A centered paragraph holding one inline picture referenced by relationship rid."""
    name = esc(alt or ("image%d" % docpr_id))
    drawing = (
        "<w:drawing><wp:inline distT=\"0\" distB=\"0\" distL=\"0\" distR=\"0\">"
        "<wp:extent cx=\"%d\" cy=\"%d\"/>"
        "<wp:effectExtent l=\"0\" t=\"0\" r=\"0\" b=\"0\"/>"
        "<wp:docPr id=\"%d\" name=\"%s\"/>"
        "<wp:cNvGraphicFramePr><a:graphicFrameLocks noChangeAspect=\"1\"/></wp:cNvGraphicFramePr>"
        "<a:graphic><a:graphicData uri=\"http://schemas.openxmlformats.org/drawingml/2006/picture\">"
        "<pic:pic><pic:nvPicPr><pic:cNvPr id=\"%d\" name=\"%s\"/><pic:cNvPicPr/></pic:nvPicPr>"
        "<pic:blipFill><a:blip r:embed=\"%s\"/><a:stretch><a:fillRect/></a:stretch></pic:blipFill>"
        "<pic:spPr><a:xfrm><a:off x=\"0\" y=\"0\"/><a:ext cx=\"%d\" cy=\"%d\"/></a:xfrm>"
        "<a:prstGeom prst=\"rect\"><a:avLst/></a:prstGeom></pic:spPr></pic:pic>"
        "</a:graphicData></a:graphic></wp:inline></w:drawing>"
        % (cx, cy, docpr_id, name, docpr_id, name, rid, cx, cy)
    )
    return "<w:p><w:pPr><w:jc w:val=\"center\"/></w:pPr><w:r>%s</w:r></w:p>" % drawing


def doc_rels_xml(image_rels_xml):
    """document.xml.rels: fixed styles+numbering rels plus any image rels."""
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">"
        "<Relationship Id=\"rId1\" "
        "Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles\" "
        "Target=\"styles.xml\"/>"
        "<Relationship Id=\"rId2\" "
        "Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering\" "
        "Target=\"numbering.xml\"/>"
        "<Relationship Id=\"rId900\" "
        "Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/header\" "
        "Target=\"header1.xml\"/>"
        + image_rels_xml +
        "</Relationships>"
    )


def header_xml():
    """Default page header: page number in the top-right corner (ДСТУ 3008:2015).
    A right-aligned paragraph carrying a PAGE field; font/size inherit docDefaults."""
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<w:hdr xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" "
        "xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\">"
        "<w:p><w:pPr><w:jc w:val=\"right\"/></w:pPr>"
        "<w:r><w:fldChar w:fldCharType=\"begin\"/></w:r>"
        "<w:r><w:instrText xml:space=\"preserve\"> PAGE </w:instrText></w:r>"
        "<w:r><w:fldChar w:fldCharType=\"end\"/></w:r>"
        "</w:p></w:hdr>"
    )


TABLE_SZ = "24"     # 12 pt (half-points); ДСТУ guides set tables at 12 pt, not the 14 pt body


def _cell_runs(text, omml, bold=False):
    """Table-cell content: emphasis markers dropped, $...$ -> inline OMML.
    `bold` bolds the plain-text runs (used for the header row / головка).
    Plain-text runs are set at the 12 pt table size; inline math keeps its own size."""
    out = []
    for i, seg in enumerate(_split_math(text)):
        if i % 2 == 0:
            seg = _clean_inline(_untext(seg))
            if seg:
                out.append(wrun(seg, bold=bold, sz=TABLE_SZ))
        else:
            out.append(omml.get(seg.strip()) or wrun(seg, bold=bold, sz=TABLE_SZ))
    return "".join(out) or wrun("", sz=TABLE_SZ)


# A cell is "numeric" (centered) if it has at least one digit and only digit/unit/
# punctuation characters -- e.g. "369", "21.7m", "0.5\*", "15.4%–90.0%". Row-label
# cells contain Cyrillic words and stay left-aligned.
#
# The class must cover the typographic signs Ukrainian tables actually use, not just
# ASCII: U+2212 MINUS SIGN for negatives and U+2248 for "≈". Both were missing until
# 2026-09-07, so "−211" and "≈ 16 646 100" fell through to left alignment while the
# plain numbers beside them were centred -- the misalignment Dmytro spotted in the
# pneumonia v3 tables. U+00A0 is here too: a non-breaking thousands space is common.
_NUMERIC_CELL = re.compile("^[\\s\\d.,%()\\-–—/*\\\\a-zA-Z−≈ ±<>=~]+$")


def _is_numeric_cell(text):
    t = text.replace("\\*", "*").strip()
    # A dash standing for "not applicable" belongs to the number column and is centred
    # with it; without this it fell through to left alignment inside a numeric column.
    if t in {"—", "–", "-", "−"}:
        return True
    return bool(t) and any(c.isdigit() for c in t) and bool(_NUMERIC_CELL.match(t))


# ---------------------------------------------------------------------------
# Column widths.
#
# Word is given an explicit <w:tblGrid> and a FIXED layout. Without a grid Word has
# to guess the column widths from the content, and for a wide table (Coyle's Table
# 5.2: 7 columns of running prose) that guess runs straight off the right edge of
# the page. Widths are computed here with the classic auto-table-layout algorithm,
# so the table always sums to exactly the usable text width.

_CELL_PAD = 240        # left+right cell margin (108+108) plus a border allowance
_EM = int(TABLE_SZ) // 2 * 20      # 12 pt in twips -> 1 em


def _char_em(ch):
    """Advance width of one character in 1/1000 em, approximating Times New Roman.
    Only needs to be good enough to apportion a grid, not to typeset."""
    if ch == " ":
        return 250
    if ch in ".,;:'!|":
        return 280
    if ch in "iljtIf()[]{}/\\-":
        return 310
    if ch.isdigit():
        return 500
    if ch in "—":
        return 1000
    if ch in "MW":
        return 900
    if ch in "mw":
        return 760
    cyrillic = 0x0400 <= ord(ch) <= 0x04FF
    if ch.isupper():
        return 780 if cyrillic else 700
    return 540 if cyrillic else 500


def _text_w(s):
    return sum(_char_em(c) for c in s) * _EM // 1000


def _cell_plain(cell):
    """The cell's visible text: emphasis markers dropped, math kept as its source
    (close enough in width, and cells rarely hold more than a symbol or two)."""
    parts = []
    for i, seg in enumerate(_split_math(cell)):
        parts.append(_clean_inline(_untext(seg)) if i % 2 == 0 else seg.strip())
    return "".join(parts)


_BREAKABLE = re.compile(r"[\s/–—-]+")


def _col_demands(rows, ncol):
    """(minimum, natural) width per column: the widest unbreakable word, and the
    width of the longest cell set on a single line."""
    lo = [_CELL_PAD] * ncol
    hi = [_CELL_PAD] * ncol
    for row in rows:
        for j, cell in enumerate(row[:ncol]):
            t = _cell_plain(cell)
            hi[j] = max(hi[j], _text_w(t) + _CELL_PAD)
            for word in _BREAKABLE.split(t):
                if word:
                    lo[j] = max(lo[j], _text_w(word) + _CELL_PAD)
    return lo, hi


def _col_widths(rows, total):
    """Apportion `total` twips across the columns (CSS auto table layout):
    grow the natural widths if they all fit, otherwise hand each column its
    minimum and split the surplus in proportion to how much more it wants."""
    ncol = max(len(r) for r in rows)
    lo, hi = _col_demands(rows, ncol)
    if sum(hi) <= total:                       # everything fits -> scale up to fill
        base, span = hi, [0] * ncol
    elif sum(lo) < total:                      # wrap: minimums plus a share of the slack
        base, span = lo, [hi[j] - lo[j] for j in range(ncol)]
    else:                                      # not even the longest words fit -> squeeze
        base, span = lo, [0] * ncol
    slack = total - sum(base)
    weight = sum(span)
    w = [base[j] + (slack * span[j] // weight if weight else slack // ncol)
         for j in range(ncol)]
    w[-1] += total - sum(w)                    # absorb integer-division drift
    return w


def table_needs_landscape(rows):
    """True when the table cannot be set portrait without breaking words apart.

    A column may give up half its padding before the text actually touches the
    border, so that slack is credited before declaring the table unfittable --
    otherwise a table only a few per cent over (Coyle's Table 3.1) is flipped
    sideways for nothing."""
    ncol = max(len(r) for r in rows)
    lo, _ = _col_demands(rows, ncol)
    return sum(lo) - ncol * (_CELL_PAD // 2) > TEXT_W


def table_math_xml(rows, omml, total_w=None):
    """Bordered table whose cells may contain inline OMML (Chen tables carry
    net-benefit / accuracy formulas in their cells). ДСТУ 3008:2015: the first row
    is the головка -- bold, centered, vertically centered, and repeated on every
    page the table spans (<w:tblHeader/>); body cells left-aligned, vertically centered."""
    borders = ("<w:tblBorders>"
               + "".join("<w:%s w:val=\"single\" w:sz=\"4\" w:space=\"0\" w:color=\"auto\"/>" % e
                         for e in ("top", "left", "bottom", "right", "insideH", "insideV"))
               + "</w:tblBorders>")
    # Cell padding so text does not jam against the borders. ДСТУ 3008:2015 sets no exact
    # value; these are Word's conventional margins (0.19 cm left/right = 108 twips) plus a
    # little breathing room top/bottom (~0.07 cm = 40 twips) for a readable, non-compact table.
    cellmar = ("<w:tblCellMar>"
               "<w:top w:w=\"40\" w:type=\"dxa\"/><w:left w:w=\"108\" w:type=\"dxa\"/>"
               "<w:bottom w:w=\"40\" w:type=\"dxa\"/><w:right w:w=\"108\" w:type=\"dxa\"/>"
               "</w:tblCellMar>")
    widths = _col_widths(rows, total_w or TEXT_W)
    tblpr = ("<w:tblPr><w:tblW w:w=\"%d\" w:type=\"dxa\"/>"
             "<w:tblLayout w:type=\"fixed\"/>" % sum(widths)
             + borders + cellmar + "</w:tblPr>")
    grid = ("<w:tblGrid>"
            + "".join("<w:gridCol w:w=\"%d\"/>" % w for w in widths)
            + "</w:tblGrid>")
    out = ["<w:tbl>", tblpr, grid]
    for r_idx, row in enumerate(rows):
        header = (r_idx == 0)
        out.append("<w:tr>" + ("<w:trPr><w:tblHeader/><w:cantSplit/></w:trPr>" if header else ""))
        for j, cell in enumerate(row):
            # header row centered; body: numeric cells centered, text (row labels) left-aligned
            jc = "center" if (header or _is_numeric_cell(cell)) else "left"
            out.append("<w:tc><w:tcPr><w:tcW w:w=\"%d\" w:type=\"dxa\"/>"
                       "<w:vAlign w:val=\"center\"/></w:tcPr>"
                       "<w:p><w:pPr><w:spacing w:after=\"0\" w:line=\"240\" w:lineRule=\"auto\"/>"
                       "<w:jc w:val=\"%s\"/></w:pPr>%s</w:p></w:tc>"
                       % (widths[j] if j < len(widths) else widths[-1], jc,
                          _cell_runs(cell, omml, bold=header)))
        out.append("</w:tr>")
    out.append("</w:tbl>")
    return "".join(out)


def _has_open_ordered_list(out):
    """True when an ordered list is still 'open': one was emitted earlier and no
    heading has closed it since."""
    for kind, _ in reversed(out):
        if kind in ("h1", "h2", "h3", "h4", "title"):
            return False
        if kind in ("olist", "olistc"):
            return True
    return False


def group_lists(blocks):
    """Fold runs of consecutive 'par' blocks that are list items into single
    ('olist'|'ulist', [item_text, ...]) blocks. Each such block later becomes a
    real Word list (own numId, so ordered lists restart at 1).

    An ordered list interrupted by formulas or explanatory prose (the "1. derive D
    <eq> 2. estimate L(D) <eq> 3. …" recipe shape) resumes at 2, 3, … in the
    markdown; such runs are emitted as 'olistc' continuation blocks, which reuse the
    previous numId so Word keeps counting instead of restarting at 1. A heading
    closes the open list."""
    out, i = [], 0
    while i < len(blocks):
        kind, data = blocks[i]
        if kind == "par" and (OLITEM_RE.match(data) or ULITEM_RE.match(data)):
            m0 = OLITEM_RE.match(data)
            ordered = bool(m0)
            first_no = int(m0.group(1)) if ordered else 0
            rx = OLITEM_RE if ordered else ULITEM_RE
            items = []
            while i < len(blocks) and blocks[i][0] == "par":
                m = rx.match(blocks[i][1])
                if not m:
                    break
                items.append(m.group(2) if ordered else m.group(1))
                i += 1
            # a run that starts at 2, 3, … continues the ordered list still open in
            # this section (the markdown itself restarts at 1 for a genuinely new list)
            cont = ordered and first_no > 1 and _has_open_ordered_list(out)
            out.append((("olistc" if cont else "olist") if ordered else "ulist", items))
        else:
            out.append(blocks[i])
            i += 1
    return out


def list_item_par(runs_xml, num_id):
    """A list-item paragraph: real Word numbering (numId) + tight spacing (no gap
    between items). The hanging indent is defined on the list level in numbering.xml."""
    return ("<w:p><w:pPr>"
            "<w:numPr><w:ilvl w:val=\"0\"/><w:numId w:val=\"%d\"/></w:numPr>"
            "<w:spacing w:after=\"0\"/><w:jc w:val=\"both\"/></w:pPr>%s</w:p>"
            % (num_id, runs_xml))


# A real empty paragraph = one blank line (ДСТУ 3008:2015 §6, "не менше ніж один рядок").
# Verified 2026-08-31 against Chen_translation.docx / Coyle_translation.docx, which use this
# exact form and do render a visible blank line above and below each formula in Word.
# (Do not "fix" this into a paragraph holding a space run — that was tried on 2026-08-31 on
# the false premise that <w:p/> has no line box, and reverted.)
BLANK = "<w:p/>"
BLANK_RE = re.escape(BLANK)


# A paragraph that belongs WITH a table rather than to the running text: below it, the
# source line, the footnote key and any marker legend. These, and the caption above,
# travel with the table when it is turned landscape.
_TBL_NOTE = re.compile(r"^(\\\*|[¹²³⁴⁵⁶⁷⁸⁹]|Джерело|Примітка|\d+\s+\S)")


def mark_landscape_tables(blocks):
    """Wrap every table too wide for a portrait page -- with its caption and its
    trailing notes -- in its own landscape section.

    A table goes sideways when the sum of its columns' widest single WORDS already
    exceeds the portrait text width (no column apportionment can avoid breaking words
    apart), or when a `<!-- landscape -->` line in the markdown asks for it. Coyle
    prints his widest tables (5.2, 5.3, and more in Розділи 7-8) sideways for exactly
    this reason. In OOXML a <w:sectPr> carried by a paragraph closes the section that
    paragraph ENDS, so a landscape island needs a portrait break before it and a
    landscape break after it."""
    out, i, forced = [], 0, False
    while i < len(blocks):
        kind, data = blocks[i]
        if kind == "landscape":         # directive: applies to the next table
            forced = True
            i += 1
            continue
        if kind != "table" or not (forced or table_needs_landscape(data)):
            out.append(blocks[i])
            i += 1
            continue
        forced = False
        island = [blocks[i]]
        # Pull the caption above the table into the island, reaching back over a
        # short label line or two ("**a. Алендронат**" above Table 6.4a). If no
        # caption turns up, those lines were ordinary text -- put them back.
        head = []
        while (out and out[-1][0] == "par" and len(out[-1][1]) <= 200
               and len(head) < 2):
            head.insert(0, out.pop())
        if out and out[-1][0] == "caption":
            island = [out.pop()] + head + island
        else:
            out += head
        # …and up to three note paragraphs sitting directly below it
        j = i + 1
        while j < len(blocks) and j - i <= 3:
            k, d = blocks[j]
            if k != "par" or len(d) > 400 or not _TBL_NOTE.match(d):
                break
            island.append(blocks[j])
            j += 1
        out.append(("sectbreak", False))        # close the portrait run
        out += island
        out.append(("sectbreak", True))         # close the landscape island
        i = j
    return _merge_landscape_islands(out)


def _merge_landscape_islands(blocks, gap=2, short=200):
    """Fuse two landscape islands separated only by a line or two of short text.

    A table printed in parts (Coyle's Table 6.4 = a. alendronate, b. etidronate,
    c. risedronate) is three markdown tables with a one-line label between them.
    Each part is wide, so each would get its own sideways page and every label
    would be stranded on the portrait page before it."""
    out = []
    for kind, data in blocks:
        if kind == "sectbreak" and data is False:
            # walk back over the short filler to a landscape-closing break
            k = len(out) - 1
            while (k >= 0 and out[k][0] in ("par", "caption")
                   and len(out[k][1]) <= short and len(out) - 1 - k < gap):
                k -= 1
            if k >= 0 and out[k] == ("sectbreak", True):
                del out[k]                      # the two islands are now one
                continue
        out.append((kind, data))
    return out


def build_body(blocks, omml, nums, imgmap):
    out = []
    docpr_id = 0
    landscape = False
    for i, (kind, data) in enumerate(blocks):
        prev_k = blocks[i - 1][0] if i > 0 else None
        next_k = blocks[i + 1][0] if i + 1 < len(blocks) else None
        if kind == "title":
            out.append(title_par(data))
        elif kind in ("h1", "h2", "h3", "h4"):
            out.append(heading_par(data, int(kind[1])))
        elif kind == "par":
            out.append(body_par(build_runs(data, omml)))
        elif kind in ("olist", "ulist", "olistc"):
            if kind == "olistc":
                num_id = len(nums)      # continuation: keep counting in the SAME list
            else:
                nums.append(0 if kind == "olist" else 1)   # abstractNumId per list
                num_id = len(nums)                          # numId is 1-based
            for item in data:
                out.append(list_item_par(build_runs(item, omml), num_id))
        elif kind == "dispeq":
            # ДСТУ: a blank line separates the formula GROUP from surrounding text, not
            # consecutive formulas from each other -> blank only at the run's edges.
            tex, label = data
            block = omml.get(tex)
            if prev_k != "dispeq":
                out.append(BLANK)
            out.append(dispeq_par(block, label) if block else wpar(wrun(tex)))
            if next_k != "dispeq":
                out.append(BLANK)
        elif kind == "sectbreak":
            # `data` is the orientation of the section this paragraph closes
            out.append(sect_break_par(data))
            landscape = not data
        elif kind == "table":
            # title (caption) sits directly above; blank line only below the table
            width = TEXT_W_LANDSCAPE if landscape else TEXT_W
            out += [table_math_xml(data, omml, width), BLANK]
        elif kind == "caption":
            out += [BLANK, wpar(build_runs(data, omml), jc="left")]   # blank line above the title
        elif kind == "figure":
            out += [figure_par(data, omml), BLANK]      # blank line below the caption
        elif kind == "image":
            alt, path = data
            rid, cx, cy = imgmap[path]
            docpr_id += 1
            out += [BLANK, image_par(alt, rid, cx, cy, docpr_id)]   # blank line above image
    # Collapse any run of adjacent blank lines into a single one. Matched against BLANK
    # itself (not a hardcoded "<w:p/>"), so changing the blank-paragraph form cannot
    # silently break group spacing — stacked formulas must keep exactly one blank between
    # the group and the surrounding text, and none between the formulas themselves.
    return re.sub(r"(?:%s){2,}" % BLANK_RE, BLANK, "".join(out))


# ---------------------------------------------------------------------------
# Styles (Normal + Heading 1/2/3; layout otherwise identical to the engine)
# ---------------------------------------------------------------------------

def styles_xml():
    def heading(idx, half_pt, italic=False, caps=False):
        ital = "<w:i/>" if italic else ""
        cap = "<w:caps/>" if caps else ""      # ДСТУ: РОЗДІЛ headings in capitals
        return ("<w:style w:type=\"paragraph\" w:styleId=\"Heading%d\">"
                "<w:name w:val=\"heading %d\"/><w:basedOn w:val=\"Normal\"/>"
                "<w:next w:val=\"Normal\"/><w:qFormat/>"
                "<w:pPr><w:keepNext/><w:outlineLvl w:val=\"%d\"/>"
                "<w:spacing w:before=\"240\" w:after=\"240\"/></w:pPr>"
                "<w:rPr><w:b/>%s%s<w:sz w:val=\"%s\"/><w:szCs w:val=\"%s\"/></w:rPr>"
                "</w:style>" % (idx, idx, idx - 1, ital, cap, half_pt, half_pt))
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<w:styles xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\">"
        "<w:docDefaults><w:rPrDefault><w:rPr>"
        "<w:rFonts w:ascii=\"%s\" w:hAnsi=\"%s\" w:cs=\"%s\"/>"
        "<w:sz w:val=\"%s\"/><w:szCs w:val=\"%s\"/></w:rPr></w:rPrDefault>"
        "<w:pPrDefault><w:pPr>"
        "<w:spacing w:after=\"0\" w:line=\"%s\" w:lineRule=\"auto\"/>"
        "</w:pPr></w:pPrDefault></w:docDefaults>"
        "<w:style w:type=\"paragraph\" w:default=\"1\" w:styleId=\"Normal\">"
        "<w:name w:val=\"Normal\"/></w:style>"
        % (FONT, FONT, FONT, SZ, SZ, LINE)
        + heading(1, "28", caps=True) + heading(2, "28") + heading(3, "28") + heading(4, "28")
        + "</w:styles>"
    )


# ---------------------------------------------------------------------------
# Numbering (real Word lists: decimal + bullet, hanging indent)
# ---------------------------------------------------------------------------

def _abstract_num(abs_id, num_fmt, lvl_text):
    return ("<w:abstractNum w:abstractNumId=\"%d\">"
            "<w:lvl w:ilvl=\"0\"><w:start w:val=\"1\"/>"
            "<w:numFmt w:val=\"%s\"/><w:lvlText w:val=\"%s\"/><w:lvlJc w:val=\"left\"/>"
            "<w:pPr><w:ind w:left=\"360\" w:hanging=\"360\"/></w:pPr>"
            "</w:lvl></w:abstractNum>" % (abs_id, num_fmt, lvl_text))


def numbering_xml(nums):
    """`nums[k]` is the abstractNumId (0=decimal, 1=bullet) for numId k+1.

    Each list gets its own numId AND an explicit `startOverride` back to 1. Without
    the override Word keeps one running counter across every numId that shares an
    abstractNum, so the second ordered list in the document would start at 5, the
    third at 9, and so on."""
    instances = "".join(
        "<w:num w:numId=\"%d\"><w:abstractNumId w:val=\"%d\"/>"
        "<w:lvlOverride w:ilvl=\"0\"><w:startOverride w:val=\"1\"/></w:lvlOverride>"
        "</w:num>" % (k + 1, abs_id)
        for k, abs_id in enumerate(nums))
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<w:numbering xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\">"
        + _abstract_num(0, "decimal", "%1.")
        + _abstract_num(1, "bullet", "•")
        + instances
        + "</w:numbering>"
    )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def _resolve_images(blocks, src_md):
    """Map each referenced image path -> (rId, cx, cy); collect media files + rels.

    Paths in the template are relative to the markdown file's directory. Each unique
    path gets one relationship (rId3+, after styles=rId1 and numbering=rId2) and one
    media part. Returns (imgmap, media, rels_xml) where media = [(arcname, fs_path)]."""
    srcdir = os.path.dirname(os.path.abspath(src_md))
    paths = [data[1] for kind, data in blocks if kind == "image"]
    alts = {}
    for kind, data in blocks:
        if kind == "image":
            alts.setdefault(data[1], data[0])
    uniq = list(dict.fromkeys(paths))
    imgmap, media, rels = {}, [], []
    for k, relpath in enumerate(uniq):
        fs = os.path.normpath(os.path.join(srcdir, relpath))
        if not os.path.exists(fs):
            raise FileNotFoundError("figure image not found: %s (from %s)" % (fs, relpath))
        cx, cy = _img_extent_emu(fs, _alt_width_frac(alts.get(relpath)))
        ext = os.path.splitext(relpath)[1].lower() or ".png"
        arc = "image%d%s" % (k + 1, ext)
        rid = "rId%d" % (k + 3)
        imgmap[relpath] = (rid, cx, cy)
        media.append((arc, fs))
        rels.append("<Relationship Id=\"%s\" "
                    "Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/image\" "
                    "Target=\"media/%s\"/>" % (rid, arc))
    return imgmap, media, "".join(rels)


def build(src_md, out_docx):
    blocks, latex = parse_md(src_md)
    blocks = group_lists(blocks)
    blocks = mark_landscape_tables(blocks)
    omml = latex_to_omml(latex)
    imgmap, media, image_rels = _resolve_images(blocks, src_md)
    nums = []                       # abstractNumId per list, in encounter order
    body = build_body(blocks, omml, nums, imgmap)
    doc = document_xml(body)

    os.makedirs(os.path.dirname(out_docx) or ".", exist_ok=True)
    with zipfile.ZipFile(out_docx, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/document.xml", doc)
        z.writestr("word/_rels/document.xml.rels", doc_rels_xml(image_rels))
        z.writestr("word/styles.xml", styles_xml())
        z.writestr("word/numbering.xml", numbering_xml(nums))
        z.writestr("word/header1.xml", header_xml())
        for arc, fs in media:
            with open(fs, "rb") as fh:
                z.writestr("word/media/%s" % arc, fh.read())

    n_eq = sum(1 for k, _ in blocks if k == "dispeq")
    n_tbl = sum(1 for k, _ in blocks if k == "table")
    n_list = sum(1 for k, _ in blocks if k in ("olist", "ulist"))
    n_img = sum(1 for k, _ in blocks if k == "image")
    n_land = sum(1 for k, d in blocks if k == "sectbreak" and d) or 0
    print("wrote %s (%d bytes)" % (out_docx, os.path.getsize(out_docx)))
    print("  %d unique equations, %d display slots, %d tables, %d lists, %d images (%d files)"
          % (len(omml), n_eq, n_tbl, n_list, n_img, len(media)))
    if n_land:
        print("  %d table(s) turned landscape (too wide for a portrait page)" % n_land)


def main(argv):
    if len(argv) != 3:
        print("usage: python build_docx.py <input.md> <output.docx>")
        return 2
    build(argv[1], argv[2])
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
