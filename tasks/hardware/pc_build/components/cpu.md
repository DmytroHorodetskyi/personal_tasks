# CPU

## What the CPU does for this machine

Two different jobs, and they reward different things.

**Development (the dominant load).** An IDE with language servers, Claude Code running tools
over a heavy repo, git operations, containers, test runs. Most of this is *bursty and
partly single-threaded*: an LSP re-index, a `git status` on a large tree, a TypeScript
type-check, a package install. The thing you feel here is **single-thread speed and memory
latency**, not core count. Core count only starts to matter when you routinely run something
embarrassingly parallel - a full C++/Rust build, a video render, several VMs at once. You
said that is not your case.

**Gaming at 1440p.** Here the CPU sets the *floor* of your frame rate - the 1% lows, the
stutter when a strategy game simulates 3000 units or an MMO loads a city. Raw averages at
1440p are mostly decided by the GPU. This is exactly what 3D V-Cache addresses.

## The characteristics that matter, and how to read them

Ordered by how much each one decides the purchase. The first two rows are the entire
9700X-vs-9800X3D question; the rest are checks, not choices.

| # | Spec (unit) | What it means, plainly | What it is here |
|---|---|---|---|
| 1 | **Boost clock (GHz)** | How fast a single core runs when only one or two are busy - which is most of what you do. IDE responsiveness, git, browser, game logic. | 9700X **5.5**, 9800X3D **5.2**, 9850X3D **5.6**. A 6% spread. Read boost, not base. |
| 2 | **L3 cache (MB)** | Fast memory on the chip itself. A core waiting on system RAM is spinning at full speed doing nothing; cache is what stops it waiting. Games wait constantly - their memory access is scattered - so cache decides **1% lows**, the stutter you feel. Compilers wait far less. | 32MB normally; the X3D parts stack an extra 64MB for **96MB**. This is the one real difference on AM5. |
| 3 | **Cores / threads** | Independent instruction streams. 8c/16t = 8 physical cores each running 2 threads (SMT). Only matters for work that is genuinely parallel - full builds, renders, several VMs. | **8 cores** is the knee of the curve for dev plus games. 6 is workable; 16 is idle silicon unless you render. |
| 4 | **TDP and PPT (watts)** | TDP is a *cooling-design* figure, not power draw. **PPT is the real ceiling.** Both decide cooler cost and how loud the machine gets. | 9700X 65W (88W PPT) - a 1 500 cooler suffices. 9800X3D 120W (**162W PPT**) - budget 2 845. |
| 5 | **Socket and platform life** | Whether a faster CPU drops in later without replacing board and RAM too. | **AM5, supported through 2029**; Zen 6 is assigned to it. Board BIOS support is per-vendor, so treat it as plausible, not promised - see [motherboard.md](motherboard.md). Intel's LGA1851 has no runway. |
| 6 | **Base clock (GHz)** | The guaranteed floor with every core loaded. Deliberately low on this list because you almost never sit at it. | 9700X 3.8, 9800X3D 4.7. The X3D's higher base is why it wins long compiles despite the lower boost. |
| 7 | **Integrated graphics** | A small GPU on the CPU die. | Every non-F Ryzen 9000 has 2 RDNA 2 CUs. Lets the machine boot and be diagnosed with the graphics card pulled. Worth having; Intel's "F" parts lack it. |
| 8 | **Memory support** | The controller runs in step with the RAM (1:1) up to ~6000 MT/s, then drops to a slower ratio. | Fixes the RAM target at **DDR5-6000** - see [ram.md](ram.md). |

**Ignore:** aggregate "CPU scores" from UserBenchmark or PassMark, IPC claims with no benchmark
attached, and any comparison of GHz between AMD and Intel - the number means something
different on each.

## Specifications

The numbers off the box, for the parts actually in contention. **Boost GHz is the one to
read** - it is what the chip runs at when one or two cores are busy, which is most of what
you do. Base GHz is only the guaranteed floor under an all-core load.

