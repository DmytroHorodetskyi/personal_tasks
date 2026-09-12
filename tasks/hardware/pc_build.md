# PC build, up to 130k UAH (work + 1440p gaming)

Choosing and optimising a complete new desktop plus monitor for Dmytro, bought new in
Ukraine. Started 2026-09-09.

## Requirements as agreed

| | |
|---|---|
| Purpose | Work first, then gaming at 2560x1440, high FPS, not competitive. Rare amateur streaming. |
| Work profile | Development: IDE + language servers, Claude Code over **heavy repos**, containers, git. **Not** render/compile-farm heavy - no need for 16 cores. |
| CUDA / local AI | **Not needed now; may be needed some day, not urgent.** Verified on the current machine (2026-09-09): no CUDA toolkit, no PyTorch/TensorFlow/CuPy install, no Ollama/ComfyUI/Blender - the GTX 1660 Ti has only ever been a gaming and display card. Existing Python work is CPU-side scikit-learn/scipy. Decision: build AMD, keep the deep-learning route open per the note below. Revisit if a concrete DL need appears. |
| Budget, main | Started at 100-120k for the full PC including the monitor; **raised to 130 000 on 2026-09-10** and explicitly not further "for now". Standing instruction: **decide by build logic, not by the price ceiling** - and name the better-but-pricier option wherever one exists. |
| Budget, extras | Keyboard, mouse, desk mat, headphones and desk priced separately, one file each in [peripherals/](pc_build/peripherals). **All five settled 2026-09-11/12; total 13 481** plus desk delivery. |
| Condition | New parts only, official warranty, Ukrainian retail. |
| Reuse | Nothing - full set, including storage and a Windows licence. |
| OS | Windows 11 **Home** (default). Budgeted at 2 500 until 2026-09-11; the real price is **7 098** (Brain, in stock) - see [price_check.md](pc_build/price_check.md). |
| Wi-Fi | **Required** (stated 2026-09-09). Rules out the non-WiFi board SKUs; see [motherboard.md](pc_build/components/motherboard.md). |
| UPS / power backup | **Parked** by Dmytro - to be discussed with a specialist, not researched here. |

Missing from the original list and added: **SSD**, **Windows licence**, **keyboard**.
Also flagged: a chair matters more than the desk for all-day work.

## Where it stands

**THREE BUILDS, SETTLED 2026-09-10.** Tiered on the whole machine, not on the graphics card.
Every earlier version of this table tiered on the GPU alone, which cannot work: the shared
platform is ~85 000 of a ~125 000 build, so a 3-10 000 card difference produced "tiers" that
landed within a few thousand of each other. Dmytro rejected four such versions before this one.

| | **Lean** | **Working** | **Max** |
|---|---:|---:|---:|
| CPU | 7500F **tray 6 519** (Brain) | 9700X BOX **13 936** (Rozetka) | 9700X BOX **13 936** (Rozetka) |
| GPU | 9070 GRE **32 179** (Telemart) | 9070 GRE **32 179** (Telemart) | **RX 9070 PURE 39 999** (Telemart) |
| Board | ASRock B850M Pro RS WiFi **6 965** (Telemart) | ASRock B850 Pro RS WiFi **8 642** (Rozetka) | ASRock **8 642** (ASUS TUF **9 399** at Telemart if Brain quotes) |
| RAM | 16GB 2x8 DDR5-6000 **16 035** (Rozetka) | 32GB CL36 **23 789** (Rozetka) | 32GB **23 789** (Rozetka) |
| SSD | WD Green SN3000 **6 999** (Telemart) | 990 EVO Plus **10 679** (Telemart) | **Kingston Renegade G5 11 999** (Telemart) |
| Cooler | **AK400 1 699.** Lean's 0 relied on the **MPK** 7500F - AMD's multipack SKU, the only one that ships a Wraith Stealth - and it is out of stock at every shop checked | AK400 **1 699** | AK400 **1 699** |
| PSU | 750W **5 419** | **5 419** | **5 419** |
| Case | Deepcool CC560 **Limited V2 2 280** (Rozetka) | Lancool 216 **4 949** (Telemart) | Lancool 216 **4 949** (Telemart) |
| Monitor | AOC Q27G4XF **6 899** (Rozetka) | Q27G4ZR 240Hz **8 669** (Rozetka) | Q27G4ZR **8 669** (Rozetka) |
| Windows 11 Home | **7 098** (Brain) | **7 098** | **7 098** |
| **Total** | **92 092** | **117 059** | **126 199** (126 956 with the TUF) |

**Priced and stock-checked across shops 2026-09-11 - [price_check.md](pc_build/price_check.md)
carries the per-part evidence.** Every figure above is the cheapest price at a named shop that
will actually sell the part, not a hotline floor; the shop is named because no single one
carries the basket. Against the previous table this is **Lean +6 805, Working +2 200, Max
+1 920**, and Max now has **3 801** of headroom rather than 5 388.

What moved: the **Windows licence is 7 098, not 2 500** - nothing sells it at 2 500, and that
alone is +4 598 per build. The **7500F MPK is out of stock at every shop checked**, so Lean pays
for a cooler and loses its 0 row. Against those, the **9700X is 1 163 cheaper** than carried and
the **Q27G4ZR is 564 cheaper**. Two first-pass bargains did **not** survive a stock check - the
32GB kit at 21 094 and the Lancool at 4 699, both listed at Brain, both unavailable.

Also: the Lean case SKU is the **CC560 Limited V2**, and no
SKU called "CC560 V2" is what that row means.

**Recomputed from parts 2026-09-11**, not adjusted from an older total. Changes this session:
the PSU dropped to a 750W (-377 each), the GRE fell 70 to 32 179, and **the Max build's GPU
changed from a 9070 XT to the RX 9070 16GB** after the XT tier priced itself out of reach - see
the section above. **The board question is closed on price:** Telemart lists the ASRock B850 Pro
RS WiFi at 8 829 and Rozetka at **8 642, in stock**, which is the figure the table now carries.
Which board to buy is still the motherboard question, handled separately.

Gaps: **+24 967**, then **+9 140**. **The range is 130 000** (revised by Dmytro 2026-09-10, up
from 125 000 and explicitly not further "for now"). All three fit, Max with **3 801 to spare**
on stock-checked prices.

**What each build is:**

- **Lean, 92 092** - the weakest that still meets the requirements. Six cores, 16GB, 1440p on
  the GRE, a measured budget panel. It accepts a full RAM re-buy later (DDR5 will not take four
  sticks - see [ram.md](pc_build/components/ram.md)), no iGPU for diagnosis with the card
  pulled, occasional stutter in a handful of AAA titles at 16GB, and 12GB of VRAM.
- **Working, 117 059** - the money goes into the **platform**, not the card: eight cores for the
  tooling, 32GB, the 240Hz panel, the measured-quiet case. Same GPU as Lean. This is the build
  for a work-first machine and it is the recommendation.
- **Max, 126 199** - the **RX 9070 16GB** over the Working build: **+18% GPU and 16GB of VRAM
  for 7 820**, with nothing else changed. It was a 9070 XT until 2026-09-11, when the XT tier
  rose out of reach; the non-XT is the better-value card at today's prices and keeps Max inside
  the budget. Measured at **29.0 dB(A)**, the same as the Hellhound this project picked on
  acoustics.

**The RX 9070 non-XT is excluded from the ladder on purpose.** At 39 999 against the XT's
42 805 it is dominated - 2 806 less for a clearly slower card. It is the part that made every
GPU-tiered version of this table collapse.

## Pricing basis - changed 2026-09-10

**Prices above are real store prices, not hotline's lowest offer.** Superseded 2026-09-11 by
[price_check.md](pc_build/price_check.md), which prices every part at four shops and checks
stock; the Telemart-only figures below are kept because the reasoning about *how wrong* a
hotline floor is still holds. Verified at Telemart on 2026-09-10 where the part is stocked there: 9700X BOX 15 099, 9070 GRE Hellhound 32 249,
9070 XT Red Devil 42 805 (a 5% promo off 45 009), Crucial Pro 32GB 24 099, 990 PRO 1TB 12 399
/ 2TB 18 899, Pure Power 13 M 850W 5 800, Lancool 216 4 949.

