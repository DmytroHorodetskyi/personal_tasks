# GPU

## What the GPU does for this machine

It decides your gaming experience at 2560x1440 almost single-handedly, and it is the single
most expensive part. For your work it does close to nothing: you confirmed no CUDA
workloads, so the GPU is a gaming purchase plus a display adapter. That is a useful
simplification - it means the choice is decided by frames per hryvnia, VRAM, and noise,
and **not** by the NVIDIA software ecosystem.

## The characteristics that matter, and how to read them

Ordered by how much each one decides the purchase. Rows 1-3 pick the card; the rest are fit
and taste.

| # | Spec (unit) | What it means, plainly | What it is here |
|---|---|---|---|
| 1 | **VRAM capacity (GB)** | Memory for textures and buffers. Running out does not gently lower the frame rate - it produces **stutter and frame-time spikes**, and it is the single thing that ages a card. | **16GB is the target** for a build meant to last past 2027. 12GB is today's floor and already exceeded by max texture settings. **This is my criterion, not a requirement Dmytro stated** - the RTX 5070 (12GB) remains on his agreed shortlist and is argued against on price/performance instead: the RX 9070 is 9.4% faster with 16GB for ~4 000 less. |
| 2 | **Raster performance at 1440p (relative %)** | Conventional rendering: ~90% of your frames. Reviewers publish it as a percentage against other cards at a given resolution. | Read charts **at 1440p only.** 1080p charts are CPU-limited and 4K charts are bandwidth-limited; neither describes your machine. The 9070 XT and the RTX 5070 Ti sit at parity here. |
| 3 | **Measured noise (dB(A)), per model** | Every 9070 XT has the same chip - **the cooler is the entire difference between models**, and it is the part you live with daily. | Hellhound **29.0 dB(A)** silent BIOS (ComputerBase, 30cm); Sapphire PULSE 25.5 dBA (TPU, 50cm); ASUS TUF OC 30.4 / 26.6 quiet (TPU). **Never compare across labs** - only inside one outlet's table. |
| 4 | **Power connector type** | 2x 8-pin PCIe, or the single 12V-2x6. The latter has a documented burn history on some cards. | The Hellhound uses **2x 8-pin and has no 12V-2x6 at all**. That is a real safety margin, not a spec-sheet nicety. |
| 5 | **Board power (TBP, watts)** | Heat produced, and how the PSU is sized. Cards also spike far above this for microseconds. | 9070 XT ~304W (Hellhound 310W) -> an 850W ATX 3.1 unit, see [psu.md](psu.md). |
| 6 | **Upscaling (FSR 4 / DLSS 4)** | Render at a lower resolution, reconstruct with AI. Extends a card's useful life more than any other feature. | FSR 4 closed most of the gap and is RDNA 4-only. Still **softer than DLSS 4**, with a measured frame-pacing defect in frame generation. Second-order at 1440p; read the evidence section before dismissing it. |
| 7 | **Ray tracing performance** | A separate hardware path, measured separately. NVIDIA is meaningfully ahead in heavy RT titles. | Matters only for RT-on AAA of the Cyberpunk / Alan Wake 2 class. Not your stated use. |
| 8 | **Media encoder** | Fixed-function H.264 / HEVC / **AV1** for streaming and video export. | RDNA 4's AV1 encoder is fine for Twitch or YouTube at 1440p. Not a reason to buy NVIDIA for rare amateur streaming. |
| 9 | **Length (mm) and slot width** | Whether it physically fits. | 9070 XT models are 280-350mm; the Hellhound is **327mm, 2.5 slots**. Every case in [case.md](case.md) clears it. |

**Ignore:** shader counts compared across brands (4 096 AMD shaders and 8 960 NVIDIA CUDA
cores are different units), TFLOPS figures, and a partner model's factory OC - it is worth
1-2% and the cooler is worth far more.

## Specifications

| | **RX 9070 XT** | RX 9070 | RX 9060 XT | RTX 5070 Ti | RTX 5070 |
|---|---|---|---|---|---|
| Architecture | RDNA 4 (Navi 48) | RDNA 4 (Navi 48) | RDNA 4 (Navi 44) | Blackwell (GB203) | Blackwell (GB205) |
| Shaders | **4 096** (64 CU) | 3 584 (56 CU) | 2 048 (32 CU) | 8 960 CUDA | 6 144 CUDA |
| Game / boost clock | 2 400 / **2 970 MHz** | 2 070 / 2 540 MHz | - | - / 2 452 MHz | - / 2 512 MHz |
| **VRAM** | **16GB GDDR6** | 16GB GDDR6 | 16GB GDDR6 | 16GB GDDR7 | **12GB** GDDR7 |
| Memory bus | 256-bit | 256-bit | 128-bit | 256-bit | 192-bit |
| Bandwidth | 640 GB/s | 640 GB/s | 320 GB/s | 896 GB/s | 672 GB/s |
| Board power | **304W** | 220W | 160W | 300W | 250W |
| Interface | PCIe 5.0 x16 | PCIe 5.0 x16 | PCIe 5.0 x16 | PCIe 5.0 x16 | PCIe 5.0 x16 |

Shader counts do **not** compare across brands - 4 096 AMD shaders and 8 960 NVIDIA CUDA
cores are different units of account. The 9070 XT and the 5070 Ti land at raster parity at
1440p despite the gap on paper. What *does* compare across brands is the VRAM row, and it is
the reason the RTX 5070 is rejected here: 12GB on a card meant to last past 2027.

### The card actually chosen

| PowerColor RX 9070 XT Hellhound | |
|---|---|
| Power connectors | **2x 8-pin PCIe** - no 12V-2x6, which is the connector with the burn history |
| Board power | 310W (slightly above the 304W reference) |
| Length x height x thickness | **327 x 128 x 49mm** (340mm with the bracket), 2.5 slots |
| Weight | 1 180g - the lightest of the group, so least sag |
| Cooling | Triple fan, ball-bearing, **PTM7950** phase-change compound, dual BIOS |
| Measured noise | **29.0 dB(A)** on the silent BIOS at 30cm (ComputerBase) |
| Display outputs | 3x DisplayPort 2.1a + 1x HDMI 2.1b |
| Fit | 327mm needs a case with 340mm+ clearance; the Lancool 216 takes 392mm |

## Price and availability collapse in the XT tier, 2026-09-11

**The Max build's card, as priced, no longer exists to buy.** Checked because the Hellhound-vs-
Red Devil question was open; what came back was bigger than the question.

| Card | What the docs said | What is true on 2026-09-11 |
|---|---:|---|
| **9070 GRE Hellhound** | 32 249 Telemart | **32 179, in stock** - unchanged (-70) |
| **9070 XT Hellhound** (merit pick) | 41 800 | **~47 500**. ek.ua shows **two shops** - Timesport 47 502, Rozetka 48 449 - **neither of which assembles**. Telemart carries only the **Spectral White at 47 665** |
| **9070 XT Red Devil** (what was quoted) | 42 805 Telemart, 5% promo | **Out of stock at Telemart.** The only other listing found is **54 269**, one shop |

**Lean and Working are untouched.** Their card did not move. This is an XT-tier event only.

**Cause, and it is not noise.** AMD notified board partners of a **~10% wholesale increase on
GPU+memory from July 2026 - the third increase of 2026** - driven by the same DRAM shortage this
project already documented. The direction is up, which is the answer this project already gave
to "should I wait".

### The cheapest *new* 9070 XT from a store that can assemble

| Store | Card | UAH |
|---|---|---:|
| **Brain** | ASUS **PRIME RX 9070 XT OC** | **45 499** |
| Telemart | Gigabyte GAMING OC | 46 709 |
| Telemart | ASUS PRIME OC | 47 187 |
| Telemart | PowerColor Hellhound **Spectral White** | 47 665 |
| Telemart | ASUS TUF Gaming OC | 48 707 |

**Reject Telemart's ASUS PRIME White OC at 36 999.** It is listed **"Factory Recertified"** -
refurbished. The standing requirement is new parts with official warranty, and this is the
cheapest listing in the tier precisely because it is not one. It will keep surfacing in price
comparisons; it is not a candidate.

### What this does to the Max build

| | Working | Max, as documented | Max, cheapest new XT at Brain |
|---|---:|---:|---:|
| GPU | 32 179 | 42 805 | **45 499** |
| **Build total** | **116 800** | 127 400 | **130 094** |
| Premium over Working | - | +10 600 | **+13 320** |

**Max no longer fits the 130 000 range** - narrowly at Brain, by more anywhere else - and the
step up from Working has grown by a quarter while buying exactly the same performance. The
Max build was already the weakest-value tier in the ladder; this makes that explicit rather
than changing it.

**The Hellhound-vs-Red Devil question is moot as posed.** Neither is obtainable at its
documented price from a store that can assemble the machine. If Max survives at all, the card
has to be re-picked from what Brain and Telemart actually stock, and **none of those candidates
has been assessed against this document's criteria** - the ASUS PRIME in particular has no
measured noise figure here.

## Re-opening the field, 2026-09-11 - the RX 9070 non-XT is back

