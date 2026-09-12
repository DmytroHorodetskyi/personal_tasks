# Storage (SSD)

## What storage does for this machine

This was missing from your original list, and for your work it is more important than the
list order suggests. Development is a *small-random-IO* workload: a language server indexing
50 000 files, `git status` on a heavy repo, `npm install`, Claude Code reading and writing
across a tree, container layers unpacking. None of that is a big sequential file - it is
thousands of tiny reads and writes where **latency and consistency** matter and the
advertised "7 300 MB/s" is irrelevant.

Games are the opposite: large sequential reads, where any modern NVMe drive is fine.

## The characteristics that matter, and how to read them

Ordered by how much each one decides the purchase. Note that the number printed largest on
the box - sequential MB/s - is last.

| # | Spec (unit) | What it means, plainly | What it is here |
|---|---|---|---|
| 1 | **DRAM cache: yes or no** | A DRAM chip on the drive holding the map of where data actually lives. DRAM-less drives borrow a little system RAM instead (HMB). Under sustained mixed small writes - compiles, container layers, unpacking a big repo - **DRAM-less drives fall off a cliff and stay slow**; DRAM drives hold up and recover. | **This is the row that matters most for your work.** The 990 PRO 2TB has 2GB of LPDDR4. It is why the Kingston NV3 is rejected. |
| 2 | **NAND type (TLC / QLC)** | Bits stored per cell. QLC is cheaper, writes slower and wears out faster. | **TLC only** for a working drive. Watch for SKUs that ship either one under a single name - the NV3 does exactly that. |
| 3 | **Random 4K read at QD1 (IOPS / us)** | Single small reads with nothing queued - which is what an OS and a toolchain actually do all day. **The most predictive number for "does the machine feel fast".** | Not on any box; only reviewers measure it. The 990 PRO leads every Gen4 drive here, at roughly 2x a cheap drive. |
| 4 | **Sustained write after the SLC cache (MB/s)** | Drives write fast into a small fast zone, then fall back to the real speed. Reviews report that floor. | Felt when you unpack a large repo or install a 150GB game. Where cheap drives embarrass themselves. |
| 5 | **Endurance (TBW)** | Total bytes writable under warranty. A dev machine writes a lot - builds, node_modules, container layers. | 990 PRO 2TB is **1 200 TBW** = ~650GB a day for five years. Comfortable. **Do not buy a drive that hides this number.** |
| 6 | **Interface (PCIe 4.0 / 5.0)** | Gen4 x4 is ~7 000 MB/s, Gen5 x4 ~14 000. | **PCIe 4.0.** Gen5 doubles only row 7, changes nothing in rows 1-5, runs hotter and costs more. |
| 7 | **Sequential read/write (MB/s)** | Big contiguous file transfers. The headline number, and the least relevant one here - nothing in this workload reads at 7 GB/s. | Every drive on the shortlist is 6 500-7 450 MB/s. Effectively a tie. Ignore it. |
| 8 | **Capacity (TB) and M.2 slots** | Windows plus tooling plus a few modern games, at 100-150GB per AAA title. | 1TB is tight-but-workable, 2TB comfortable. Every board in [motherboard.md](motherboard.md) has 2+ M.2 slots, so a second drive later is always an option. |

**Ignore:** the sequential MB/s on the box, "PS5 compatible" marketing, bundled cloning
software, and any drive whose controller and NAND the manufacturer will not name.

## Specifications

| | **Samsung 990 PRO 2TB** | 990 PRO 1TB | SK hynix Platinum P41 2TB |
|---|---|---|---|
| Interface | PCIe 4.0 x4, NVMe 2.0 | PCIe 4.0 x4 | PCIe 4.0 x4 |
| Form factor | M.2 2280, single-sided | M.2 2280 | M.2 2280 |
| Controller | Samsung Pascal (8nm) | Samsung Pascal | SK hynix Aries |
| NAND | Samsung V-NAND **TLC** | TLC | **TLC** |
| **DRAM cache** | **2GB LPDDR4** | 1GB LPDDR4 | yes |
| Sequential read | **7 450 MB/s** | 7 450 MB/s | 7 000 MB/s |
| Sequential write | **6 900 MB/s** | 6 900 MB/s | 6 500 MB/s |
| Random read (QD32) | 1 550 000 IOPS | 1 200 000 IOPS | 1 400 000 IOPS |
| Random write (QD32) | 1 400 000 IOPS | 1 550 000 IOPS | 1 300 000 IOPS |
| **Endurance (TBW)** | **1 200 TBW** | 600 TBW | 1 200 TBW |
| Warranty | 5 years | 5 years | 5 years |