The old method - price everything at hotline's cheapest anonymous offer, append a "10-15%
understated" warning, then compare the total to the budget - was incoherent, and Dmytro said so.
What the switch revealed is that **the understatement is not uniform and not always upward**:

| Part | hotline floor | Telemart | Δ |
|---|---:|---:|---:|
| 9700X BOX | 12 599 | 15 099 | **+20%** |
| 990 PRO 2TB | 16 299 | 18 899 | +16% |
| 32GB DDR5-6000 CL36 | 21 250 | 24 099 | +8% |
| Lancool 216 | 4 667 | 4 949 | +6% |
| Pure Power 13 M 850W | 5 759 | 5 800 | +1% |
| 9070 GRE | 33 000 | 32 249 | **-2%** |
| 9070 XT | 46 500 | 42 805 | **-8%** |

A blanket percentage would have been wrong in both directions - and the GPU, the largest single
line, was **over**stated in the old docs rather than under. The monitor has also fallen: hotline
now shows the Q27G4ZR from 9 233 against the 9 551 in [monitor.md](pc_build/components/monitor.md).

~~**Still market-floor, not store-checked:** the 7500F MPK, the 16GB kit, the AK400, the budget
monitor and the 9600X. **Only Telemart could be read** - Brain and Rozetka return HTTP 403 to
automated requests.~~ **Closed 2026-09-11.** Every part is now read at four shops with stock
confirmed - [price_check.md](pc_build/price_check.md). Brain serves its own quick-search API,
Rozetka reads fine in a browser, and hotline *does* carry per-shop prices in its page payload,
which is how the directory column is built.

**Component picks are made on merit, market-wide. Stock at one shop is a purchase-time
filter, not a selection criterion** - a correction Dmytro made after an earlier version dropped
the ASRock board and the 16GB kit merely because Telemart was out of them.

## URGENT, 2026-09-11: the Max build's GPU is no longer buyable at its quoted price

Checked while resolving the Hellhound-vs-Red-Devil question. The question turned out to be moot.

- **9070 XT Red Devil, quoted at 42 805: out of stock at Telemart.** The only other listing
  found is **54 269** at a single shop.
- **9070 XT Hellhound, the merit pick at 41 800: effectively unavailable.** Two shops carry it,
  at **47 502** and **48 449**, and **neither assembles**. Telemart has only the Spectral White
  at **47 665**.
- **The GRE is unchanged at 32 179** - so **Lean and Working are untouched**. This is an
  XT-tier event only.
- **Cause:** AMD raised GPU+memory wholesale prices **~10% from July 2026, the third rise of
  2026**. Up, not down - which is the answer this file already gives to "should I wait".

**Cheapest *new* XT from a store that can assemble: Brain, ASUS PRIME RX 9070 XT OC, 45 499.**
Telemart's cheapest new one is 46 709. **Telemart's ASUS PRIME White at 36 999 is "Factory
Recertified" - refurbished, and fails the new-parts-only requirement.**

| | Working | Max as documented | Max, cheapest new XT |
|---|---:|---:|---:|
| **Total** | **116 800** | 127 400 | **130 094** |
| Premium over Working | - | +10 600 | **+13 320** |

**Max now misses the 130 000 range** - but the field was re-opened rather than just re-priced,
and that produces a better answer than any of the three obvious ones.

### The RX 9070 non-XT is back, and it is the recommendation

It was excluded for one stated reason: *"at 39 999 against the XT's 42 805 it is dominated."*
**The XT is now 45 499, so the gap is 5 500, not 2 806.** The reason is gone; the card has not
moved. It is **16GB**, 220W and 2x 8-pin - the same power and connectors as the GRE, so it
changes nothing else in the build.

| Max option | GPU | Total | vs Working | Buys |
|---|---:|---:|---:|---|
| **A. RX 9070 16GB** (Sapphire PURE, Telemart, in stock) | **39 999** | **124 594** | **+7 794** | **+18% over the GRE, 16GB, inside budget** |
| B. RX 9070 XT 16GB (ASUS PRIME, Brain) | 45 499 | 130 094 | +13 320 | ~+32%, but 94 over the range |
| C. Drop Max | - | - | - | Working at 116 800 stands |

**Two corrections came out of the re-check.** The XT is **~32% over the GRE**, not the "25-30%"
this file claimed. And this project **rejects the RTX 5070 for having 12GB "on a card meant to
last past 2027" while putting a 12GB GRE in two of three builds** - both cannot be true. The GRE
survives because it is priced far better here (24% under the 9070) than in the US reviews that
panned it, but 16GB is the real future-proofing in this band, and the non-XT is where it starts.

**NVIDIA re-checked at today's prices, then corrected after Dmytro challenged the figure.** The
RTX 5070 is 42 999 against the RX 9070's 39 999. The earlier "8-13% slower" was a **raster-only**
number stated without that qualification, and "dominated outright" was too strong. Verified:
**raster ~5-15%** to the 9070 depending on the suite (Tom's Hardware +3-6%, TechSpot +13%,
GECID +10-20%); **standard ray tracing is a tie** (+0.23%); **path tracing goes to NVIDIA by
40%**. The 9070 is still the pick - this build is 1440p raster with no RT or CUDA requirement,
and 16GB beats 12GB on a machine meant to last past 2027 - but the reason is narrower than
stated. The RTX 5070 Ti is 59 999, +20 000 out of band. The RTX 5060 Ti 16GB at 38 999
is slower than the GRE. And the **RTX 50 SUPER refresh is delayed indefinitely** - late 2026 or
CES 2027 - so there is nothing to wait for.

**The cheap Hellhound 9070 is a trap, the same one as the XT.** At 35 999 it uses the cooler
this project already vetted, but **neither Telemart nor Brain stocks it** - only eight small
shops and Rozetka do. From a store that can actually assemble and warrant the machine, the
RX 9070 is **39 999** either way: Sapphire PURE at Telemart, ASUS PRIME OC EVO at Brain.

**Reject both "Recertified" listings** that show up as the cheapest in their tiers - Telemart's
ASUS PRIME XT White at 36 999 and Sapphire PURE 9070 at 36 999 are refurbished.

**Noise: closed 2026-09-11.** ComputerBase's RX 9070 non-XT roundup measures the **Sapphire PURE
at 29.0 dB(A)** under gaming load - identical to the PowerColor Hellhound's OC BIOS and to the
Hellhound XT this project chose on acoustics, and within 1 dB of the quietest cards tested. It
calls the Pure, Pulse, TUF and Hellhound "extremely to nearly inaudible". **Buy the Sapphire PURE
at Telemart.** The ASUS PRIME EVO at Brain was not in that roundup and stays unmeasured, so
Telemart is the preferred route for the Max build.

Note for the acceptance sheet: ComputerBase measured the PURE at **247W**, not the 220W TBP -
it carries a bigger factory overclock. Max still draws only ~400W, **53% of the 750W PSU**.

Full evidence in [gpu.md](pc_build/components/gpu.md).

## Still open