| Model | Base GHz | **Boost GHz** | Cores / threads | L2 | **L3 cache** | TDP (PPT) | Socket |
|---|---:|---:|---|---:|---:|---:|---|
| Ryzen 5 **7500F** | 3.7 | 5.0 | 6 / 12 | 6MB | 32MB | 65W (88W) | AM5 |
| Ryzen 7 **7700X** | 4.5 | 5.4 | 8 / 16 | 8MB | 32MB | **105W (142W)** | AM5 |
| Ryzen 5 9600X | 3.9 | 5.4 | 6 / 12 | 6MB | 32MB | 65W (88W) | AM5 |
| Ryzen 5 7600X3D | 4.1 | 4.7 | 6 / 12 | 6MB | 96MB | 65W (88W) | AM5 |
| **Ryzen 7 9700X** | 3.8 | **5.5** | 8 / 16 | 8MB | 32MB | 65W (88W) | AM5 |
| Ryzen 7 7800X3D | 4.2 | 5.0 | 8 / 16 | 8MB | 96MB | 120W (162W) | AM5 |
| **Ryzen 7 9800X3D** | 4.7 | **5.2** | 8 / 16 | 8MB | **96MB** | 120W (162W) | AM5 |
| Ryzen 7 9850X3D | 4.7 | **5.6** | 8 / 16 | 8MB | 96MB | 120W (162W) | AM5 |
| Ryzen 9 9900X3D | 4.4 | 5.5 | 12 / 24 | 12MB | 128MB | 120W (162W) | AM5 |
| Ryzen 9 9950X | 4.3 | 5.7 | 16 / 32 | 16MB | 64MB | 170W (230W) | AM5 |
| Ryzen 9 9950X3D | 4.3 | 5.7 | 16 / 32 | 16MB | 128MB | 170W (230W) | AM5 |
| Intel Core Ultra 7 265KF | 3.9 P / 3.3 E | 5.5 P / 4.6 E | 20 / 20 (8P+12E) | 36MB | 30MB | 125W (250W) | LGA1851 |
| Intel Core Ultra 9 285K | 3.7 P / 3.2 E | 5.7 P / 4.6 E | 24 / 24 (8P+16E) | 40MB | 36MB | 125W (250W) | LGA1851 |

Common to every Ryzen 9000 part above: **TSMC 4nm Zen 5**, PCIe 5.0, dual-channel DDR5 with
**DDR5-5600 official / 6000 the practical 1:1 limit**, a 2-CU RDNA 2 iGPU (enough to drive a
monitor and diagnose the machine with the GPU pulled), and no bundled cooler on X and X3D
parts. AM5 uses an **LGA socket - the pins are in the board, not on the chip.**

The two **Zen 4** parts differ on three rows that matter here: TSMC 5nm and a generation-older core, and the **7500F has no iGPU at all** - so with the graphics card pulled it gives you no display and no way to diagnose the machine. The 7700X keeps the iGPU but is a **105W part**, which is a cooler decision, not just a CPU one.

### The 9700X vs 9800X3D trade in four numbers

| | 9700X | 9800X3D | Difference |
|---|---:|---:|---|
| Boost clock | 5.5 GHz | 5.2 GHz | **-0.3 GHz (-5%)** for the X3D |
| L3 cache | 32MB | 96MB | **3x** for the X3D |
| TDP | 65W | 120W | nearly **2x** the heat |
| Price (real, mid-market BOX) | ~13 500 | ~22 000 | **+8 500** |

That is the whole decision. Why the slower chip wins in games: a core waiting on system RAM
is spinning at full speed doing nothing, and games wait constantly because their memory
access is scattered. The extra 64MB of stacked cache removes most of that waiting, which is
worth far more than 5% more clock. Code that *doesn't* wait much - git, single-threaded
tooling - just pays the 5% and gets nothing back. Both effects are small in absolute terms;
neither part is twice the other at anything.

## Options

Prices: lowest hotline.ua offer, 2026-09-09, UAH; the two Zen 4 rows were checked 2026-09-10. **These are understated - see the store
prices below before using any of them.**