Which of those numbers actually matters for this machine, in order:

1. **DRAM cache: yes or no.** A drive with its own DRAM keeps the map of where data lives on
   the drive. DRAM-less drives borrow system RAM and fall apart under sustained mixed small
   writes - compiles, container layers, unpacking a big repo. This is the single most
   important row.
2. **TLC, not QLC.** Bits per cell. QLC is cheaper, writes slower and wears faster.
3. **Random 4K at QD1** - not in the table because manufacturers don't publish it, only
   reviewers measure it. It is what "the machine feels fast" actually is. The 990 PRO leads
   every Gen4 drive here.
4. **TBW** - how much you may write under warranty. 1 200 TBW is roughly 650GB written every
   day for five years. You will not reach it.
5. **Sequential MB/s** - the number on the box, and the least relevant of the five. Nothing
   in this workload reads 7 GB/s sequentially.

This is also why Gen5 is rejected: it doubles row 5 and changes none of rows 1-4, while
running hotter.

## Options

Prices: lowest hotline.ua offer, 2026-09-09, UAH.

| Model | UAH | Cap | Interface | DRAM | Verdict |
|---|---:|---|---|---|---|
| ~~Kingston NV3 1TB~~ | 7 199 | 1TB | PCIe 4.0 | no | **Rejected after the deep pass - variable BOM, see below.** |
| ~~Kingston NV3 2TB~~ | 12 762 | 2TB | PCIe 4.0 | no | **Rejected - same reason.** |
| ~~Kingston KC3000 1TB~~ | 9 999 | 1TB | PCIe 4.0 | yes | **Withdrawn - appears end-of-life**, a 2021 Phison E18 design, and its QD1 latency is not competitive with the 990 PRO. |
| **Samsung 990 PRO 1TB** | **10 149** | 1TB | PCIe 4.0 | 1GB | Best-measured QD1 random read of any Gen4 drive. The cheap-but-right option. |
| **Samsung 990 PRO 2TB** | **16 299** | 2TB | PCIe 4.0 | 2GB | **The pick.** Same drive, twice the space, in the year when NAND is structurally expensive. |
| SK hynix Platinum P41 1TB | 14 249 | 1TB | PCIe 4.0 | yes | Excellent drive - best documented sustained write in Gen4 (1.5-1.8 GB/s post-cache) - but **4 100 more than a 990 PRO 1TB** here. Wrong market for it. |
| SK hynix Platinum P41 2TB | 17 560 | 2TB | PCIe 4.0 | yes | +1 261 over the 990 PRO 2TB. Fine if the shop has it and Samsung is out of stock. |
| Samsung 9100 PRO 1TB | 10 860 | 1TB | PCIe 5.0 | yes | Gen5 does nothing for this workload, and it wants the board's M.2 heatsink. No. |
| SK hynix Platinum P51 2TB | 34 258 | 2TB | PCIe 5.0 | yes | Same objection, twice the price. No. |
| Apacer AS2280Q4U 1TB | 9 090 | 1TB | PCIe 4.0 | - | PS5-marketed, undocumented internals. No. |
| Wibrand Caiman 1TB | 5 850 | 1TB | PCIe 3.0 | no | Gen3, unknown controller. No. |

## Evidence (revised after the deep review pass, 2026-09-09)

**The Kingston NV3 is disqualified, and not for performance reasons.** Different reviewers
and specification databases identify **different silicon under the same product name**:
Phison E27T with Kioxia BiCS6 TLC, Silicon Motion SM2268XT2, TenaFE TC2201, and some
variants with **232-layer QLC NAND from YMTC**. Tom's Hardware describes this as a
deliberate variable-BOM strategy that varies "depending on capacity and availability". The
variation spans **TLC versus QLC**, not just controllers - so two drives with the same SKU
on the same invoice can differ in sustained write speed and effective endurance. You cannot
know what you are buying. Its warranty is also **3 years** (vs 5 for the Samsung), with
320/640 TBW at 1/2TB.

