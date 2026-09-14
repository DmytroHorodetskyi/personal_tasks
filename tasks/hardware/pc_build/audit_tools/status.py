"""Per-component status: join verify_audit.py's PASS/FAIL with the component map."""
import io
import subprocess
import sys
from collections import OrderedDict

ROOT = r"C:\Users\Dmitriy\Documents\GitHub\personal_tasks"
GROUPS = ROOT + r"\tasks\hardware\pc_build\sources\GROUPS.tsv"
VERIFY = ROOT + r"\tasks\hardware\pc_build\verify_audit.py"

group = {}
for line in io.open(GROUPS, encoding="utf-8"):
    if line.startswith("#") or not line.strip():
        continue
    parts = line.rstrip("\n").split("\t")
    if len(parts) >= 2:
        group[parts[1]] = parts[0]

out = subprocess.run([sys.executable, VERIFY], capture_output=True, text=True,
                     encoding="utf-8", errors="replace").stdout

status = {}
for line in out.splitlines():
    bits = line.split()
    if len(bits) >= 2 and bits[1] in ("PASS", "FAIL"):
        status[bits[0]] = bits[1]

order = ["psu", "ssd", "ram", "monitor", "cooler", "case", "build",
         "mb", "gpu", "combo", "mouse", "keyboard", "headset", "laptop", "earbuds"]
tally = OrderedDict((k, [0, 0]) for k in order)
for vid, g in group.items():
    st = status.get(vid, "FAIL")
    tally.setdefault(g, [0, 0])
    tally[g][0] += 1
    if st == "PASS":
        tally[g][1] += 1

print("%-10s %5s %5s  %s" % ("component", "total", "done", "status"))
done_t = tot_t = 0
for g, (tot, done) in tally.items():
    tot_t += tot
    done_t += done
    mark = "DONE" if done == tot else ("-" if done == 0 else "partial")
    print("%-10s %5d %5d  %s" % (g, tot, done, mark))
print("%-10s %5d %5d" % ("TOTAL", tot_t, done_t))