1. **PSU: settled 2026-09-11.** Dropped to the **be quiet! Pure Power 13 M 750W, 5 419** at
   Telemart, in all three builds. Same FSP platform, ATX 3.1, four 6+2-pin and a 160mm depth as
   the 850W it replaces, 10-year warranty - and it **measures quieter**, 6.51 dBA against 10.65.
   Peak draw is ~368W (Lean, Working) and ~488W (Max), so 750W sits at 49-65% load. **The saving
   is 377 per build, not the ~1 300 estimated** - be quiet! prices 650/750/850W almost flat, so
   the reason to drop a size was correctness, not money: the 850W had been sized against a
   9800X3D build that no longer exists. The 650W at 4 921 is rejected - only 2x PCIe 6+2-pin and
   a 450W 12V-2x6.

   **Sizing verified 2026-09-11, not estimated.** Sustained peak is **373W** (Lean, Working) and
   **463-483W** (Max, depending on which XT) - 50% and 62-64% of 750W, the band where the fan
   stays stopped. Worst case, with the 9700X manually put in its optional 105W mode (142W PPT),
   Max reaches 537W, **72%**. Transients are covered by the ATX 3.1 certification - 2x rated
   power for 100 microseconds, ie 1 500W - not by continuous headroom; measured RDNA4 excursions
   run ~13% over nominal. **AMD's own official recommendation for the 9070 XT is 750W**; the Red
   Devil box's 900W is a model claim AMD has publicly disowned. **Cross-checked against the
   Seasonic Wattage Calculator, run directly for all three configs: 550W / 550W / 700W
   recommended** - comfortable everywhere. Full budget, calculator table and sources in
   [psu.md](pc_build/components/psu.md).

   **Correction that fell out of it:** the docs said every candidate card needs 2x 8-pin. True of
   the GRE and the Hellhound XT, **but the Red Devil XT needs three**. The 750W supplies four, so
   it fits either way.

   **Checked against five PSU buying guides 2026-09-11** (Dmytro's list, read via
   `code/yt_transcript.py`). Nothing overturned the pick; three gaps closed. The **SPL PSU tier
   list** - a teardown-based grading this project was not using, now in [tools.md](pc_build/tools.md) -
   grades the **750W and 850W at A**, the 650W at **B+** (85C bulk caps, a better reason to
   reject it than the connector count), and the **1000W at A-** for poor 200% excursion
   response, so in this family buying bigger is graded *worse*. Cabling for the Red Devil's three
   8-pin sockets is now specified rather than left open. And a build rule was missing entirely:
   **never reuse a modular cable from another PSU** - pinouts are not standardised and it
   destroys drives. One guide dissents on sizing (a blanket 1.5x rule that would put Max on
   850W); why it does not win is recorded in [psu.md](pc_build/components/psu.md).

   **Same unit in all three builds, checked rather than assumed.** Lean and Working run the same
   CPU class and the same GRE, so their peak is identical - no sizing difference exists between
   them. Every cheaper 650-750W candidate was priced against the tier list: the 650W saves 500
   for a B+ part, the previous-generation Pure Power 12 M is 10 240 at one shop, and the MSI
   A850GLS is 930 *more* expensive at a lower grade. The only unit graded above the pick is the
   **Super Flower Leadex VII XG 750W at 6 277 (A+)**, which is an upgrade, not a saving.
2. ~~**The board has to survive substitution.**~~ **Closed 2026-09-11.** The premise was wrong:
   **Telemart does stock the ASRock B850 Pro RS WiFi - 8 829, in stock**, cheaper than the
   ~9 400 assumed. **Brain** is the shop with no such board (its only ASRock B850 is the
   LiveMixer WiFi 9 499, itself a fine substitute at 57 C). The three unchecked Telemart boards
   have now been measured against this doc's criteria: **ASUS TUF B850-PLUS WIFI 9 399 passes
   everything** (54 C - second-best of 47 boards tested - ATX, 3x M.2, Wi-Fi 7), Gigabyte B850M
   GAMING X WIFI6E 8 799 passes (62 C, mATX, 2x M.2), and **MSI B850M GAMING PRO WIFI6E 7 599 -
   the Lean build's board - has no published VRM spec and has never been tested by anyone.**
   Two corrections fell out: the MSI Tomahawk measures **64 C**, not the 58 C this repo quoted,
   and the ASRock's wireless is confirmed **Wi-Fi 6E, not Wi-Fi 7**. Full pass in
   [motherboard.md](pc_build/components/motherboard.md).
3. **The Crucial brand is being wound down** (Micron, consumer shipments ending through 2026;
   warranty and support continue). Does not change the RAM pick - never-mix-kits means a future
   replacement is a whole kit anyway - but Kingston FURY Beast at 27 899 (+1 700) is from a brand
   that is staying, if warranty exchange matters more than the money.
4. **Written quotes from Brain and Telemart** for the whole basket, per build. This is the only
   number that can be held to, and one store has to supply and assemble everything.
5. **Storage: settled 2026-09-10.** One **1TB NVMe, Gen 4, no built-in heatsink**. 2TB is
   dropped - Dmytro does not need it, and the 6 500 is what puts the Max build under 130 000.
   A 512GB SSD + 1TB HDD split was researched and rejected: HDDs now cost the same per TB as
   NVMe, so the split totals 12 368 against a 12 399 single 990 PRO, and 512GB would start
   life over half full (current machine: 270GB used, of which games are 2.3GB). The live
   choice is drive tier, not capacity. **Drive tier closed 2026-09-11, and tiered per build:**
   Lean **WD Green SN3000 6 999**, Working **990 EVO Plus 10 399**, Max **Kingston FURY Renegade
   G5 11 999**. The Renegade G5 was dropped and then reinstated on verification: **Telemart sells
   it at 11 999 - 400 *cheaper* than the 990 PRO there** - it ships without a built-in heatsink
   (SFYR2S/1T0, the right SKU), does not thermally throttle, and on PCMark 10 Storage measures
   **8 062 / 1 178 MB/s against the 990 PRO's 4 651 / 743**. **The 990 PRO ends up in no build:**
   neither cheapest nor fastest. The EVO Plus takes Working because it matches the PRO on
   real-world system-drive tests for 2 000 less; its ~850 MB/s post-cache write is a number this
   workload never reaches, the SLC cache being ~12% of the drive. Full
   reasoning and the video evidence in [storage.md](pc_build/components/storage.md).

**Assembly: Dmytro will not build the machine himself.** It must be bought and assembled by
one store, which constrains the final basket to that store's catalogue. Best found so far:
**Brain** (own service centre since 2008, **36 months warranty on the assembly** if all parts
bought there) and **Telemart** (configurator with compatibility checks, assembly 299 UAH + 1% of
components, but only a **14-day** assembly warranty).

**Buy retail SKUs, not tray.** A tray CPU carries the shop's warranty (often 12 months), not
AMD's 36 - the gap is 360-1 409 depending on the chip. See the SKU table in
[cpu.md](pc_build/components/cpu.md).

Nothing bought.

## Artefacts

Per-component docs. Each one has: what the part does *for this machine*; **the
characteristics that matter, and how to read them** - every spec named with its unit,
**numbered in order of how much it decides the purchase**, with a closing line on what to
ignore; a **`## Specifications` datasheet** of the actual numbers for the shortlisted parts;
the full option list with Ukrainian prices; the published evidence; and a verdict with a
cheaper and a better-but-pricier alternative named.

Both of those sections were rewritten on 2026-09-09. The first pass shipped verdicts without
ever printing the plain specs - the CPU doc had **no clock speed anywhere in it** - and its
characteristics tables listed specs in no particular order, so nothing told you which rows
were the decision and which were noise. Every figure now comes from the manufacturer's own
spec page or a named review; the two corrections that fell out of the exercise are below.

**[build_specs.md](pc_build/build_specs.md) is the acceptance sheet** - every component in
every build with the characteristics that decide it, the required values, and the grounds for
rejection. Use it when a store proposes a substitute.