**How bad the HMB path can get:** a representative HMB QLC drive collapses to **400 MB/s**
once its SLC cache fills. HMB itself is capped at roughly **64MB** of borrowed system RAM -
a small mapping window for a multi-terabyte drive full of small files - and DRAM-less
designs carry higher write amplification and degrade specifically "when you're using most
of your system RAM (heavy multitasking, VMs)". That is a description of your machine.

**Why the 990 PRO wins the metric that matters here:** it carries real onboard LPDDR4
(1GB at 1TB, 2GB at 2TB), read latency around **40 microseconds**, and reviewers describe it
as the best random-read, low-queue-depth performance tested among Gen4 drives (~22 000 IOPS
read at QD1 on the 2TB). QD1 random read is the number your language server, git and
container layers actually consume - not the 7 000 MB/s on the box.

**The 990 PRO's own history, checked:** the 2022 launch firmware had erroneous SMART
health-calculation logic causing false accelerated "health decline"; firmware 1B2QJXD7
(Feb 2023) stopped it. Drives manufactured since early 2023 ship fixed, so **this is a
non-issue for a new purchase** - check the SMART health value on arrival and then leave it
alone. Later firmwares are messier: 6B2QJXD7 was **withdrawn by Samsung**, and there are
2TB-specific user reports of performance loss after 7B2QJXD7. Posture: run whatever ships,
do not chase firmware updates on this drive.

**Gen5 (9100 PRO, P51)** gives nothing for gaming or development, and the 9100 PRO measures
83-84 C without a heatsink with sustained-write throttling reported - so it wants the
board's M.2 heatsink. Sources disagree on how badly, but there is no upside to buy into.

## Verdict (revised)

> **Capacity superseded 2026-09-10: buy 1TB, not 2TB.** See "Reversed for the three builds"
> and the shortlist at the end of this document. The drive choice below stands; the capacity
> does not.

**Buy the Samsung 990 PRO 2TB at 16 299.**

This reverses my earlier recommendation (KC3000 1TB, "add a second drive later"), for three
reasons that came out of the deep pass:

1. The KC3000 appears to be **end-of-life** and its latency is no longer class-competitive,
   and the NV3 I offered as the budget option has a **variable bill of materials that can
   ship you QLC**. The two cheap options both fell over on inspection.
2. The 990 PRO leads the one benchmark this workload lives on, has a 2GB DRAM cache and a
   5-year warranty, and its one historical defect is fixed in anything you can buy today.
3. "Add capacity later" was reasonable advice in a normal market. In this one - NAND up
   33-38% then 70-75% quarter-on-quarter through 2026, no relief before 2028 - the second
   drive will cost more than the first. Buying 2TB once is the cheaper path.

- **Cheaper: Samsung 990 PRO 1TB at 10 149** (-6 150). Same drive and same qualities, and
  the board's second M.2 slot still exists if you gamble on prices. 1TB fills fast with
  modern games plus container layers.
- **Better but pricier: SK hynix Platinum P41 2TB at 17 560** (+1 261) - the
  best-documented sustained write in Gen4, ahead of the Samsung once the SLC cache is
  exhausted. Take it if the 990 PRO is out of stock; the two are close enough that stock
  should decide.
- **Avoid: Kingston NV3 (both capacities)** - unknowable internals, possible QLC, 3-year
  warranty. **KC3000** - EOL. **SK hynix P41 1TB at 14 249** - a good drive at a bad local
  price, 4 100 above a better 990 PRO 1TB.

**Also**: keep ~15% of any SSD free. A full NVMe drive loses a large fraction of its write
performance - a bigger effect than any model choice above.

**Also**: keep ~15% of any SSD free. A full NVMe drive loses a large fraction of its write
performance, which is a much bigger effect than the model choice above.


## Reversed for the three builds (2026-09-10): 1TB, not 2TB

All three builds in [../../pc_build.md](../../pc_build.md) carry the **990 PRO 1TB**. Telemart's
real prices are **12 399 for 1TB against 18 899 for 2TB**, and that 6 500 is what puts the Max
build under the 130 000 range. The board's second M.2 slot stays free, which makes this the one
capacity decision in the build that is genuinely reversible - unlike RAM, which cannot be staged
on DDR5.

The 2TB argument above is not withdrawn: if NAND keeps climbing, buying 2TB once really is the
cheaper path. But it rests on a **price forecast**, and 6 500 now is certain. Revisit if the
budget moves or NAND pricing turns.


