#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
style_check.py — mechanical gate for Ukrainian dissertation prose (knowledge/WRITING_STYLE.md).

    python code/build/style_check.py <draft.md> [--no-lt] [--lt-level default|picky] [--json]

Three things happen:
  1. The markdown template is parsed into blocks (prose, display formulas, tables, headings,
     lists, reference list). Formulas ($$…$$ and $…$) are recognised the same way
     build_docx.py recognises them, so nothing that will become a Word equation is ever
     spell-checked or mistaken for prose.
  2. Repo rules from code/build/style_rules.json (the machine half of WRITING_STYLE.md §2–§6)
     plus structural checks: result-first opening, «де» gloss after every display formula,
     bracket stacking, bare "(табл. N)", bold/run-in headings, lists, decimal points,
     citations without a reference entry, unglossed formula symbols.
  3. LanguageTool uk-UA (public API, free, rate-limited) on the prose only, with inline
     formulas replaced by their plain symbol so grammar around them still parses.

Exit code 1 if any error-severity finding exists. This script REPORTS; it never rewrites.
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
RULES_PATH = HERE / "style_rules.json"

# --- block recognisers (kept in step with build_docx.py) ---------------------------------
DISPEQ_RE = re.compile(r"^\$\$(?P<tex>.+?)\$\$\s*(?:\((?P<label>[^()]+)\))?\s*$")
INLINE_MATH_RE = re.compile(r"\$(?P<tex>[^$\n]+?)\$")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
TBL_ROW_RE = re.compile(r"^\|.*\|\s*$")
TBL_CAPTION_RE = re.compile(r"^Таблиця\s+([\d.]+)\s*(?P<sep>[—–-]\s|\.\s)(?P<title>.*)$")
FIG_CAPTION_RE = re.compile(r"^(Рисунок|Рис\.)\s+[\d.]+")
IMAGE_RE = re.compile(r"^!\[[^\]]*\]\([^)]+\)")
LIST_RE = re.compile(r"^(\s*[-*]\s+|\s*\d+\.\s+)")
CITE_RE = re.compile(r"\[(\d+(?:[,;–-]\s*\d+)*)\]")
# A confidence interval is written [lo; hi] with decimal commas, which CITE_RE also
# matches: [0,04; 0,71] parsed as citations 0, 4 and 71 and every one was reported
# missing from the reference list (18 false errors on the COVID report, 2026-09-08).
CI_IN_BRACKETS = re.compile(r";|\d,\d|[−+]")


def is_citation(content):
    """True for [1], [1, 2], [4–6]; False for a numeric interval such as [0,04; 0,71]."""
    return not CI_IN_BRACKETS.search(content)
REF_ENTRY_RE = re.compile(r"^(\d+)\.\s+\S")
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)

LATEX_CMDS = {
    "sum", "cdot", "qquad", "quad", "sim", "equiv", "frac", "sqrt", "left", "right", "mathrm",
    "text", "bar", "hat", "tilde", "times", "approx", "le", "ge", "leq", "geq", "neq", "ne",
    "infty", "int", "prod", "max", "min", "arg", "log", "ln", "exp", "dfrac", "operatorname",
    "over", "partial", "nabla", "pm", "mid", "big", "Big", "ldots", "cdots", "dots", "to",
    "rightarrow", "in", "subset", "cup", "cap", "forall", "exists", "sigma", "mu", "lambda",
    "alpha", "beta", "gamma", "delta", "theta", "phi", "Phi", "Delta", "Sigma", "epsilon",
    "varepsilon", "pi", "rho", "tau", "omega", "Omega", "nu", "kappa", "eta", "zeta", "chi",
    "xi", "psi", "Psi", "Gamma", "Lambda", "prime", "vert", "lvert", "rvert", "langle",
    "rangle", "binom", "mathbb", "mathcal", "mathbf", "boldsymbol", "hspace", "vspace", "displaystyle",
}
GREEK_PLAIN = {
    "Delta": "Δ", "delta": "δ", "lambda": "λ", "sigma": "σ", "mu": "μ", "Phi": "Φ", "phi": "φ",
    "alpha": "α", "beta": "β", "gamma": "γ", "theta": "θ", "pi": "π", "rho": "ρ", "tau": "τ",
    "epsilon": "ε", "varepsilon": "ε", "omega": "ω", "Omega": "Ω", "Sigma": "Σ", "nu": "ν",
    "kappa": "κ", "eta": "η", "chi": "χ", "xi": "ξ", "psi": "ψ", "Gamma": "Γ", "Lambda": "Λ",
}

