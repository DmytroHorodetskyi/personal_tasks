"""Post-process pandoc/texmath OMML: clean the <m:eqArr> it emits for line-broken eqs.

`linebreak_eqs.py` wraps an over-wide display equation in ``\\begin{aligned} … \\\\ … \\end{aligned}``
so Word stacks it instead of overflowing the right margin. pandoc's texmath converts that to an
``<m:eqArr>`` (equation array) -- but with TWO artifacts Word renders as garbage:

  1. the ``&`` alignment tab leaks through as a LITERAL ``&`` text run (a visible ampersand);
  2. each ``\\\\`` row break leaves an EMPTY ``<m:e/>`` row, which Word draws as a dotted box.

``clean_eqarr`` walks every ``<m:eqArr>`` and removes both: empty ``<m:e>`` rows are dropped and
any run whose only text is ``&`` is deleted. What remains is clean stacked rows (centered) -- no
boxes, no stray ampersands. Pure stdlib; operates on one ``<m:oMath>…</m:oMath>`` string.
"""
from __future__ import annotations

import xml.etree.ElementTree as ET

_MATH_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"


def clean_eqarr(omath_xml: str) -> str:
    """Strip texmath's aligned artifacts (empty rows + literal ``&`` runs) from every eqArr."""
    if "<m:eqArr>" not in omath_xml:
        return omath_xml  # nothing to clean
    wrapped = omath_xml.replace(
        "<m:oMath>", '<m:oMath xmlns:m="%s">' % _MATH_NS, 1)
    ET.register_namespace("m", _MATH_NS)
    root = ET.fromstring(wrapped)
    e_tag = f"{{{_MATH_NS}}}e"
    r_tag = f"{{{_MATH_NS}}}r"
    t_tag = f"{{{_MATH_NS}}}t"
    for arr in root.iter(f"{{{_MATH_NS}}}eqArr"):
        for e in list(arr):
            if e.tag != e_tag:
                continue
            # an empty row (no children, no text) is texmath's row-break artifact -> a box
            if len(e) == 0 and not (e.text and e.text.strip()):
                arr.remove(e)
                continue
            # a run whose only text is the alignment tab '&' leaks as a visible ampersand
            for r in list(e):
                if r.tag == r_tag:
                    txt = "".join(t.text or "" for t in r.iter(t_tag))
                    if txt.strip() == "&":
                        e.remove(r)
    out = ET.tostring(root, encoding="unicode")
    return out.replace(' xmlns:m="%s"' % _MATH_NS, "", 1)