## 512GB SSD + HDD: researched and rejected (2026-09-10)

Dmytro's idea, to cut the price. It does not work, because **HDDs were caught in the same
price crisis as NAND and DRAM** - datacentre demand has pushed 1TB mechanical drives to the
price of 1TB NVMe.

| Option | Telemart |
|---|---:|
| Kingston NV3 **500GB** + WD Blue 1TB HDD | **12 368** |
| Samsung 990 PRO 1TB (the pick) | 12 399 |
| WD Green SN3000 1TB NVMe | 6 999 |

1TB internal HDDs at Telemart on the day: Seagate SkyHawk 6 769, BarraCuda 6 805, WD Blue
6 899. The split therefore costs the same as the single good drive it was meant to undercut,
and the 500GB half of it is the **Kingston NV3 - the drive this doc already rejected** for a
variable bill of materials that can ship QLC.

**It also fails on merit, not only price.** PC Builder's 2026 SSD guide: hard drives "are just
not fast enough for gaming anymore - only for bulk storage of files you don't access very
often". A spinning drive would also undermine the acoustic work behind the case and PSU picks.

**And 512GB is too small, measured.** Dmytro's current C: is 470GB with **270GB used** - of
which `C:\Chel` is 182.7GB and `Users` 98.4GB, while `Games` is **2.3GB** (a 1660 Ti machine
with nothing installed). On the new machine 1440p titles run 100-150GB each, so migrating the
existing 270GB plus three or four games lands at 700-900GB. **1TB is one drive-fill with no
room to spare**; 512GB would start life over half full.

## What four SSD videos changed (2026-09-10)

Read via `code/yt_transcript.py`: Linus Tech Tips "Please Stop Buying the Wrong SSD"
(2026-04), PC Builder "Best SSD for Gaming 2026" (2026-05), Tech Notice "Ultimate SSD Guide"
(2024-12), Tech Guided "How to Choose an SSD" (2024-01, nothing usable).

**Heat-sink SKU: conditional, not a blanket no** (revised after Dmytro asked whether these
rules were verified - the first version of this section overstated it from one source).

- **A Gen 4 drive needs no cooler of its own, provided the board's M.2 slot has a heat cover.**
  Both 2026/2024 sources agree; Tech Notice states the condition explicitly. Case airflow does
  the rest.
- **A Gen 5 drive most likely does need cooling** - "very very important", in Tech Notice's
  words - unless the board has a beefy double-sided heatsink on that slot. They note Gigabyte
  tends to fit double-sided M.2 cooling while ASUS often does so only on the top slot.
- The practical reasons against the heat-sink SKU stand: the drive's own heatsink may not fit
  under the board's, and removing it can void the warranty.

**So: buy the bare Gen 4 drive, and confirm the chosen board actually has an M.2 heat cover.**
That last check is **not done** - ASRock's product page is JavaScript-rendered and could not be
read here, and the board itself is still unsettled (see
[motherboard.md](motherboard.md)). Verify it against whichever board the assembling store
actually supplies.

**Sequential speeds are close to noise for this workload** - two sources plus a mechanism, so
this one holds. Tech Notice's measured PCMark10 runs put every Gen 4 drive within a hair of each
other on sequential read and write, and LTT independently argue real-world behaviour beats spec
sheets. The only chart that separates them is
the **full system drive** test - random small I/O, which is exactly what an OS-plus-tooling
drive does all day. That is the benchmark this doc already chose the 990 PRO on, so the verdict
survives, but the reason is now better stated: **ignore the MB/s on the box.**

**DRAM matters most for precisely this drive.** LTT: the one case where they "strongly
recommend a DRAM cache" is an **operating-system drive**, and the effect grows as the drive
fills - system responsiveness during background work like updates and scans. DRAM-less with
host memory buffer is "perfectly performant, especially as a secondary storage drive". This
build has **one** drive, and it is the OS drive.

**But DRAM is not the whole story.** On Tech Notice's full-system-drive chart the best value
were the **Solidigm P44 Pro and Samsung 990 EVO Plus - "one with DRAM, one without"**. A good
controller without DRAM can match a DRAM drive for this workload. What cannot is a *cheap*
DRAM-less drive: the WD Green SN3000 and Patriot P400 Lite are not 990 EVO Pluses. PC Builder
adds the mechanism - cache affects **write** speed, not game loading or reads - so the DRAM
question is about the small-write half of the workload, which is the dev half.