RESULT_VERBS = re.compile(
    r"\b(встановлено|показано|виявлено|доведено|отримано|дорівнює|становить|склада[єю]|"
    r"є економічно (виправдан|доцільн)|є ефективн|перевищує)\b", re.I)


# ------------------------------------------------------------------------------------------
class Finding:
    def __init__(self, line, rule, severity, snippet, message, source="repo"):
        self.line, self.rule, self.severity = line, rule, severity
        self.snippet, self.message, self.source = snippet, message, source

    def as_dict(self):
        return dict(line=self.line, rule=self.rule, severity=self.severity,
                    snippet=self.snippet, message=self.message, source=self.source)


class Block:
    def __init__(self, kind, start, lines):
        self.kind, self.start, self.lines = kind, start, lines  # start is 1-based line no.

    @property
    def text(self):
        return " ".join(l.strip() for l in self.lines)


def tex_to_plain(tex):
    """$C_T$ -> C_T ; \\Delta D -> ΔD ; \\mathrm{INB} -> INB ; \\bar{D} -> D̄ (roughly)."""
    s = tex
    s = re.sub(r"\\(mathrm|text|operatorname|mathbf|boldsymbol)\{([^}]*)\}", r"\2", s)
    s = re.sub(r"\\bar\{([^}]*)\}", lambda m: m.group(1) + "\u0304", s)
    s = re.sub(r"\\hat\{([^}]*)\}", lambda m: m.group(1) + "\u0302", s)
    s = re.sub(r"\\([A-Za-z]+)", lambda m: GREEK_PLAIN.get(m.group(1), ""), s)
    s = s.replace("{", "").replace("}", "").replace("^", "").replace("\\", "")
    s = re.sub(r"\s+", "", s)
    return s or "X"


def formula_identifiers(tex):
    """Symbols a «де» gloss should define. Returns plain forms like C_T, ΔD, INB, b_0."""
    ids = set()
    for m in re.finditer(r"\\(mathrm|operatorname)\{([^}]+)\}", tex):
        ids.add(m.group(2).strip())
    stripped = re.sub(r"\\(mathrm|text|operatorname)\{[^}]+\}", " ", tex)
    for m in re.finditer(r"\\([A-Za-z]+)(?:\s*([A-Za-z]))?", stripped):
        cmd, nxt = m.group(1), m.group(2)
        if cmd in GREEK_PLAIN and cmd not in ("sum", "cdot"):
            ids.add(GREEK_PLAIN[cmd] + (nxt or ""))
    stripped = re.sub(r"\\[A-Za-z]+", " ", stripped)
    for m in re.finditer(r"(?<![A-Za-z])([A-Za-z])(?:_\{([^}]+)\}|_(\w))?", stripped):
        base, sub = m.group(1), m.group(2) or m.group(3)
        ids.add(base + ("_" + sub if sub else ""))
    return ids