Fair challenge from Dmytro: the ladder had narrowed to three cards. It was re-opened at current
Ukrainian prices, and the narrowing turns out to have been an artefact of prices that no longer
hold.

### The measured gaps, corrected

| Comparison | Figure | Source |
|---|---|---|
| 9070 **non-XT** over **GRE**, 1440p | **+18%** | TechSpot, 9070 GRE review |
| 9070 **XT** over **non-XT**, 1440p | **+11-13%** | multiple, incl. GamersNexus |
| 9070 **XT** over **GRE**, 1440p | **~+32%** | the two above, compounded |

**This document said the XT was "~25-30%" over the GRE. That understates it; ~32% is closer.**
TechSpot is blunter still about the GRE: it is **11% slower at 1440p than the 7900 GRE it
replaces**, and they call it "an awkward addition to the lineup".

**That verdict does not transfer to Ukraine unchanged, and it matters that it does not.**
TechSpot's complaint is that at US prices the GRE saves "less than 10%" against the 9070. Here
the gap is **32 179 against 39 999 - 24%**. The GRE is far better positioned in this market than
in the one TechSpot reviewed. It stays in Lean and Working on that basis.

### But the 12GB inconsistency has to be said out loud

This document rejects the RTX 5070 with the words: *12GB "on a card meant to last past 2027"*.
**The GRE is also a 12GB card**, and it sits in two of the three builds. Both things cannot be
true. The honest position: 12GB is adequate at 1440p today and the GRE is priced accordingly
here, but **16GB is the single most future-proof thing available in this price band**, and the
RX 9070 non-XT is where it starts.

### Why the non-XT was excluded, and why that reason is gone

The exclusion was explicit: *"At 39 999 against the XT's 42 805 it is dominated - 2 806 less for
a clearly slower card."* **That was true, and it is no longer true.** The XT's real price from a
store that can assemble is now **45 499**, so the gap is **5 500, not 2 806** - and the non-XT
has not moved.

### The field at current prices, from stores that actually assemble

| Card | VRAM | Store | UAH | vs GRE | Notes |
|---|---|---|---:|---|---|
| **RX 9070 GRE Hellhound** | 12GB | Telemart, in stock | **32 179** | baseline | 220W, 2x 8-pin |
| **RX 9070 Sapphire PURE** | **16GB** | Telemart, in stock | **39 999** | **+18%** | **220W, 2x 8-pin, no 12V-2x6** |
| RX 9070 ASUS PRIME OC EVO | 16GB | Brain | 39 999 | +18% | 2x 8-pin, fan-stop below 55C |
| RX 9070 XT ASUS PRIME OC | 16GB | Brain | 45 499 | ~+32% | **3x 8-pin**, 304W |
| RX 9070 XT Gigabyte GAMING OC | 16GB | Telemart, in stock | 46 709 | ~+32% | not assessed here |
| RTX 5060 Ti 16GB | 16GB | Brain | 38 999 | slower | below the GRE at 1440p |
| RTX 5070 | **12GB** | Brain | 46 919 | - | dearer than a 9070 XT, 12GB. No |
| RTX 5070 Ti | 16GB | Brain | 62 999 | - | +17 500 over the XT. Out of band |

**NVIDIA still offers nothing in this band** - re-checked at today's prices, not inherited from
the earlier pass. The 5070 is now *more expensive than a 9070 XT* while carrying 12GB.

**Reject both "Recertified" listings.** Telemart shows an ASUS PRIME XT White at 36 999
("Factory Recertified") and a Sapphire PURE 9070 at 36 999 ("Seller Recertified"). They are the
cheapest entries in their tiers because they are refurbished. New parts with official warranty
is a standing requirement.

### What this does to the ladder

The non-XT costs the same 220W and the same 2x 8-pin as the GRE, so **it changes no other part
of the build** - not the PSU, not the case, not the cooling.

| Max build option | GPU | Total | vs Working | Buys |
|---|---:|---:|---:|---|
| **A. RX 9070 non-XT 16GB** | 39 999 | **124 594** | **+7 794** | +18%, **16GB**, in budget |
| B. RX 9070 XT 16GB | 45 499 | 130 094 | +13 320 | ~+32%, 16GB, **94 over the range** |
| C. Drop Max | - | - | - | Working at 116 800 stands as the top build |

**Option A is the recommendation.** It restores the Max build to the budget, gives the 16GB
this document says matters, and costs 5 500 less than the XT for 11-13% less performance - the
same trade the XT was previously winning only because it was nearly free. The XT is now the one
paying a premium for the last tier of performance, which is exactly the position the non-XT was
rejected for holding.

**Still to check before buying Option A:** the Sapphire PURE 9070 and ASUS PRIME 9070 EVO have
**no measured noise figure in this document**. That is the same gap that got the ASRock
Challenger and PowerColor Reaper marked "unknown" here, and it should be closed the same way.

## NVIDIA re-checked properly, 2026-09-11 - and it is not close

Asked for directly. Every NVIDIA card in or near the band, at today's Ukrainian prices from
stores that can assemble:

| Card | VRAM | Cheapest **new** | vs RX 9070 at 39 999 |
|---|---|---:|---|
| RTX 5060 Ti 16GB | 16GB | 38 999 (Brain) | Slower than the **GRE** at 1440p. No |
| **RTX 5070** | **12GB** | **42 999** (ASUS Dual OC, Telemart) | **3 000 dearer.** Slower in raster, **tied in ray tracing, and 40% faster in path tracing** - see the corrected section below. And 12GB |
| RTX 5070 Ti | 16GB | 59 999 (Gigabyte GAMING OC, Telemart) | **+20 000.** Out of the band entirely |

**Correction, 2026-09-11: "comprehensively dominated" was too strong, and the earlier "8-13%
slower" was a raster figure quoted without saying so.** Both are fixed in the section below.
The RTX 5070 loses on raster-per-hryvnia and on VRAM. It does **not** lose across the board.

**Do not wait for the SUPER refresh.** The RTX 50 SUPER series (RTX 5070 SUPER 18GB, 5070 Ti
SUPER 24GB) has been **delayed indefinitely** - partners were informed, and current expectation
is late 2026 or CES 2027, gated on the same memory shortage driving prices up. There is no
near-term NVIDIA card that changes this table.

**What NVIDIA does buy** is DLSS 4, better heavy ray tracing and CUDA. CUDA is explicitly not
needed here, ray tracing is not the stated use, and neither is worth paying more for a slower
card with less VRAM.

## Corrected: RTX 5070 vs RX 9070, properly sourced (2026-09-11)

Dmytro challenged the "8-13% slower" figure. He was right to. It came from a search summary,
it was a **raster-only** number presented without that qualification, and the surrounding claim
of "comprehensively dominated" was not supportable. Verified below against four primary sources
plus a video review he supplied.

### Rasterisation at 1440p - the spread is wider than one figure suggests

| Source | Suite | RX 9070 over RTX 5070 |
|---|---|---|
| Tom's Hardware | non-RT geomean | **+3-6%** |
| Digital Foundry | aggregate | +8-10% |
| TechSpot | 23 games | +13% |
| **GECID.com** | 20+ games, 1440p, Ukrainian retail cards | **"about 10-20% in most modern projects"** |

**The honest figure is "roughly 5-15% in raster, depending on the suite", not a crisp 8-13%.**
Every source puts the 9070 ahead; they disagree on by how much.

### Ray tracing - where the earlier claim was simply incomplete

| Workload | Result |
|---|---|
| **Standard ray tracing, 1440p** | **Essentially tied** - Tom's Hardware 15-game RT geomean gives the 9070 **+0.23%** |
| **Path tracing** (Cyberpunk 2077) | **RTX 5070 +40%** |

Three of the four videos Dmytro supplied are ray-tracing comparisons, which is precisely the
workload where the gap closes or reverses. **That is the part the earlier table got wrong by
omission.**

### The GECID review - the most relevant single source found

