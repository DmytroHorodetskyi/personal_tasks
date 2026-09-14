"""Did each video actually reach a working document, or is it only logged in the audit?

    PYTHONUTF8=1 venv/Scripts/python.exe tasks/hardware/pc_build/audit_tools/accounted.py
    ...                                                                      --orphans

`verify_audit.py` proves every video was read and quoted in source_audit.md.  That is not
the same as the video being *used*.  A transcript can be read, quoted, and then contribute
nothing to cpu.md / headphones.md / earbuds.md - and the audit has already caught three
"nothing usable here" dismissals that turned out to be false, so silence is not evidence of
irrelevance.

For each of the 99 ids this reports where it is accounted for:

    DOC-ID     the id itself appears in a working document - the strongest form
    DOC-NAME   the channel or the video title appears in a working document
    AUDIT      it appears only in source_audit.md, so the audit must say why nothing
               was taken.  --orphans prints the audit's own verdict lines for these so
               the dismissal can be read rather than trusted.

"Working document" means every .md under tasks/hardware/ except source_audit.md itself and
the sources/ transcripts.
"""

import glob
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
HARDWARE = os.path.dirname(ROOT)
SOURCES = os.path.join(ROOT, "sources")
AUDIT = os.path.join(ROOT, "source_audit.md")

STOP = {"tech", "the", "and", "pc", "tv", "ua", "com", "gaming", "hardware", "reviews",
        "review", "channel", "official", "media", "studio", "audio", "news"}


def working_docs():
    """Every .md under tasks/hardware/ that is not the audit and not a transcript."""
    out = {}
    for path in glob.glob(os.path.join(HARDWARE, "**", "*.md"), recursive=True):
        full = os.path.abspath(path)
        if full == os.path.abspath(AUDIT):
            continue
        if os.path.abspath(SOURCES) in full:
            continue
        out[os.path.relpath(full, HARDWARE)] = io.open(full, encoding="utf-8").read()
    return out


def meta(path):
    """(title, channel) from a transcript header: '# Title' then 'Channel | date | ...'."""
    title, channel = "", ""
    with io.open(path, encoding="utf-8") as fh:
        lines = [next(fh, "") for _ in range(6)]
    for ln in lines:
        ln = ln.strip()
        if ln.startswith("# ") and not title:
            title = ln[2:].strip()
        elif "|" in ln and not channel and not ln.startswith("#"):
            channel = ln.split("|")[0].strip()
    return title, channel


def name_keys(title, channel):
    """Distinctive strings worth searching a document for."""
    keys = []
    if channel and len(channel) > 3:
        keys.append(channel)
    # the longest few words of the title, which is what a doc would quote
    words = [w.strip(".,!?:()\"'") for w in title.split()]
    words = [w for w in words if len(w) > 4 and w.lower() not in STOP]
    keys.extend(sorted(set(words), key=len, reverse=True)[:4])
    return keys


def classify():
    docs = working_docs()
    blob = "\n".join(docs.values())
    rows = []
    for path in sorted(glob.glob(os.path.join(SOURCES, "*.md"))):
        base = os.path.basename(path)
        vid = os.path.splitext(base)[0].split("_", 1)[1]
        if len(vid) != 11:
            continue
        title, channel = meta(path)
        where = [n for n, t in docs.items() if vid in t]
        if where:
            rows.append((vid, base, "DOC-ID", channel, title, where))
            continue
        hits = [k for k in name_keys(title, channel) if k and k in blob]
        if hits:
            where = sorted({n for n, t in docs.items()
                            if any(k in t for k in hits)})
            rows.append((vid, base, "DOC-NAME", channel, title, where[:3]))
        else:
            rows.append((vid, base, "AUDIT", channel, title, []))
    return rows


def audit_verdicts(vid):
    """The audit's own lines mentioning this id, so a dismissal can be read."""
    out = []
    for ln in io.open(AUDIT, encoding="utf-8"):
        if vid in ln:
            out.append(ln.strip())
    return out


def main(argv):
    rows = classify()
    counts = {"DOC-ID": 0, "DOC-NAME": 0, "AUDIT": 0}
    for vid, base, kind, channel, title, where in rows:
        counts[kind] += 1
    if "--orphans" in argv:
        for vid, base, kind, channel, title, where in rows:
            if kind != "AUDIT":
                continue
            print("=" * 78)
            print("%s  %s" % (vid, base))
            print("  %s - %s" % (channel, title))
            for ln in audit_verdicts(vid)[:6]:
                print("  | %s" % ln[:300])
            print("")
        return 0

    for vid, base, kind, channel, title, where in rows:
        tag = {"DOC-ID": "DOC-ID  ", "DOC-NAME": "DOC-NAME", "AUDIT": "AUDIT   "}[kind]
        print("%s %-12s %-34s %s" % (tag, vid, base,
                                     ", ".join(where[:2]) if where else "(audit only)"))
    print("")
    print("cited by id in a working document   : %d" % counts["DOC-ID"])
    print("cited by channel or title           : %d" % counts["DOC-NAME"])
    print("only in source_audit.md             : %d" % counts["AUDIT"])
    print("total                               : %d" % len(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