def parse_blocks(src):
    src = HTML_COMMENT_RE.sub(lambda m: "\n" * m.group(0).count("\n"), src)
    lines = src.split("\n")
    blocks, buf, buf_start = [], [], None

    def flush():
        nonlocal buf, buf_start
        if buf:
            blocks.append(Block("prose", buf_start, buf))
        buf, buf_start = [], None

    in_refs, in_fig = False, False
    for i, raw in enumerate(lines, 1):
        line = raw.rstrip()
        s = line.strip()
        if not s:
            flush(); in_fig = False
            continue
        if in_fig:  # continuation of a multi-line *[Рисунок N — …]* caption
            blocks[-1].lines.append(s)
            if s.endswith("]*"):
                in_fig = False
            continue
        if s.startswith("Перелік посилань") or re.match(r"^#+\s*Перелік посилань", s):
            flush(); in_refs = True
            blocks.append(Block("refhead", i, [s])); continue
        if in_refs:
            m_ref = REF_ENTRY_RE.match(s)
            if m_ref and int(m_ref.group(1)) < 400:  # «2020. …» is a wrapped line, not entry 2020
                flush(); blocks.append(Block("ref", i, [s]))
            elif blocks and blocks[-1].kind == "ref":
                blocks[-1].lines.append(s)  # wrapped reference entry
            continue
        if DISPEQ_RE.match(s):
            flush(); blocks.append(Block("formula", i, [s])); continue
        if HEADING_RE.match(s):
            flush(); blocks.append(Block("heading", i, [s])); continue
        if TBL_ROW_RE.match(s):
            flush(); blocks.append(Block("table", i, [s])); continue
        if TBL_CAPTION_RE.match(s) or s.startswith("Таблиця "):
            flush(); blocks.append(Block("tblcap", i, [s])); continue
        if FIG_CAPTION_RE.match(s) or IMAGE_RE.match(s) or s.startswith("*["):
            flush(); blocks.append(Block("figure", i, [s]))
            in_fig = s.startswith("*[") and not s.endswith("]*")
            continue
        if LIST_RE.match(s) and not in_refs:
            flush(); blocks.append(Block("list", i, [s])); continue
        if buf_start is None:
            buf_start = i
        buf.append(s)
    flush()
    return blocks


URL_RE = re.compile(r"https?://\S+|www\.\S+")


def prose_plain(text, for_lt=False):
    """Prose with inline formulas replaced by plain symbols and markdown emphasis removed.
    for_lt=True: formulas whose plain form carries Cyrillic (\\text{пац}) or subscripts become a
    neutral 'X' so the spell-checker does not chew on them."""
    def repl(m):
        p = tex_to_plain(m.group("tex"))
        if for_lt and (re.search(r"[А-Яа-яІіЇїЄєҐґ_]", p) or len(p) > 12):
            return "X"
        return p
    t = INLINE_MATH_RE.sub(repl, text)
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    t = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"\1", t)
    t = t.replace("&nbsp;", " ")
    return t


def split_sentences(text):
    return [s for s in re.split(r"(?<=[.!?;])\s+(?=[А-ЯІЇЄA-Z«$(])", text) if s.strip()]