[GECID.com, 2026-06-22](https://www.youtube.com/watch?v=cUSxa4PxI4I), 30 minutes, 1440p. It is
the most applicable test located because it compares **the exact two cards sold here** - ASUS
Prime RTX 5070 OC and ASUS Prime RX 9070 EVO OC, same cooler family, same 2.5 slots, ~30cm.
Choosing two cards from **one series** is deliberate and good method: it isolates the GPUs from
the board partners, which the Jegs TV comparison (Sapphire Pulse against Palit Infinity 3) does
not do.

> **Conflict of interest, recorded 2026-09-13 after reading the transcript in full.** This is not
> only a card loan. The video runs a **paid Telemart promotion with a live discount code** -
> *"до 5 липня за промокодом GESID 500 ви можете отримати додаткову знижку у 500 грн на всі
> відеоприскорювачі **від ASUS**"* - and the two cards under test are ASUS. **Telemart is one of
> the two stores that would assemble this build**, and this review is the single source this
> document leans on hardest.
>
> Weigh it, do not discard it. All **fourteen** of its claims were checked line by line against
> the transcript in [../source_audit.md](../source_audit.md) and every one is verbatim accurate,
> and its conclusion is genuinely balanced - it ends by recommending the **RTX 5070** for buyers
> who want no compatibility surprises, which is not what a bought review does.

Its verdict, in full rather than the convenient half:

- **Raster: the RX 9070 wins**, "about 10-20% ahead in most modern projects". Specific margins
  cited: Death Stranding 2 **+16%**, Stalker 2 **+13%**, Resident Evil Requiem **+20 FPS**,
  Assassin's Creed Shadows 64 FPS against under 60, Battlefield 6 90+ FPS with the 5070 dropping
  below 60 in heavy firefights.
- **The RTX 5070 wins outright in several titles** - The Long Dark by **~80 FPS**, plus GTA 5,
  Dying Light: The Beast and The Witcher 3.
- **12GB is already the limit.** In Cyberpunk RT Ultra and RE Requiem the 5070's memory is
  "filled to the brim", and GECID attributes part of the 9070's 20 FPS lead to that.
- **AMD's software cost is real and was not in this document.** Doom: The Dark Ages **would not
  launch on the current AMD driver**; Pragmata and RE Requiem **cannot enable path tracing at
  all** on the 9070; Subnautica 2 has no FSR support; The Witcher 3 offers only FSR 2. NVIDIA
  has Ray Reconstruction, more mature DLSS, and broader engine support.
- Its closing line is a genuine split: **RX 9070 for performance-per-money, VRAM and a future 4K
  panel; RTX 5070 to "enable everything and not worry about compatibility or driver nuances".**

**The other three videos have now been read** - see below. They are commentary-free benchmark
videos whose numbers live in on-screen graphs, so `code/yt_transcript.py` returns nothing. That
gap is now closed by **`code/yt_frames.py`**, which pulls stills at given timestamps so the charts
can be read directly.

### The benchmark videos, read from their frames (2026-09-11)

Written after building `code/yt_frames.py`. Figures below are read off the videos' own charts
and overlays, not from narration or summaries.

**BENCHMARKS FOR GAMERS, 13 games, 1440p, DLSS 4.5 / FSR 4.1 Quality** ([`2ufCzwK73GM`](https://www.youtube.com/watch?v=2ufCzwK73GM), 2026-05-22; average chart @ 10:38, **re-verified 2026-09-13**) - its closing average
chart states plainly: **"13% faster on average at 1440p"**, in the RX 9070's favour. Per-game
percentage difference, 9070 over 5070:

| Game | Δ | | Game | Δ |
|---|---:|---|---|---:|
| Forza Horizon 6 (RT) | **+25%** | | Marvel's Spider-Man 2 (RT) | +13% |
| Pragmata (RT) | +24% | | Stalker 2 | +12% |
| Resident Evil Requiem (RT) | +20% | | Silent Hill f | +12% |
| Mafia: The Old Country | +20% | | Crimson Desert (RT) | +4% |
| Clair Obscur: Expedition 33 | +19% | | Kingdom Come: Deliverance II | +3% |
| Borderlands 4 | +16% | | Cyberpunk 2077 (RT) | +1% |
| | | | ARC Raiders (RT) | **-6%** |

Direction confirmed from the raw overlay rather than assumed - Forza Horizon 6 RT at 1440p:
**RTX 5070 73.8 avg / 65.3 1% low against RX 9070 92.4 avg / 81.2 1% low.** The same frame shows
the 5070 at **11 230 MB of its 12 288 MB** in use - the VRAM ceiling, visible in a still.

**Jegs TV, Cyberpunk 2077, 1440p, RT Overdrive preset, frame generation off** (cards: **Sapphire Pulse RX 9070** against **Palit RTX 5070 Infinity 3** - near-reference designs, not the OC cards GECID used)
([`hIZj4MOk6fo`](https://www.youtube.com/watch?v=hIZj4MOk6fo), 2026-07-16; Cyberpunk 2077 QHD chapter @ 14:50) - the
path-tracing case: **RTX 5070 59 avg / 49 1% low against RX 9070 45 avg / 37 1% low. NVIDIA +31%
on the average and +32% on the 1% low.**

> **Corrected 2026-09-13.** This line previously read "45 avg / **41** 1% low". The overlay at
> 15:10 reads **37**. The 41 could not be reproduced at any frame checked, and the original entry
> recorded no timestamp, so it cannot be traced. The average, the preset and the +31% are all
> confirmed exactly; only the 9070's 1% low was wrong, and it was wrong **in the 9070's favour** -
> the real 1% low deficit is 32%, not 20%.

**Testing Games, Cyberpunk 2077 RT with upscaling, 2160p**
([`4UqYr3nAj90`](https://www.youtube.com/watch?v=4UqYr3nAj90), 2026-03-09; chapter @ 3:59, **re-verified
2026-09-13**) - RX 9070 39, RTX 5070 38, RX 9070 XT 48, RTX 5070 Ti 52. A tie at the 9070/5070 tier; the 5070 Ti takes the XT tier by 8%.

### This refines the ray-tracing claim again

The "standard ray tracing is a tie" line above came from Tom's Hardware's 15-game geomean. The
measured 2026 suite disagrees: **with upscaling on and current drivers, the RX 9070 leads by 13%
across a mostly ray-traced set**, losing only ARC Raiders. The consistent picture across every
source now checked:

| Workload | Winner |
|---|---|
| Raster, 1440p | **RX 9070**, +3-15% depending on suite |
| Ray tracing with upscaling, 1440p | **RX 9070**, ~+13% on a current 13-game set (tie on older geomeans) |
| **Path tracing / RT Overdrive** | **RTX 5070, +31 to +40%** - the one clear NVIDIA win |
| VRAM headroom | **RX 9070** - the 5070 is measurably at its 12GB ceiling |

### The site that says the opposite, and why it does

Dmytro raised [technical.city](https://technical.city/en/gpu/GeForce-RTX-5070-vs-Radeon-RX-9070),
which recommends the **RTX 5070 as 12.9% faster**. It is worth answering properly rather than
waving away, because it is the only source found that reverses the conclusion.

**Its six synthetic scores disagree with each other:**

| Test | Winner |
|---|---|
| 3DMark 11 | **RX 9070 +23.7%** |
| 3DMark Fire Strike | RX 9070 +4.5% |
| 3DMark Vantage | RX 9070 +1.9% |
| Passmark | RTX 5070 +12.9% |
| 3DMark Ice Storm | RTX 5070 +16.7% |
| 3DMark Cloud Gate | RTX 5070 +24.2% |

Three each way, across a **48-point spread on the same two cards**. That is not a measurement
being aggregated, it is noise. And **Cloud Gate, Ice Storm and Vantage are DX9/DX10 tests from
2008-2013** - Ice Storm was built to benchmark phones. They cannot say anything meaningful about
RDNA4 against Blackwell.

**Its game sample is the real problem.** The "1440p" figure rests on **six titles: Counter-Strike
2, CS:GO, Valorant, GTA V, Metro Exodus and Battlefield 5.** Three are esports games that run
CPU-bound at hundreds of frames per second - a workload where NVIDIA's lower driver overhead
genuinely does win, and where the GPU is barely the limit. **Nothing in the set is newer than
2023.**

Set against the 13-game 2026 suite read from frames above - Forza Horizon 6, Pragmata, Resident
Evil Requiem, Borderlands 4, Silent Hill f, Stalker 2, Crimson Desert, Clair Obscur, ARC Raiders,
Mafia - these are not contradictory findings. **They are answers to different questions.**
technical.city measures legacy and esports throughput; this build is specified for **modern AAA
at 1440p**, and Dmytro's stated requirement is explicitly *"high FPS, not competitive"* - so even
the workload technical.city measures well is the one he said does not matter.

**The weight of controlled testing is not close:** TechSpot, Tom's Hardware, GamersNexus, Digital
Foundry, GECID and the frame-read suite all put the RX 9070 ahead in modern raster. One spec
aggregator with self-contradicting synthetics does not move that. It is now in
[../tools.md](../tools.md)'s distrust list with this worked example.

### Does the recommendation change? No - but the reason is narrower

**The RX 9070 remains the pick for this machine**, on the requirements as agreed:

- The stated use is **1440p, high FPS, not competitive**, work first. **Ray tracing and path
  tracing are nowhere in the requirements**, and CUDA is explicitly not needed. Raster and VRAM
  are what this build is buying.
- It is **3 000 cheaper** (39 999 against 42 999) while winning the workload that matters here.
- **16GB against 12GB**, on a machine meant to last past 2027 - the same test this document
  already applied when rejecting the 5070 the first time.

**What must be said alongside it:** if path tracing or guaranteed day-one technology support
ever became a priority, the 5070 would be the better card despite costing more and having less
memory. On this requirements list, it is not.

## The Hellhound trap, a second time

The PowerColor **Hellhound RX 9070 non-XT** looks like the ideal card: **35 999**, and it uses
the exact cooler this document already vetted on the GRE and XT - 29.0 dB(A) on the silent BIOS,
PTM7950, ball-bearing fans, dual BIOS, 0.47% RMA across 4 340+ units, 2x 8-pin.

**It is not buyable from a store that can assemble the machine.** Eight shops list it -
cthp 35 999, luckylink 36 561, smartmag 37 046, openshop 37 236, kvshop 38 377, mta 39 699,
Rozetka 40 218 - and **Telemart and Brain are not among them**, exactly as with the Hellhound XT.

**PowerColor's Hellhound 9070 and 9070 XT SKUs have thinned out of the two assembling
retailers.** The GRE Hellhound is still stocked at Telemart at 32 179, so the brand has not
vanished - these two SKUs have. Any plan built on a Hellhound 9070 or 9070 XT price is a plan
that ends at a shop which cannot build or warrant the machine.

**So from an assembling store the RX 9070 costs 39 999 either way:** Sapphire PURE at Telemart
(in stock) or ASUS PRIME OC EVO at Brain.

## Closed: the RX 9070 noise figures, measured (2026-09-11)

The open item is settled. **ComputerBase ran a dedicated RX 9070 non-XT custom-design roundup**
that includes the card Telemart stocks. Measured under gaming load, after 30 minutes:

| Card | BIOS | **dB(A)** | Fan RPM |
|---|---|---:|---:|
| Sapphire Pulse | default | **28.0** | 1 065 |
| Asus TUF Gaming | Quiet | **28.0** | <700 |
| PowerColor Hellhound | Silent | **28.0** | <700 |
| **Sapphire PURE** (Telemart, 39 999) | default | **29.0** | 1 081 |
| PowerColor Hellhound | OC | 29.0 | - |
| Asus TUF Gaming | Performance | 30.0 | 1 001 |
| PowerColor Reaper | default | 32.5 | 1 165 |
| XFX Quicksilver | both | **36.0** | 1 190 |

**The Sapphire PURE measures 29.0 dB(A)** - identical to the PowerColor Hellhound on its OC BIOS,
and within 1 dB of the three quietest cards tested. For scale, the **Hellhound XT this document
chose on acoustics measures 29.0 dB(A)** on its silent BIOS. The buyable card is not a compromise
on the axis this project cares most about.

ComputerBase's summary: the TUF, Hellhound, Pulse and Pure are *"extremely to nearly inaudible"*;
only the XFX Quicksilver "steps out of line", and even it "is anything but loud". Their own line
is that **"gamers make no technical mistake with any of the tested custom designs"** bar the XFX.

**So the Telemart option is verified and the Brain option is not.** The ASUS **PRIME** OC EVO was
not in this roundup - ComputerBase tested the **TUF**, a tier above it, and reviewers of the PRIME
*XT* called it louder than its peers. **Prefer the Sapphire PURE at Telemart.** If the build goes
to Brain instead, the PRIME EVO remains unmeasured and is a small, known risk rather than an
unknown one.

### One figure this corrects elsewhere

ComputerBase measured the **Sapphire PURE at 247W**, the highest of the non-XT group - it carries
a larger factory overclock than the 220W TBP suggests. **This does not change the PSU**: Max with
this card is 247 + 88 + 65 = **400W, 53% of the 750W unit**, comfortably inside the band in
[psu.md](psu.md). Worth carrying into the acceptance sheet so a 220W figure is not quoted as if
measured.

## Corrected: RTX 5070 vs RX 9070, properly sourced (2026-09-11)

Dmytro challenged the "8-13% slower" figure. He was right to. It came from a search summary,
it was a **raster-only** number presented without that qualification, and the surrounding claim
of "comprehensively dominated" was not supportable. Verified below against four primary sources
plus a video review he supplied.

### Rasterisation at 1440p - the spread is wider than one figure suggests

| Source | Suite | RX 9070 over RTX 5070 |
|---|---|---|
| Tom's Hardware | non-RT geomean | **+3-6%** |
| Digital Foundry | aggregate | +8-10% |
| TechSpot | 23 games | +13% |
| **GECID.com** | 20+ games, 1440p, Ukrainian retail cards | **"about 10-20% in most modern projects"** |

**The honest figure is "roughly 5-15% in raster, depending on the suite", not a crisp 8-13%.**
Every source puts the 9070 ahead; they disagree on by how much.

### Ray tracing - where the earlier claim was simply incomplete

| Workload | Result |
|---|---|
| **Standard ray tracing, 1440p** | **Essentially tied** - Tom's Hardware 15-game RT geomean gives the 9070 **+0.23%** |
| **Path tracing** (Cyberpunk 2077) | **RTX 5070 +40%** |

Three of the four videos Dmytro supplied are ray-tracing comparisons, which is precisely the
workload where the gap closes or reverses. **That is the part the earlier table got wrong by
omission.**

### The GECID review - the most relevant single source found

[GECID.com, 2026-06-22](https://www.youtube.com/watch?v=cUSxa4PxI4I), 30 minutes, 1440p. It is
the most applicable test located because it compares **the exact two cards sold here** - ASUS
Prime RTX 5070 OC and ASUS Prime RX 9070 EVO OC, same cooler family, same 2.5 slots, ~30cm.
Choosing two cards from **one series** is deliberate and good method: it isolates the GPUs from
the board partners, which the Jegs TV comparison (Sapphire Pulse against Palit Infinity 3) does
not do.

> **Conflict of interest, recorded 2026-09-13 after reading the transcript in full.** This is not
> only a card loan. The video runs a **paid Telemart promotion with a live discount code** -
> *"до 5 липня за промокодом GESID 500 ви можете отримати додаткову знижку у 500 грн на всі
> відеоприскорювачі **від ASUS**"* - and the two cards under test are ASUS. **Telemart is one of
> the two stores that would assemble this build**, and this review is the single source this
> document leans on hardest.
>
> Weigh it, do not discard it. All **fourteen** of its claims were checked line by line against
> the transcript in [../source_audit.md](../source_audit.md) and every one is verbatim accurate,
> and its conclusion is genuinely balanced - it ends by recommending the **RTX 5070** for buyers
> who want no compatibility surprises, which is not what a bought review does.

Its verdict, in full rather than the convenient half:

- **Raster: the RX 9070 wins**, "about 10-20% ahead in most modern projects". Specific margins
  cited: Death Stranding 2 **+16%**, Stalker 2 **+13%**, Resident Evil Requiem **+20 FPS**,
  Assassin's Creed Shadows 64 FPS against under 60, Battlefield 6 90+ FPS with the 5070 dropping
  below 60 in heavy firefights.
- **The RTX 5070 wins outright in several titles** - The Long Dark by **~80 FPS**, plus GTA 5,
  Dying Light: The Beast and The Witcher 3.
- **12GB is already the limit.** In Cyberpunk RT Ultra and RE Requiem the 5070's memory is
  "filled to the brim", and GECID attributes part of the 9070's 20 FPS lead to that.
- **AMD's software cost is real and was not in this document.** Doom: The Dark Ages **would not
  launch on the current AMD driver**; Pragmata and RE Requiem **cannot enable path tracing at
  all** on the 9070; Subnautica 2 has no FSR support; The Witcher 3 offers only FSR 2. NVIDIA
  has Ray Reconstruction, more mature DLSS, and broader engine support.
- Its closing line is a genuine split: **RX 9070 for performance-per-money, VRAM and a future 4K
  panel; RTX 5070 to "enable everything and not worry about compatibility or driver nuances".**

**The other three videos have now been read** - see below. They are commentary-free benchmark
videos whose numbers live in on-screen graphs, so `code/yt_transcript.py` returns nothing. That
gap is now closed by **`code/yt_frames.py`**, which pulls stills at given timestamps so the charts
can be read directly.

### The benchmark videos, read from their frames (2026-09-11)

Written after building `code/yt_frames.py`. Figures below are read off the videos' own charts
and overlays, not from narration or summaries.

**BENCHMARKS FOR GAMERS, 13 games, 1440p, DLSS 4.5 / FSR 4.1 Quality** ([`2ufCzwK73GM`](https://www.youtube.com/watch?v=2ufCzwK73GM), 2026-05-22; average chart @ 10:38, **re-verified 2026-09-13**) - its closing average
chart states plainly: **"13% faster on average at 1440p"**, in the RX 9070's favour. Per-game
percentage difference, 9070 over 5070:

| Game | Δ | | Game | Δ |
|---|---:|---|---|---:|
| Forza Horizon 6 (RT) | **+25%** | | Marvel's Spider-Man 2 (RT) | +13% |
| Pragmata (RT) | +24% | | Stalker 2 | +12% |
| Resident Evil Requiem (RT) | +20% | | Silent Hill f | +12% |
| Mafia: The Old Country | +20% | | Crimson Desert (RT) | +4% |
| Clair Obscur: Expedition 33 | +19% | | Kingdom Come: Deliverance II | +3% |
| Borderlands 4 | +16% | | Cyberpunk 2077 (RT) | +1% |
| | | | ARC Raiders (RT) | **-6%** |

Direction confirmed from the raw overlay rather than assumed - Forza Horizon 6 RT at 1440p:
**RTX 5070 73.8 avg / 65.3 1% low against RX 9070 92.4 avg / 81.2 1% low.** The same frame shows
the 5070 at **11 230 MB of its 12 288 MB** in use - the VRAM ceiling, visible in a still.

**Jegs TV, Cyberpunk 2077, 1440p, RT Overdrive preset, frame generation off** (cards: **Sapphire Pulse RX 9070** against **Palit RTX 5070 Infinity 3** - near-reference designs, not the OC cards GECID used)
([`hIZj4MOk6fo`](https://www.youtube.com/watch?v=hIZj4MOk6fo), 2026-07-16; Cyberpunk 2077 QHD chapter @ 14:50) - the
path-tracing case: **RTX 5070 59 avg / 49 1% low against RX 9070 45 avg / 37 1% low. NVIDIA +31%
on the average and +32% on the 1% low.**

> **Corrected 2026-09-13.** This line previously read "45 avg / **41** 1% low". The overlay at
> 15:10 reads **37**. The 41 could not be reproduced at any frame checked, and the original entry
> recorded no timestamp, so it cannot be traced. The average, the preset and the +31% are all
> confirmed exactly; only the 9070's 1% low was wrong, and it was wrong **in the 9070's favour** -
> the real 1% low deficit is 32%, not 20%.

**Testing Games, Cyberpunk 2077 RT with upscaling, 2160p**
([`4UqYr3nAj90`](https://www.youtube.com/watch?v=4UqYr3nAj90), 2026-03-09; chapter @ 3:59, **re-verified
2026-09-13**) - RX 9070 39, RTX 5070 38, RX 9070 XT 48, RTX 5070 Ti 52. A tie at the 9070/5070 tier; the 5070 Ti takes the XT tier by 8%.

### This refines the ray-tracing claim again

The "standard ray tracing is a tie" line above came from Tom's Hardware's 15-game geomean. The
measured 2026 suite disagrees: **with upscaling on and current drivers, the RX 9070 leads by 13%
across a mostly ray-traced set**, losing only ARC Raiders. The consistent picture across every
source now checked:

| Workload | Winner |
|---|---|
| Raster, 1440p | **RX 9070**, +3-15% depending on suite |
| Ray tracing with upscaling, 1440p | **RX 9070**, ~+13% on a current 13-game set (tie on older geomeans) |
| **Path tracing / RT Overdrive** | **RTX 5070, +31 to +40%** - the one clear NVIDIA win |
| VRAM headroom | **RX 9070** - the 5070 is measurably at its 12GB ceiling |

### The site that says the opposite, and why it does

Dmytro raised [technical.city](https://technical.city/en/gpu/GeForce-RTX-5070-vs-Radeon-RX-9070),
which recommends the **RTX 5070 as 12.9% faster**. It is worth answering properly rather than
waving away, because it is the only source found that reverses the conclusion.

**Its six synthetic scores disagree with each other:**

| Test | Winner |
|---|---|
| 3DMark 11 | **RX 9070 +23.7%** |
| 3DMark Fire Strike | RX 9070 +4.5% |
| 3DMark Vantage | RX 9070 +1.9% |
| Passmark | RTX 5070 +12.9% |
| 3DMark Ice Storm | RTX 5070 +16.7% |
| 3DMark Cloud Gate | RTX 5070 +24.2% |

Three each way, across a **48-point spread on the same two cards**. That is not a measurement
being aggregated, it is noise. And **Cloud Gate, Ice Storm and Vantage are DX9/DX10 tests from
2008-2013** - Ice Storm was built to benchmark phones. They cannot say anything meaningful about
RDNA4 against Blackwell.

**Its game sample is the real problem.** The "1440p" figure rests on **six titles: Counter-Strike
2, CS:GO, Valorant, GTA V, Metro Exodus and Battlefield 5.** Three are esports games that run
CPU-bound at hundreds of frames per second - a workload where NVIDIA's lower driver overhead
genuinely does win, and where the GPU is barely the limit. **Nothing in the set is newer than
2023.**

Set against the 13-game 2026 suite read from frames above - Forza Horizon 6, Pragmata, Resident
Evil Requiem, Borderlands 4, Silent Hill f, Stalker 2, Crimson Desert, Clair Obscur, ARC Raiders,
Mafia - these are not contradictory findings. **They are answers to different questions.**
technical.city measures legacy and esports throughput; this build is specified for **modern AAA
at 1440p**, and Dmytro's stated requirement is explicitly *"high FPS, not competitive"* - so even
the workload technical.city measures well is the one he said does not matter.

**The weight of controlled testing is not close:** TechSpot, Tom's Hardware, GamersNexus, Digital
Foundry, GECID and the frame-read suite all put the RX 9070 ahead in modern raster. One spec
aggregator with self-contradicting synthetics does not move that. It is now in
[../tools.md](../tools.md)'s distrust list with this worked example.

### Does the recommendation change? No - but the reason is narrower

**The RX 9070 remains the pick for this machine**, on the requirements as agreed:

- The stated use is **1440p, high FPS, not competitive**, work first. **Ray tracing and path
  tracing are nowhere in the requirements**, and CUDA is explicitly not needed. Raster and VRAM
  are what this build is buying.
- It is **3 000 cheaper** (39 999 against 42 999) while winning the workload that matters here.
- **16GB against 12GB**, on a machine meant to last past 2027 - the same test this document
  already applied when rejecting the 5070 the first time.

**What must be said alongside it:** if path tracing or guaranteed day-one technology support
ever became a priority, the 5070 would be the better card despite costing more and having less
memory. On this requirements list, it is not.

## The Hellhound trap, a second time

The PowerColor **Hellhound RX 9070 non-XT** looks like the ideal card: **35 999**, and it uses
the exact cooler this document already vetted on the GRE and XT - 29.0 dB(A) on the silent BIOS,
PTM7950, ball-bearing fans, dual BIOS, 0.47% RMA across 4 340+ units, 2x 8-pin.

**It is not buyable from a store that can assemble the machine.** Eight shops list it -
cthp 35 999, luckylink 36 561, smartmag 37 046, openshop 37 236, kvshop 38 377, mta 39 699,
Rozetka 40 218 - and **Telemart and Brain are not among them**, exactly as with the Hellhound XT.

**PowerColor's Hellhound 9070 and 9070 XT SKUs have thinned out of the two assembling
retailers.** The GRE Hellhound is still stocked at Telemart at 32 179, so the brand has not
vanished - these two SKUs have. Any plan built on a Hellhound 9070 or 9070 XT price is a plan
that ends at a shop which cannot build or warrant the machine.

**So from an assembling store the RX 9070 costs 39 999 either way:** Sapphire PURE at Telemart
(in stock) or ASUS PRIME OC EVO at Brain.

## Open: neither buyable RX 9070 has a measured noise figure

This is the same standard that got the ASRock Challenger and PowerColor Reaper marked
"unknown" here, and it is not met by either candidate:

- **Sapphire PURE RX 9070 (non-XT)** - no published dB(A) measurement found. The *XT* version of
  the PURE measures 33.6 dB(A) under load against 31.9 idle, which is reasonable but is a
  different card, and Sapphire's PULSE and NITRO+ both carry documented problems elsewhere in
  this document. 2x 8-pin, no 12V-2x6 - that part is clean.
- **ASUS PRIME RX 9070 OC EVO** - fan-stop below 55 C, 2x 8-pin. But reviewers of the **PRIME
  XT** describe it as **louder than other cards tested recently, with audible fan noise under
  typical gaming load**. Cooler families carry across SKUs, so that is a warning, not noise.

**This is a genuine gap, not a formality** - the whole case for the Hellhound over cheaper
cards in this document was measured acoustics. Close it before buying.

## Options

| Model | UAH | VRAM | Verdict |
|---|---:|---|---|
| XFX RX 9060 XT Swift OC | 26 100 | 16GB | 1440p at medium-high. Only if the budget collapses. |
| PowerColor RX 9070 Hellhound (non-XT) | 35 999 | 16GB | ~8% slower than the XT for 1 700 less. The XT is the better buy. |
| ASUS PRIME RTX 5070 OC | 37 220 | **12GB** | Same price as a 9070 XT, slower in raster, and the VRAM is the part that will age badly. No. |
| **ASRock RX 9070 XT Challenger** | **37 700** | 16GB | Cheapest 9070 XT. Cooler is basic and its noise is not independently measured - the one unknown. |
| PowerColor RX 9070 XT Reaper | 40 160 | 16GB | PowerColor's *entry* cooler. **No published measurement of any kind.** |
| **PowerColor RX 9070 XT Hellhound** | **41 800** | 16GB | **29.0 dB(A) measured on the silent BIOS** (ComputerBase), 310W, **2x 8-pin - no 12V-2x6 at all**, 330mm, lightest of the group at 1180g. |
| Sapphire RX 9070 XT PULSE | 42 499 | 16GB | **25.5 dBA at 50cm verified** (TechPowerUp) - the quietest measured - but TechSpot's 14-card roundup found it the **warmest GPU and worst VRM (86 C) of the group**, and Gamers Nexus documented **erratic fan-RPM cycling** (ramping and de-ramping every few seconds) that Sapphire never fixed. Quiet by way of a lazy fan curve. |
| Sapphire RX 9070 XT PURE | 46 755 | 16GB | PULSE hardware in white with +13W. Ships **Honeywell PTM7950** phase-change material (ComputerBase). Very thinly reviewed - only one small outlet published noise figures. |
| **PowerColor RX 9070 XT Red Devil** | **46 862** | 16GB | **29.0 / 29.5 dB(A) measured** silent/OC BIOS - the best acoustics under OC of any card measured - plus "high-quality material selection and workmanship" (ComputerBase). Costs you 342mm of length and 3 full slots. |
| ~~ASRock RX 9070 XT Steel Legend~~ | - | 16GB | **Avoid.** Quiet in stock trim (34.2 dB) but only because the fan curve is lazy: at a **normalised 40 dBA it finished last of 14 RX 9070 XT coolers tested**, with owner-reported hotspots of 88-93 C. |
| ~~Sapphire RX 9070 XT NITRO+~~ | 49 439 | 16GB | **Avoid - the one recurring hardware defect found in this whole category.** At least **8 independent reports of burned 12V-2x6 adapters between October 2025 and June 2026**, mostly on Sapphire's bundled blue-tipped 3x 8-pin adapter, some at stock settings after months of use. Sapphire implemented **no per-wire load balancing**, there is **no dual BIOS** to fall back on, and at least one warranty claim was flatly rejected (the service load-tested the card, declared it fine, returned it with the damaged cable and told the owner to use a native PSU cable). Also 1893g and 3.2 slots, and its connector does not click when seated. |
| ~~XFX RX 9070 XT Mercury~~ | - | 16GB | **Avoid.** The only card ComputerBase criticises outright: 354W with fans running "particularly fast" for performance rivals match far more quietly, and 350mm long. |
| MSI RTX 5070 Ti SHADOW 3X OC | 52 399 | 16GB | Faster in heavy ray tracing, better upscaler, has CUDA - which you said you do not need. **+14 700 (+39%)** over the ASRock. |
| Gainward RTX 5080 Phoenix | 72 999 | 16GB | Two-thirds of the entire budget in one part. No. |

## Why this list looks AMD-heavy

It is a filtering artefact, not a preference. Three things produce it:

1. **The multiple "RX 9070 XT" rows are one GPU, not several.** Challenger, Reaper,
   Hellhound, PULSE and NITRO+ are the same AMD chip with different board-partner coolers.
   That is the only choice that matters once the chip is decided, so the list enumerates it.
2. **NVIDIA has no card that fits the filter.** The criteria here are 1440p-capable, **16GB
   VRAM**, and roughly 35-45k UAH. NVIDIA's entry in that price band is the RTX 5070, which
   fails on VRAM (12GB); its 16GB card is the 5070 Ti, which sits a whole price tier up at
   52 400. AMD happens to put 16GB in that exact band. Move the band and the list flips - at
   ~26-35k the RTX 5060 Ti 16GB (34 599) competes with the RX 9060 XT, and above 70k
   NVIDIA owns the market outright.
3. **NVIDIA still wins on ray tracing, upscaling and compute** - see the evidence below.
   Those are real advantages; they are just not advantages this brief asked for.

The mindshare is also real and has a cause: NVIDIA holds roughly **nine tenths of the
discrete GPU market**, so it gets most of the coverage, most of the game-engine integration
work, and all of the CUDA ecosystem. "I have heard more about RTX" is an accurate
observation about marketing and market share, not about frames per hryvnia at 1440p.

### RTX 5070 Ti models, for symmetry

If you decide to take the NVIDIA path after all, the model choice looks like this:

| Model | UAH |
|---|---:|
| MSI RTX 5070 Ti SHADOW 3X OC | 52 399 |
| PNY RTX 5070 Ti Overclocked Triple Fan | 54 999 |
| GIGABYTE RTX 5070 Ti WINDFORCE SFF 16G | 57 650 |
| Zotac RTX 5070 Ti GAMING SOLID CORE OC | 57 999 |
| ASUS RTX 5070 Ti PRIME | 57 999 |
| MSI RTX 5070 Ti VENTUS 3X OC | 58 999 |
| GIGABYTE RTX 5070 Ti GAMING OC 16G | 59 999 |

All are 16GB GDDR7 on a 256-bit bus. The MSI SHADOW at 52 399 is the price floor; the rest
charge 2 600-7 600 for cooler and brand differences.

> **Shop change, 2026-09-13.** At **click.ua**, where Dmytro buys, the **RX 9070 GRE does not
> exist in any brand**, so the ladder moves up a rung: Lean **PowerColor RX 9060 XT 16GB
> 29 659** (-23% on the GRE, +4GB), Working **Sapphire RX 9070 PURE 16GB 43 908** (+18%, same
> 220W and 2x 8-pin, so no other part moves), Max **Gigabyte RX 9070 XT Gaming 16GB 52 034**
> (+30%, 304W on 3x 8-pin, this model's cooler not assessed here). Nothing sits between the
> 9060 XT and the 9070 there: the RTX 5060 Ti 16GB at 38 999 measures below the GRE. See [../click_basket.md](../click_basket.md).

## Evidence (revised after the deep review pass, 2026-09-09)

**The 1440p numbers, from the best 2026-dated like-for-like dataset** - ComputerBase's May
2026 test parcours, 23 games, average FPS at 2560x1440:

| Card | Raster | vs 5070 Ti | Ray tracing | vs 5070 Ti |
|---|---:|---:|---:|---:|
| RTX 5070 Ti 16GB | 100.1 | 100% | 80.7 | 100% |
| **RX 9070 XT 16GB** | **100.5** | **+0.4%** | 77.1 | -4.7% |
| RX 9070 16GB | 90.7 | -9.4% | 68.3 | -15.4% |
| RTX 5070 12GB | 82.8 | -17.3% | 66.0 | -18.2% |
| RX 9070 GRE 12GB | 77.2 | -22.9% | 58.2 | -27.9% |
| RTX 5060 Ti 16GB | 61.0 | -39.1% | 49.3 | -38.9% |
| RX 9060 XT 16GB | 59.2 | -40.9% | 45.2 | -44.0% |

Read that as **raster parity** and a modest RT deficit, not the 5% deficit the launch
reviews reported. The trajectory: 5% behind at launch (March 2025) -> **+9% from drivers**
by July 2025 -> level or ~1.5% behind in 2026 depending on whose suite you read.
**Sources disagree on the RT gap**: ComputerBase's parcours says 4.7%, Hardware Unboxed's
52-game set is quoted at 14-15%, and ComputerBase's *own* aggregate ranking says +8.7% for
NVIDIA. The spread is driven by how many path-traced titles are included.

Two useful side-findings: the **RX 9070 beats the RTX 5070 by 9.4%** - they are not the same
tier despite similar prices; and the **RTX 5060 Ti 16GB beats the RX 9060 XT 16GB**, the one
slot in the band where NVIDIA wins outright.

Globally the 9070 XT sells for ~$700-740 against $980-1 277 for a 5070 Ti. In Ukraine the
gap is **28%** (41 800 vs 52 399). Either way you are paying a whole CPU tier for RT.

### The serious AMD problem the first pass missed: FSR frame generation

Hardware Unboxed's slow-motion analysis (August 2026, RX 9070 XT, 10 games) found FSR
"Redstone" frame generation has a **broken frame-pacing pattern** - a "double tap" where one
frame is displayed roughly **four times longer than the next**, so a reported 120 FPS feels
like 60. **V-Sync does not fix it.** The cause is that AMD paces frames in software instead
of using hardware flip metering, which is exactly what DLSS 4 does use. Worst in God of War
Ragnarok, Cyberpunk 2077, Alan Wake 2. Present since FSR 3, with no committed fix.

**This is the strongest argument for NVIDIA in the whole document**, and it is worth being
plain about: if you intend to use frame generation on a high-refresh panel, AMD's does not
currently deliver smoothness. Note the scope - **FSR 4 *upscaling* quality is not
implicated**, only frame generation, and a 9070 XT at 1440p is fast enough that frame
generation is a nice-to-have rather than a requirement.

### Driver state, both vendors, 2026 - neither is clean

- **AMD**: Adrenalin **26.8.1 crashes Apex Legends specifically on the RX 9070 XT** (black
  screens, device-removed errors). The Apex team confirmed it publicly; AMD had not listed
  it in known issues as of late August. Fix is rolling back to 26.7.1.
- **NVIDIA**: the **596.x** branch has recurring reports of video freezes on a secondary
  monitor, worsening through 596.36-596.49, with 591.74 cited as the stable fallback.
- **NVIDIA's missing-ROP defect affected the 5070 Ti** - eight of 112 ROPs disabled on ~0.5%
  of units, worth about 8% performance. If you buy any RTX 50 card, **check the ROP count in
  GPU-Z before the return window closes.**
- **12V-2x6**: melting is concentrated on 5090/5080, but a melted connector has been
  documented on a plain RTX 5070, and the mechanism (per-wire current imbalance, seating and
  bend radius) is not wattage-specific. The Hellhound's **2x 8-pin** design sidesteps this
  entirely - a quiet point in its favour.
- **VR on RDNA 4**: only anecdotal reports (F1 25 distortion, Valve Index red screens), no
  systematic testing. If VR matters to you, that is an open risk on AMD.

### Actual failure rates - the best evidence in this whole document

German and Czech retailers (Mindfactory, Alza) publish service-request data. Someone
compiled it across RX 9070 XT models in July 2026, counting only claims where the retailer
identified the GPU as the faulty part. Sample sizes are in the hundreds to thousands per
model. Panel average is about 1%.

| Model | Units in sample | RMA rate |
|---|---:|---:|
| ASUS Prime OC | 590+ / 1 000+ | 0.17% / 1.07% |
| **PowerColor Hellhound** | **4 340+** | **0.47%** |
| ASRock Challenger | 1 800+ | 0.48% |
| PowerColor Red Devil | 1 110+ | 1.28% |
| Sapphire PULSE | 2 000+ | 2.14% |
| XFX Swift | 2 000+ | 2.34% |
| ASRock Steel Legend | 500+ | 2.73% |
| XFX Quicksilver | 200+ | 2.84% |
| **PowerColor Reaper** | **2 350+** | **3.28% - worst in panel** |

Two things to take from it. First, **the Hellhound has the lowest failure rate of any
high-volume model** - 0.47% across the largest sample in the table - which independently
corroborates the acoustic and build evidence. Second, **the Reaper is the worst**, partly
attributed to an early production run with scratching and whistling fans; the rate has been
falling as newer stock enters the sample. My original Reaper recommendation was doubly wrong.

Note also that **the ASRock Challenger, which no reviewer has measured, has a good 0.48%
failure rate over 1 800+ units.** Unmeasured acoustics, but not an unreliable card.

### The Hellhound "Reva" question, answered

It is **not a defect fix** - it is PowerColor's first mascot-themed special edition, announced
October 2025, with a genuinely new and better cooler: reinforced shroud, higher-efficiency
fans, expanded heatsink, 10+3 VRM, 3 slots and 1 285g. TechPowerUp measured it at **24.3 dBA
with memory at 84 C - the quietest RX 9070 XT they have ever tested**, rated 5/5. It is a
separate, dearer SKU (~+$75), trivially distinguishable (white shroud, printed mascot,
magnetic second backplate, RGB kill switch), not a silent mid-cycle swap. If a shop has one
near the standard Hellhound's price, take it.

### Context you need before the defect lists alarm you

- **90 C memory is normal on RDNA 4, not a fault.** Sapphire's VBIOS sets the fan target for
  memory at 90-95 C against a TJmax of 108 C, so every reviewer measures VRAM in the high
  80s with a 56-60 C core. Igor's Lab investigated it across many RDNA 4 cards and found it
  is a deliberate fan-curve choice favouring silence; PowerColor's own support tells owners
  90-95 C VRAM is normal. The AMD "memory" sensor is a memory *hotspot* reading, not an
  average.
- **The platform baseline, from a 2 245-response owner poll:** 66.8% reported no issues,
  27.1% rare crashes, **6.1% serious recurring problems** - and the consensus attributed most
  instability to drivers, OS or PSU configuration rather than the card. Read every anecdote
  above against that denominator.
- **One Hellhound-relevant incident, for honesty:** the 2025 "pitted GPU die" case - deep
  pitting on the die backside, hotspot 113 C, unfixable by repasting - was found by Igor's
  Lab on a **PowerColor Hellhound**. A follow-up noted a small cluster of brand-new cards
  hitting 112-115 C hotspot within seconds: **two PowerColor and one Sapphire**, all RMA'd.
  Igor called it an individual quality-control escape rather than a series weakness, and the
  0.47% RMA rate above supports that reading. But it is the card I am recommending, so:
  **check hotspot temperature in the first hour.** Anything over ~100 C means return it.

### Still unmeasured, and I am not going to pretend otherwise

The deep pass obtained **no data at all** for the ASRock Challenger and Steel Legend, the
PowerColor Reaper, the Sapphire PULSE, any GIGABYTE 9070 XT, the ASUS PRIME 9070 XT, the XFX
Swift, the MSI SHADOW 3X, or the Zotac SOLID CORE - and no owner-report defect data for any
model, because Reddit and the TechPowerUp forums were unreachable. Silence is a gap in the
search, not a clean bill of health.
- **VRAM**: 12GB is described as the practical 1440p minimum in 2026, with max-setting
  texture packs (The Last of Us Part II, Star Wars Outlaws, Indiana Jones) already pushing
  past it; 16GB is the recommendation for longevity past 2027.
- **Upscaling**: FSR 4.1 "Redstone" reduced artifacts ~12% versus FSR 4, but reviewers still
  place DLSS 4.5 ahead on sharpness and frame pacing.
- **Noise, per model** (TechPowerUp, load): PowerColor Reva/Hellhound 24 dBA, Sapphire Pulse
  25.5 dBA, ASUS TUF OC 30 dBA / 26.6 dBA quiet BIOS.

## SHORTLIST (2026-09-09) - narrowed to four, NOT settled

**The earlier "decided: Hellhound at 41 800" was wrong on both the price and the status.**
41 800 was hotline's lowest offer, from a shop with 33 reviews. Reputable stores charge
**45 500-49 000** for a 9070 XT, confirmed independently. The decision is reopened.

### Realistic price ladder

Ranges are the full hotline spread with the number of shops carrying it; "realistic" is what
an established store actually charges. Performance = ComputerBase 2026 suite, 23 games,
average FPS at 2560x1440.

| Card | Range (shops) | Realistic | Perf |
|---|---|---:|---:|
| RX 9060 XT 16GB | 25 775-33 540 | ~30 000 | 59.2 |
| **RTX 5060 Ti 16GB** | 34 599-43 426 | ~38-40 000 | 61.0 |
| RX 9070 GRE 12GB | 30 042-35 103 (9) | ~33 000 | 77.2 |
| **RTX 5070 12GB** | 35 599-49 970 | ~42-45 000 | 82.8 |
| **RX 9070 Hellhound** | **36 561-39 699 (7)** | **~38-39 000** | **90.7** |
| **RX 9070 XT Hellhound** | 41 800-47 502 (5) | ~46-47 000 | 100.5 |
| RTX 5070 Ti | 52 399-62 991 | ~57-60 000 | 100.1 |

**Dmytro's shortlist, agreed 2026-09-09: RTX 5060 Ti, RTX 5070, RX 9070, RX 9070 XT** - with
the **9070 XT as the ceiling** of what he will consider. Anything above it (5070 Ti, 5080) is
out; the 9060 XT and 9070 GRE are below the floor.

### What the realistic prices changed

- **The XT's case weakened badly.** At hotline minimums it was only 1 700-5 800 over the
  non-XT. At store prices the gap is **~8 000 for +10.8%** - no longer an obvious buy.
- **The RX 9070 becomes the value pick.** Same Hellhound cooler family (PTM7950, Japanese
  ball-bearing fans, the brand with the 0.47% RMA record), 16GB, and **7 shops carry it**
  versus 5 for the black XT. It also **beats an RTX 5070 on both price and performance**
  (~38 500 vs ~42-45 000, and +9.5% faster). Tom's Hardware independently calls the RX 9070
  the "1440p raster value champ".
- **The 5060 Ti is the weakest hryvnia in the list**: at ~38-40 000 it costs the same as an
  RX 9070 for **-35% performance**.

### Availability note that matters for a shop-built machine

The plain black Hellhound XT is stocked by only 5 shops, mostly small ones. The variants
reputable stores actually carry are the **Hellhound Reva** (11 offers, incl. Telemart, MOYO,
Foxtrot, COMPX.UA, CAN.UA) and the **Spectral White** (10 offers). The Reva is also the better
card - TechPowerUp's quietest 9070 XT ever tested at 24.3 dBA.


### Safe alternatives, if the Hellhound is out of stock

Safe = low retailer failure rate **and** published acoustic data **and** no known defect
pattern. Four models clear that bar:

| Rank | Model | UAH | Evidence | Size |
|---|---|---:|---|---|
| 1 | PowerColor Hellhound | 41 800 | RMA **0.47%** / 4 340+ units, 29.0 dB(A), PTM7950, ball-bearing fans, 2x 8-pin | 330mm, 2.5 slot, 1180g |
| 2 | PowerColor Hellhound **Reva** | ~48 400 | TPU **24.3 dBA - quietest 9070 XT ever tested**, memory 84 C, 5/5 | 340mm, 3 slot, 1285g |
| 3 | ASUS TUF Gaming OC | 42 199 | TPU **26.6 dB(A)** quiet BIOS, 51/79/84 C, dual BIOS, removable fans | 330mm, 3.1 slot, 1444g |
| 4 | PowerColor Red Devil | 46 862 | 29.0 / **29.5 dB(A) even on OC BIOS**, RMA 1.28% | 342mm, 3 slot, 1534g |

Budget-safe: **ASRock Challenger, 37 700** - RMA 0.48% over 1 800+ units, so demonstrably
reliable, but **no published noise measurement of any kind**.

Caveats: the TUF had audible coil whine on two review samples, and ASUS's RMA handling has
been publicly criticised. Red Devil and Reva are 340mm+ and 3 slots - check case clearance.

### Per-game reality, and a correction

The overall raster lead is real but **game-dependent**, and one of my earlier statements was
wrong:

- **Overall raster, vs RTX 5070: 9070 XT ahead by 7-17%** depending on title.
- **Cyberpunk 2077, raster Ultra:** 9070 XT slightly beats even the 5070 Ti. With ray
  tracing on, the 5070 Ti takes a **15% lead**.
- **STALKER 2 genuinely favours NVIDIA** - the 5070 Ti leads the 9070 XT by **9-12%** across
  resolutions and presets. I earlier said a retailer's STALKER 2 figure "contradicted every
  benchmark"; the *direction* was right and I was wrong. What was off was the magnitude:
  against the plain 5070, one native 1440p test has the 9070 XT **7% faster**, and realistic
  native 1440p for the 9070 XT is ~73-80 FPS.
- **UE5/Lumen and RT-heavy titles are NVIDIA's territory; raster is AMD's.** If STALKER 2 and
  ray tracing are the main diet, the RTX 5070 Ti is a legitimate choice at +11 000 - but not
  the 5070, which loses raster and has 12GB.

### Buy-day checks

- Verify hotspot temperature in the first hour. Over ~100 C = a bad die-contact unit, return
  it inside the window.
- Run the **silent BIOS**.
- Buy from a shop with a service department; on a 40k part the 5% saved at an unknown shop is
  not worth the RMA risk.

## Verdict

**RX 9070 XT, and spend the model premium rather than the brand premium.**

- **Recommended: PowerColor RX 9070 XT Hellhound, 41 800.** It now wins on every axis the
  deep pass could measure: **0.47% RMA rate across 4 340+ units** (lowest of any high-volume
  model), **29.0 dB(A) measured on its silent BIOS** with a 20 C hotspot delta, **Honeywell
  PTM7950** phase-change material and **Japanese dual ball-bearing fans** from the factory,
  the lightest card at 1180g, 2.5 slots, and **2x 8-pin so there is no 12V-2x6 connector to
  worry about**. Run the silent BIOS: the OC BIOS costs 3.5 dB(A) for ~4% more power.
- **Also excellent: ASUS TUF Gaming RX 9070 XT OC, 42 199.** The only card with a genuine
  quiet BIOS verified by TechPowerUp: **26.6 dB(A)** (30.4 stock), GPU 51 C / hotspot 79 C /
  memory 84 C, dual BIOS, removable fan assembly, and the best measured cooler of the group.
  Caveats: 3.125 slots and 1444g, two independent reviewers noted **coil whine on their
  samples**, and ASUS's RMA handling has been publicly criticised. Cross-lab noise figures
  are not directly comparable, so treat this and the Hellhound as co-equal.
- **Better but pricier: PowerColor Red Devil, 46 862** (+5 062). The best-measured acoustics
  of any 9070 XT - 29.0 dB(A) silent BIOS, **29.5 dB(A) even on the OC BIOS** - plus
  ComputerBase's praise for materials and workmanship, and a reliable fan-stop at idle. The
  cost is physical: 342mm long and a full 3 slots. Check it against your case first.
- **Cheapest: ASRock Challenger, 37 700** (-4 100), and better than I thought: **no reviewer
  has ever measured it** - no noise figure, no temperatures, nothing but content-farm numbers
  - but its **retailer RMA rate is a good 0.48% over 1 800+ units.** So: unknown acoustics,
  demonstrably not unreliable. A reasonable gamble if you want the 4 100 elsewhere.
- **Not the PowerColor Reaper (40 160)** - my original recommendation, and the **worst card
  in the RMA table at 3.28%**, partly from an early batch with scratching and whistling fans.
  Also has the hottest VRM measured of the group (87 C).
- **Not the Sapphire PULSE (42 499)**, despite it having the lowest verified noise number
  (25.5 dBA at 50cm). It buys that quiet with a lazy fan curve: TechSpot found it the warmest
  GPU and **worst VRM (86 C) of 14 cards**, and Gamers Nexus documented erratic fan-RPM
  cycling that Sapphire never fixed. Quiet, but the least well-cooled card in the group.
- **Not the ASRock Steel Legend** - last of 14 coolers at a normalised 40 dBA.
- **Avoid the Sapphire NITRO+ (49 439)** - burned bundled adapters, no per-wire load
  balancing, no dual BIOS, and a rejected warranty claim on record.
- **Avoid the GIGABYTE GAMING OC (40 982)** - the only card two independent reviewers
  actively steer buyers away from: **42 dBA measured**, memory to 98 C on the quiet BIOS,
  "hottest and loudest" of TechSpot's roundup, and HWCooling's review ends by telling you to
  buy the Aorus Elite instead. Gigabyte also has a lab-verified problem with the thermal
  putty and paste used on this generation - Igor's Lab found pores, poor adhesion and paste
  cracking after three months, and Gigabyte's own April 2025 statement names the RX 9000
  series while calling it cosmetic.
- **Avoid the ASUS PRIME 9070 XT (42 113)** - a 2.5-slot cooler under a 330W card: hotspot
  89-92 C, memory 90 C in review and one owner logging **110 C against a 108 C limit**,
  reviewer-flagged as loud with audible coil whine.

**If frame generation matters to you, buy NVIDIA instead: ASUS PRIME RTX 5070 Ti, 57 999.**
That is +16 200 over the Hellhound, and it buys working frame generation with hardware flip
metering, a 5-15% ray-tracing lead, roughly 20% lower power, and better VR odds. It measured
the coolest memory of any card examined (60 C) with no coil-whine remarks. On your brief -
1440p, not competitive, no CUDA - I do not think it is worth 16 200. But it is a real
argument now that I have the frame-pacing evidence, and it is your call rather than mine.
- **Do not** buy the RTX 5070 Ti at 52 399 on this brief. With no CUDA requirement and
  streaming that is rare and amateur, you would be paying 14 700 - a whole CPU tier - for
  better ray tracing and a slightly better upscaler.
- **Do not** buy the RTX 5070 at the same price as a 9070 XT: 12GB is the wrong bet for a
  four-year machine.

## What about waiting for the Super refresh?

A 24GB RTX 5070 Ti SUPER at 350W has been rumoured all year. It has slipped repeatedly
because 3GB GDDR7 modules are scarce, and current reports point at late 2026 or **CES 2027**.
Meanwhile memory prices are still rising, which means the refresh will not launch cheap. Do
not plan around it.


## Store prices and the ladder (2026-09-10)

Verified at Telemart, in stock:

| Card | This doc (hotline floor) | Telemart | Delta |
|---|---:|---:|---:|
| RX 9070 GRE, PowerColor Hellhound 12GB | 33 000 | **32 249** | -2% |
| RX 9070 16GB, Sapphire PURE | 38 500 | **39 999** | +4% |
| RX 9070 XT, PowerColor Red Devil 16GB | 46 500 | **42 805** | **-8%** |

The XT figure is a **5% promo against a 45 009 list price** - today's number, not a settled one.
Telemart's other in-stock XT is the ASUS TUF at 44 999. A Gigabyte XT listed at 35 999 is **out
of stock**; it shows up in search results and should not be planned around.

**The GPU was over-stated in this doc, not under** - which matters because every earlier build
total assumed the opposite, and because the XT is the largest single line in the machine.

**The RX 9070 non-XT is excluded from the build ladder.** At 39 999 against the XT's 42 805 it is
dominated: 2 806 less for a clearly slower card. Aggregator lows hint at a wider spread across
the market (9070 from ~29 800, XT from ~36 400, both unverified), which would revive it - so
re-check the pair at Brain and Rozetka before settling. As priced at the one store that could be
read, it has no place in the ladder, and tiering on it is what made four earlier versions of the
build table collapse into each other.

**Assigned:** GRE to Lean **and** Working, XT to Max - see [../../pc_build.md](../../pc_build.md).

**Model substitution to resolve.** This doc's XT pick is the **PowerColor Hellhound at 41 800**,
chosen on measured evidence: 0.47% RMA across 4 340+ units, 29.0 dB(A) on the silent BIOS,
PTM7950, no 12V-2x6 connector. **Telemart listed no 9070 XT Hellhound** on 2026-09-10 - its
in-stock XTs were the Red Devil 42 805 and the ASUS TUF 44 999 - so the Max build carries the
**Red Devil purely on availability**, and at 1 005 *more* than the Hellhound's floor price. The
GRE side is consistent: the Hellhound GRE at 32 249 is the assigned card.

**So: ask for the XT Hellhound by name in the store quotes.** If no assembler carries it, the
Red Devil substitution needs the same RMA/noise check this doc applied to the Hellhound before it
is accepted - it has not had one.