| Doc | Verdict in one line, current as of 2026-09-10 |
|---|---|
| [cpu.md](pc_build/components/cpu.md) | **Superseded on price 2026-09-11** - see price_check.md. The **MPK** multipack (the SKU that includes a cooler) is out of stock everywhere, so Lean takes the **tray 7500F at 6 519** (Brain) plus an AK400; **Working + Max 9700X BOX 13 936** (Rozetka). 9600X dropped from every build; 7700X rejected - its 105W moves the cooler and eats the saving. Buy retail SKUs, never tray |
| [gpu.md](pc_build/components/gpu.md) | **Lean + Working 9070 GRE** 32 249 / **Max 9070 XT** 42 805 (a 5% promo). **RX 9070 non-XT excluded** - 2 806 under the XT for a slower card |
| [ram.md](pc_build/components/ram.md) | **Working + Max 32GB** DDR5-6000 CL36 (Crucial Pro 24 099 at Telemart) / **Lean 16GB** 2x8 15 599. CL30 not worth paying for - now on measured data, not AMD's |
| [storage.md](pc_build/components/storage.md) | **One 1TB NVMe, no built-in heatsink - tiered.** Lean **WD Green SN3000 6 999** / Working **990 EVO Plus 10 399** / Max **Kingston Renegade G5 11 999** (Gen 5, verified at Telemart, 400 *cheaper* than the 990 PRO and measurably faster). **The 990 PRO now has no build** |
| [motherboard.md](pc_build/components/motherboard.md) | **Lean ASRock B850M Pro RS WiFi** 6 965 / **Working ASRock B850 Pro RS WiFi** 8 829 / **Max conditional** - the same ASRock 8 829 if Telemart quotes the build, **ASUS TUF B850-PLUS WIFI** 9 399 if Brain does (their only shortlisted board). The undocumented MSI was dropped from Lean: no tier-1 review exists, and the ASRock is cheaper, tested and has more M.2. Wi-Fi 7 is worthless here - the router is Wi-Fi 5 with 100 Mbit ports |
| [psu.md](pc_build/components/psu.md) | **be quiet! Pure Power 13 M 750W** 5 419 (Telemart), all three builds. Same platform as the 850W it replaces and 4 dBA quieter; 650W rejected on connectors |
| [cooling.md](pc_build/components/cooling.md) | **Working + Max Deepcool AK400 1 699** (price-checked at both shops 2026-09-11; the old 1 515 was a non-assembling shop). ~~**Lean: no cooler**~~ - that rested on the 7500F **MPK**, AMD's multipack SKU and the only one bundling a Wraith Stealth. **It is out of stock at every shop checked 2026-09-11**, so Lean buys the tray chip and an AK400 too. Every build uses a 65W CPU, so the Phantom Spirit is not needed. No extra fans yet |
| [case.md](pc_build/components/case.md) | **Working + Max Lian Li Lancool 216** 4 949 (Telemart) / **Lean Deepcool CC560 V2** 2 280 |
| [monitor.md](pc_build/components/monitor.md) | **Working + Max AOC Q27G4ZR** 240Hz **8 669** / **Lean AOC Q27G4XF 6 899** - both Rozetka, in stock, per [price_check.md](pc_build/price_check.md) 2026-09-11. *(Corrected 2026-09-12 from the hotline figures 9 233 / 6 757.)* **Open:** the Philips 27M2N3501PA at 9 139 is listed as an identical-panel 260Hz option and has never been assessed |

**Peripherals are priced separately from the 130 000 build budget** and none of them has to
come from the shop that assembles the machine. One file each, in
[peripherals/](pc_build/peripherals). Candidates are priced and stock-checked at named shops
as of 2026-09-11. **All five are now settled** - keyboard 1 699, mouse 2 499, mat 299,
headphones 5 990, desk 2 994 = **13 481**, plus desk delivery at the carrier's rate.