# ------------------------------------------------------------------------------------------
def repo_checks(blocks, rules):
    F = []
    # A rule may set "case_sensitive": true when its pattern relies on capitalisation
    # (META_AUTHOR_METHOD spots a surname that way); re.I would defeat the test.
    banned = [(r, re.compile(r["pattern"],
                             re.M if r.get("case_sensitive") else re.I | re.M))
              for r in rules["banned"]]
    allowed_latin = set(rules.get("allowed_latin", []))
    prose_blocks = [b for b in blocks if b.kind == "prose"]

    # 1. first prose paragraph must not carry a number or a result ------------------------
    title_seen = any(b.kind == "heading" for b in blocks[:3])
    if prose_blocks:
        first = prose_plain(prose_blocks[0].text)
        first_sentence = split_sentences(first)[0] if split_sentences(first) else first
        # A proper noun that carries a digit (COVID-19, SARS-CoV-2) is a name, not a
        # quantity; §1 bans opening with numbers/results, not with the disease's name.
        named = re.sub(r"\b(?:%s)(?:[-\u2011\u2013]?[A-Za-z0-9]+)*" % "|".join(
            sorted(map(re.escape, allowed_latin), key=len, reverse=True)),
            "", first_sentence, flags=re.I)
        if re.search(r"\d", named):
            F.append(Finding(prose_blocks[0].start, "OPEN_WITH_NUMBER", "error", first_sentence[:120],
                             "first sentence contains a number — open with the conceptual problem (§1)"))
        if RESULT_VERBS.search(first_sentence):
            F.append(Finding(prose_blocks[0].start, "OPEN_WITH_RESULT", "error", first_sentence[:120],
                             "first sentence states a finding — never open with the result (§1)"))

    # 2. banned phrases / calques / AI tells / meta-commentary ---------------------------
    for b in prose_blocks + [x for x in blocks if x.kind in ("tblcap", "list")]:
        plain = prose_plain(b.text)
        for rule, rx in banned:
            for m in rx.finditer(plain):
                lo, hi = max(0, m.start() - 35), min(len(plain), m.end() + 35)
                F.append(Finding(b.start, rule["id"], rule["severity"], "…" + plain[lo:hi] + "…",
                                 "→ " + rule["fix"]))

    # 2b. colons: placement, then how many per paragraph ---------------------------------
    # A colon is correct Ukrainian where the second clause explains, specifies or gives the
    # cause of the first -- anywhere «а саме» could be inserted -- so these are style, not
    # grammar, with one exception. Two rules, both from the academic style guides:
    #   * a colon may follow only a COMPLETE clause, never a preposition. That one is an
    #     error. Detected narrowly, on a closed list of prepositions, because a general
    #     "is this a complete clause" test needs a parser and would misfire.
    #   * SEVERAL colons in ONE PARAGRAPH means sentences that want splitting. The guides
    #     put this per paragraph, not per document, and note the sciences use the colon
    #     less than the humanities. Explanatory colons are also the punctuation form of the
    #     «тому …» consequence-chaining §2b already bans in conjunctions.
    # A colon ENDING a paragraph introduces the display formula, list or table that follows;
    # the format requires it, and it is never counted.
    PREPS = ("з", "із", "зі", "у", "в", "на", "за", "до", "від", "при", "про", "для",
             "між", "під", "над", "як", "і", "та", "а", "але", "що")
    for b in prose_blocks:
        plain = prose_plain(b.text).strip()
        body = plain[:-1] if plain.endswith(":") else plain
        hits = list(re.finditer(r"(?<=\w):\s+(?=\S)", body))
        for m in hits:
            last = re.findall(r"[\w'’-]+", body[:m.start()])
            if last and last[-1].lower() in PREPS:
                lo = max(0, m.start() - 45)
                F.append(Finding(b.start, "COLON_AFTER_PREP", "error",
                                 "…" + body[lo:m.end() + 25] + "…",
                                 "colon after «%s» — a colon may follow only a complete "
                                 "clause" % last[-1]))
        if len(hits) > 1:
            lo = max(0, hits[0].start() - 30)
            F.append(Finding(b.start, "COLON_PARAGRAPH_DENSITY", "warn",
                             "…" + body[lo:hits[0].end() + 30] + "…",
                             "%d explanatory colons in one paragraph — split the sentences "
                             "or state the condition first (§2)" % len(hits)))

    # 3. structure: lists, bold, run-in lead-ins, tiny sections --------------------------
    for b in blocks:
        if b.kind == "list":
            F.append(Finding(b.start, "LIST_IN_PROSE", "error", b.text[:80],
                             "bullet/numbered list — carry the reasoning in prose (§2)"))
        if b.kind == "prose":
            if re.match(r"^\*\*[^*]{2,80}\*\*[.:]?\s", b.text) or re.match(r"^\*[^*]{2,80}\*[.:]?\s", b.text):
                F.append(Finding(b.start, "RUNIN_LEADIN", "error", b.text[:80],
                                 "run-in subtitle lead-in (bold/italic) — use numbered headings or plain prose (§2)"))
            elif "**" in b.text:
                F.append(Finding(b.start, "BOLD_IN_BODY", "error", b.text[:80],
                                 "bold in body text — bold only in the document title (§2)"))
    heads = [i for i, b in enumerate(blocks) if b.kind == "heading"]
    for k, hi in enumerate(heads):
        if hi == heads[0] and blocks[hi].lines[0].startswith("# "):
            continue  # document title
        nxt = heads[k + 1] if k + 1 < len(heads) else len(blocks)
        n_par = sum(1 for b in blocks[hi + 1:nxt] if b.kind == "prose")
        if n_par <= 1:
            F.append(Finding(blocks[hi].start, "TINY_SECTION", "warn", blocks[hi].text[:80],
                             "heading over ≤1 paragraph — fragmented sectioning is an AI tell (§2)"))

    # 4. formulas: «де» gloss and symbol coverage ----------------------------------------
    # A symbol counts as defined once it has appeared in earlier prose (e.g. «стандартною похибкою
    # SE(ΔD)»), in an earlier gloss, or as the left-hand side of an assignment inside the formula.
    NOISE = {"N", "n", "i", "j", "k", "E", "P", "d", "e", "f", "L", "x", "t", "max", "min"}
    defined, seen_prose = set(), ""
    for i, b in enumerate(blocks):
        if b.kind == "prose":
            seen_prose += " " + prose_plain(b.text).replace(" ", "")
            continue
        if b.kind != "formula":
            continue
        tex = DISPEQ_RE.match(b.lines[0]).group("tex")
        nxt = blocks[i + 1] if i + 1 < len(blocks) else None
        follow = prose_plain(nxt.text) if nxt and nxt.kind == "prose" else ""
        ids = {x for x in formula_identifiers(tex) if x and x not in NOISE}
        lhs = set()
        for part in re.split(r"[,;]|\\quad|\\qquad", tex):
            if "=" in part:
                lhs |= {x for x in formula_identifiers(part.split("=")[0]) if x not in NOISE}
        new_ids = {x for x in ids - defined - lhs if x.replace(" ", "") not in seen_prose}
        if not re.match(r"^де\b", follow):
            if new_ids:
                F.append(Finding(b.start, "FORMULA_NO_DE", "error", tex[:80],
                                 "display formula not followed by a «де …» gloss (§3); symbols never introduced before: " + ", ".join(sorted(new_ids))))
        else:
            gloss = follow.split(".")[0] if "." in follow[:600] else follow
            gloss_norm = gloss.replace(" ", "")
            missing = [x for x in sorted(new_ids) if x.replace(" ", "") not in gloss_norm]
            if missing:
                F.append(Finding(b.start, "FORMULA_SYMBOL_UNGLOSSED", "info", tex[:80],
                                 "symbols not found in the «де» gloss (first time seen): " + ", ".join(missing)))
        defined |= ids | lhs

    # 5. tables: caption form, referenced in text ----------------------------------------
    all_prose = " ".join(prose_plain(b.text) for b in prose_blocks)
    for b in blocks:
        if b.kind == "tblcap":
            m = TBL_CAPTION_RE.match(b.text)
            if not m:
                F.append(Finding(b.start, "TBL_CAPTION_FORM", "error", b.text[:80],
                                 "caption must be «Таблиця N — Назва» (ДСТУ 3008:2015 §8)"))
            else:
                if m.group("sep").startswith("."):
                    F.append(Finding(b.start, "TBL_CAPTION_PERIOD", "error", b.text[:80],
                                     "period after the number — use an em dash, no period (§5)"))
                num = m.group(1)
                if not re.search(r"таблиц[іюя]\s+" + re.escape(num) + r"\b", all_prose, re.I):
                    F.append(Finding(b.start, "TBL_NOT_REFERENCED", "warn", b.text[:80],
                                     "table %s is never named in the prose («наведено в таблиці %s»)" % (num, num)))

    # 6. numbers: decimal point, thousands, bracket stacking -----------------------------
    for b in prose_blocks:
        plain = prose_plain(b.text)
        for m in re.finditer(r"(?<![\w.\[])\d+\.\d+(?![\w.\]])", plain):
            F.append(Finding(b.start, "DECIMAL_POINT", "error", plain[max(0, m.start()-25):m.end()+25],
                             "decimal point in prose — Ukrainian uses a comma (0,015)"))
        for m in re.finditer(r"(?<![\d,.])\d{5,}(?![\d,.])", plain):
            F.append(Finding(b.start, "THOUSANDS_NO_SPACE", "warn", plain[max(0, m.start()-25):m.end()+25],
                             "large number without thousands separator (8 735)"))
        for s in split_sentences(INLINE_MATH_RE.sub("X", b.text)):
            # equation cross-references «(2) у (1)» and brackets inside formulas are not bracketed numbers
            n_brackets = len([g for g in re.findall(r"\(([^()]*\d[^()]*)\)", s) if not re.fullmatch(r"\d+", g.strip())])
            if n_brackets >= 2:
                F.append(Finding(b.start, "BRACKET_STACK", "warn", s[:120],
                                 "%d bracketed numbers in one sentence — restructure (§2)" % n_brackets))

    # 7. Latin-script words in prose that are not allowed abbreviations ------------------
    for b in prose_blocks:
        plain = URL_RE.sub(" ", prose_plain(b.text))
        for m in re.finditer(r"(?<![\w\u0300-\u036f])[A-Za-z][A-Za-z-]{2,}(?![\w\u0300-\u036f])", plain):
            w = m.group(0)
            if w in allowed_latin or w.upper() in allowed_latin or w.rstrip("s") in allowed_latin:
                continue
            F.append(Finding(b.start, "LATIN_WORD", "info", plain[max(0, m.start()-25):m.end()+25],
                             "Latin-script word «%s» in Ukrainian prose — abbreviation, symbol or anglicism?" % w))

    # 8. citations resolve to reference entries -----------------------------------------
    refs = {int(REF_ENTRY_RE.match(b.text).group(1)) for b in blocks if b.kind == "ref"}
    cited = set()
    for b in prose_blocks + [x for x in blocks if x.kind in ("tblcap", "figure", "table")]:
        for m in CITE_RE.finditer(b.text):
            if not is_citation(m.group(1)):
                continue
            for part in re.split(r"[,;]\s*", m.group(1)):
                if re.search(r"[–-]", part):
                    a, z = re.split(r"[–-]", part)
                    cited |= set(range(int(a), int(z) + 1))
                else:
                    cited.add(int(part))
            missing = [n for n in sorted(cited) if refs and n not in refs]
    if refs:
        for n in sorted(cited - refs):
            F.append(Finding(0, "CITE_NO_REF", "error", "[%d]" % n, "cited but absent from «Перелік посилань»"))
        for n in sorted(refs - cited):
            F.append(Finding(0, "REF_NOT_CITED", "warn", "[%d]" % n, "in the reference list but never cited"))
    elif cited:
        F.append(Finding(0, "NO_REF_LIST", "warn", "", "citations present but no «Перелік посилань» block found"))

    return F