| Model | UAH | **Boost GHz** | Cores | Cache | TDP | Verdict for your mix |
|---|---:|---:|---|---|---|---|
| **Ryzen 5 7500F (tray)** | **5 825** | 5.0 | 6c/12t | 32MB | 65W | **The cheapest way onto AM5** - 1 745 under the 9600X, and 64 shops carry it. Zen 4, tray-only warranty, no iGPU. A sub-floor option: see below. |
| Ryzen 7 7700X | 9 500 | 5.4 | 8c/16t | 32MB | **105W** | Eight Zen 4 cores for 1 690 under a 9700X tray - but 105W moves the cooler from the AK400 to the Phantom Spirit (+1 330), so the real saving is ~360. No. |
| Ryzen 5 9600X (tray) | 7 570 | 5.4 | 6c/12t | 32MB | 65W | Saves 3 600 over the 9700X and costs you headroom in exactly the place a dev machine feels it - parallel tooling. No. |
| Ryzen 5 7600X3D | 12 399 | 4.7 | 6c/12t | 96MB | 65W | Cheap way to X3D gaming, but 6 cores and the older Zen 4 core. No, for a work-first machine. |
| **Ryzen 7 9700X (tray / box)** | **11 190 / 12 599** *(hotline floors — the build sheet carries **13 936** BOX at Rozetka; see the note below)* | **5.5** | 8c/16t | 32MB | 65W | **The value pick.** Cool, quiet, cheap to cool, 8 cores for tooling. Gives up 1% lows in CPU-heavy games. |
| Ryzen 7 7800X3D (tray) | 14 087 | 5.0 | 8c/16t | 96MB | 120W | Still a great gaming chip, but Zen 4 and only 5 000 below the strictly better 9800X3D. No. |
| **Ryzen 7 9800X3D (tray / box)** | **19 230 / 19 781** | **5.2** | 8c/16t | 96MB | 120W | **The justified upgrade.** Best gaming CPU of the generation, and *also ~6% faster than the 9700X in productivity*, so it is not a gaming-only tax. |
| Ryzen 7 9850X3D | 21 950 | **5.6** | 8c/16t | 96MB | 120W | 2026 refresh, small clock bump for +2 700. Skip. |
| Ryzen 9 9900X3D | 22 999 | 5.5 | 12c/24t | 128MB | 120W | Cache is on one CCD only, so game scheduling is fussier than the 9800X3D. Skip. |
| Ryzen 9 9950X | 22 099 | 5.7 | 16c/32t | 64MB | 170W | For render/compile farms. You said the work is lighter than that. No. |
| Ryzen 9 9950X3D | 28 199 | 5.7 | 16c/32t | 128MB | 170W | Does both jobs at the top, matches 9800X3D in games. Only if the work grows into 16 cores. |
| Intel Core Ultra 5 245K / 245KF | ~9 500 | 5.2 | 14c (6P+8E) | 24MB | 125W | **Cheapest 14-core here.** Loses to the 9700X in games and has no upgrade path. No. |
| Intel Core Ultra 7 265K / 265KF | ~15 000 | 5.5 | 20c (8P+12E) | 30MB | 125W | **~80% more multi-core than a 9700X**, and **18% slower in games across 100+ titles**. Buys the thing you said you don't need, at the cost of the thing you said you want. No. |
| Intel Core Ultra 9 285K | ~21 000 | 5.7 | 24c (8P+16E) | 36MB | 125W | Measured ~24-35% behind the 9800X3D in gaming across test suites. No. |