| Doc | Where it stands |
|---|---|
| [keyboard.md](pc_build/peripherals/keyboard.md) | **SETTLED 2026-09-11: AULA F75 Pink Switch, wired, 1 699** (Brain / ITbox / Foxtrot / Telemart, identical price at all four). 75%, Kailh Pink linear, gasket, hot-swap, EN/UA. Parameters verified against six buying guides; numpad ruled out on checked use cases; two confirmed drawbacks (non-shine-through legends, unreliable vendor software) dismissed against actual use |
| [mouse.md](pc_build/peripherals/mouse.md) | **Closed 2026-09-11 (confirmed): Razer Cobra, 2 499** (Telemart, ITbox, Foxtrot - same price). Eight buyer's guides put **hand fit first and weight second**; the hand (19.0 x 10.0 cm) and the G102 in use set a 115-125 mm target. The Cobra is +3 mm on that shell at 58 g vs 85 g. Rules out the G502 family and the MX Master 3S on size. Wireless alternative: G305 X Superlight **3 628**. Open: nothing - buy at a shop with a service department, test the wheel inside 14 days |
| [mat.md](pc_build/peripherals/mat.md) | **Closed 2026-09-11: A4Tech X7-300MP, 299** (Telemart, Brain, ITbox). 437x350x3 mm, cloth, stitched edges - larger and 150 cheaper than the HATOR first picked. Basic is acceptable - stated by Dmytro - so the mat covers the mouse, not the desk. SHLab SHM-846 rejected: no shop read direct carries it, and one article number covers three sizes. Open: nothing |
| [headphones.md](pc_build/peripherals/headphones.md) | **SETTLED 2026-09-12: SteelSeries Arctis Nova 5 Wireless, from 5 990** (Rozetka; 6 799 Telemart/ITbox local). Closed-back, retractable boom, 265 g, ~60 h, wired fallback on 3.5 mm. Chosen on the only mic in the field endorsed by a measuring outlet for conference calls by name. Razer BlackShark V2 Pro and Barracuda X rejected on a documented cracking-frame record |
| [desk.md](pc_build/peripherals/desk.md) | **Closed 2026-09-11 (confirmed): Стіл Оптима L, 138x82x75, 2 994 + ~400 delivery (seller's claim, not a Rozetka quote)** (Rozetka, seller CyberStaff, 169 reviews). Found by Dmytro; 82 cm deep, 12 cm past the target, and cheaper delivered than the 2 587 desk this file had picked. Four earlier passes missed it because they searched "140x70" literally - a minimum depth was typed in as an exact figure. Open: 90-day warranty and a marketplace seller are accepted trade-offs |

Regenerate these prices with [`code/ua_prices.py`](../../code/ua_prices.py) against
[peripherals.json](pc_build/peripherals.json).

| Other | Contents |
|---|---|
| [builds.md](pc_build/builds.md) | The three settled builds costed per-part, with the shop for each price, plus the separate peripherals total. Generated - do not edit by hand. |
| [builds.py](pc_build/builds.py) | Price table + build definitions. **Rewritten 2026-09-12** onto named-shop prices and the three settled tiers; the old six-build hotline version is gone. Edit here, then regenerate. |
| [price_check.md](pc_build/price_check.md) | **Every part of all three builds priced at four named shops, 2026-09-11.** Telemart, Brain, Rozetka and Foxtrot read direct; hotline demoted to a directory of who stocks what. Confirmed totals and the five corrections they force. Regenerate with [`code/ua_prices.py`](../../code/ua_prices.py) against [parts.json](pc_build/parts.json) |
| [tools.md](pc_build/tools.md) | Benchmark sites, comparison tools, price aggregators, and what to distrust. Includes how to read commentary-free benchmark videos, whose numbers exist only as on-screen graphs. |

```bash
PYTHONUTF8=1 venv/Scripts/python.exe tasks/hardware/pc_build/builds.py > tasks/hardware/pc_build/builds.md
```

## The finding that shapes everything: the 2026 memory crisis

AI/HBM demand has pulled DRAM and NAND capacity away from consumer parts. Consumer DDR5 rose
~110% in Q1 2026 and NAND/SSD contract prices ~147%; TrendForce expects further rises through
Q3-Q4 2026, and relief is not expected before 2028.

Effect here: **32GB of RAM plus a 1TB SSD is ~33 000 UAH, over a quarter of the build.** The
same two parts were ~8 000 in 2024. That is roughly one GPU tier of purchasing power gone,
and it is why a 120k build in 2026 is not the machine a 120k build was two years ago.

It also settles the "should I wait" question: the forecast is up, not down.

## Candidate builds A-F (superseded 2026-09-10, kept for the reasoning)

These six builds and the Build F recommendation below predate the three-build table above and
are priced at hotline floor prices. They are kept because the upgrade-ladder reasoning is still
sound; the numbers and the conclusion are not. Read the three builds above instead.

Cheapest = lowest hotline.ua offer, 2026-09-09. Realistic = +7% for buying at a proper
retailer with a service department. Full part lists in [builds.md](pc_build/builds.md).

| Build | Cheapest | Realistic | What it is |
|---|---:|---:|---|
| A. Value floor | 105 715 | ~113 100 | 9700X, cheapest measured-acceptable parts throughout. |
| C. Optimum, trimmed | 115 085 | ~123 100 | 9800X3D, but with the unmeasured ASRock GPU and the weak-VRM/1GbE board. |
| **F. Recommended balance** | **124 375** | **~133 100** | **The pick.** Every part measured-good; 1TB instead of 2TB and a plain case to hold the price. |
| B. Build-logic optimum | 135 713 | ~145 200 | Every component doc's verdict with no ceiling applied. |
| D. NVIDIA path | 151 912 | ~162 500 | Now has a real argument - see the FSR frame-pacing finding. |
| E. No-compromise ceiling | 149 750 | ~160 200 | Reference: Sapphire PURE, 4K monitor, RM850x, 2TB 990 PRO. |

**The honest headline: evidence-based part selection pushed this build past your original
ceiling.** Not because I lost discipline - because three of my cheap picks turned out to be
either unmeasured or defective, and the replacements cost money. The 100-120k band buys build
A or C in 2026; the build I would actually put in your room is F at ~133 000 realistic.

## What the deep review pass changed (2026-09-09)

The first pass picked parts on price, popularity and spec sheets. A dedicated pass then read
the actual reviews, lab data and retailer failure statistics per model. **Five of my nine
picks changed.** Recorded here because the pattern matters more than the parts: the cheap
option that looks fine on a spec sheet is often the one nobody has measured.

| Component | Was | Now | Why |
|---|---|---|---|
| **PSU** | ASUS TUF 850W Gold EVO | **be quiet! Pure Power 13 M 850W** | The EVO measures **29.4 dBA, LAMBDA A-, no fan-stop mode, 55 mV ripple**, 8-year warranty. The be quiet! is **A++ at 10.65 dBA**, FSP-built, best transient on the list - and 380 cheaper. |
| **Storage** | Kingston KC3000 1TB, NV3 as budget | **Samsung 990 PRO 2TB** | The NV3 ships **four different controllers and TLC-or-QLC under one SKU**; the KC3000 appears end-of-life. The 990 PRO leads QD1 random read, the metric this workload lives on. |
| **Motherboard** | GIGABYTE B850 EAGLE | MSI MAG B850 TOMAHAWK WIFI *(since superseded)* | The EAGLE ran **over 80 C** and has **1 GbE only**. The MSI was then believed to measure 58 C; **TechSpot's completed 47-board test puts it at 64 C** and the board is off the list - see [motherboard.md](pc_build/components/motherboard.md). |
| **RAM** | GOODRAM CL30 (23 455) | **Corsair Vengeance CL36 EXPO** (22 389) | AMD's own 30-game data: DDR5-4800 vs 6000 differs ~1% on an X3D chip. CL30 is not worth 1 750, and the GOODRAM 6000 CL30 2x16 SKU could not be found in GOODRAM's own catalogue. |
| **Monitor** | AOC Q27G3XMN mini-LED as the upgrade | **withdrawn entirely** | It is **VA, not IPS** as I claimed, has the **worst VRR flicker RTINGS had measured**, coil whine, broken DDC/CI over DisplayPort and no firmware support. My worst call of the first pass. |
| **GPU model** | PowerColor Reaper | **PowerColor Hellhound** | Retailer data: the **Reaper has the worst RMA rate of any 9070 XT at 3.28%**; the Hellhound has **0.47% across 4 340+ units**, the best of any high-volume model. |
| Also withdrawn | GIGABYTE G27Q20, ASUS VG27AQ5A, GIGABYTE B650 GAMING X, ~~ASRock B850 Pro RS~~ | - | The two monitors have **no credible measurements anywhere** (and the ASUS has no height adjustment). The B650 has no tier-1 review and owner RMA reports. **The ASRock board was reinstated** once the 9800X3D left every build - the ~82% failure share is X3D-only, and no tier now runs an X3D chip. |

Two claims of mine were also corrected rather than replaced:

- **The X3D is a gaming purchase, not a work upgrade.** Phoronix data at equal power: the
  9800X3D is 6-10% faster on compiles, **4-6% slower single-threaded**, and **4.5% slower on
  git**. A 9950X is 58-65% faster on compiles than either. The one dev workload where V-Cache
  is transformative is local databases (pgbench read-only +116%).
- **The Zen 6 upgrade path is not guaranteed.** The socket is supported through 2029 and
  Olympic Ridge is assigned to AM5 in AMD's docs, but board BIOS support is per-vendor and
  flash-capacity constrained. Treat it as plausible, not promised.

### What the specification pass corrected (2026-09-09)

Writing the datasheets out in full caught two errors that the verdict-first format had hidden:

- **CPU peak power was understated in the PSU sizing.** The load table used the 9800X3D's
  **120W TDP**, but TDP is a cooling-design figure - the chip's actual power limit (PPT) is
  **162W**. Build peak is ~530W, not ~485W. The 850W recommendation is unaffected; the
  arithmetic behind it now matches.
- **Phantom Spirit 120 SE height: 154mm, not 157mm.** Thermalright's own spec sheet says
  125 x 110 x **154mm**; several retailers list 157mm, which is the near-identical EVO.
  Immaterial in practice - the Lancool 216 clears 180.5mm - but the number was wrong in three
  files.

## The upgrade ladder: A to F, item by item

Every step is a separate yes/no, ordered by how much I think it is worth. Stop anywhere.

| # | Step | Cost | Why it earns its money |
|---|---|---:|---|
| 1 | 9700X -> **9800X3D** | +8 040 | The only part you cannot upgrade later without replacing it, and it sets your 1% lows for years. Now honestly labelled: a gaming purchase. |
| 2 | ASRock -> **PowerColor Hellhound GPU** | +4 100 | **0.47% vs unmeasured acoustics** - and 29.0 dB(A), PTM7950, ball-bearing fans, no 12V-2x6. The best-evidenced part in the build. |
| 3 | 180Hz -> **240Hz monitor** | +2 794 | Both are measured and good; 240Hz is the last visible step, on the part that outlives the PC. |
| 4 | EAGLE -> **ASUS TUF B850-PLUS** | +2 396 | 14+2+1 80A VRM, Wi-Fi 7, 2.5 GbE instead of gigabit. |
| 5 | AK400 -> **Phantom Spirit 120 SE** | +1 330 | Required by the 120W X3D chip. Measured: 124W on AM5 at 36.4 dBA. |
| 6 | TUF 850G -> **Pure Power 13 M** | +733 | 10.65 dBA vs no lab data at all. The cheapest genuinely-justified upgrade here. |
| | **Total A -> F** | **+19 393** | **= 125 108** |
| 7 | 1TB -> **2TB 990 PRO** | +6 150 | Comfort, in the year NAND is structurally expensive. |
| 8 | CC560 -> **Lancool 216** | +2 387 | Gamers Nexus's out-of-box CPU co-leader. Quieter all day. |
| 9 | ~~TUF -> **MSI Tomahawk board**~~ | +998 | Withdrawn: the Tomahawk measures **64 C against the TUF's 54 C**, so this step buys 5 GbE and ALC4080 on a *warmer* board - and 5 GbE is useless on a 100 Mbit router. |
| 10 | Crucial -> **Corsair Vengeance EXPO** | +690 | Deepest AM5 QVL presence. Boots first time. |
| | **Total A -> B** | **+29 618** | **= 135 333** |

## Recommendation (superseded 2026-09-10)

> Replaced by the **Working build at 117 200** in "Where it stands". Build F was one of the
> six GPU-tiered candidates above, priced at hotline floors. The reasoning below on why the GPU
> choice is well-evidenced still holds.

**Build F, at 125 108 cheapest / ~133 900 realistic.**

Reasoning, after the deep pass rather than before it:

1. **The GPU choice is now the best-evidenced decision in the build.** No CUDA need, and the
   RX 9070 XT measures at raster **parity** with an RTX 5070 Ti at 1440p (ComputerBase, 23
   games: 100.5 vs 100.1 FPS) for 12-16k less. Within the 9070 XT models, the Hellhound has
   the lowest failure rate of any high-volume card (0.47%), verified 29.0 dB(A), PTM7950 and
   no 12V-2x6 connector.
2. **The money went where measurements justified it**, not where the spec sheets pointed:
   into a PSU that is 19 dBA quieter than my first pick, an SSD whose internals are knowable,
   a board with a measured VRM temperature and 5 GbE (that board has since been dropped - it
   measures 64 C, and 5 GbE is useless on a 100 Mbit router), and a GPU model with field-failure
   data behind it.
3. **The X3D stays, relabelled.** It is a gaming purchase - the compile gain is 6-10% at
   equal power and git is actually slower. If you would rather have the 8 040, build A is
   honest and the machine is still fast.
4. **One genuine argument against the whole plan:** FSR frame generation has a measured,
   unfixed frame-pacing defect (one frame shown ~4x longer than the next; V-Sync does not
   help). If you intend to lean on frame generation, the NVIDIA path (build D, ~162k
   realistic) is the answer. At 1440p with this card you should not need to.

Explicitly rejected, with reasons on file: RTX 5070 Ti (no CUDA need), RTX 5070 and RX 9070
GRE (12GB), Ryzen 9 9950X/9950X3D (work is not 16-core), OLED and mini-LED monitors,
64GB RAM (59 486 at crisis pricing), X870 boards, and every part for which no
independent measurement exists.

### Buy-day checklist that came out of this research

- **Flash the motherboard BIOS before first real use**, then enable EXPO. The worst 9800X3D
  outcomes cluster on stale firmware.
- **Check the GPU hotspot in the first hour.** Over ~100 C means a bad die-contact unit -
  return it inside the window.
- **Use DisplayPort, not HDMI**, for the monitor: these panels cap at 144Hz over HDMI 2.0.
- **Set the GPU to its silent BIOS** and leave PBO alone.
- **Check the SSD's SMART health on arrival**, then stop updating its firmware.
- **Verify the exact SKU**: MSI A850**GLS** not A850GL; SeaSonic Focus GX-850 **ATX 3.1** not
  3.0; ASUS **TUF** B850-PLUS not **Prime**; Samsung 990 PRO **2TB**.
- Handle the AM5 socket carefully - bent pins are the one failure mode proven to kill both
  CPU and board.

## How these lists were built, and what that limits

Stated plainly so the numbers can be judged rather than trusted.

**Prices - first-hand, one snapshot.** Every UAH figure comes from
[hotline.ua](https://hotline.ua/ua/computer/) fetched directly on **2026-09-09**: the
category listings (GPUs, CPUs, boards, RAM, SSDs, PSUs, coolers, cases, monitors) plus
keyword searches for specific families. Figures are the **lowest offer** in the aggregator,
which is often a small shop - hence the +7% "realistic retail" column. No individual shop was
named per SKU; that check happens at purchase time.

**Model lists - broad, not exhaustive.** hotline's GPU category alone holds 778 products and
257 RX 9070 XT entries. What is in these docs is what surfaced across the category pages
(sorted by popularity) and the targeted searches - which reliably catches every *chip* and
the mainstream board-partner models, but will miss individual rare SKUs. If a shop offers
something not on the list, it is not disqualified; ask and I will price it.

**Performance and noise claims - second-hand.** TechPowerUp, Tom's Hardware, cpu-monkey and
nanoreview all block automated fetching (HTTP 403), so their figures reached these docs via
**search-result summaries of those pages**, not by reading the pages themselves. That is
enough for "24 dBA", "9% at 1440p", "Cybenetics Lambda A-" - but before buying, open the
review page for the specific model and confirm. The links are all in the Sources section.

**Weakest inputs, flagged honestly.** The 2026 search landscape is full of SEO sites
(FPS calculators, bottleneck calculators, "best GPU 2026" aggregators). Claims that appear
*only* in those - the VRAM thresholds, some of the 1440p-vs-4K text-clarity argument - are
directionally right and consistent across sources, but they are not lab measurements.
[tools.md](pc_build/tools.md) lists which sources to distrust and why.

**One error this produced, corrected.** I first recommended the PowerColor **Reaper** on the
strength of a 24 dBA measurement that actually belongs to PowerColor's **Hellhound** (the
review covers the "Reva Hellhound"). Reaper is the entry-level cooler and has no published
measurement. The verdict now names the Hellhound (41 800) or the Sapphire PULSE (42 499),
which changed build B by +1 640.

## Deep learning on AMD - the parked question

Flagged as a *possible future* need, not a requirement. Recorded so the reasoning does not
have to be rebuilt later.

- **ROCm 7.2 (March 2026)** is the first release with **official** support for the RX 9070 /
  9070 XT (gfx1201). On Linux, PyTorch training and inference are fully supported.
- **On Windows** native ROCm for ML is effectively not supported. The supported route is
  **WSL2**, through AMD's ROCDXG (librocdxg) translation layer, which has production support
  for PyTorch on Radeon under WSL; an RX 9070 XT is confirmed working there. Ollama,
  llama.cpp and ComfyUI/Stable Diffusion also run on ROCm.
- **Where it hurts**: anything shipping hand-written CUDA kernels - flash-attention,
  bitsandbytes, xformers, a large share of fresh research repos - lags or never works.
  Mainstream PyTorch is fine; following a new paper's repo is friction.
- **Both candidate cards have 16GB**, which is entry-level for real training either way.
- **The GPU is the most replaceable and resellable part of the build**; CPU, board and RAM
  are not. Buying NVIDIA now to cover a need that may arrive in 2028 pays a 12 200 premium
  for an option a 2028 card would serve better.
- **Plan if DL arrives**: mainstream work through WSL2 + ROCm; actual training runs on a
  rented cloud GPU (a few dollars an hour, many times faster than any card in this budget);
  if it becomes daily work, sell the card and buy the NVIDIA of that year.

## Open questions

1. **Which of the three builds?** Lean 92 092, Working 117 059 (the recommendation) or Max
   126 199. **Only one item in "Still open" above is still open** - item 4, the written quotes
   from Brain and Telemart. Items 1, 2 and 5 are settled and item 3 is advisory, so nothing
   blocks a quote but the quote itself. *(Count corrected 2026-09-12; it read "four".)*
2. ~~**Text quality vs frame rate**~~ **Closed 2026-09-11.** Dmytro refused 4K outright. Both
   monitors confirmed as they stand - **Lean Q27G4XF 6 899, Working + Max Q27G4ZR 8 669, both
   at Rozetka and both in stock**, which is what the build table above uses. *(Corrected
   2026-09-12: this paragraph quoted 6 757 and a 9 687 "floor", hotline figures that the
   2026-09-11 named-shop pass superseded - see [price_check.md](pc_build/price_check.md).)* Buy the monitor from any shop: it is a peripheral, so the
   one-store assembly constraint does not reach it, and neither AOC is stocked at Brain or
   Telemart though a dozen other shops carry both. See
   [monitor.md](pc_build/components/monitor.md).
3. ~~**The five peripherals**~~ **Closed 2026-09-11/12.** Keyboard AULA F75 1 699, mouse
   Razer Cobra 2 499, mat A4Tech X7-300MP 299, headphones Arctis Nova 5 5 990, desk
   Стіл Оптима L 2 994 - **13 481** plus desk delivery. One file each in
   [peripherals/](pc_build/peripherals); each records what was rejected and why.
4. ~~**Assembly**: self-build or paid?~~ **Answered:** Dmytro will not build it himself, so
   one store must supply and assemble everything. Brain gives 36 months on the assembly if all
   parts are bought there; Telemart charges 299 UAH + 1% but warrants the assembly for 14 days.

## Sources

**Prices in the three-build table come from [price_check.md](pc_build/price_check.md) - four
shops read direct, 2026-09-11.** The hotline sweep below was the original 2026-09-09 pass and is
kept only as the record of how the field was found; hotline is a directory of who stocks what,
not a price. *(Clarified 2026-09-12: this section previously presented hotline as the price
source for the whole document, contradicting price_check.md.)*

Original field sweep: [hotline.ua](https://hotline.ua/ua/computer/), all categories, 2026-09-09.

Market and evidence: [Tom's Hardware on the memory price
surge](https://www.tomshardware.com/pc-components/ram/memory-price-surge-begins-to-cool-as-consumers-hit-affordability-limit-ai-demand-still-keeps-dram-and-nand-prices-climbing-through-q3-2026)
- [Wccftech memory crisis roundup](https://wccftech.com/roundup/memory-crisis/)
- [TechPowerUp: RX 9070 XT gains 9% at 1440p with newer
drivers](https://www.techpowerup.com/338591/amd-radeon-rx-9070-xt-gains-9-performance-at-1440p-with-latest-driver-beats-rtx-5070-ti)
- [TechPowerUp Sapphire RX 9070 XT Pulse review](https://www.techpowerup.com/review/sapphire-radeon-rx-9070-xt-pulse/44.html)
- [TechPowerUp PowerColor RX 9070 XT Reva review](https://www.techpowerup.com/review/powercolor-radeon-rx-9070-xt-reva-hellhound/40.html)
- [Tom's Hardware best CPUs](https://www.tomshardware.com/reviews/best-cpus,3986.html)
- [XDA: 9800X3D vs 9700X](https://www.xda-developers.com/ryzen-7-9800x3d-vs-ryzen-7-9700x/)
- [Tom's Hardware: AMD confirms AM5 support through 2029](https://www.tomshardware.com/pc-components/cpus/amd-confirms-am5-support-through-2029-zen-4-and-5-platform-will-likely-see-two-more-generations-at-least)
- [Newegg: DDR5-6000 CL30 is the AM5 sweet spot](https://www.newegg.com/insider/ddr5-memory-buying-guide-for-am5-why-6000-cl30-is-the-sweet-spot/)
- [Cybenetics: ASUS TUF Gaming 850W Gold EVO evaluation](https://www.cybenetics.com/evaluations/psus/3165/ch/)
- [Hardware Busters PSU picks 2026](https://hwbusters.com/best_picks/best-atxv3-pcie5-ready-psus-picks-hardware-busters/)
- [TechSpot: FSR 4.1 tested vs DLSS](https://www.techspot.com/article/3102-amd-fsr-41-tested/)
- [OC3D Lancool 216 review](https://overclock3d.net/reviews/cpu_mainboard/lian_li_lancool_216_pc_case_review/3/)
- [OC3D: RTX 50 SUPER targeting CES 2027](https://overclock3d.net/news/gpu-displays/nvidia-rtx-50-super-series-targets-ces-2027-launch-report-claims/)

Full tool list, and which sources to distrust, in [tools.md](pc_build/tools.md).

## Balance audit, build by build (2026-09-11)

Checking each build for internal balance rather than per-part merit: is anything over- or
under-specified for what sits next to it, and does everything physically fit. Bottleneck
*calculator* sites were rejected as sources - they are estimates, not measurements, and two of
them gave contradictory numbers for the same pair.

### LEAN - 85 287

**Compatibility: clears, with margin on every dimension.**

| Constraint | Limit | Part | Margin |
|---|---|---|---|
| GPU length | CC560 V2: **370mm** | Hellhound 9070 GRE ~327mm | 43mm |
| CPU cooler height | CC560 V2: **165mm** | Wraith Stealth (low-profile) | large |
| PSU length | CC560 V2: **170mm** | Pure Power 13 M: 160mm | 10mm |
| Motherboard | CC560 V2 takes ATX / mATX / ITX | ASRock B850M Pro RS WiFi (mATX) | fits |
| GPU power | PSU has 4x 6+2-pin | GRE needs **2x 8-pin**, 220W | 2 spare |
| Case fans | needs 2 intake + 1 exhaust | 3x 120 front + 1x 120 rear | met |

**CPU-to-GPU: correctly matched.** The 7500F holds **95%+ of an RX 9070 XT** in the aggregated
public sample sets; the GRE is a slower card than the XT, so at 1440p the GPU is the limit and
the CPU is not the thing holding this build back. Six cores is the right size for this card.

**Cooler: verified adequate, not guessed.** Owner testing of the 7500F on its bundled Wraith
Stealth reports **65 C typical and under 70 C in demanding games**. The caveat is explicit: it
is adequate **at stock only** - no PBO, no overclocking. That matches how this build is
specified, and it is why the AK400 is not bought here.

**The one genuine imbalance: 16GB of RAM.** Not because average frame rate suffers - that
difference is a couple of percent - but because when a 16GB system runs out, Windows pages to
the SSD and **1% lows collapse**, which is the number you feel as stutter. And this is the one
Lean compromise that is **expensive to reverse**: DDR5 will not take four sticks at speed and
kits must not be mixed, so going to 32GB later means re-buying the whole kit, not adding to it.
The jump to the Working build's 32GB costs **+8 500** - 10% of this entire build.

**Over-specified, deliberately: the 750W PSU** against a measured **~373W** peak - 50% load.
That is not a fault (see [psu.md](pc_build/components/psu.md): one PSU SKU across all three
builds, and the 650W was rejected on connector count for only ~500 less), but it is the least
Lean-like line in the Lean build.

**Also noted, not a defect:** the board (6 965) costs more than the CPU (6 589), which breaks
the usual rule of thumb. It is the floor for AM5 with mandatory Wi-Fi, so there is nothing to do
about it - but it is a sign this tier's money sits in the platform rather than in performance.

**Verdict: balanced, with one real weak point.** Everything fits, nothing is throttled by
anything else, and the only component that will visibly limit the machine is the 16GB kit - a
choice this tier makes knowingly, and the only one that cannot be fixed cheaply later.

#### Lean audit cross-checked against four build guides (2026-09-11)

Sources: ScatterVolt *PC Parts Explained* (2025-09), GamingScan *How To Make Sure All Your
Hardware Parts Are Compatible* (2020), JayzTwoCents *Common PC Building Mistakes* (2021),
optimum *Avoid These PC Build Mistakes* (2022). None measures anything; two are assembly-process
videos. They confirm two of the audit's conclusions, correct a third, and add one handover item.

**Confirmed - the CPU pairing, by name.** ScatterVolt: a **"Ryzen 5 7500F or even 9600X can
handle pretty much any modern-day GPU that isn't an RTX 5090"**, and the people who need to
worry about bottlenecks are "those who are going to exclusively play at 1080p on very easy to
run PC games like Valorant, Counter-Strike 2, or Fortnite". This build is 1440p. The audit's
"the GPU is the limit and the CPU is not" stands, now with the exact chip named.

**Confirmed - 16GB is the weak point.** ScatterVolt's flat answer for DDR5 is **"32GB, that's
all you need"** - stated as the target, with no budget exception offered. Third independent
source saying the same thing.

**Correction - the 750W PSU is not over-specified.** The audit called it "the least Lean-like
line in the Lean build". GamingScan's rule is that **power supplies are at their best operating
between 50% and 80% of maximum capacity**; Lean's measured ~373W peak against 750W is **~50%** -
the bottom edge of that band, not outside it. ScatterVolt's rule points the same way: take the
GPU maker's recommended wattage and add ~100W for safety. The 750W is correctly sized, and the
earlier remark is withdrawn.

**Frame check (not transcript-only).** Stills pulled at the bottleneck, RAM and PSU sections of
the ScatterVolt video and the PSU section of GamingScan's. Three of the five frames are
talking-head or b-roll with no data. **One carries a claim the audio never states:** an
on-screen card reading **"AM5 ideal RAM kits: 6000MHz CL30 DDR5 / 6000MHz CL28 DDR5"**. This
build buys **6000 CL36** on Working and Max. It is not an oversight - [ram.md](pc_build/components/ram.md)
does the arithmetic (CL36 at 6000 = **12.0 ns**, CL30 = **10.0 ns**) and prices the 2 ns at
**1-4% in games, mostly in 1% lows, near nothing in tooling, for 1 750**. Recorded as a third
source preferring CL30, and overruled on the same measured grounds as before.

**Added to the handover, because a shop assembles this machine:** a 2-stick DDR5 kit **must go
in the second and fourth DIMM slots** (A2/B2) or it runs single-channel - the most common
build error in all four videos, and the one with the largest silent performance cost. Worth
stating explicitly on the order, and worth verifying in BIOS on collection. The remaining
mistakes these videos cover - thermal paste quantity, paste in the socket, standoffs, front
panel headers, GPU clearance against drive cages - are the assembler's responsibility under
the warranty, not ours.

### WORKING - 114 859

**Compatibility: clears everywhere, wider margins than Lean.**

| Constraint | Limit | Part | Margin |
|---|---|---|---|
| GPU length | Lancool 216: **392mm** | Hellhound 9070 GRE ~327mm | 65mm |
| CPU cooler height | Lancool 216: **180.5mm** | Deepcool AK400 ~155mm | 25mm |
| PSU length | ample | Pure Power 13 M 160mm | - |
| Motherboard | Lancool 216 takes ATX | ASRock B850 Pro RS WiFi (ATX) | fits |
| GPU power | 4x 6+2-pin available | GRE needs 2x 8-pin, 220W | 2 spare |
| Case fans | 2 intake + 1 exhaust needed | 2x 160 front + 1x 140 rear | met |
| PSU load | best at 50-80% of rating | ~373W peak / 750W = **50%** | in band |

**This build is not a faster gaming machine than Lean - by design.** It carries the **same
RX 9070 GRE**. At 1440p both builds are GPU-bound, so the +8 510 spent on the CPU (9700X 15 099
against 7500F 6 589) buys **almost nothing in games** and buys the actual brief instead: **8
cores against 6, Zen 5 against Zen 4**, for compiles, containers and everything that runs while
a game does not. [pc_build.md](pc_build.md) states this openly - "the money goes into the
platform, not the card" - and the audit confirms the machine matches that statement rather than
contradicting it.

**Two things the 9700X adds beyond cores**, both relevant to a work machine and both absent on
Lean:

- **An iGPU (2-CU RDNA 2).** The 7500F has none. With the graphics card pulled, this machine
  still posts to a display - the diagnosis path Lean has to solve with debug LEDs.
- **65W with a 5.5GHz boost**, which is what lets the AK400 be a single tower rather than the
  dual tower a 105W 7700X would have forced ([cooling.md](pc_build/components/cooling.md)).

**RAM is correctly sized here and is the main reason to prefer this tier.** 32GB removes the one
failure mode the Lean audit identifies - paging to the SSD and 1% lows collapsing - and DDR5
cannot be staged later, so this is the tier where the memory decision is actually made.

**The one internal inconsistency: the 240Hz monitor.** Working spends **+2 930** over Lean's
panel on the Q27G4ZR, driven by **the same GPU** that Lean pairs with a 180Hz screen. A 9070 GRE
does not reach 240 fps at 1440p outside esports titles, and this is the tier whose justification
is work rather than gaming. It is defensible on panel quality - **400 cd/m2 against 300, 0.3 ms
against 0.5 ms** - and that is now the recorded reason
([monitor.md](pc_build/components/monitor.md)); it is not defensible on refresh rate. Dmytro has
ruled the tiers must differ, so the line stays.

**Verdict: balanced and coherent for its stated purpose.** Nothing throttles anything else,
every clearance has margin, and the money sits where the brief says it should - CPU, memory,
case and board rather than the card. The one line that does not follow the brief is the monitor,
and it is a deliberate tier separator rather than an error.

### MAX - 124 279

**Compatibility: clears, and the power picture changed when the XT left the build.**

| Constraint | Limit | Part | Margin |
|---|---|---|---|
| GPU length | Lancool 216: **392mm** | Sapphire PURE RX 9070: **320mm**, **3 slots** | **72mm** - verified against Sapphire's spec, not assumed |
| CPU cooler height | 180.5mm | AK400 ~155mm | 25mm |
| Motherboard | ATX | ASRock B850 Pro RS WiFi (or ASUS TUF) | fits |
| GPU power | 4x 6+2-pin | **2x 8-pin, no 12V-2x6** | 2 spare |
| Gen 5 SSD | board M2_1 is **PCIe 5.0 x4 from the CPU** with a heatsink | Kingston FURY Renegade G5 | correct slot, cooled |

**Sourcing of this audit, stated so it can be checked:** clearances from
[case.md](pc_build/components/case.md); the card's 220W / 2x 8-pin / +18% from
[gpu.md](pc_build/components/gpu.md); the drive's pricing and test result from
[storage.md](pc_build/components/storage.md); the power figures from
[psu.md](pc_build/components/psu.md). **The card's 320mm length and 3-slot width come from
Sapphire's own specification, checked 2026-09-11** - it was asserted before that and is now
verified. **The claim that Max draws the same as Working is arithmetic, not a measurement:**
both builds now use a 220W card on the same platform, so the documented 373W Working figure
carries across. No wall measurement of this configuration exists.

**The power budget in [psu.md](pc_build/components/psu.md) is now conservative for this build.**
Its Max figures - 463-483W, 62-64% of 750W - were computed against a **304W RX 9070 XT** drawing
through **3x 8-pin**. The Max build no longer uses that card: the **Sapphire PURE RX 9070 is
220W on 2x 8-pin**, identical to the GRE in the other two builds. **Max therefore draws the same
~373W as Working**, not 483W, and sits at the same ~50% of the 750W supply. Nothing to change -
but the "Max is the build that needs the headroom" reasoning no longer applies, and the 750W is
now sized by the other two builds rather than by this one.

**What Max actually buys over Working, in full:** a **16GB RX 9070 instead of a 12GB GRE**
(+7 820, **+18%** at 1440p and four more gigabytes of VRAM) and a **Gen 5 Renegade G5 instead of
the 990 EVO Plus** (+1 600). Nothing else differs. That is a clean, single-axis upgrade - unlike
the Lean-to-Working step, which changes CPU, RAM, case, board and monitor at once.

**The SSD step is not a tax.** [storage.md](pc_build/components/storage.md) records the Renegade
G5 as **cheaper than the 990 PRO at the same shop** while being the fastest of the three on the
real-world system-drive test, and the board's first M.2 is a CPU-attached Gen 5 slot with a
heatsink, so the drive is in the right place and cooled. The only caution is the general one for
Gen 5 drives - they run hot, and this one is under the board's heatsink rather than its own.

**The VRAM step is the real argument for this tier.** 12GB is the figure this project criticised
NVIDIA's RTX 5070 for; the GRE carries the same 12GB in Lean and Working. Max is the only build
that resolves that, and VRAM is the one spec that cannot be worked around later without
replacing the card.

**Verdict: the most internally consistent of the three builds.** Same platform as Working, one
axis of improvement, power draw identical, every clearance met, and the money goes to the part
that is hardest to upgrade afterwards. The open item is not internal - it is that the Max board
is still conditional on which shop quotes ([motherboard.md](pc_build/components/motherboard.md)).

#### Bottleneck check on Max, done explicitly (2026-09-11)

The Lean audit's pairing finding was carried across to Working and Max without being checked for
those builds. Doing it properly:

**The calculator sites are useless here, and this is the evidence for saying so.** Asked about
the same pair - **Ryzen 7 9700X + RX 9070 at 1440p** - they return:

| Site | Verdict |
|---|---|
| One | "excels at 1440p and **won't bottleneck any modern GPU**", minor *GPU* limitation |
| Another | an estimated **21% CPU bottleneck**, "the CPU significantly limiting the build" |
| A third | "performance balance behavior in the current public sample set" |

Three answers, same inputs, no methodology published by any of them. They are excluded as
sources, consistent with [tools.md](pc_build/tools.md).

**What can be said from evidence:**

1. **ScatterVolt, on record:** a **Ryzen 5 7500F** "can handle pretty much any modern-day GPU
   that isn't an RTX 5090", and bottlenecks matter to people playing **1080p esports**. The
   9700X is a faster chip than the 7500F and this build targets 1440p.
2. **The internal comparison settles it more cleanly than any external source.** Max runs the
   **same 9700X as Working** with a GPU only **18% faster** than Working's. A faster card moves
   a system *toward* CPU-limited, so Max is marginally closer to it than Working is - but 18% is
   a small step, and both sit at 1440p where the card is the limit.
3. **The tier above is where it would start to matter.** psu.md's note that only a 400W-class
   future card changes the power picture applies to the CPU question too: a card materially
   faster than the 9070 would be the first point at which the 9700X is worth re-examining.

**Conclusion: no CPU bottleneck in Max at 1440p, and the CPU is the part with headroom rather
than the part running out of it.** Recorded with its sources rather than asserted, because the
first version of this audit asserted it.
