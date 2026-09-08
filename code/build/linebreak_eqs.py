import re, io
BS="\\"
WIDTH=74.0
NUMW=50.0          # target width per stacked-numerator row
REBREAK_WIDTH=58.0 # target max row width when re-packing already-broken eqs (see rebreak())

def est(s):
    i=0;w=0.0;n=len(s)
    def grab(i):
        d=0;j=i
        while j<n:
            if s[j]=='{':d+=1
            elif s[j]=='}':
                d-=1
                if d==0:return s[i+1:j],j+1
            j+=1
        return s[i+1:],n
    while i<n:
        c=s[i]
        if c==BS:
            m=re.match(r"\\[A-Za-z]+",s[i:])
            if m:
                cmd=m.group(0);i+=len(cmd)
                if cmd==BS+"frac":
                    a,i=grab(i) if i<n and s[i]=='{' else ("",i)
                    b,i=grab(i) if i<n and s[i]=='{' else ("",i)
                    w+=max(est(a),est(b))+0.6
                elif cmd in(BS+"mathrm",BS+"text",BS+"sqrt",BS+"hat",BS+"tilde"):
                    ex=1.0 if cmd==BS+"sqrt" else 0.0
                    if i<n and s[i]=='{':
                        inner,i=grab(i);w+=est(inner)+ex
                elif cmd==BS+"cdot":w+=1.0
                elif cmd in(BS+"dots",BS+"ldots"):w+=1.5
                elif cmd==BS+"times":w+=1.2
                elif cmd in(BS+"left",BS+"right"):w+=0.6
                else:w+=1.1
            else:i+=2;w+=1.0
        elif c in '_^':
            i+=1
            if i<n and s[i]=='{':
                inner,i=grab(i);w+=0.55*est(inner)
            else:w+=0.55;i+=1
        elif c=='{':
            inner,i=grab(i);w+=est(inner)
        elif c=='}':i+=1
        elif c==' ':i+=1;w+=0.4
        elif c in '+-=<>':i+=1;w+=1.4
        else:i+=1;w+=1.0
    return w

def neutralize(s):
    s=s.replace(BS+"left\\{","\\{").replace(BS+"right\\}","\\}")
    s=s.replace(BS+"left(","(").replace(BS+"right)",")")
    s=s.replace(BS+"left[","[").replace(BS+"right]","]")
    s=s.replace(BS+"left.","").replace(BS+"right.","")
    return s

def split_top(s, ops="+-=", times=True, maxdepth=0):
    n=len(s);i=0;depth=0;segs=[];cur=[]
    def flush():
        if cur:segs.append("".join(cur));cur.clear()
    while i<n:
        c=s[i]
        if c in '{([':depth+=1;cur.append(c);i+=1;continue
        if c in '})]':depth-=1;cur.append(c);i+=1;continue
        if depth<=maxdepth and c==BS:
            if times and re.match(r"\\times\b",s[i:]):
                flush();cur.append(BS+"times");i+=6;continue
            m=re.match(r"\\dots|\\ldots",s[i:])
            if m:flush();segs.append(m.group(0));i+=len(m.group(0));continue
            m2=re.match(r"\\[A-Za-z]+",s[i:])
            if m2:cur.append(m2.group(0));i+=len(m2.group(0));continue
            cur.append(s[i:i+2]);i+=2;continue
        if depth<=maxdepth and c in ops:
            flush();cur.append(c);i+=1;continue
        cur.append(c);i+=1
    flush()
    return [x.strip() for x in segs if x.strip()]

def pack(segs, width=WIDTH):
    lines=[];cur="";cw=0.0;first=True
    for seg in segs:
        sw=est(seg)
        op_lead=(bool(seg) and seg[0] in '+-=') or seg.startswith(BS+"times")
        if first:cur=seg;cw=sw;first=False;continue
        if cw+sw<=width or not op_lead:
            cur+=" "+seg;cw+=sw+0.4
        else:
            lines.append(cur);cur=seg;cw=sw
    if cur:lines.append(cur)
    return lines

def stack_numerator(num):
    """num = inner string of \\frac{...} (may include surrounding [ ]). Stack at top-level +,-."""
    core=num.strip()
    lb=rb=""
    if core.startswith("[") and core.endswith("]"):
        lb,rb="[ "," ]";core=core[1:-1].strip()
    pieces=split_top(core, ops="+-", times=False, maxdepth=0)
    plines=pack(pieces, width=NUMW)
    # any single row still too wide (e.g. an atomic  -2(x+y+z)  term)? split one level deeper.
    fixed=[]
    for pl in plines:
        if est(pl)>WIDTH-4:
            fixed.extend(pack(split_top(pl, ops="+-", times=False, maxdepth=1), width=NUMW))
        else:
            fixed.append(pl)
    plines=fixed
    if len(plines)<2:
        return None
    inner=BS+"begin{aligned} & "+plines[0]
    for pl in plines[1:]:
        inner+=" "+BS*4+" & "+pl
    inner+=" "+BS+"end{aligned}"
    return lb+inner+rb