# ------------------------------------------------------------------------------------------
LT_URL = "https://api.languagetool.org/v2/check"


def lt_check(blocks, level, ignore_rules, ignore_words=()):
    """Send prose (formulas → plain symbols) to LanguageTool uk-UA in ≤ 9000-char chunks.
    Reference entries are not sent (mostly English titles and DOIs)."""
    F = []
    ignore_words = [re.compile(p, re.I) for p in ignore_words]
    pieces = []  # (block, plain)
    for b in blocks:
        if b.kind in ("prose", "tblcap"):
            pieces.append((b, prose_plain(b.text, for_lt=True)))
        elif b.kind == "figure" and b.text.startswith("*["):
            cap = re.sub(r"^\*\[|\]\*$", "", b.text)
            pieces.append((b, prose_plain(cap, for_lt=True)))
        elif b.kind == "table":
            cells = [c.strip() for c in b.text.strip("|").split("|")]
            txt = " ; ".join(c for c in cells if c and not re.fullmatch(r"[-:\s]+", c))
            if re.search(r"[А-Яа-яІіЇїЄє]{4,}", txt):
                pieces.append((b, prose_plain(txt, for_lt=True)))
    chunks, cur, cur_len = [], [], 0
    for b, t in pieces:
        if cur and cur_len + len(t) + 2 > 9000:
            chunks.append(cur); cur, cur_len = [], 0
        cur.append((b, t)); cur_len += len(t) + 2
    if cur:
        chunks.append(cur)

    for ci, chunk in enumerate(chunks):
        text, offsets = "", []
        for b, t in chunk:
            offsets.append((len(text), len(text) + len(t), b))
            text += t + "\n\n"
        data = urllib.parse.urlencode({"language": "uk-UA", "text": text, "level": level}).encode()
        req = urllib.request.Request(LT_URL, data=data, headers={"User-Agent": "style_check/1.0"})
        for attempt in range(4):
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    resp = json.load(r)
                break
            except Exception as e:  # rate limit → back off
                if attempt == 3:
                    F.append(Finding(0, "LT_UNAVAILABLE", "warn", "", "LanguageTool request failed: %s" % e, "lt"))
                    resp = {"matches": []}
                else:
                    time.sleep(8 * (attempt + 1))
        for m in resp.get("matches", []):
            rid = m["rule"]["id"]
            if rid in ignore_rules:
                continue
            off = m["offset"]
            blk = next((b for lo, hi, b in offsets if lo <= off < hi), None)
            ctx = m["context"]
            bad = ctx["text"][ctx["offset"]:ctx["offset"] + ctx["length"]]
            if rid == "UPPERCASE_SENTENCE_START" and bad.lower() == "де":
                continue  # «де …» gloss legitimately opens lowercase after a display formula
            if rid.startswith("MORFOLOGIK") and any(rx.fullmatch(bad) for rx in ignore_words):
                continue  # domain vocabulary the LT dictionary lacks (drug names, нерандомізований…)
            if rid.startswith("MORFOLOGIK") and (bad == "X" or re.search(r"[A-Za-z_]", bad)):
                continue  # placeholder or symbol fragment, not a word
            repl = [r["value"] for r in m.get("replacements", [])[:3]]
            cat = m["rule"]["category"]["name"]
            sev = "warn" if cat in ("Варваризми", "Граматика", "Правопис", "Пунктуація") else "info"
            snippet = ctx["text"][max(0, ctx["offset"] - 30):ctx["offset"] + ctx["length"] + 30]
            msg = "%s | «%s»%s — %s" % (cat, bad, (" → " + " / ".join(repl)) if repl else "", m["message"])
            F.append(Finding(blk.start if blk else 0, "LT:" + rid, sev, snippet, msg, "lt"))
        if ci + 1 < len(chunks):
            time.sleep(3.5)  # public API: stay under the per-minute limit
    return F


