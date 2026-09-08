"""
docx_engine — the shared layout/packaging primitives for building .docx files.

Stdlib-only. A .docx is a zip of XML parts; this module provides the document-wide
constants (Times New Roman 14 pt, 1.5 spacing), the low-level run/paragraph builders,
the document.xml wrapper, and the fixed package parts ([Content_Types], _rels, doc rels).
It is deliberately document-agnostic: no headings, tables, or equation logic live here.

`build_docx.py` is the single builder that imports this engine and adds the markdown +
inline-LaTeX→OMML layer. (Extracted 2026-08-10 from the former build_voi_docx.py so there
is one engine and one builder, not a per-document script per deliverable.)
"""
from __future__ import annotations

# --- document-wide layout constants ---------------------------------------
FONT = "Times New Roman"
SZ = "28"          # half-points -> 14 pt
LINE = "360"       # 240=single, 360=1.5, 480=double


# --- XML escaping -----------------------------------------------------------
def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# --- run / paragraph builders ----------------------------------------------
def wrun(text: str, italic=False, bold=False, sz=None) -> str:
    rpr = ""
    props = (("<w:b/>" if bold else "") + ("<w:i/>" if italic else "")
             + (f"<w:sz w:val=\"{sz}\"/><w:szCs w:val=\"{sz}\"/>" if sz else ""))
    if props:
        rpr = f"<w:rPr>{props}</w:rPr>"
    return f"<w:r>{rpr}<w:t xml:space=\"preserve\">{esc(text)}</w:t></w:r>"


def wpar(runs_xml: str, jc="both") -> str:
    return (f"<w:p><w:pPr><w:jc w:val=\"{jc}\"/></w:pPr>{runs_xml}</w:p>")


# --- page geometry (A4 portrait, ДСТУ 3008:2015 margins) --------------------
PG_W, PG_H = 11906, 16838          # A4 in twips
MAR_TOP, MAR_RIGHT, MAR_BOTTOM, MAR_LEFT = 1134, 850, 1134, 1701

#: usable text width, portrait and landscape -- the width a table must fit into.
TEXT_W = PG_W - MAR_LEFT - MAR_RIGHT            # 9355
TEXT_W_LANDSCAPE = PG_H - MAR_LEFT - MAR_RIGHT  # 14287


def sect_xml(landscape: bool = False) -> str:
    """A <w:sectPr>. ДСТУ 3008:2015: page number top-right -> a default header
    (rId900, a distinctive id so it never collides with image rels, which start at
    rId3). Landscape keeps the same margins, so the binding margin stays on the left."""
    w, h = (PG_H, PG_W) if landscape else (PG_W, PG_H)
    orient = " w:orient=\"landscape\"" if landscape else ""
    return ("<w:sectPr>"
            "<w:headerReference w:type=\"default\" r:id=\"rId900\"/>"
            f"<w:pgSz w:w=\"{w}\" w:h=\"{h}\"{orient}/>"
            f"<w:pgMar w:top=\"{MAR_TOP}\" w:right=\"{MAR_RIGHT}\" "
            f"w:bottom=\"{MAR_BOTTOM}\" w:left=\"{MAR_LEFT}\" "
            "w:header=\"720\" w:footer=\"720\" w:gutter=\"0\"/></w:sectPr>")


def sect_break_par(landscape: bool = False) -> str:
    """An empty paragraph carrying a <w:sectPr>. In OOXML a sectPr inside a
    paragraph CLOSES the section that paragraph ends, so `landscape` describes the
    orientation of the content ABOVE this paragraph, not below it."""
    return f"<w:p><w:pPr>{sect_xml(landscape)}</w:pPr></w:p>"


# --- document.xml wrapper + fixed package parts ----------------------------
def document_xml(body: str) -> str:
    sect = sect_xml(landscape=False)     # final, body-level section: portrait
    return (
        "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
        "<w:document "
        "xmlns:w=\"http://schemas.openxmlformats.org/wordprocessingml/2006/main\" "
        "xmlns:m=\"http://schemas.openxmlformats.org/officeDocument/2006/math\" "
        "xmlns:r=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships\" "
        "xmlns:wp=\"http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing\" "
        "xmlns:a=\"http://schemas.openxmlformats.org/drawingml/2006/main\" "
        "xmlns:pic=\"http://schemas.openxmlformats.org/drawingml/2006/picture\">"
        f"<w:body>{body}{sect}</w:body></w:document>"
    )


CONTENT_TYPES = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<Types xmlns=\"http://schemas.openxmlformats.org/package/2006/content-types\">"
    "<Default Extension=\"rels\" ContentType=\"application/vnd.openxmlformats-package.relationships+xml\"/>"
    "<Default Extension=\"xml\" ContentType=\"application/xml\"/>"
    "<Default Extension=\"png\" ContentType=\"image/png\"/>"
    "<Default Extension=\"jpeg\" ContentType=\"image/jpeg\"/>"
    "<Default Extension=\"jpg\" ContentType=\"image/jpeg\"/>"
    "<Override PartName=\"/word/document.xml\" "
    "ContentType=\"application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml\"/>"
    "<Override PartName=\"/word/styles.xml\" "
    "ContentType=\"application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml\"/>"
    "<Override PartName=\"/word/numbering.xml\" "
    "ContentType=\"application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml\"/>"
    "<Override PartName=\"/word/header1.xml\" "
    "ContentType=\"application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml\"/>"
    "</Types>"
)

RELS = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">"
    "<Relationship Id=\"rId1\" "
    "Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument\" "
    "Target=\"word/document.xml\"/></Relationships>"
)

DOC_RELS = (
    "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>"
    "<Relationships xmlns=\"http://schemas.openxmlformats.org/package/2006/relationships\">"
    "<Relationship Id=\"rId1\" "
    "Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles\" "
    "Target=\"styles.xml\"/>"
    "<Relationship Id=\"rId2\" "
    "Type=\"http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering\" "
    "Target=\"numbering.xml\"/></Relationships>"
)