**Correction to an earlier note in this session:** the WD Black **SN7100 and SN770 are
DRAM-less**; only the SN850X in that line has DRAM. WD's colour tiers carry no consistent
meaning - the same model can have DRAM at 2TB and not at 512GB. Samsung, Kingston and Acer
Predator disclose DRAM on their spec pages; WD, SanDisk, Seagate, MSI, Corsair, Crucial and
Netac have all hidden it. **Verify on TechPowerUp, never from the vendor page.**

**Gen 5: not worth paying a premium for - but that was the wrong reason to drop the Renegade
G5.** Two independent sources agree on the general point (PC Builder: don't pay for Gen 5
unless the deal is absurd; Tech Notice: "for 99% of people Gen 5 drives are a waste of money").
But the same Tech Notice testing measures Gen 5 at **~20% faster on the full-system-drive
random test** - the one chart that matters here - and names a Gen 5 drive the best they have
tested. So Gen 5 is genuinely faster; it is the price premium that usually kills it.

**And the Kingston FURY Renegade G5 at 11 999 was *cheaper* than the 990 PRO at 12 399**, so
the premium argument never applied to it. An earlier version of this section said "Gen 5 buys
nothing here", which was wrong. The honest position: it is a legitimate candidate on price and
speed, and what it needs is the **thermal check** above - Gen 5 drives run much hotter and the
board's M.2 cooling has not been confirmed. Park it there rather than rejecting it.

**Keep 15% of the drive empty** - it slows measurably as it fills. Another reason 1TB is the
floor here rather than a comfort.

**Endurance yardstick:** ~600 TBW per 1TB with a five-year warranty is the industry standard.
Use it to compare drives instead of speed claims.

**Price outlook:** SSD prices are not expected to improve before **early 2027**, and then
perhaps only to ~$100/TB. Buy what is needed now - the same conclusion the RAM reached.

## Shortlist as it now stands (Telemart, in stock, 2026-09-10)

| Drive | Price | DRAM | Verdict |
|---|---:|---|---|
| **Samsung 990 PRO 1TB** | **12 399** | yes | **The pick.** Leads the full-system-drive chart, 5-year warranty, DRAM on the one drive in the machine. |
| **Samsung 990 EVO Plus 1TB** | **10 679** | no (HMB) | **The documented cheaper option, -1 720.** Named best-value on the chart that matters despite having no DRAM. Market floor is ~9 100, so a second store may widen the saving. |
| Kingston KC3000 1TB | 10 779 | yes | 31% off, but end-of-life and its latency is no longer class-competitive. |
| WD Green SN3000 1TB | 6 999 | no | **Lean build only** (-5 400). Cheap DRAM-less on a single OS drive is the wrong cut for a work machine. |
| Patriot P400 Lite / P410 1TB | 7 399 / 7 699 | no | No reason over the SN3000. |
| Kingston NV3 1TB | 7 799 | no | Still rejected - variable BOM. |
| Kingston FURY Renegade G5 1TB | 11 999 | yes | **Unparked 2026-09-11** - see below. Gen 5, DRAM, and the thermal blocker is answered. |

**Decided: one 1TB NVMe, Gen 4, no built-in heatsink.** 990 PRO in the Working and Max builds,
SN3000 in Lean. The 990 EVO Plus at 10 679 is the live alternative if the 1 720 is wanted.

## Closed 2026-09-11: buy the 990 PRO, and the reason changed

Four videos from Dmytro plus a price re-check. **The recommendation is unchanged but its
justification is now the opposite of what it was** - the 990 EVO Plus was the live alternative
because it saved 1 720. At today's prices it does not.

### Correction: the saving did NOT evaporate

An earlier version of this section claimed the gap had collapsed to 225. **That was wrong**, and
wrong by the exact mistake this project corrected once before: it compared **hotline's floor for
one drive against hotline's floor for another**, which are different sellers with different
warranty terms. Dmytro caught it.

**Same shop, both drives, verified 2026-09-11:**