def stack_fracs_in(seg):
    """Find \\frac{NUM}{DEN} groups; stack wide numerators."""
    out=[];i=0;n=len(seg)
    def grab(i):
        d=0;j=i
        while j<n:
            if seg[j]=='{':d+=1
            elif seg[j]=='}':
                d-=1
                if d==0:return seg[i+1:j],j+1
            j+=1
        return seg[i+1:],n
    while i<n:
        if seg[i:i+5]==BS+"frac" and i+5<n and seg[i+5]=='{':
            num,j=grab(i+5)
            if j<n and seg[j]=='{':
                den,k=grab(j)
                if est(num)>NUMW+6:
                    st=stack_numerator(num)
                    if st is not None:
                        out.append(BS+"frac{"+st+"}{"+den+"}");i=k;continue
                out.append(seg[i:k]);i=k;continue
        out.append(seg[i]);i+=1
    return "".join(out)

def anchor(row):
    idx=row.find('=')
    if idx==-1:return row
    return row[:idx].rstrip()+" &= "+row[idx+1:].lstrip()

def break_general(tex):
    neu=neutralize(tex)
    segs=split_top(neu, ops="+-=", times=True)
    # merge LHS with its '=' segment so the head isn't stranded
    if len(segs)>=2 and segs[1].startswith('='):
        segs=[segs[0]+" "+segs[1]]+segs[2:]
    # stack wide fractions inside each segment
    segs=[stack_fracs_in(s) for s in segs]
    lines=pack(segs)
    changed_stack=any("begin{aligned}" in s for s in segs)
    if len(lines)==1:
        if changed_stack:
            return lines[0]           # single fraction w/ stacked numerator, no outer aligned
        return None
    body=anchor(lines[0])
    for row in lines[1:]:
        body+=" "+BS*4+" &"+row
    return BS+"begin{aligned} "+body+" "+BS+"end{aligned}"

NESTED_ENVS = ("begin{cases}", "begin{bmatrix}", "begin{vmatrix}", "begin{pmatrix}",
               "begin{matrix}", "begin{array}", "begin{split}", "begin{gathered}")


def flatten_aligned(inner):
    """Collapse an aligned body back to one linear expression (drop `\\\\` breaks and `&` tabs)."""
    s = inner.replace(BS * 4, " ").replace("&", " ")
    return re.sub(r"\s+", " ", s).strip()


def rebreak(tex, width=REBREAK_WIDTH):
    """Re-pack a display eq (single-line OR already-`aligned`) so every ROW is <= width.

    The original ``process()`` only breaks a *single-line* eq once and never revisits an
    already-broken one -- so a broken eq can still have one row wider than the column. rebreak
    flattens the aligned wrapper (discarding its old break points), then re-splits at top-level
    +,-,=,\\times and re-packs. Returns new tex, or None if it can't improve or the eq contains a
    nested environment (cases/matrix) that must not be reflowed. Round-trip token check is the
    caller's job. Used to fix the Ch.4-5 multi-row overflows Dmytro flagged (2026-08-12)."""
    t = tex.strip()
    m = re.match(r"^\\begin\{aligned\}(.*)\\end\{aligned\}$", t, re.S)
    if m:
        inner = m.group(1)
        if any(e in inner for e in NESTED_ENVS):
            return None
        linear = flatten_aligned(inner)
    else:
        if "begin{" in t:
            return None
        linear = t
    neu = neutralize(linear)
    segs = split_top(neu, ops="+-=", times=True)
    if len(segs) >= 2 and segs[1].startswith("="):
        segs = [segs[0] + " " + segs[1]] + segs[2:]
    segs = [stack_fracs_in(s) for s in segs]
    lines = pack(segs, width=width)
    if len(lines) == 1:
        return None
    body = anchor(lines[0])
    for row in lines[1:]:
        body += " " + BS * 4 + " &" + row
    return BS + "begin{aligned} " + body + " " + BS + "end{aligned}"


def rebreak_all(md_path, width=REBREAK_WIDTH, apply=False):
    """Re-break every display eq (incl. already-aligned) so rows fit `width`. Round-trip
    token-checked -- only line breaks change, never a math token. Returns a report; writes in
    place when apply=True. Note: a nested cases/matrix row (e.g. the double-cases g(z), the
    EVSI_J brace) is skipped -- those were hand-broken; see [[chen-equation-rendering]]."""
    lines = io.open(md_path, encoding="utf-8").read().split("\n")
    rep = []
    for i, raw in enumerate(lines):
        m = DISP.match(raw.strip())
        if not m:
            continue
        tex = m.group(2).strip()
        is_multi = "begin{aligned" in tex
        if not (is_multi or "begin{" not in tex):
            continue
        nt = rebreak(tex, width)
        if nt is None:
            continue
        if strip_markup(neutralize(tex)) != strip_markup(nt):
            rep.append((i + 1, "SKIP: round-trip token mismatch"))
            continue
        old = max_row(tex) if is_multi else est(neutralize(tex))
        new = max_row(nt)
        if new >= old - 0.5:
            continue        # only accept a genuine improvement (protects hand-broken eqs like EVSI_J)
        rep.append((i + 1, "rebroke maxrow %.0f -> %.0f" % (old, new)))
        if apply:
            lines[i] = raw[:len(raw) - len(raw.lstrip())] + "$$" + nt + m.group(3)
    if apply:
        io.open(md_path, "w", encoding="utf-8").write("\n".join(lines))
    return rep