# ------------------------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path")
    ap.add_argument("--no-lt", action="store_true", help="skip the LanguageTool pass")
    ap.add_argument("--lt-level", default="picky", choices=["default", "picky"])
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--rules", default=str(RULES_PATH))
    ap.add_argument("--fragment", action="store_true",
                    help="text is a mid-document excerpt: skip the opening-sentence checks")
    a = ap.parse_args()

    if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")

    rules = json.loads(Path(a.rules).read_text(encoding="utf-8"))
    src = Path(a.path).read_text(encoding="utf-8")
    blocks = parse_blocks(src)
    findings = repo_checks(blocks, rules)
    if a.fragment:
        findings = [f for f in findings if not f.rule.startswith("OPEN_WITH_")]
    if not a.no_lt:
        findings += lt_check(blocks, a.lt_level, set(rules.get("lt_ignore_rules", [])),
                             rules.get("lt_ignore_words", []))

    order = {"error": 0, "warn": 1, "info": 2}
    findings.sort(key=lambda f: (order[f.severity], f.line, f.rule))

    if a.json:
        print(json.dumps([f.as_dict() for f in findings], ensure_ascii=False, indent=1))
    else:
        n_prose = sum(1 for b in blocks if b.kind == "prose")
        n_form = sum(1 for b in blocks if b.kind == "formula")
        n_inl = len(INLINE_MATH_RE.findall(src))
        print("style_check: %s — %d paragraphs, %d display formulas, %d inline formulas (excluded from LT)"
              % (a.path, n_prose, n_form, n_inl))
        counts = {k: sum(1 for f in findings if f.severity == k) for k in order}
        print("errors: %(error)d   warnings: %(warn)d   info: %(info)d\n" % counts)
        for sev in ("error", "warn", "info"):
            grp = [f for f in findings if f.severity == sev]
            if not grp:
                continue
            print("== %s ==" % sev.upper())
            for f in grp:
                loc = ("L%d" % f.line) if f.line else "doc"
                print("%-5s [%s] %s" % (loc, f.rule, f.message))
                if f.snippet:
                    print("      %s" % f.snippet.replace("\n", " "))
            print()
    sys.exit(1 if any(f.severity == "error" for f in findings) else 0)


if __name__ == "__main__":
    main()
