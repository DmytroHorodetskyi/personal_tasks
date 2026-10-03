# RAM

## What RAM does for this machine

Capacity decides *whether* your work fits; speed and latency decide how fast games and the
CPU feel. For your load - IDE with language servers, Claude Code walking a heavy repo,
containers or WSL2, a browser with many tabs - RAM is the resource you exhaust first if you
under-buy. When you exhaust it, Windows pages to the SSD and everything gets slow at once.

This is also the component where 2026 hurts most: see the crisis note in
[../../pc_build.md](../../pc_build.md). A 32GB kit costs what a GPU tier used to.

## The characteristics that matter, and how to read them

Two rows decide this purchase and the rest are hygiene. RAM is the component where the
biggest number on the box is most often the wrong buy.

| # | Spec (unit) | What it means, plainly | What it is here |
|---|---|---|---|
| 1 | **Capacity (GB)** | How much fits before Windows starts swapping to the SSD. | **32GB for the Working and Max builds**, 16GB for Lean. The earlier wording here called 16GB "a false economy on a work machine" - too strong, and measurement says so: see the 16GB section below. 64GB is for video editing and many VMs, and costs 59 486 at crisis pricing. |
| 2 | **Speed (MT/s) and the 1:1 ratio** | Transfers per second. **On AM5, higher is not better past ~6000**: the memory controller runs in step with the RAM up to there, then halves the ratio and loses more in latency than the extra speed returns. | **DDR5-6000, full stop.** A 6000 kit beats a 7200 kit on this platform. Do not pay for 6400+. |
| 3 | **CAS latency (CL) -> real latency (ns)** | CL is clock cycles before data comes back, so it is **meaningless on its own** - it only means something next to the speed. **ns = CL x 2000 / MT/s.** | CL36 at 6000 = **12.0 ns**; CL30 at 6000 = **10.0 ns**. That 2 ns is worth 1-4% in games, mostly in 1% lows, and near nothing in tooling. Not worth 1 750. |
| 4 | **EXPO / XMP profile** | A one-click BIOS profile that applies the rated speed. Without enabling it the kit runs at the JEDEC default of 4800. | Buy **EXPO** (AMD's own) or an XMP kit known to work on AM5. Enabling it is one BIOS setting - skipping it wastes the entire purchase. |
| 5 | **2 DIMMs, not 4** | AM5 boards are 2-DIMM-optimised (daisy-chain topology). Filling all four slots forces a lower speed. | Buy **one 2x16GB kit**. Never mix two kits bought separately, never populate four slots. |
| 6 | **Kit, not single sticks** | A kit is binned and tested as a matched pair. | Always a kit - two singles are not the same thing even with identical part numbers. |
| 7 | **Module height (mm)** | Tall RGB heatspreaders collide with the front fan of a big air cooler. | Plain kits ~34mm, RGB ~44mm. The Phantom Spirit leaves ~42mm; check clearance if you buy tall RGB. |

**Ignore:** RGB, "gaming" branding, anything rated above 6400 MT/s on AM5, and heatspreader
design. Also ignore the temptation to add a second kit later - buy the capacity now.

## Specifications

| | **The pick: Corsair Vengeance 32GB EXPO** | Crucial 32GB Pro OC | GOODRAM IRDM Black |
|---|---|---|---|
| Capacity | 32GB (2x16GB) | 32GB (2x16GB) | 32GB (2x16GB) |
| Speed | DDR5-6000 (6000 MT/s) | DDR5-6000 | DDR5-6000 |
| CAS latency | CL36 | CL36 | **CL30** |
| **Real latency** | **12.0 ns** | 12.0 ns | **10.0 ns** |
| Voltage | 1.35V | 1.35V | 1.35V |
| Profile | **AMD EXPO** (one BIOS click) | XMP, works on AM5 | AMD EXPO |
| Module height | ~44mm (RGB) / ~34mm (plain) | ~34mm, plain heatspreader | ~44mm |
| Rank | single-rank per module | single-rank | single-rank |

How to read the two numbers that matter:

- **MT/s** is transfers per second. 6000 is the target on AM5 and higher is *worse*, because
  above ~6000 the memory controller drops to a half-speed ratio and loses more in latency
  than the extra speed returns.
- **CL** is how many clock cycles pass before data comes back. It is only meaningful
  alongside the speed: **real latency in nanoseconds = CL x 2000 / MT/s.** CL36 at 6000 is
  12.0 ns; CL30 at 6000 is 10.0 ns. A CL40 kit at 8000 would be 10.0 ns too - identical
  latency, and on AM5 it would still be slower because of the ratio above.

The 2 ns between CL36 and CL30 is worth roughly 1-4% in games and near nothing in tooling,
which is why the CL36 kit is the pick. Buy **one 2x16 kit**, never two 1x16 sticks and never
four modules - AM5's daisy-chained slots lose speed when all four are filled.

Note on sub-timings: Corsair ships several CL36 EXPO SKUs (36-36-36-76 and 36-44-44-96 exist
under similar names). Any of them is fine here; verify the SKU code at purchase.


## REPRICED 2026-09-14: the kit in the build sheet costs 4 296 more, and that changes the pick

Dmytro noticed the RAM had moved. It has. **Every 2×16GB DDR5-6000 kit click.ua stocks was read
directly today** (not a hotline floor), and the sheet's 25 099 no longer exists at any of them.

| Kit (click.ua SKU) | CL / timings | **Real latency** | Profile | V | Height | **UAH** | Stock |
|---|---|---:|---|---|---|---:|---|
| Prologix Black (PRO32GB6000B5K) | **not published** | ? | ? | ? | ? | **28 639** | in stock |
| **Kingston Fury Beast (KF560C36BBE2K2-32)** — the sheet's kit | 36 | **12.0 ns** | EXPO | 1.35 | ~34.9 mm | **29 395** | in stock |
| **Patriot Viper Elite 5 Ultra (VEU532G6028K)** | **28-40-40-100** | **9.33 ns** | XMP + EXPO | **1.40** | not verified | **29 734** | in stock |
| **G.Skill Flare X5 (F5-6000J3036F16GX2-FX5)** | **30-36-36-96** | **10.0 ns** | XMP + **EXPO** | 1.35 | **33 mm** | **30 328** | in stock |
| Kingston Fury Beast RGB (KF560C36BBE2AK2-32) | 36 | 12.0 ns | EXPO | 1.35 | ~44 mm | 32 312 | in stock |
| G.Skill Ripjaws S5 (F5-6000J3040F16GX2-RS5K) | 30-40-40 | 10.0 ns | EXPO | 1.35 | ~33 mm | 32 778 | in stock |
| Kingston Fury Beast (KF560C30BBEK2-32) | 30 | 10.0 ns | EXPO | 1.35 | ~34.9 mm | 32 867 | in stock |

Flare X5 timings, voltage and the 33 mm height are from
[G.SKILL's own specification page](https://www.gskill.com/product/165/396/1722406261/F5-6000J3036F16GX2-FX5):
*"32GB (2x16GB) … Up to DDR5-6000\* CL30-36-36-96 1.35V … Intel XMP / AMD EXPO"* and *"a
low-profile height of just 33mm"*. Patriot's 28-40-40-100 at 1.4 V is from the vendor's own
Viper Elite 5 Ultra page and its SKU sheet.

### What changed in the reasoning

This file declined CL30 on a specific number: *"That 2 ns is worth 1-4% in games … **Not worth
1 750**."* **That gap is now 933** — Flare X5 CL30 at 30 328 against the Kingston CL36 at 29 395.
The argument was never "CL30 is pointless", it was "not at 1 750". At 933, with a **lower profile
(33 mm vs ~34.9)** and the same 1.35 V, the CL36 kit stops being the better buy.

Note also that the **Kingston CL30 kit is 32 867** — the Flare X5 delivers the identical 10.0 ns
for **2 539 less**.

### The two that are close, stated honestly

**Patriot (9.33 ns, 29 734) is cheaper than the Flare X5 (10.0 ns, 30 328) and has the lower CL.**
It is not a clean win:

- CL is the headline number, but **tRCD/tRP matter about as much**, and there the Flare X5's
  **36-36** beats the Patriot's **40-40**. A 28-40-40 kit and a 30-36-36 kit land close in practice.
- The Patriot runs **1.4 V** against 1.35 V — more heat, and further from JEDEC.
- Its **module height was not verified** in this pass, which criterion 7 says to check.

**The Prologix at 28 639 is the cheapest and is not recommended**: no published CL, no published
profile, no binning information. Saving 1 689 on the one component where a bad bin means an
unstable machine is the wrong trade. Criterion 4 cannot even be evaluated for it.

### Verdict

**Take the G.Skill Flare X5 F5-6000J3036F16GX2-FX5 at 30 328.** AMD EXPO, 1.35 V, 30-36-36-96 at
6000 (10.0 ns), 33 mm low profile, and it is the reference kit for AM5 — the one with the most
compatibility mileage on this platform.

- **Cheaper: Patriot Viper Elite 5 Ultra, 29 734 (−594).** Lower CL, looser tRCD/tRP, 1.4 V,
  height unverified. A fine kit; the 594 does not buy a better one.
- **Cheapest that still meets spec: the sheet's own Kingston CL36 at 29 395 (−933).** Nothing wrong
  with it — it is simply 2 ns slower for 933 less, and that is now a closer call than it was.
- **Do not buy** the Kingston CL30 at 32 867 (the Flare X5 is the same latency for 2 539 less) or
  the RGB kit at 32 312 (44 mm, and criterion 7 warns about cooler clearance).

### What this does to the build totals

The sheet carries **25 099**. Nothing on the shelf is near that any more, so Working and Max both
rise whichever kit is chosen:

| Kit | RAM | **Working** (was 129 581) | **Max** (was 142 245) |
|---|---:|---:|---:|
| Kingston CL36 (same kit, new price) | 29 395 | **133 877** | **146 541** |
| Patriot CL28 | 29 734 | **134 216** | **146 880** |
| **G.Skill Flare X5 CL30 — the pick** | **30 328** | **134 810** | **147 474** |

[builds.md](../builds.md) has **not** been edited — the kit is Dmytro's choice, and the totals move
with it. Once he picks, that line and both totals change together.

## Options

Prices: lowest hotline.ua offer, 2026-09-09, UAH. All 2x16GB unless noted.

| Kit | UAH | Speed / CL | Real latency | Verdict |
|---|---:|---|---|---|
| **Crucial 32GB Pro Overclocking** | **21 699** | 6000 CL36 | 12.0 ns | Cheapest 32GB on the market. Micron dies, plain heatspreader, no RGB. The value pick. |
| Corsair 32GB Vengeance RGB AMD EXPO | 22 389 | 6000 CL36 | 12.0 ns | Native EXPO, RGB, tall. |
| PATRIOT 32GB Viper Venom | 22 630 | 6000 CL36 | 12.0 ns | Fine, less common in stock. |
| Lexar 32GB Thor RGB | 22 766 | 6000 CL38 | 12.7 ns | Worst timings of the group. No. |
| **GOODRAM 32GB IRDM Black** | **23 455** | **6000 CL30** | **10.0 ns** | The one CL30 kit at a sane price here. +1 756 over the Crucial. |
| Kingston FURY Beast 32GB | 24 899 | 6000 CL36 | 12.0 ns | Good brand, but you are paying 3 200 over the Crucial for the same timings. |
| Kingston FURY Beast 64GB (2x32) EXPO | 59 486 | 6000 CL30 | 10.0 ns | **2.7x the price of 32GB.** Crisis pricing. No. |
| **Kingston FURY 16GB (2x8) EXPO** | **15 599** | 6000 CL30 | 10.0 ns | Cheapest genuine dual-channel 16GB kit, 57 offers. **Assigned to the Lean build.** |
| Crucial 16GB, single 1x16 module | 10 499 | 6000 CL36 | 12.0 ns | Cheaper still, and **single-channel** - a large measured loss for a small saving. Never. |

## Evidence (revised after the deep review pass, 2026-09-09)

- DDR5-6000 at 1:1 is still the AM5 optimum. Claims that 6400 CL30 is now the sweet spot
  trace to an article whose only data is AIDA64 bandwidth/latency - no game or application
  results - so treat "6400 guaranteed 1:1" as unproven. 8000 forces 2:1 and measures flat
  or worse.
- **CL30 over CL36 is not worth paying for on an X3D chip.** AMD's own 30+ game data set
  for the 9850X3D shows DDR5-4800 vs DDR5-6000 differing by **~1% on average and never
  more than 2%**. If a 1 200 MT/s frequency gap is worth ~1%, a CL36 -> CL30 timing change
  at fixed 6000 is worth less. The 3D V-Cache is what absorbs memory latency - that is the
  entire point of the chip. Caveat: this is AMD marketing data, and no rigorous independent
  CL30-vs-CL36-at-6000 test was found.
- **Die identity cannot be verified per kit and mostly does not matter at 6000.** Vendors do
  not publish the die and are documented as changing it mid-production run. Die choice
  becomes load-bearing above ~6400 or for manual subtiming work, neither of which applies.
- 32GB (2x16) is the 2026 baseline; 64GB is for video editing, many VMs or local AI.
- Market context, firmer than before: DRAM contract prices rose **55-60% quarter-on-quarter
  in Q1 2026** and a further **58-63% in Q2**. This is a structural reallocation of wafer
  capacity to HBM, not a cycle; new fab capacity does not arrive in volume before late 2027.

## Verdict (revised)

> **Updated 2026-09-10.** Still 32GB DDR5-6000 CL36 for the Working and Max builds, but at
> **Superseded 2026-09-13: click.ua does not stock the Crucial Pro 2x16 CL36 kit.** The build
> takes the **Kingston Fury Beast 2x16GB DDR5-6000 CL36 (KF560C36BBE2K2-32) at 25 099** - same
> capacity, same speed, same CL36 - and Lean the **Fury Beast 2x8GB DDR5-6000 CL30 at 17 974**.
> See [../click_basket.md](../click_basket.md). The reasoning below is unchanged.
>
> store prices the kit is the **Crucial Pro at 24 099** - Telemart had no Corsair Vengeance in
> stock. **The Crucial also wins on merit, not only availability:** 36-38-38-80 against the
> Corsair's 36-44-44-96 at the same CL36 and data rate. The **Lean build carries 16GB** (15 599);
> see the 16GB section below for why that is legitimate and what it costs. Note the Crucial
> consumer brand is being wound down through 2026 - warranty continues, matching kits may not.

**Buy the Corsair Vengeance 32GB DDR5-6000 CL36 AMD EXPO at 22 389.**

Native EXPO (the Z-suffix part number), the deepest AM5 motherboard QVL presence of any kit
here, and a brand whose parts every board vendor validates against. On a machine whose RAM
should boot once and never be thought about again, QVL presence is worth more than a timing
number.

- **Cheaper: Corsair Vengeance RGB RS EXPO at 21 999**, or the **Crucial Pro CL36 at
  21 699** (Micron in-house, plain heatspreader). Both fine.
- **Not the GOODRAM CL30 (23 455)** - and not because Wilk Elektronik is a relabeler; it
  is a genuine European module manufacturer with a lifetime warranty. The problem is
  verification: the deep pass could not find a **6000 CL30 2x16 SKU in GOODRAM's own
  catalogue**, found no independent AM5 testing of IRDM DDR5 anywhere, and could not confirm
  QVL presence on any AM5 board. Thin verification on the one part whose whole job is to
  boot at EXPO and be forgotten.
- **Not the G.Skill Flare X5 CL30 (27 934)** - the AM5-native line with the best QVL record,
  and in another year I would recommend it, but +5 545 for ~1% is indefensible in this
  market.
- **Not the Lexar Thor CL38 (22 766)** - looser timings for more money than the Crucial.

**Set-up rules that matter more than the kit choice:** flash the board to the current BIOS
*before* enabling EXPO; use two DIMMs only; if you see instability, disable Memory Context
Restore and accept the slower POST. Documented AM5 instability reports on Ryzen 9000 cluster
on stale AGESA and on 4-DIMM configurations, not on kit defects.

## On 64GB - the one place the deep pass disagrees with me

The research pass argued that if 64GB is affordable at all, **this is where the money should
go**, not into timings or a faster CPU. Its reasoning:

- Docker Desktop's WSL2 backend defaults to a VM cap of **50% of host RAM** - on a 32GB
  machine it will help itself to 16GB before you tune it. That is the practical squeeze
  point for your exact workload.
- Prices are rising 55-63% per quarter, so "buy 2x16 now, add later" is the **expensive**
  path: the second kit will cost more than the first, and mixing two separately bought kits
  is the most common cause of EXPO failure.
- If 64GB, it must be **2x32** - 4x16 at 6000 on AM5 is documented as materially harder to
  stabilise.

I still recommend 32GB, for one reason: **59 486 UAH is 47% of the whole build** at current
crisis pricing, and the evidence for 64GB being *necessary* for IDE-plus-containers work is
the weakest section of the research - the pass found only opinion-grade blog sources, no
measured language-server or WSL2 footprints. Spending 37 000 more on an unmeasured need,
in the one component whose price is most inflated, is not a trade I would make for you.

**Mitigation instead of money**: cap Docker/WSL2 memory explicitly in `.wslconfig` rather
than letting it take 16GB by default, and watch actual peak usage for a few weeks. The
decision rule from the research: move to 64GB if your normal peak exceeds ~45-50GB. If it
turns out you do need it, it is a *replacement* 2x32 kit, not an addition.


## 16GB, priced and argued properly (added 2026-09-10)

Prompted by Dmytro asking why 16GB could not serve the low tier. The first answer given was
wrong twice over, and both errors are recorded here because both are easy to repeat.

**The saving is a quarter, not a half.** 32GB CL36 at 21 250 against the cheapest real
dual-channel 16GB kit at 15 599 is **-5 651**. Kit price at the low end is set by brand, PCB and
module count, not linearly by capacity. At Telemart's real prices 32GB is 24 099, so the gap is
wider there, but still nothing like half.

**Error 1: the 15.8GB figure.** An earlier turn read Windows' **Committed Bytes** as memory
demand and concluded 16GB would be exhausted before an IDE opened. Committed Bytes is what
processes have *reserved*, backed by RAM **plus the pagefile** - which is why it can exceed
installed RAM and why it says little about need. Measured properly on the current machine
(7 539MB installed; Chrome + Claude Code + Slack; no IDE, no game):

| | |
|---|---:|
| Sum of working sets, resident | 6 434 MB |
| Sum of private commit | 11 579 MB |
| Committed total (the misread number) | 15 802 MB |
| Pagefile in use / peak | 1 651 / 2 586 MB |
| Hard faults from disk | ~1.7/sec |

Real appetite is **~8-11.5GB**, so **16GB fits today's workload** and the "at its limit before
you open an IDE" claim was false. Verify in Task Manager -> Performance -> Memory: "In use" and
"Committed" are the two lines that were conflated.

**Error 2: "buy 16GB now, add another 2x8 later" does not exist on DDR5.** DDR5 memory
controllers do badly with four modules; two sticks is the practical maximum. That is why DDR4
builders are told to buy 16GB and DDR5 builders are not. Going 16 -> 32GB means **replacing the
kit**, so the 15 599 is sunk. Source: PC Builder's 2026 RAM guide, which says so explicitly and
recommends 16GB for DDR4 *because* DDR4 tolerates four sticks.

**What 16GB actually costs**, from TechSpot/Hardware Unboxed testing quoted in that guide: with
unlimited memory available most games stay under 16GB for the whole system; **a handful of AAA
titles occasionally micro-stutter** at 16GB; **Hogwarts Legacy in busy areas drops FPS and
stutters significantly**. Not game-breaking, and developers are optimising downward under the
memory crisis - but a real cost, not a free saving.

**Conclusion: 16GB is a legitimate Lean-build choice.** It meets the measured requirement; it
buys 5 651-8 500; it costs occasional stutter now plus a full kit re-buy later. It is not right
for the Working build, where the money is deliberately going into the platform rather than the
card.

## Speed and timings: the independent data the first pass could not find (added 2026-09-10)

The evidence section above flagged that no rigorous independent CL30-vs-CL36 test could be found
and that only AMD's own marketing data supported "timings barely matter". Two 2026 sources close
that gap:

- **Hardware Unboxed, via PC Builder:** Ryzen 7700X, RTX 4090, 1080p, seven games - **8.5%**
  between DDR5-6000 CL30 and DDR5-6000 **CL40**. Our CL36 sits between them, and the gap shrinks
  with a slower GPU or a higher resolution. On 13th/14th-gen Intel the comparable figure was
  5.6% between CL30 and DDR5-**5200** CL40.
- **Linus Tech Tips, February 2026** - four CPUs at eight DDR5 speeds from 4800 up. **Citation
  corrected 2026-09-13:** the two CPUs say different things and an earlier version of this line
  merged them. *"Anything with a tuned expo profile, you probably won't notice a difference"* is
  said of the **9950X**. Of the **9800X3D** he says *"6,000 mega transfer CL30 is still the sweet
  spot"* - so LTT names CL30, and citing him against paying for it was wrong. The spread does
  narrow with ray tracing or at higher resolution. Their exception is productivity: **their
  compile test did gain from faster memory**, which is the half of this machine's workload that
  matters, and their advice for that case is explicit - *"if you're making money with your
  machine, you might want to consider ponying up for a high-speed, low latency kit."* They also
  note module capacity can matter as much as speed.
- **Gamers Nexus, 2020** (`vbHyF50m-rs`, supplied by Dmytro and previously uncited) is the
  counterweight, and it is the only source here that benchmarked **production** work against
  memory tuning: **3.5% in Blender and 1.6% in 7-zip**, against 10-17% in games. His own
  conclusion points the same way as this document's - once the faster memory costs ~$100 more,
  *"you're kind of approaching just the better class of CPU."*

**Net: this doc's "DDR5-6000, do not pay for CL30" verdict holds** - but on the Hardware Unboxed
8.5% figure and the Gamers Nexus production measurements, **not** on LTT, who names CL30 as the
sweet spot. **The size of the compromise, stated as a number for the first time:** PC Builder's
absolute-latency formula is CL x 2000 / speed, so the CL36 kit is **12.0 ns** against **10.0 ns**
for 6000 CL30 and 6400 CL32, and 9.33 ns for 6000 CL28.

## Price check, 2026-09-10

Telemart, in stock: **Crucial Pro 32GB 6000 at 24 099** (cheapest 32GB there), Kingston FURY
Beast 32GB CL36 27 899, CL30 30 299. Telemart stocked **no 16GB DDR5-6000 kit at all** that day -
a purchase-time problem for the Lean build, not an argument against 16GB. One conflict to
re-check before buying: PC Builder (April 2026) reports retail RAM prices coming *off* the peak,
against the structural rise recorded in the market-context note above.


## Brand, die and rank: what the sources actually say (2026-09-10)

From Socket-X's "Every 2026 RAM Brand Explained" (2026-05) and a reader guide Dmytro supplied.
Two findings change something here.

**1. The Crucial consumer brand is being wound down.** Micron has announced that consumer
shipments end **through 2026**, with warranty and support continuing afterwards. The Crucial Pro
kit is this build's value pick at 24 099, so this is worth knowing before buying: the kit itself
and its warranty are unaffected, but a matching replacement kit may not exist in a year. It does
not change the pick - **never mix kits** is already the rule, so a future replacement would be a
full kit anyway - but if a warranty exchange matters more than 1 700, the Kingston FURY Beast at
27 899 is from a brand that is staying.

**2. The rank claim in the spec sheet was wrong, and is corrected.** Every DDR5 IC is currently
16Gb, so a **16GB DDR5 module can only be single-rank**; dual-rank starts at 32GB *modules*.
Both the 2x8GB and the 2x16GB kits here are therefore single-rank. Dual-rank is worth roughly
**9%**, but reaching it means 2x32GB - 64GB at 2.7x the price. It is not a lever in this build.
(The DDR4-era advice that "16GB DIMMs tend to be dual-rank" does not transfer.)

**What the brands actually are**, since none of them make the silicon - SK Hynix, Samsung and
Micron do:

- **Crucial is Micron's own consumer brand**, controlling silicon through to final module. Lowest
  failure rates in the consumer market, conservative timings, limited overclocking headroom.
  This is why the die-identity problem flagged earlier in this document does not apply to it -
  and it is the strongest argument for the Crucial Pro pick.
- **Kingston sources dynamically from all three suppliers** by batch price, so two identical
  mid-range kits bought months apart can contain different silicon. Its **Fury Beast uses
  low-profile stamped heat spreaders specifically to clear large air coolers** - convenient for
  the Lean build with an AK400.
- **Corsair also swaps chips within the same part number**, and prints a **tiny version number on
  the module sticker**. Combining two Vengeance kits with different version numbers causes
  memory-training errors and boot loops. That is the concrete mechanism behind this document's
  "never mix two kits" rule - and the version number is the thing to check if a shop offers to
  make up 32GB from two 16GB kits.
- **Patriot leans on well-binned SK Hynix** in its higher-end kits.

**Secondary timings are where two "identical" kits differ.** The full string is
tCAS-tRCD-tRP-tRAS and tighter is better throughout. At the same CL36 and the same 6000 MT/s:

| Kit | Timings |
|---|---|
| **Crucial Pro** | **36-38-38-80** |
| Corsair Vengeance | 36-44-44-96 |

That is a real advantage to the Crucial beyond its price, and it was already in the options table
above without being read.

**Build note: populate the A2/B2 slots**, i.e. the second slot of each channel. Open A1/B1 slots
cause fewer signal reflections than open A2/B2 ones. The labelling is in the board manual and is
not always printed on the PCB.

**One more argument for 16GB being defensible:** games allocate a *percentage* of installed RAM
rather than a fixed amount, so observed usage on a larger machine overstates what a game actually
needs. Measured usage on a 32GB machine is not evidence that 16GB would have failed.

**GamingScan's "How To Choose RAM" (2019), re-read in full 2026-09-13 - the earlier dismissal
was wrong on both counts.** It was recorded here as *"nothing usable ... its quad-channel and
four-stick advice is actively wrong for AM5"*. It does not give four-stick advice: it recommends
**two sticks** and explicitly confines quad-channel's benefit to *"servers and workstations
running memory hungry software"*, not gaming. That is correct for AM5. It also carries the
**never-mix-kits rule independently** - *"we don't advise combining different RAM modules
especially ones from different manufacturers ... it can lead to some unexpected compatibility
issues crashes"* - which is a second source for the rule this document derives from Corsair
version numbers. What **is** genuinely obsolete is its capacity advice: *"32 gigabytes is a bit
too much for gaming at the moment"*, DDR4-era and superseded.

## "Heavy repos" has no number, so the 32GB case rests on references (2026-09-11)

Dmytro's challenge: measuring his current machine is a bad way to size RAM, because it only
captures what he happens to run today. He is right, and the earlier measurement in this document
is now framed accordingly: **~8-11.5GB with Chrome + Claude Code + Slack, no IDE and no
containers running** tells you what today's subset costs, not what the workload needs.

**And the requirement itself was never quantified.** "Heavy repos" is Dmytro's phrase from the
requirements table, repeated across five component documents, with no repo size, file count or
memory figure ever attached. It cannot be checked against anything.

So the sizing below comes from published component costs instead, which do not depend on
knowing his repo:

| Component | Typical resident cost | Source type |
|---|---|---|
| VS Code or a JetBrains IDE, one window | **400-600 MB** | dev-tooling guides, 2026 |
| Language servers / Node dev server | 200-300 MB | same |
| Browser, several tabs | 500 MB - 1 GB | same |
| Slack or Teams | ~300 MB | same |
| **Docker Desktop VM, idle** | **1.2-2 GB** | Docker Desktop requirements, 2026 |
| Docker engine process | 200-400 MB | same |
| A typical Compose stack (web + API + Postgres) | **1-2 GB**, and **4-8 GB** for a fuller stack with cache and a worker | same |
| **WSL2 behaviour** | **does not release memory back until shutdown**, builds disk cache to fill what it is allowed, and defaults to **half of system RAM**; large image builds **spike to 20GB+** | Microsoft/Docker forums and Docker Desktop docs |

**The pattern that decides it is WSL2, not the IDE.** On Windows, containers run in a WSL2 VM
that claims memory and holds it until shutdown, with a default ceiling of half the machine.
On a 16GB box that is an 8GB ceiling shared with everything else; the published guidance is
that Docker, WSL2, an IDE and a browser together can pressure even a 32GB machine, and that
`.wslconfig` limits are mandatory rather than optional.

**Published recommendations, stated plainly:** 16GB is described as the *practical minimum* for
2026 development; **32GB as the minimum for Docker-based development**; 64GB only for VMs,
multiple stacks or JVM tooling. The stated reason for 32GB over 16GB is not today's peak but
that it keeps the machine relevant through several framework and tooling cycles - which is
exactly Dmytro's objection to measuring today's load.

**Conclusion, and it changes the argument rather than the pick.** The 32GB kit on Working and
Max is **not** headroom-for-its-own-sake and does not need his current machine to justify it:
the stated work profile includes containers, and every reference sizes container development at
32GB on Windows because of how WSL2 holds memory. The **16GB on Lean remains a real compromise**
- it is the practical minimum, not a comfortable figure, and it is the tier's largest
irreversible decision since DDR5 cannot be topped up later.

### Correction and the real justification (2026-09-11, verified at source)

Two things were wrong in the section above and are corrected here.

**1. The WSL2 memory claim, checked against Microsoft's own `.wslconfig` reference:**

| Claim made | What Microsoft documents | |
|---|---|---|
| WSL2 defaults to half the machine's RAM | `memory` default: **"50% of total memory on Windows"** | correct |
| WSL2 holds memory until shutdown | `autoMemoryReclaim` default: **`dropCache`** - "cached memory will be reclaimed immediately" | **wrong**; true of older WSL2, not current |

**2. Containers are not this machine's load.** Dmytro, 2026-09-11: *"I rarely run Docker
containers."* The container-based argument for 32GB therefore does not apply to him, whatever
the published guidance says about container developers generally. Both are struck.

**The justification that does hold, and it is on the same axis as the CPU upgrade.**
Dmytro's test for the Working build: the GPU is unchanged and only the CPU rises, so the RAM
increase has to be justified by the same thing the CPU increase is - the work load - or not
made at all. It is:

- His own requirements name **"IDE + language servers, Claude Code over heavy repos"**.
- **Language servers are the memory-hungry part of that sentence, not the IDE.** Reported
  figures for rust-analyzer on large workspaces: **1-4GB typical, spiking past 8GB**, ~2.5GB on
  an ordinary company repo, and ~13GB on an 830-dependency cargo workspace. TypeScript's server
  sits in the same class on large codebases. These are the reports of the people running them,
  not a lab, but they are consistent across years of issue threads.
- The measurement in this document - **8-11.5GB** - was taken **with no IDE and no language
  server running**. Add one heavy-repo language server at its typical 1-4GB and the machine sits
  at **12-15GB against a 16GB ceiling that Windows also has to live inside**. That is the
  condition where Windows pages and everything stalls.

**So the 32GB on Working and Max is justified, on the work case and not on games or
containers** - the same justification as the 9700X, and it does not depend on the GPU. The two
upgrades are coherent with each other.

**And the same evidence is what makes Lean's 16GB a real compromise rather than a neutral
saving:** one heavy-repo language server is enough to reach the ceiling, and DDR5 cannot be
topped up later.

## The proper source: TechSpot's 8 / 16 / 32 / 64GB test (2026-01), read 2026-09-11

This replaces the container argument, the language-server argument and the current-machine
measurement as the basis for the 16-vs-32 decision. All three were weak: the first did not apply
(Dmytro rarely runs Docker), the second came from GitHub complaint threads rather than a lab,
and the third measured only what happens to be running today. **This is a lab test, by Steven
Walton - the same tester behind the 47-board B850 roundup this project already relies on.**

**Method, and why it is trustworthy:** a **three-year-old Windows 11 install** with games and
everyday applications already on it - explicitly not a fresh bench - with **Chrome on six tabs,
Discord and monitoring tools open during every run**. Capacity was varied by limiting what
Windows could address on a single 64GB kit, so timings, frequency and ranks are identical across
all four configurations. That removes the usual confound where "more RAM" also means different
memory.

**Findings:**

| | Result |
|---|---|
| 8GB | The only configuration that actually breaks - poor frame-time consistency |
| **16GB vs 32GB** | **"Largely the same"** - comparable averages *and* comparable 1% lows in most titles |
| The exception | **Mafia: The Old Country** needs ~**20GB**; 16GB is not enough and a 24-32GB kit is recommended |
| **The dependency that decides it** | **VRAM.** On a 16GB graphics card, going 16 -> 32GB system RAM changes nothing. On an **8GB** card the same change improves **1% lows by over 60%**, because assets spilling out of the VRAM buffer land in system memory instead |

**Verdict as published:** *"32GB is the sweet spot for gamers... it provides enough capacity to
ensure optimal performance across all titles and should continue to do so for the foreseeable
future."* But also: *"most games still run perfectly well with 16GB"*, and in the current DRAM
market 16GB is *"a perfectly viable option"*. The explicit split is **"for higher-end builds, it
generally makes sense to absorb the pain of current DRAM pricing and invest in a solid 32GB
kit"**, while budget builders can take 16GB to cut cost.

**Applied to this build - and it matches the tiering already in place.**

- The **9070 GRE carries 12GB of VRAM**, between the two cases tested. Less spillover exposure
  than the 8GB card that benefited most from 32GB, more than the 16GB card that benefited not
  at all.
- **Lean keeps 16GB.** It is the budget tier, and the lab's own words for that case are
  "perfectly viable". The compromise is real but bounded: one known title so far, plus whatever
  follows it.
- **Working and Max keep 32GB.** These are the higher-end builds the same article tells you to
  absorb the DRAM pricing for, and the capacity that is expected to hold "for the foreseeable
  future" - which matters because **DDR5 cannot be topped up later** and the kit would have to
  be re-bought.

**This is the justification. The earlier ones are withdrawn.**

### What the CPU and GPU vendors actually recommend (checked 2026-09-11)

Asked directly: what do the parts themselves specify?

| Source | What it states about memory |
|---|---|
| **AMD, Ryzen 7 9700X product page** | System Memory Type **DDR5**; Memory Channels **2**; Subtype **UDIMM**; Max Memory Speed **DDR5-5600** (2x1R, JEDEC). **No capacity recommendation of any kind.** |
| **AMD, Radeon RX 9070 product page** | **Minimum PSU 650W** and nothing else - no system-memory line at all |

**So neither vendor recommends a capacity.** The CPU constrains *type, channels and JEDEC
speed*; the GPU says nothing. Capacity is specified by software, not by the hardware - which is
why every argument in this document has had to come from workload evidence rather than a
spec sheet.

**Where the recommendation does exist: the games themselves, at this build's exact target.**
Mafia: The Old Country's published PC specs list **32GB as recommended**, and the recommended
tier is explicitly defined as **2560x1440 at the High preset** - the resolution and quality
target in the requirements table. Its recommended CPU and GPU (Ryzen 7 5800X / RX 6950 XT) sit
below this build's, so the 32GB figure is not attached to some higher tier of machine.

This is also the title TechSpot's lab test independently found to need **~20GB** - so the
publisher's 32GB and the lab's measurement agree in direction, and the lab number shows the
recommendation is not pure padding.

**Conclusion, consistent with everything above and not a new argument:** there is no vendor
recommendation to appeal to, and the software recommendation at 1440p High has now reached
32GB for at least one shipping title, with Unreal Engine 5 games generally reported in the
18-24GB range. **Working and Max at 32GB meet the current recommended spec for their own target
resolution and preset. Lean at 16GB sits below it**, which is the compromise that tier is
already documented as making.

### Beyond the vendor pages: what builders and testers say (2026-09-11)

The vendor pages specify no capacity, so the question was put to sources that either test or
build for a living.

**1. Puget Systems** - a workstation builder with a published labs team, whose recommendations
come from their own testing rather than software vendors' spec sheets:

> a system with **16 GB of RAM reduced performance across all content creation applications, and
> it is not recommended for creative workloads - especially with top-tier components**

Their tiering: **32GB is "a cost-effective option" for lighter workloads**; 64GB is the sweet
spot for professional content creation. In other words the builder that tests this for money
treats **32GB as the practical floor for a working machine and 16GB as not recommended at all**.

**2. The prebuilt market, at this build's exact components.** Machines sold around a **9700X
paired with an RX 9070 GRE / 9070 / 9070 XT** ship predominantly with **32GB DDR5** -
iBuyPower, AVGPC, VTG, Dan's Custom, Micro Center's PowerSpec among them.

> **The Ukrainian half of this, added 2026-09-13 by the source audit.** Every builder named above
> is American, which was the weak point of this line of evidence. Dmytro had already sent two
> Ukrainian machines and neither was ever recorded: the **ASGARD Hel at click.ua, 96 099 ₴** — a
> Ryzen 5 8400F with an **RX 9070 XT 16GB** and **32GB DDR5-5600** — and **gamingpc.com.ua's
> Vision 5 Pro at 119 073 ₴** — a Ryzen 7 7700 with an RTX 5070 and **32GB DDR5-5600**. **Both
> ship 32GB**, one beside each of the two GPUs this build has considered. That is the local
> corroboration the argument was missing. 16GB configurations
of the same pairing do exist (CyberPowerPC lists a 9700X + 9070 GRE 12GB with 16GB DDR5-6000),
so it is not unheard of - but 32GB is the configuration the market treats as standard for this
class of machine.

**Where all four lines of evidence now stand:**

| Source | Type | Says |
|---|---|---|
| AMD (CPU and GPU pages) | vendor spec | **nothing about capacity** |
| TechSpot, Jan 2026 | lab test, stated method | 16 vs 32GB **equivalent for gaming** with adequate VRAM; one title already needs ~20GB; "32GB is the sweet spot" |
| Game publishers | software requirement | **32GB recommended at 1440p High** on at least one shipping title |
| Puget Systems | builder with test lab | **16GB not recommended** for work machines; 32GB the floor |
| Prebuilt market | what actually ships | **32GB standard** on 9700X + 9070-class machines |

They converge: **16GB is a gaming-acceptable budget choice and a poor working-machine choice;
32GB is the standard for this class.** That is exactly the split already built into the three
tiers - Lean 16GB, Working and Max 32GB - and it is now supported by a lab, a builder, the
publishers and the market rather than by any single argument.

## Every video behind this document

**Added 2026-09-13 by the source audit.** This file named its videos by channel and year only — **no id, no link** — which is the exact complaint the audit was started over: *"the docs were found to cite videos by channel name with no ID and no timestamp, leaving nothing Dmytro could re-check."* 4 of the 5 RAM videos could not be traced from this page at all. The full set, with the transcript on disk and the quote-by-quote record in [source_audit.md](../source_audit.md):

| Video | Channel | Date | Title |
|---|---|---|---|
| [`vbHyF50m-rs`](https://www.youtube.com/watch?v=vbHyF50m-rs) | Gamers Nexus | 2020-05-22 | Intel i5-10600K Cache Ratio & RAM Overclock Beats 10900K: How Much Memory Matters |
| [`mkpCvaBBo-c`](https://www.youtube.com/watch?v=mkpCvaBBo-c) | GamingScan | 2019-11-02 | How To Choose RAM [Ultimate Guide] |
| [`05HRLuU--jI`](https://www.youtube.com/watch?v=05HRLuU--jI) | Linus Tech Tips | 2026-02-26 | Stop WASTING Money on Fancy RAM |
| [`9-yjwxhmr40`](https://www.youtube.com/watch?v=9-yjwxhmr40) | PC Builder | 2026-04-11 | 🛑STOP🛑 Buying Bad RAM! Best Ram for Gaming 2026 / DDR4 vs DDR5 |
| [`eFmQG4BuiGw`](https://www.youtube.com/watch?v=eFmQG4BuiGw) | Socket-X | 2026-05-21 | Every 2026 RAM Brand Explained. What’s the Real Difference? |