def strip_markup(s):
    s=s.replace(BS+"begin{aligned}","").replace(BS+"end{aligned}","")
    s=s.replace(BS*4,"").replace("&","")
    return re.sub(r"\s+","",neutralize(s))

def max_row(newtex):
    inner=newtex.replace(BS+"begin{aligned}","").replace(BS+"end{aligned}","")
    return max(est(r.replace("&","")) for r in inner.split(BS*4))

def matrix_convert(tex):
    """S_{10} = [ A , B ; C , D ]  ->  bmatrix (a 2x2 MATRIX with [ ] brackets).

    NOT vmatrix: | | denotes a determinant (a scalar), which is wrong for defining a
    covariance matrix -- Chen's text says "2x2 matrix". Row separator is TWO backslashes
    (texmath renders `\\\\` in a matrix as an empty-cell box; `\\` gives clean rows) -- see
    [[chen-equation-rendering]]."""
    m=re.match(r"^(.*?=)\s*\[(.+)\]\s*$", tex, re.S)
    if not m: return None, None
    lhs, body = m.group(1), m.group(2)
    rows=split_top(body, ops=";", times=False)
    cells=[split_top(r, ops=",", times=False) for r in rows]
    flat=[c for row in cells for c in row]
    mat=BS+"begin{bmatrix} "+(" "+BS*2+" ").join(" & ".join(row) for row in cells)+" "+BS+"end{bmatrix}"
    return lhs+" "+mat, flat

DISP = re.compile(r"^(\$\$)(.+?)(\$\$.*)$")
MULTI = ("begin{aligned}", "begin{vmatrix}", "begin{bmatrix}", "begin{pmatrix}",
         "begin{cases}", "begin{array}", "begin{matrix}", "begin{split}", "begin{gathered}")
# Calibration (2026-08-12, from Dmytro's Word screenshots): rows really overflow the ~16.5cm
# column around est 74; already-broken rows at 72-79 still ran off. So re-break to <= 58 for
# margin (see rebreak() below). OVERFLOW is the detection threshold for still-single eqs.
OVERFLOW = 82.0        # detection threshold for still-single-line eqs (REBREAK_WIDTH is at top)


def process(md_path, threshold=OVERFLOW, apply=False):
    """Auto-detect single-line display equations wider than `threshold` and line-break
    them (operator / \\times split, wide-fraction numerator stacking). Returns a report;
    writes the file in place when apply=True. Every rewrite is round-trip token-checked, so
    only line breaks are inserted -- no math token is ever changed.

    NOTE: an [ A , B ; C , D ] 2x2-matrix mis-transcription is a STRUCTURAL fix (changes
    tokens), so it is NOT auto-applied -- it is only reported, for a human to verify vs the
    source and convert with matrix_convert()."""
    lines = io.open(md_path, encoding="utf-8").read().split("\n")
    rep = []
    for i, raw in enumerate(lines):
        m = DISP.match(raw.strip())
        if not m:
            continue
        tex = m.group(2).strip()
        if any(x in tex for x in MULTI):
            continue
        if est(neutralize(tex)) <= threshold:
            continue
        # matrix mis-transcription: report only (structural, needs human verify vs PDF)
        if re.match(r"^.*?=\s*\[.+;.+\]\s*$", tex):
            rep.append((i + 1, "MATRIX? verify vs source, then matrix_convert()"))
            continue
        nt = break_general(tex)
        if nt is None:
            rep.append((i + 1, "OVERFLOW est=%.0f but no clean break point" % est(neutralize(tex))))
            continue
        if strip_markup(neutralize(tex)) != strip_markup(nt):
            rep.append((i + 1, "SKIP: round-trip token mismatch"))
            continue
        rep.append((i + 1, "broke -> rows fit, maxrow=%.1f" % max_row(nt)))
        if apply:
            lines[i] = raw[:len(raw) - len(raw.lstrip())] + "$$" + nt + m.group(3)
    if apply:
        io.open(md_path, "w", encoding="utf-8").write("\n".join(lines))
    return rep


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("usage: python linebreak_eqs.py <template.md> [--apply] [--rebreak]")
        print("  (default) break over-wide SINGLE-line eqs at operators")
        print("  --rebreak re-pack ALL eqs (incl. already-aligned) so rows <= %g" % REBREAK_WIDTH)
        raise SystemExit(2)
    do_apply = "--apply" in sys.argv[2:]
    runner = rebreak_all if "--rebreak" in sys.argv[2:] else process
    for ln, msg in runner(sys.argv[1], apply=do_apply):
        print("%5d  %s" % (ln, msg))
    print("(dry run -- pass --apply to write)" if not do_apply else "(applied)")
