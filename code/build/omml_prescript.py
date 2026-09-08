"""Post-process pandoc OMML: turn empty-base left-subscripts into real prescripts.

Chen's Chapter 5 uses a leading (left) subscript for the test index, written in the
markdown as ``{}_{1}\\alpha`` (an empty group carrying the subscript, placed before the
base). pandoc/texmath renders ``{}`` as a subscript whose BASE is a zero-width space, so
Word draws its empty-base placeholder -- a dotted box -- before every such symbol.

``fix_prescripts`` rewrites each ``<m:sSub>`` whose base is empty/zero-width, merging its
subscript onto the FOLLOWING sibling as a proper ``<m:sPre>`` (pre-sub-superscript). Word
renders m:sPre with no placeholder box, giving the intended ``₁α`` look.

Pure stdlib (xml.etree); operates on one ``<m:oMath>...</m:oMath>`` string and returns it.
"""
from __future__ import annotations

import re
import xml.etree.ElementTree as ET

M = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/math"
MNS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/math"
# the real math namespace used by pandoc's OMML:
NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/math"

# pandoc emits the standard math namespace; detect it from the document instead of guessing.
_ZWS = "​"


def _is_empty_base(e_elem, ns):
    """True if an <m:e> holds nothing but whitespace / zero-width spaces."""
    txt = "".join(t.text or "" for t in e_elem.iter(f"{{{ns}}}t"))
    return txt.strip().strip(_ZWS) == ""


def _fix_children(parent, ns):
    """Walk one element's child list, merging empty-base sSub + next sibling -> sPre."""
    children = list(parent)
    i = 0
    out = []
    sSub = f"{{{ns}}}sSub"
    e_tag = f"{{{ns}}}e"
    sub_tag = f"{{{ns}}}sub"
    while i < len(children):
        c = children[i]
        if (c.tag == sSub and i + 1 < len(children)):
            base = c.find(e_tag)
            sub = c.find(sub_tag)
            if base is not None and sub is not None and _is_empty_base(base, ns):
                # build m:sPre wrapping the NEXT sibling as its base
                nxt = children[i + 1]
                pre = ET.Element(f"{{{ns}}}sPre")
                # order per schema: sPrePr, sub, sup, e
                new_sub = ET.SubElement(pre, f"{{{ns}}}sub")
                for ch in list(sub):
                    new_sub.append(ch)
                # pre-subscript only: the sup slot MUST exist (schema-required) but must
                # not be an EMPTY optional argument -- Word draws empty math slots as a
                # dotted placeholder box (and since ~2024 prints them). Fill it with an
                # invisible, zero-size phantom so the slot is non-empty yet renders/measures
                # as nothing. (MS-OODF3 s14.5: show=0 + zeroWid/zeroAsc/zeroDesc.)
                new_sup = ET.SubElement(pre, f"{{{ns}}}sup")
                phant = ET.SubElement(new_sup, f"{{{ns}}}phant")
                phant_pr = ET.SubElement(phant, f"{{{ns}}}phantPr")
                for prop in ("show", "zeroWid", "zeroAsc", "zeroDesc"):
                    p = ET.SubElement(phant_pr, f"{{{ns}}}{prop}")
                    p.set(f"{{{ns}}}val", "0" if prop == "show" else "1")
                # phantom base holds a REAL run (not another empty slot, which would itself
                # box); the char is hidden by show=0 and takes no space via the zero-* props.
                phant_e = ET.SubElement(phant, f"{{{ns}}}e")
                phant_r = ET.SubElement(phant_e, f"{{{ns}}}r")
                phant_t = ET.SubElement(phant_r, f"{{{ns}}}t")
                phant_t.text = "."
                new_e = ET.SubElement(pre, f"{{{ns}}}e")
                new_e.append(nxt)
                out.append(pre)
                i += 2
                continue
        out.append(c)
        i += 1
    # replace parent's children with the rewritten list
    for ch in list(parent):
        parent.remove(ch)
    for ch in out:
        parent.append(ch)
    # recurse into the (possibly new) children
    for ch in list(parent):
        _fix_children(ch, ns)


_MATH_NS = "http://schemas.openxmlformats.org/officeDocument/2006/math"


def fix_prescripts(omath_xml: str) -> str:
    """Rewrite empty-base left-subscripts to m:sPre in one <m:oMath> string.

    The input is an ``m:``-prefixed fragment with no namespace declaration; we inject the
    standard OMML math namespace to parse it, then strip the redundant declaration back off
    (document.xml already declares ``m``)."""
    if _ZWS not in omath_xml:
        return omath_xml  # no empty-base subscripts here
    wrapped = omath_xml.replace(
        "<m:oMath>", '<m:oMath xmlns:m="%s">' % _MATH_NS, 1)
    ET.register_namespace("m", _MATH_NS)
    root = ET.fromstring(wrapped)
    _fix_children(root, _MATH_NS)
    out = ET.tostring(root, encoding="unicode")
    return out.replace(' xmlns:m="%s"' % _MATH_NS, "", 1)
