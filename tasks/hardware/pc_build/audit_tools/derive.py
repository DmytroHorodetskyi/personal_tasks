"""Re-derive every link the user sent, from the raw session transcripts."""
import json, os, re, glob, sys

TDIR = r"C:\Users\Dmitriy\.claude\projects\C--Users-Dmitriy-Documents-GitHub-personal-tasks"

YT = re.compile(
    r"(?:youtube\.com/(?:watch\?(?:[^\s\"'<>]*&)?v=|embed/|shorts/|live/)|youtu\.be/)"
    r"([A-Za-z0-9_-]{11})")
URL = re.compile(r"https?://[^\s\)\]\"'<>,]+")

def text_of(msg):
    c = msg.get("content")
    if isinstance(c, str):
        return c
    out = []
    if isinstance(c, list):
        for b in c:
            if isinstance(b, dict) and b.get("type") == "text":
                out.append(b.get("text", ""))
            elif isinstance(b, str):
                out.append(b)
    return "\n".join(out)

vids = {}      # id -> (file, lineno, first url seen)
others = {}    # url -> (file, lineno)
order = []

for path in sorted(glob.glob(os.path.join(TDIR, "*.jsonl"))):
    base = os.path.basename(path)
    with open(path, encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except Exception:
                continue
            if rec.get("type") != "user":
                continue
            msg = rec.get("message") or {}
            if msg.get("role") != "user":
                continue
            t = text_of(msg)
            if not t:
                continue
            # skip tool results / system reminders injected as user turns
            if rec.get("toolUseResult") is not None:
                continue
            for u in URL.findall(t):
                u = u.rstrip('.,;:')
                m = YT.search(u)
                if m:
                    vid = m.group(1)
                    if vid not in vids:
                        vids[vid] = (base, ln, u)
                        order.append(vid)
                else:
                    if u not in others:
                        others[u] = (base, ln)

print("YOUTUBE:", len(vids))
for v in order:
    b, ln, u = vids[v]
    print(f"{v}\t{b[:8]}:{ln}\t{u}")
print()
print("NON-YOUTUBE:", len(others))
for u, (b, ln) in others.items():
    print(f"{b[:8]}:{ln}\t{u}")