| Drive | eStore | Telemart | Samsung Experience Store | hotline floor |
|---|---:|---:|---:|---:|
| **Samsung 990 PRO 1TB** | **11 899** (reg 12 589), low stock | **12 399**, in stock | - | 10 100 (86 offers) |
| **Samsung 990 EVO Plus 1TB** | **10 399** (reg 10 969), ending | **not stocked** | 12 074, in stock | 9 875 |
| Kingston FURY Renegade G5 1TB | - | 1TB not listed | - | 11 999 (63 offers) |

**The real gap is ~1 500** (11 899 against 10 399 at the same shop), against the 1 720 this
document originally recorded. It narrowed slightly; it did not disappear. Note also that the
**official Samsung store sells the EVO Plus for 12 074 - more than eStore charges for a PRO** -
which is why single-seller floors prove nothing.

So the price argument for the EVO Plus **still stands**, and the decision has to be made on
performance rather than waved through on price. It is below.

### What the 1 500 would actually cost, measured

### What the 225 would actually cost, measured

The DRAM question is no longer abstract. **Sustained write once the SLC cache is exhausted:**

| Drive | Post-cache write |
|---|---|
| Samsung 990 PRO 1TB | **~3 000-4 000 MB/s** |
| Samsung 990 EVO Plus | 1 200-1 777 MB/s (Tom's Hardware, StorageReview) |
| Samsung 990 EVO Plus **1TB, measured** | **~850 MB/s** (proSSD, on the exact 1TB SKU) |

**Three to four times slower on the 1TB model.** The SLC cache is only ~12% of the drive, so a
large container pull or repo checkout reaches that floor. That is what the 1 500 buys.

proSSD adds a defect the written reviews miss: **the SLC cache does not recover predictably.**
After a 15-minute idle pause the drive still benchmarked below its earlier figures - "the results
are not always stable". On a work machine that is a worse property than the raw number.

### Tech Notice's finding still stands, and it is not a contradiction

This document's case for the EVO Plus came from Tech Notice's **full-system-drive benchmark**,
where it beat the 990 PRO by ~2-2.5% and he called it the best system drive Samsung offers. That
is confirmed, not withdrawn. But the **same video's drive-consistency test** - filling the drive
three times, 20TB written over 20 hours - is where he says DRAM-less drives "absolutely fall
apart", and a **990 PRO 1TB beat an EVO Plus at twice the capacity**.

So both are true: the EVO Plus is excellent for OS and application loading, and poor under
sustained writes. **The build's stated workload is containers, heavy repos and git** - the write
half. When the two cost the same, there is nothing to weigh.

### The Renegade G5 is unparked, and it is the real alternative

It was parked on one condition: *"needs the board's M.2 thermal solution confirmed first"*.
**Confirmed** - the ASRock B850 Pro RS WiFi has a **Blazing M.2 (PCIe Gen5 x4) slot with an
extra-large aluminium heatsink** specified for Gen5 drives. The G5 is also among the cooler Gen5
drives by design: a 6nm controller, and it ships without a heatsink because Kingston expects the
board to supply one. Reviews titled "Look, Ma, No Heatsink!" and "Super Fast, Impressively Cool"
back that.

At **11 999 against the PRO's 10 100 floor it is now +1 899**, not cheaper as this document
previously recorded - it was compared against Telemart's 12 399. Tech Notice measured Gen 5 at
**~20% faster on the full-system-drive random test**, so the money buys something real.

**Caveat if it is chosen:** it needs the board's Gen5 M.2 slot, which is the one nearest the CPU
and on some boards shares lanes with the GPU slot. Confirm against the final board - that is the
motherboard question, not this one.

### Verdict - tiered, 2026-09-11

| Build | Drive | UAH | Why this tier gets it |
|---|---|---:|---|
| **Lean** | WD Green SN3000 1TB | **6 999** | Cheapest acceptable. DRAM-less with a weak controller - the compromise Lean is allowed to make, and the same logic as its 16GB RAM and budget panel |
| **Working** | **Samsung 990 EVO Plus 1TB** | **10 399** | The value pick. HMB rather than DRAM, but it **matches or beats the 990 PRO on Tech Notice's full-system-drive test** - the metric this workload lives on - for 2 000 less |
| **Max** | **Kingston FURY Renegade G5 1TB** | **11 999** | Gen 5, DRAM, and **cheaper than the 990 PRO at the same shop**. Measurably the fastest of the three on the real-world system-drive test |

### Kingston Renegade G5: dropped, then verified and reinstated (2026-09-11)

It was dropped an hour earlier for good reasons - a category-level speed claim, an unverified
hotline floor, thermals cleared only from a spec sheet. Dmytro asked for it to be checked
properly. **Every objection cleared:**

| Objection | Finding |
|---|---|
| Price was an unverified hotline floor | **Telemart sells it at 11 999**, 47% off 22 449 - the store the rest of the basket comes from, and **400 cheaper than the 990 PRO there** |
| "Gen 5 ~20% faster" was a category claim | **Measured, like-for-like on PCMark 10 Storage:** 990 PRO **4 651 / 743 MB/s**; Renegade G5 **8 062 / 1 178 MB/s** (StorageReview). The category claim *understated* it |
| Thermals cleared only from the board spec | StorageReview: **no thermal throttling**, the 6nm SM2508 controller "eliminating the need for aggressive heat spreaders". The ASRock board's Gen5 M.2 heatsink is belt and braces |
| Might have a built-in heatsink, which this doc rules out | **SFYR2S/1T0 ships without one** - correct SKU. (hotline's listing claims otherwise and is wrong; the with-heatsink part is a different, older model, SFYRSK/1000G) |

**Honest caveat:** StorageReview tested the **2TB**. The 1TB has fewer NAND dies and is rated
lower by Kingston itself - 14 200/11 000 MB/s against the 2TB's 14 800/14 000 - so its real score
will land below 8 062. Even discounted heavily it stays clear of the 990 PRO's 4 651. The
direction is not in doubt; the exact margin is.

**Which makes the 990 PRO the drive with no build.** It is not the cheapest, not the fastest, and
at Telemart it costs 400 more than a Gen 5 drive that beats it. That is the same position the
9070 XT ended up in - a part that was the right answer until the prices moved.

**Prices are same-shop verified where it matters:** eStore lists the 990 PRO at 11 899 and the
EVO Plus at 10 399; Telemart has the PRO at 12 399 and **does not stock the EVO Plus**. So the
Working build's drive comes from a second shop - a purchase-time problem for the quoting stage,
not a reason to change the pick.

### Earlier verdict, superseded

### Verdict

**Buy the Samsung 990 PRO 1TB** - in stock at Telemart at 12 399, 11 899 at eStore, 86 offers
nationally. **On performance, not on price:** the ~1 500 saving on the EVO Plus is real, and the
case against taking it is that it costs **3-4x sustained write speed** on the write half of this
machine's workload, plus an SLC cache that does not recover predictably. **Telemart does not
stock the EVO Plus at all**, so on the single-store basket the question does not arise.

- **Cheaper: Samsung 990 EVO Plus 1TB, 10 399 at eStore (-1 500).** Still a defensible buy for
  someone whose load is OS and application reads - it beats the PRO on Tech Notice's
  full-system-drive test. **Not for this machine**, whose stated workload is containers and heavy
  repos. Take it only if the 1 500 matters more than sustained write, and accept splitting the
  order across two shops.
- **Better but pricier: Kingston FURY Renegade G5 1TB at 11 999** (+1 899 over the PRO's floor) -
  Gen 5, DRAM, ~20% faster on the test that matters, thermally cleared by the board's Gen5
  heatsink. The genuine upgrade if the money is there.
- **Lean build: WD Green SN3000 at 6 999** unchanged.


### Sourcing of the rules above

Dmytro asked, correctly, which of these were verified and which came from a single video.

| Claim | Sources |
|---|---|
| Sequential MB/s barely matters; the full-system-drive random test is the metric | Tech Notice (measured charts) + LTT (principle). **Two.** |
| Gen 5 not worth a price premium | PC Builder + Tech Notice. **Two** - but both also concede Gen 5 is faster, so this is about price, not capability. |
| DRAM matters most on an OS drive, and more as it fills | LTT. **One**, though PC Builder's "cache affects writes, not reads" supplies the mechanism and Tech Notice's chart shows a good HMB drive can match a DRAM one. |
| Gen 4 needs no drive-mounted heatsink if the board has a heat cover | PC Builder + Tech Notice. **Two.** |
| Gen 5 drives need active thought about cooling | Tech Notice. **One.** |
| Keep 15% free; ~600 TBW per TB; no price relief before 2027 | PC Builder (15%, outlook), Tech Notice (TBW). **One each** - industry-standard figures rather than test results. |