**Price provenance, added 2026-09-13 by the source audit.** Dmytro sent
[click.ua's AM5 list](https://click.ua/configurator/catalog/protsessoryi/14=am5) asking *"Ryzen 7
9700X Tray - is it bad? the tray? dont see BOX on click, can you check yourself?"* **He was right
on both counts.** Of the 24 AM5 SKUs that page lists, BOX versions exist for the 7700X, 9900X,
7900X, 9800X3D, 7600X, 7400, 7800X3D, 9950X3D and 7600 — **but not for the 9700X**, which is tray
only there at **12 892 ₴, in stock**.

**It is above the 12 599 in the table above, and that is the expected direction.** *(An earlier
version of this note said the table's provenance was unrecorded. That was wrong — the header two
lines above the table states it: lowest hotline.ua offer, 2026-09-09. Corrected.)* Those are
**hotline floors, not offers**, so the real figures run higher: [price_check.md](../price_check.md)
found the 9700X BOX at **13 936 Rozetka / 14 499 Telemart / 15 099** elsewhere, and **13 936 is
what the build sheet carries**. click.ua's **12 892 tray** sits between the floor and the shelf,
which is what a tray SKU should do.

**The part that was never answered: it is tray-only there.** Nine other AM5 chips on that page
have a BOX SKU and the 9700X does not, so "buy the BOX, never tray" — the rule in
[../pc_build.md](../pc_build.md) — cannot be followed at click.ua at all. Buy it where a BOX SKU
exists, or accept tray warranty terms knowingly.

**Settled 2026-09-13: tray accepted.** Dmytro buys at click.ua and answered *"tray - idk, let it
be"*. So Working and Max take the **9700X tray at 12 892**, knowingly on the shop's warranty
rather than AMD's 36 months. **Lean takes the 7500F Multipack at 7 085 instead of its tray at
6 938** - 147 more, and it bundles the Wraith Stealth that [cooling.md](cooling.md) already
specified for that build, so it is 1 552 cheaper than tray plus an AK400.

## Real shop prices (checked 2026-09-09)

The hotline figures in the options table are the aggregator's **lowest** offer, which is
usually a one-person shop. Checked against ek.ua's per-shop listings and the two assembly
candidates, they are understated by **10-25%**. Ranges below are across all listed Ukrainian
shops; "mid-market" is where the established retailers actually cluster.

| Model | Doc said | Real range | **Mid-market** | Telemart | Brain |
|---|---:|---|---:|---:|---:|
| Ryzen 5 9600X BOX | 7 570 (tray) | 7 999 - 20 276 | **~9 800** | ~9 800 | - |
| Ryzen 7 7800X3D BOX | 14 087 (tray) | 15 029 - 26 324 | **~17 000** | - | - |
| **Ryzen 7 9700X BOX** | 11 190 / 12 599 | 12 599 - 21 946 | **~13 500** | 14 499 | **18 080** |
| **Ryzen 7 9800X3D tray** | 19 230 | - | **~21 500** | **21 499** | - |
| **Ryzen 7 9800X3D BOX** | 19 781 | 20 279 - 30 851 | **~22 000** | 23 799 | blocked |
| Ryzen 7 9850X3D OEM | 21 950 | 23 270 - 34 364 | **~24 000** | 23 999 | - |
| Ryzen 7 9850X3D BOX | - | 24 048 - 32 544 | **~25 000** | - | - |

Three things fall out of this:

1. **The 9700X -> 9800X3D premium is bigger than the docs said.** Comparing like with like at
   mid-market BOX prices: ~13 500 -> ~22 000 = **+8 500**, and at Telemart specifically
   14 499 -> 23 799 = **+9 300**. The doc's +8 040 was the floor-price version of the same
   gap. The ranking does not change; the size of the bet does, by ~10%.
2. **Brain is expensive on CPUs.** Its 9700X is **18 080** against Telemart's 14 499 - a 25%
   premium on one part. Since the plan is to buy and have one store assemble, that difference
   compounds across the whole build. Brain's 36-month assembly warranty may still justify it,
   but it has to be priced as a whole basket, not part by part.
3. **The tray/BOX gap is real money now, not 551 UAH.** Telemart: tray 21 499 vs BOX 23 799 =
   **2 300**. That changes the earlier "just take the BOX" advice into a genuine judgement
   call - the BOX buys AMD's own 3-year warranty rather than the shop's terms.

The absolute floors in the range column (Justbuy, Luckylink, Openshop) are real listings but
are single-shop offers with no service department, which is precisely what the assembly
constraint rules out.

## Evidence (updated after the deep review pass, 2026-09-09)

- Tom's Hardware places the 9800X3D at the top of the gaming hierarchy, above every Core
  Ultra part, at roughly **24-35% ahead of the Core Ultra 9 285K** depending on suite.
- Against the 9700X: at 1440p **the gap narrows sharply** (you become GPU-bound), while the
  9800X3D still holds higher minimum frame rates. In productivity it is about **6-8% faster**
  in multi-threaded work, not slower. The 9700X's counter-argument is power: **65W vs 120W**.
### Does 3D V-Cache help *your* work? Now measured properly - and mostly no

This is the claim I have had to walk back twice, so here is the actual data. Phoronix ran
these on Linux with a **9700X at a 105W cTDP** as a control, which isolates cache from the
power/clock advantage (the 9800X3D is a 120W part, the stock 9700X a 65W one). Times in
seconds, lower is better:

| Compile benchmark | 9700X stock | 9700X @105W | 9800X3D | 9950X | X3D vs 9700X @105W |
|---|---:|---:|---:|---:|---:|
| Linux kernel defconfig | 87.9 | 80.3 | 75.9 | **47.3** | +5.7% |
| Linux kernel allmodconfig | 1178 | 1065 | 999 | **586** | +6.6% |
| LLVM (Ninja) | 566 | 535 | 485 | **300** | +10.4% |
| Godot | 300 | 279 | 254 | **162** | +9.8% |
| PHP | 47.9 | 45.7 | 43.3 | **34.6** | +5.7% |

What that says:

- **Most of the apparent compile advantage is power, not cache.** Against a stock 65W 9700X
  the X3D looks 10-18% faster; at equal power it is only **6-10%** faster.
- **The 9950X is 58-65% faster than the 9800X3D on every compile.** If build times were your
  bottleneck, cores - not cache - would be the purchase. You told me they are not.
- **Single-threaded work is 4-6% *slower* on the X3D** (a 300 MHz boost deficit plus 4 extra
  cycles of L3 latency). It shows up in real places: the CPython PGO+LTO build is **1.5%
  slower** than on a 9700X, and Chrome Octane 3.7% slower.
- **Git is 4.5% slower on the 9800X3D than on the 9700X** (Phoronix's "common git commands"
  test: 32.8s vs 31.4s). Git is latency-bound and serial - it pays the clock penalty and gets
  nothing back from the cache. You specifically mentioned heavy repos, so this matters.
- The first-generation 7800X3D gave **zero** compile benefit over a 7700X - slightly slower
  on kernel builds - so this is not "X3D helps development"; it is gen-2 clawing back its own
  clock deficit.

**The one dev scenario that flips it completely: local databases.** Gen-2 V-Cache is
transformative there - **pgbench read-only +116%**, ClickHouse +22-25%, CockroachDB +17%,
nginx +32%, Apache +26%, Memcached +15% versus the 9700X. If your containers run a local
Postgres or ClickHouse that you actually hammer, the premium pays for itself on work grounds
alone. If they run a web app and a queue, it does not.

**Conclusion: for your described workload the X3D premium is a gaming purchase.** That is a
legitimate thing to buy - you asked for high-FPS gaming - but I should not have dressed it up
as a productivity upgrade, and the earlier "~30% faster at shader compilation" line came from
a weak secondary source that this data supersedes.
- **9850X3D - and this one got more interesting.** The change is a **400 MHz boost bump**
  (5.2 -> 5.6 GHz) from better binning; cores and cache are identical. Gaming gain 4-7%,
  compiles +2-3.5% over the 9800X3D. Tom's Hardware, judging it as a gaming chip, says "an
  extra $30 buys you very little". But Phoronix's data shows something the gaming reviews
  miss: **it is the first X3D with no single-thread penalty at all** - fastest of the group on
  Speedometer 3.1 and Node.js web tooling, ahead of the 9700X. Since the ST deficit is
  precisely the X3D's cost for your workload, the 9850X3D is the one that removes it.
  Locally: **+2 720 (14%) over the 9800X3D**. Reasonable if you want X3D gaming without
  giving up any interactive responsiveness; skippable otherwise. Note it also has one
  credible failure report of its own (see below).
- **Platform, with the caveat I owed you**: AMD stated at Computex that **AM5 is supported
  through 2029**, and Zen 6 desktop ("Olympic Ridge") is assigned to AM5 in AMD's own
  technical documentation. But **board-level support is not automatic** - it depends on each
  vendor shipping a BIOS, no vendor has committed to Zen 6 on B650, and BIOS flash capacity
  is already a constraint. Treat the upgrade path as plausible, not guaranteed. Details in
  [motherboard.md](motherboard.md).

## Reliability: this affects which board you pair it with

The 9800X3D has a documented failure cluster - roughly 108-157 reported cases, of which
**~82% occurred on ASRock motherboards**, plus a second wave on ASUS 800-series boards in
January 2026. The cause is still disputed and unresolved as of April 2026, when failures
were still being reported on ASRock's newest BIOS.

This does **not** change the CPU choice - the rate is tiny against the hundreds of thousands
sold, and the 9700X/9600X show no pattern at all. It changes the **board** choice, which is
why [motherboard.md](motherboard.md) now recommends MSI rather than the ASRock board I
originally listed. Practical rules: flash the board to the current BIOS before first real
use, leave PBO alone, and handle the AM5 socket carefully - bent pins are the one failure
mode unambiguously proven to destroy both CPU and board.

## Why the Intel side of this list is short (and what was wrong with my reasons)

Challenged on 2026-09-09: Tom's Hardware's CPU hierarchy carries far more Intel parts than
this doc did, so the short list needed justifying rather than assuming. Checked properly,
**two of my three original reasons were false.**

| My claim | Verdict |
|---|---|
| "The board costs 5-10k more" | **Wrong.** B860 boards start at **~8 200-8 700** (MSI B860M GAMING PLUS WIFI 8 179, MSI B860 GAMING PLUS WIFI 8 399, ASUS PRIME B860M-A WIFI 8 599). That is **the same as or cheaper than** the B850 boards in [motherboard.md](motherboard.md). The platform-cost argument does not exist. |
| "More multicore per hryvnia" (said dismissively) | **True, and understated.** The Core Ultra 7 265K at ~15 000 scores roughly **80% higher in multi-core** than a 9700X at ~13 500 - it is 20 cores against 8. Per hryvnia of throughput, Intel wins this tier outright. |
| "Dead-end socket" | **True, and now confirmed rather than predicted.** Intel has associated Nova Lake-S with the **new LGA1954 socket**; LGA1851 gets Arrow Lake and its refresh only. AM5 is supported through 2029. |

So Intel is **neither expensive nor bad** here. The list is short for one reason only:

**Gaming.** The Ryzen 7 9700X is **~18% faster than the Core Ultra 7 265K averaged over 100+
games**, and the 9800X3D is **24-35% ahead of the Core Ultra 9 285K**. Intel also draws
**~25% more power** for that result.

That maps onto the brief exactly the wrong way round. The requirements say **high-FPS 1440p
gaming is wanted** and **16 cores are not needed** - so Intel's single advantage is aimed at
the thing explicitly ruled out, while its single disadvantage lands on a stated requirement.

**When the Intel answer would flip:** if the work grew into sustained all-core throughput -
video encoding, large parallel builds, several VMs at once - the 265K at ~15 000 plus a
~8 500 B860 board would be the better machine, and cheaper than a 9950X. That is a different
brief, not this one. The 245K at ~9 500 is also genuinely the cheapest route to 14 cores if
gaming is dropped entirely.

Two Intel parts are **not** listed on purpose: 14th-gen Raptor Lake (14600K/14700K) carries
the Vmin-degradation history and an older, fully dead platform, and the non-K Core Ultra
parts cannot be paired with the cheap overclocking-capable boards that make the Intel value
case work in the first place.

## DECISION (2026-09-09): one CPU per tier, not one CPU

> **Superseded 2026-09-10 by the three builds in [../../pc_build.md](../../pc_build.md).** The
> Ceiling/Probable/Floor table below tiered on the GPU alone and its prices are hotline floors.
> Current assignment: **7500F MPK to Lean, 9700X BOX to Working and Max**; the 9600X is in no
> build. The reasoning below is kept because the per-tier method and the three rejected drafts
> are still worth having.

Corrected after Dmytro pointed out that this is a **three-tier exercise**, not a single
build: the maximum his range allows, the most probable build, and the weakest one that still
meets the requirements. An earlier version of this section named the 9700X flatly and threw
the other two tiers away. **The other options are not dropped - they are assigned.**

| Tier | CPU | GPU | CPU + GPU | Build total |
|---|---|---|---:|---:|
| **Ceiling** - max the range allows | **Ryzen 7 9700X** ~13 500 | RX 9070 **XT** ~46 500 | **~60 000** | ~125 000 |
| **Probable** - the working plan | **Ryzen 7 9700X** ~13 500 | RX **9070** ~38 500 | **~52 000** | ~117 000 |
| **Floor** - weakest still acceptable | **Ryzen 5 9600X** ~9 800 | RX 9070 **GRE** ~33 000 | **~42 800** | ~108 000 |

### The floor alternative and the rejected one: the two Zen 4 parts (added 2026-09-10)

Added at Dmytro's instruction after reading ScatterVolt's 1440p+ tier, which builds on exactly
these two chips - [../scattervolt_2026.md](../scattervolt_2026.md). Neither was priced in the
first pass; both are now (hotline floor, 2026-09-10, so understated 10-15% like every other
figure here).

| | 7500F | 9600X (the floor) | 7700X | 9700X (probable/ceiling) |
|---|---:|---:|---:|---:|
| Price | **5 825** tray | 7 570 tray | **9 500** | 11 190 tray / 12 599 box |
| Cores | 6c/12t | 6c/12t | 8c/16t | 8c/16t |
| Core | Zen 4 | Zen 5 | Zen 4 | Zen 5 |
| TDP | 65W | 65W | **105W** | 65W |
| Cooler it needs | AK400 1 515 | AK400 1 515 | **Phantom Spirit 2 845** | AK400 1 515 |
| iGPU | **none** | 2-CU RDNA 2 | 2-CU RDNA 2 | 2-CU RDNA 2 |

**The 7700X is not a saving.** It undercuts a 9700X tray by 1 690, then hands 1 330 of it
straight back in cooler ([cooling.md](cooling.md) picks the AK400 *because* the chip is 65W).
What is left is ~360 for a generation-older core in a hotter, louder machine, on the socket
whose upgrade runway is the reason for buying AM5 at all. Rejected.

**The 7500F is accepted as the floor alternative (Dmytro, 2026-09-10).** Same 6c/12t, same
65W, same cooler, and the cheapest entry onto AM5 that exists. Buy the **MPK** SKU at 6 589,
not the tray at 5 825 - see the SKU note below. Against a 9600X BOX at 7 930 that is
**-1 341**, and the MPK bundles a Wraith Stealth, so a further 1 515 is available by dropping
the AK400 if noise stops mattering.

Two costs stay attached to it, and neither is a warranty problem once the MPK SKU is bought:

- **No iGPU.** Every other chip here can drive a monitor with the graphics card pulled. On a
  first build, and during any GPU RMA, that is the difference between diagnosing the machine
  and guessing. This is the main reason it is the alternative and not the assigned floor.
- **Zen 4.** A generation-older core on the socket whose upgrade runway is a stated reason for
  choosing AM5.

### Tray vs BOX vs MPK - buy retail at every tier

**tray** is the bare chip in a builder's tray: no box, no cooler, and **no AMD warranty** - only
the shop's, typically 12 months against AMD's 36. **BOX** is retail sealed (the "WOF" part
numbers are box-without-cooler). **MPK** is AMD's multipack retail, split by retailers, and on
the 7500F it includes a Wraith Stealth cooler.

| CPU | tray | retail | Gap | Shops carrying retail |
|---|---:|---:|---:|---|
| 7500F | 5 825 | **6 589** (MPK) | +764 | **13**, vs 64 on tray |
| 9600X | 7 570 | **7 930** (BOX) | +360 | 71 |
| 9700X | 11 190 | **12 599** (box) | +1 409 | - |

**Buy retail at every tier.** The gap is 360-1 409 on a ~120 000 machine, the build is being
assembled by one store rather than by Dmytro, so a retail SKU keeps any RMA the shop's
responsibility instead of an argument, and tray would mean relaxing the official-warranty
requirement set at the start. Every price in this document remains a **tray** figure unless
marked otherwise - add the gap above before totalling.

**Two things for the written store quotes** (the next step with Brain and Telemart): whether
they stock the **7500F MPK** at all, given one store has to supply the whole build, and **what
warranty term they actually give on an MPK part** - it is a multipack SKU and handling varies
by retailer.

Settled 2026-09-09 after three wrong drafts. What was wrong with them, so it is not repeated:

- **The first put the 9800X3D at the ceiling.** 22 000 + a 9070 XT is ~68 500, which with a
  ~65 000 rest-of-build is a **~133 000 machine** - outside the stated range entirely. The
  X3D is not the ceiling of this budget; it is above it.
- **The second used the RX 9060 XT as the floor card.** It is dominated by the **RX 9070 GRE
  at +3 000 for +30% performance** (77.2 vs 59.2). The GRE had been excluded on a 12GB VRAM
  rule that was my criterion, not a requirement Dmytro set - the same rule that wrongly
  marked the RTX 5070 as rejected. The 9060 XT has no reason to exist next to the GRE.
- **The third put a 7800X3D at the ceiling to make the tiers look different.** At 1440p that
  3 500 buys more as GPU than as cache. Cosmetic variety is not a build argument.

### The rules the ladder follows

1. **Money goes to the GPU first.** At 1440p the graphics card sets the frame rate; the CPU
   only sets the floor under it. Every tier spends its marginal hryvnia on the card.
2. **The CPU is identical at the top two tiers, deliberately.** 13 500 buys the correct chip
   at both budgets. It drops to a 9600X only at the floor, where saving 3 700 is the entire
   point of the tier.
3. **The rest of the build is ~65 000 lean / ~75 000 mid** at realistic prices - of which
   **~25 000 is 32GB of RAM**, a fifth of the machine, buying no performance. That is the
   2026 memory crisis, and it is what caps CPU+GPU at ~60 000 rather than ~70 000.

**Consequence worth carrying forward: no tier contains a 9800X3D.** The 9800X3D failure
cluster (~82% on ASRock boards) was the main argument for the MSI motherboard pick. That
argument no longer applies to any tier - see [motherboard.md](motherboard.md).

This is why the floor tier keeps a 9700X: **9 800 for a 9600X is not a saving worth making
on a work-first machine**, while ~8 500 off the GPU is.

### Why the 9700X specifically

- **8 cores at 5.5 GHz** - the highest boost clock of any realistic option here, and boost is
  what IDE responsiveness, git and single-threaded tooling actually run on.
- **65W (88W PPT)**, so a 1 515 cooler is sufficient instead of a 2 845 one - the saving is
  really ~9 700, not 8 500.
- **No failure pattern.** The 9800X3D has a documented cluster (~108-157 cases, ~82% on
  ASRock boards); the 9700X has none. This also relaxes the board choice - see below.
- Phoronix data: the X3D is **4-6% slower single-threaded** and **4.5% slower on git**, which
  is the workload Dmytro named. The CPU being given up is not better at his work.

### What would move a tier

| Trigger | New answer |
|---|---|
| **The probable tier moves up to an RX 9070 XT** | It becomes the ceiling build: 9800X3D at ~22 000 is then defensible - the card is fast enough for the CPU to matter |
| Wanting X3D cache cheaply | **7800X3D at ~17 000** - only +3 500 over the 9700X instead of +8 500. Costs 0.5 GHz of boost, Zen 4, and any upgrade path on the socket |
| Work grows into sustained all-core throughput | Intel **Core Ultra 7 265K at ~15 000** plus a ~8 500 B860 board - beats a 9950X and costs less. A different brief |

### Knock-on effects of choosing the 9700X

1. **Cooler drops to the Deepcool AK400 (1 515)** instead of the Phantom Spirit 120 SE
   (2 845). 65W does not need a dual-tower. See [cooling.md](cooling.md).
2. **The motherboard constraint loosens.** The MSI Tomahawk pick in
   [motherboard.md](motherboard.md) was driven mainly by the 9800X3D failure cluster being
   ~82% ASRock. With a 9700X that argument evaporates, which reopens the **ASRock B850 Pro RS
   at 6 993** - the best VRM of 47 boards tested, 54 C. That is a ~3 300 saving to re-argue.
3. **PSU sizing falls.** Peak drops from ~530W to ~455W (88W CPU, 220W GPU). 850W is now
   generous rather than necessary; 750W or even 650W is defensible. Re-check
   [psu.md](psu.md).

What you should *not* do: buy a 9600X to save another 3 700, buy the 9850X3D, or buy 16 cores
you said you will not use.

## Superseded verdict (kept for the reasoning)

**Buy the 9800X3D (19 230-19 781) if you are keeping this machine four or five years** - but
the case is narrower than I first put it, and the deep pass is why:

- It is the one component you cannot meaningfully improve later without replacing it
  outright. GPU, RAM, storage and monitor are all add-later parts.
- It sets your frame-time floor - the 1% lows in simulation, strategy and MMO titles - which
  is the thing you feel rather than the average FPS.
- Premium: 8 040 over the 9700X, ~7% of the build.
- Be clear-eyed that this is a **gaming purchase**: at equal power it is 6-10% faster on
  compiles, 4-6% *slower* single-threaded, and 4.5% slower on git.

**The 9700X (11 190) is the more defensible choice than I implied**, on three grounds that
came out of this pass: at 1440p you are GPU-bound most of the time, the X3D's work benefit is
smaller than the gaming charts suggest, and the 9700X has **no failure pattern** while the
9800X3D has a documented one. Putting the 8 040 into the 2TB Samsung 990 PRO
(see [storage.md](storage.md)) instead is a genuinely competing use of the money for a dev
machine, not a consolation prize.

What you should *not* do: buy a 9600X to save another 3 600, buy the 9850X3D for 14% more,
or buy 16 cores you told me you will not use.

## Cooler consequence

- **9700X (65W) - the chosen part: Deepcool AK400 at 1 515 is enough.**
- 9800X3D (120W): Thermalright Phantom Spirit 120 SE at 2 845. See [cooling.md](cooling.md).


## Build assignment and store price (2026-09-10)

| Build | CPU | Price used |
|---|---|---:|
| **Lean** | **Ryzen 5 7500F, MPK SKU** | 6 589 (market floor, not store-checked) |
| **Working** | **Ryzen 7 9700X, BOX** | **15 099 at Telemart** |
| **Max** | **Ryzen 7 9700X, BOX** | **15 099 at Telemart** |

The 9700X BOX at Telemart is **15 099 against 12 599 at hotline floor - plus 20%**, the largest
understatement of any part in the build and consistent with the 10-25% found in the shop-price
section above. The 9600X is no longer carried in any build: with the 7500F below it and the
9700X above, six Zen 5 cores at 7 930-9 500 sit between two better answers.

See [../../pc_build.md](../../pc_build.md) for the three builds.
