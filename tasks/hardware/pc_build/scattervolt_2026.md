# ScatterVolt, "Best CPU GPU Combo for Every Budget! (2026)" — full record

Source: [youtu.be/UyKvDu9dZUs](https://www.youtube.com/watch?v=UyKvDu9dZUs), 49:26, published
2026-08-16, 220k views. Read via `code/yt_transcript.py` on 2026-09-10. **Transcript kept from 2026-09-13** at [`sources/combo_UyKvDu9dZUs.md`](sources/combo_UyKvDu9dZUs.md) - 47 476 chars, re-read end to end by the source audit, which found every tier-9 and tier-10 figure below to be verbatim accurate.

**Source tier: opinion, not measurement.** A build-guide channel with no test rig and no
methodology page, quoting US prices. Under the rules in [tools.md](tools.md) it is good for
direction and for what a builder would pair, and it is not a source for any number. Every
figure below is his, in USD, as of mid-August 2026.

Caption artefacts, decoded throughout: "RX970" = RX 9070, "RX960 XT" = RX 9060 XT,
"RTX 570 Ti" / "RTX 5070 Ti" = RTX 5070 Ti, "LGA700" = LGA1700, "Rockm/Rockheim" = ROCm.

## The twelve combos as he gives them

Each tier is CPU options / cooler / board / RAM / PSU, then a **minimum** and a **maximum** GPU
list — he treats the GPU as the free variable and the rest as a platform that carries any of them.

### Content creation — deliberately Intel

Reason given: Intel outperforms Ryzen in multi-threaded creative applications and runs cooler
out of the box; LGA1700 also allows DDR4, which is far cheaper than DDR5 at current prices.

| # | Tier | CPU | Board / RAM / PSU | GPU |
|---|---|---|---|---|
| 1 | **Budget video + photo editing** — ~$1 000 build ([dE98eU](https://pcbuilds.gg/b/dE98eU)) | i3-14100F, or i5-14400F for complex timelines | B760 **DDR4**, 16–32 GB DDR4, 550–750 W | Any **Intel Arc**: A570/A580, B570, B580. Arc for the 4K 10-bit 4:2:2 HEVC decode and for VRAM per dollar; RTX 4060/5060 only have 8 GB |
| 2 | **Editing + 3D modelling** — ~$1 500 build ([dVH6UA](https://pcbuilds.gg/b/dVH6UA)) | i5-14400F floor (6 cores for game dev), i5-14600K, i7-14700K | B760 DDR4, 32–64 GB DDR4, same PSU | Arc B570 (editing), used RTX 4060 (3D only), Arc B580 12 GB at $300, RTX 5060 / 5060 Ti (Blackwell 4:2:2 engines), **RTX 5070 12 GB** as the ceiling |
| 3 | **Professional workstation** ([Bw9zzN](https://pcbuilds.gg/b/Bw9zzN)) | Core Ultra **250K Plus / 270K Plus** | **Z890** (M.2 count, RAID), ≤850 W unless a 5090 | Nvidia only here. 5060 Ti 16 GB → 5070 12 GB → 5070 Ti 16 GB (**overpriced**) → **RTX 5080, the pick**: same encoder/decoder count as the 5090 for far less |
| 4 | **Local LLM / AI** ([3A5mp1](https://pcbuilds.gg/b/3A5mp1)) | Ryzen 9 **9900X / 9950X** — 24–32 threads for the scripting around the model | **X870E** for lanes, M.2 slots and multi-GPU; **64–256 GB**; 850 W single card, up to 1600 W with dual 12 V headers for two | "The name of the game is VRAM, that's basically it." RTX 3060 12 GB, Arc A770 16 GB, RX 7600 XT 16 GB (if ROCm covers your model), **4060 Ti 16 GB / 5060 Ti 16 GB as the bread and butter** |

### Gaming

| # | Tier | CPU | Board / RAM / PSU | Minimum GPU | Maximum GPU |
|---|---|---|---|---|---|
| 5 | **Budget 1080p, Intel** — $800 ([FPZN0R](https://pcbuilds.gg/b/FPZN0R)) | **i3-14100F** — better single-thread than any 6-core Ryzen at the price; upgrade path i5-14600KF / i7-14700KF | B760M **DDR4**, 16 GB DDR4, 550–650 W bronze | Used RTX 2070 Super / 2080 at $170–180 (1st-gen RT cores age better than RX 6000); new Arc A570/A580/B570 | Used RX 6800, used RX 7700 XT, RTX 5060 Ti 8 GB (**1080p only**), RX 9060 XT 16 GB |
| 6 | **Budget "1080p−", AMD** — $700 ([An6D7I](https://pcbuilds.gg/b/An6D7I)) | Ryzen 5 5500 — cheap **because it is PCIe 3.0**; upgrade path 5600X3D/5700X3D/5800X3D | B550M DDR4, 16 GB DDR4, 550–650 W | Used RTX 2000 **specifically**: they have a full x16 slot, so PCIe 3.0 costs nothing. Arc is ruled out here — it needs Gen 4 | Same as tier 5 |
| 7 | **1080p+ / "1440p−"** — $1 000 ([4X3Gg3](https://pcbuilds.gg/b/4X3Gg3)) | **Ryzen 5 7500F** — "you won't tell the difference" vs 7600X/9600X, save the $30 for the cooler | B850, 16 GB DDR5, 650–750 W | Arc A580/A750, used RTX 3060 Ti 8 GB (256-bit bus), Arc B570/B580 | RTX 5070 or **RX 9070 16 GB** — beyond that, get a faster CPU |
| 8 | **1440p** — $1 200 ([KhA8pw](https://pcbuilds.gg/b/KhA8pw)) | Same 7500F class | Same, PSU beefed up | Used **RTX 2080 Ti 11 GB at $250**, new Arc B580, used RX 6800 16 GB, used RTX 3080 10 GB (wide bus compensates), new RX 9060 XT 16 GB — overpriced, but better 1440p value than a 5060 Ti 16 GB | RX 9070 XT, RTX 5070 Ti |
| 9 | **1440p+** — $1 500 ([xF7JLC](https://pcbuilds.gg/b/xF7JLC)) — **the tier that matches this task** | 7500F floor; **7700X at $220 (8c/16t) "really hard to beat"**, ≥$100 under a 7800X3D. X3D optional, changes nothing at 1440p | **B850, not X870.** 16 GB DDR5, 32 if the budget allows. 650–750 W | **RX 9070 GRE at $550, price locked** — "probably the one GPU that isn't going to go up." A discounted RX 9070 16 GB is the best option if you can find one; not worth a premium over the GRE above $100 | **RX 9070 XT.** The 5070 Ti is ~$300 more for too little; the 5080 is +$600 for at most 1.2× |
| 10 | **1440p++** — $2 000 ([9vMtMc](https://pcbuilds.gg/b/9vMtMc)) | Same as 9 | Same, PSU up to **850 W** | **RX 9070 XT** — "the best GPU of this generation from all the major brands. The pricing is unmatched" | RTX 5080, 5090 |
| 11 | **1080p esports, high refresh** ([wyFpyp](https://pcbuilds.gg/b/wyFpyp)) | **X3D only** — CPU-bound at 360+ FPS, and L3 cache decides the 1% lows | **X870** if a 9000-series X3D (those overclock; 7000 X3D are locked). ≥16 GB, 750–1050 W | **RTX 5060 Ti 8 GB** — fastest 8 GB card, and 8 GB SKUs have escaped the memory-price rises that hit the 16 GB model | Anything; the CPU cannot bottleneck |
| 12 | **4K ultimate** — $2 500 ([xV66IA](https://pcbuilds.gg/b/xV66IA)) | 9800X3D, or **9950X3D2** 16c/32t | B850, or X870 for OC headroom and power phases. 32–64 GB, 1050–1200 W | RX 9070 XT if money-conscious | RTX 5080, 5090 |

## The four things worth taking from it

1. **Price direction, mid-August 2026.** RTX 5070 and RX 9070 each took **+$50 in 30 days**;
   the 5060 Ti 16 GB has had "hefty" rises while the 8 GB model has not; the **9070 GRE is the
   one card holding at $550**. Cause: industry-wide memory shortage. Everything he says points
   one way — parts get dearer from here, so a delay costs money rather than saving it. This is
   a second, independent signal behind the re-pricing flag in [../../pc_build.md](../pc_build.md).
2. **The RX 9070 XT is the generation's value pick**, said twice and unprompted. Independent of
   this task's own reasoning, which reached the same place from TechPowerUp and Tom's.
3. **Bottlenecking is not a thing to design around** at 1440p: "it's not like Skyrim potions,
   there's no special sauce." Same conclusion as [tools.md](tools.md), which rejects bottleneck
   calculators outright.
4. **ROCm support is widening across LLM software** — a small mark in favour of the parked
   "CUDA some day" question being genuinely parkable on an AMD build.

## Where he is wrong for this build

**16 GB of DDR5 — and he was more right than this note first allowed.** He says 16 is still fine
in 2026 and 32 a luxury. For the Working and Max builds that is still wrong: this is a work
machine first, and [components/ram.md](components/ram.md) holds 32 GB there. But measurement
later showed real demand on the current machine is only ~8-11.5 GB, and the **Lean build now
carries 16 GB** for exactly his reasons. Corrected 2026-09-11.

**Everything else he recommends, this task already decided independently** and with better
sourcing: B850 over X870, AM5 for socket life, an air cooler, 750–850 W, the 9070-class GPU.
Nothing in the video changes a decision.

## How his tiers map onto this task's builds

> **Written 2026-09-10 against the old Floor/Probable/Ceiling tiers, at hotline floor prices.**
> The build table has since been rebuilt as **Lean / Working / Max** on real store prices - see
> [../pc_build.md](../pc_build.md). The mapping below still reads correctly if you substitute
> Floor->Lean-ish, Probable->(deleted), Ceiling->Max, but **do not take any number from it**.
> What survives unchanged: his GPU ladder is the same ladder this task arrived at, and his
> $1 500 tier is where he says to stop.

### The original mapping, for the record

**All three of our builds fit inside his single $1 500 tier, and our ceiling is the boundary
into his $2 000 one.** His GPU ladder for tier 9 is rung-for-rung our three-build exercise:

| His rung | His words | Our tier |
|---|---|---|
| Tier 9 **minimum** — RX 9070 GRE | "$550, price locked, the one GPU that isn't going to go up" | **Floor** — GRE ~33 000 |
| Tier 9 **best** — RX 9070 16 GB | "the absolute best GPU option **if you can find it discounted**"; not worth a premium over the GRE above $100 | **Probable** — 9070 ~38 500 |
| Tier 9 **maximum** = tier 10 **minimum** — RX 9070 XT | "the best GPU of this generation from all the major brands" | **Ceiling** — 9070 XT ~46 500 |
| Tier 10 **maximum** — RTX 5080 / 5090 | "+$600 for at most 1.2× faster" | Rejected in [components/gpu.md](components/gpu.md) |

So his structure and this task's are the same shape, reached independently: **one platform,
the GPU as the free variable.** His tiers 9 and 10 share CPU, cooler, board and RAM and differ
only in the card and the PSU; our three tiers share board, RAM, SSD, case and PSU and differ
only in CPU and GPU.

Where they diverge:

1. **CPU generation.** He holds one CPU across both tiers — 7500F floor, 7700X ($220, 8c/16t)
   as the value pick — and never raises it as the GPU climbs, because at 1440p the CPU is not
   the lever. Our 9700X is that same 8-core one generation up; our top two tiers already share
   it, so only the floor's drop to a 9600X departs from his pattern, and it departs in the
   direction he would endorse.
2. **PSU, and this one is actionable.** He splits 650–750 W for tier 9 and 850 W only at tier
   10. Our ladder carries 850 W throughout, and [../../pc_build.md](../pc_build.md) already
   records that the 9700X decision dropped system peak to ~455 W, making 850 W "generous rather
   than required". His split is a second voice for the same conclusion: on measured draw this is
   a 750 W build at every tier, including the ceiling.
3. **RAM.** 16 GB in both his tiers, 32 GB in all three of ours. We sit above his whole ladder
   here, correctly — see the note above on why his advice does not apply to a work machine.
4. **Scope.** His totals are the tower only. Ours carry the monitor (~7 800–11 000) and Windows
   (2 500), so strip ~10 000–13 500 before any comparison: our ceiling is a ~111 500 tower, the
   probable ~105 500, the floor ~97 700.

**On the money, the comparison is worth one look and no more.** His $1 500 tower against our
~105 500 probable is not a like-for-like gap: his prices are US retail before sales tax, ours
Ukrainian retail including 20% VAT and import duty, and ours carries twice the RAM at crisis
pricing (~25 000, a fifth of the machine, buying no performance). The one clean single-part
check is the GRE: his $550 against our ~33 000 hotline floor. Whatever rate is applied, ours is
the dearer end — and since the hotline floor is itself understated 10-15%, the real Ukrainian
premium on that card is larger than it first looks. That is a reason to re-price at store
level, not a reason to import.

**What his advice amounts to for this build:** the Probable tier is the build, the Ceiling is
exactly where he would stop ("beyond this is just diminishing returns"), and the money above it
buys nothing. Which is where this task had already arrived.

## Component-by-component, his two tiers against ours

His prices are US, mid-August 2026; ours are the UAH figures from the component verdicts.

### Every build, one column each

| Part | His 1440p+ $1 500 | His 1440p++ $2 000 | Our floor | Our probable | Our ceiling |
|---|---|---|---|---|---|
| CPU | 7500F ~$120, or **7700X $220** | 7700X $220, unchanged | 9600X **9 800** | 9700X **13 500** | 9700X **13 500** |
| Cooler | air, $50-60 class | air, $50-60 class | AK400 **1 515** | AK400 **1 515** | AK400 **1 515** |
| Board | B850 | B850 | B650M GAMING PLUS WIFI **7 100** | B850 Pro RS WiFi **9 400** | B850 Pro RS WiFi **9 400** |
| RAM | 16 GB DDR5 | 16 GB DDR5 | 32 GB DDR5-6000 **25 000** | 32 GB **25 000** | 32 GB **25 000** |
| SSD | not itemised | not itemised | 990 PRO 2TB **16 299** | 990 PRO 2TB **16 299** | 990 PRO 2TB **16 299** |
| GPU | RX 9070 GRE $550 | RX 9070 XT | 9070 GRE **33 000** | 9070 **38 500** | 9070 XT **46 500** |
| PSU | 650-750 W | 850 W | Pure Power 13 M 850W **5 759** | same **5 759** | same **5 759** |
| Case | not itemised | not itemised | Lancool 216 **4 667** | Lancool 216 **4 667** | Lancool 216 **4 667** |
| Monitor | none | none | Q27G4ZR **9 551** | Q27G4ZR **9 551** | Q27G4ZR **9 551** |
| Windows | none | none | **2 500** | **2 500** | **2 500** |
| **Tower only** | **$1 500** | **$2 000** | **103 140** | **114 640** | **122 640** |
| **With monitor + OS** | - | - | **115 191** | **126 691** | **134 691** |

His towers carry a case, SSD and PSU he does not name; the $1 500 and $2 000 are the totals of
his own pcbuilds.gg templates, so they are comparable to our tower-only row and not to the
full one.

### The GPU ladder

| | GPU | His rung | CPU+GPU+board | Our build total |
|---|---|---|---:|---:|
| **Our floor** | RX 9070 GRE ~33 000 | his tier 9 **minimum**, $550 and price-locked | 49 900 | **~115 200** |
| **Our probable** | RX 9070 ~38 500 | his tier 9 **best, if discounted** | 61 400 | **~126 700** |
| **Our ceiling** | RX 9070 XT ~46 500 | his tier 9 **max** = tier 10 **minimum** | 69 400 | **~134 700** |
| - | RTX 5080 / 5090 | his tier 10 max | - | rejected, [components/gpu.md](components/gpu.md) |

### The arithmetic that falls out of this

**Every tier is ~7 000 above the running estimate in [../../pc_build.md](../pc_build.md)**
(108 000 / 120 000 / 130 000). The estimates still carry SSD ~11 700 and monitor ~7 800, while
the settled verdicts are the 990 PRO 2TB at 16 299 and the Q27G4ZR at 9 551 - **+6 350 between
them**. This is arithmetic, not a new price rise, and it is on top of the 10-15% hotline
understatement already flagged. Re-price and re-total together.

Two levers if the ceiling has to come back under 125 000: the **750 W PSU** his tier-9 split
endorses (system peak is ~455 W), and the **Q27G4XF monitor at 6 757** (-2 794).
