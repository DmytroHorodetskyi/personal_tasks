# PC build, up to 130k UAH (work + 1440p gaming)

Choosing and optimising a complete new desktop plus monitor for Dmytro, bought new in
Ukraine. Started 2026-09-09.

> **Shop settled 2026-09-13: Dmytro buys at click.ua.** Every price in this file below this
> banner was read at Telemart, Brain, ITbox, Foxtrot or Rozetka, because `code/ua_prices.py`
> contacted four shops and click.ua was not one of them. **The live basket is
> [click_basket.md](pc_build/click_basket.md)** and the costed builds are
> [builds.md](pc_build/builds.md); both are click.ua prices, stock-checked 2026-09-13.
>
> click.ua does not stock five of the parts chosen here - the **RX 9070 GRE**, the **Crucial Pro
> 2x16 CL36** kit, the **be quiet! Pure Power 13 M 750W**, the **Lancool 216** and both **AOC**
> monitors - and carries **no BOX AM5 CPU** at all. The substitutions, and the reasoning for
> each, are in click_basket.md. Current totals: **Lean 94 475 / Working 129 581 / Max 142 245**.

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
| UPS / power backup | **Parked** by Dmytro - to be discussed with a specialist, not researched here. **The seven UPS videos he sent are read and quoted anyway**, in [source_audit.md](pc_build/source_audit.md) → "UPS - 7 of 7 read IN FULL": `1oNdbI8NFgk` `JL71IH5HShI` `NyfoqRIFg4k` `fiKra9BXqoA` `gFCOowZV3Cw` `hebLFKBSEd4` `ovZAbCqh_A0`. They are the only videos in the project with no component document, because the component has none. **If it is ever unparked, the sizing arithmetic, the line-interactive verdict and the shutdown-over-USB requirement are already worked out there - do not re-research it.** |

Missing from the original list and added: **SSD**, **Windows licence**, **keyboard**.
Also flagged: a chair matters more than the desk for all-day work.

## Where it stands

**THREE BUILDS, SETTLED 2026-09-10.** Tiered on the whole machine, not on the graphics card.
Every earlier version of this table tiered on the GPU alone, which cannot work: the shared
platform is ~85 000 of a ~125 000 build, so a 3-10 000 card difference produced "tiers" that
landed within a few thousand of each other. Dmytro rejected four such versions before this one.

**Superseded by [click_basket.md](pc_build/click_basket.md) - the table below is the Telemart
basket of 2026-09-11, kept because the rest of this document argues against it.**

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
| Monitor | **ASGARD AS275QC 6 999** (click.ua / Foxtrot) | **ASGARD AS275QC 6 999** | **ASGARD AS275QC 6 999** |
| Windows 11 Home | **7 098** (Brain) | **7 098** | **7 098** |
| **Total** | **92 192** | **115 389** | **124 529** (125 286 with the TUF) |

**Every source Dmytro sent is being re-checked against these docs - [source_audit.md](pc_build/source_audit.md)**, with transcripts in `pc_build/sources/` and frames in `pc_build/frames/`. 10 of 99 videos done; one wrong figure found and corrected so far.

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

- **Lean, 92 192** - the weakest that still meets the requirements. Six cores, 16GB, 1440p on
  the GRE, a measured budget panel. It accepts a full RAM re-buy later (DDR5 will not take four
  sticks - see [ram.md](pc_build/components/ram.md)), no iGPU for diagnosis with the card
  pulled, occasional stutter in a handful of AAA titles at 16GB, and 12GB of VRAM.
- **Working, 115 389** - the money goes into the **platform**, not the card: eight cores for the
  tooling, 32GB, the 240Hz panel, the measured-quiet case. Same GPU as Lean. This is the build
  for a work-first machine and it is the recommendation.
- **Max, 124 529** - the **RX 9070 16GB** over the Working build: **+18% GPU and 16GB of VRAM
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
6. **The ASRock brand-risk paragraph contradicts the build.**
   [motherboard.md:103](pc_build/components/motherboard.md) withdrew the ASRock B850 Pro RS **"on
   brand risk, not hardware"**, on a 2025 Reddit megathread of ~108 CPU failures - while all three
   tiers ship an **ASRock B850 Pro RS WiFi**. One of the two has to move. A May 2026 brand survey
   (Socket-X, 406k views) says the old reputation *"doesn't really fit anymore"* and raises no
   reliability concern in its ASRock section. Raised by the source audit 2026-09-13.

7. ~~**Front USB-C header never checked against the case.**~~ **CHECKED AND CLOSED 2026-09-13,
   against both manufacturers' own spec pages - the port works.** ASRock lists
   *"1 x Front Panel Type C USB 3.2 Gen2x2 Header (20 Gb/s)"* on the B850 Pro RS WiFi; AeroCool
   lists the D502A's front I/O as *"Type C x 1 | USB3.0 x 2 | HD Audio & Mic."* Header present,
   port present, they mate. **Three clearances confirmed in the same pass**, all comfortable:
   **CPU cooler up to 171mm** (AK400 is 155mm), **GPU up to 400mm** without a front radiator
   (Sapphire 9070 PURE ~320mm), **PSU up to 220mm including cables**.

8. ~~**Gen 5 NVMe heat and M.2 lane sharing, unconfirmed.**~~ **CHECKED AND CLOSED 2026-09-13
   against ASRock's own specification page. There is no lane sharing with the graphics slot at
   all** - the fear this item was written on does not apply to this board:

   | Slot | Attached to | Speed with a 9000-series CPU | Sharing |
   |---|---|---|---|
   | **M2_1** | CPU | **Gen5 x4** - *"M2_1 is the first priority for M.2 installation"* | **none** |
   | M2_2 | CPU | Gen4 x4 | none |
   | M2_3 | Chipset | Gen4 x4 | *"If M2_3 is occupied, PCIE2 will be disabled"* - PCIE2 is the secondary slot, **not** the graphics slot |
   | M2_4 | Chipset | Gen3 x4 | drops to Gen3 x2 if SATA3_1 or SATA3_2 is used |

   **Assembly instruction: put the 990 PRO in M2_1.** It is CPU-attached, it is ASRock's stated
   first priority, a Gen4 drive runs there at its full Gen4 x4, it costs nothing elsewhere in the
   board, and M2_1 is the slot carrying the large Gen5-rated heatsink. Gen 5 heat is moot for this
   build - the drive bought is Gen 4.

9. **Card models missing from the Jegs TV citation.** That test used a **Sapphire Pulse RX 9070**
   against a **Palit RTX 5070 Infinity 3** - both near-reference designs, not the OC cards GECID
   used. [gpu.md](pc_build/components/gpu.md) cites the source without naming either.

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


### Opened by the source audit, 2026-09-13 (PSU and SSD passes)

From reading all 5 PSU and all 8 SSD videos end to end. Evidence and verbatim quotes for every
line below are in [source_audit.md](pc_build/source_audit.md); nothing here is asserted without
a quote there. **This covers 13 of 99 videos — the audit is not finished.**

1. **SSD: the 990 EVO Plus is not the "-1 720 alternative" the docs make it.** Both reviewers who
   actually tested it recommend against it. Tech Notice's closing line is *"it's probably best
   going with the Evo rather than the Evo plus because the Evo offers better performance in
   pretty much every case scenario"*; proSSD, on the exact **1TB** SKU this build would buy, ends
   *"не вижу я смысла в его покупке"*. [storage.md](pc_build/components/storage.md) keeps it on
   the strength of the one chart where it wins, quoted accurately but without the verdict that
   follows it. **The 990 PRO pick is unaffected.** What to decide: whether the EVO Plus stays
   listed as the saving.

2. **SSD: the plain 990 EVO is in no document and may beat the shortlisted drive.** It is faster
   than the EVO Plus on three of Tech Notice's four charts and is the drive he recommends;
   NASCompares independently calls it the power-efficiency pick. **Never priced in Ukraine.**
   Price it before the EVO Plus is offered again.

3. **SSD: the ~20% Gen 5 figure is attached to the wrong chart.** Tech Notice speaks the 20%
   over the **quick** system-drive test, which he defines as a secondary documents drive. Over the
   full-system chart he gives **no figure at all**. The number is real; what it measures is not
   this machine's workload. **Closed 2026-09-13:** the claim is struck from storage.md, and the
   G5's pick survives it - the drive is justified by a measured PCMark 10 Storage comparison
   (StorageReview) and by costing 400 **less** than the 990 PRO at Telemart, not by the 20%. The
   "+1 899" in the same sentence was itself a hotline-floor-against-shop comparison and is
   withdrawn.

4. **PSU: the connector margin on the pick is thinner than written.** psu.md says the four
   6+2-pin connectors arrive on *"three cables - one dual-head and two single-head"* and credits
   the video. The video says **three connectors**, not three cables, and adds a constraint the
   doc never records: *"One of them you have to not use the 12 V high power for."* The Red Devil
   XT's 3x 8-pin still fits, because no AMD card here uses the 12V-2x6 — but that is now the
   reason it fits, and it should be checked against the unit's manual before buying.

5. **PSU: "the only source of the five that would size this build above 750W" is wrong.**
   JayzTwoCents recommends **1000W** for *"something like a 6800 xt or higher"*, which an RX 9070
   XT is. Two of five size above 750W, not one. The 750W conclusion still holds — Jay's 2021
   reasoning predates ATX 3.x — but the sentence is withdrawn.

6. **SSD: the one budget cross-check that does not pass.** storage.md records Tech Guided's SSD
   guide as *"nothing usable"*. It carries the same class of heuristic the docs accept from that
   channel for motherboards: *"spend anywhere between 3 to 7% of your total budget on your SSD"*.
   The 990 PRO 1TB at 12 399 in the 115 389 Working build is **10.7%**. Not decisive on its own —
   the drive is chosen on QD1 latency for a work load, and the heuristic comes from a $1 000
   build — but it should be recorded rather than dismissed.

7. **Five of the thirteen videos read so far are vendor-sponsored, and no document says so.**
   GeekaWhat 2023 by **Corsair** (a PSU maker, in a PSU buying guide — the sharpest conflict
   found), GeekaWhat 2026 by **ASUS**, Tech Notice by **AMD Ryzen Pro**, PC Builder's SSD guide
   by **VIP-SCDKey**, and `VgWrOSG24Yg` by the same grey-market-key sponsor. None of it changes a
   conclusion. The pattern now holds across PSU, motherboard and storage, so sponsorship should
   be recorded as a matter of course when a guide is cited.

8. **Counting errors in the audit's own scope, corrected.** There are **8** SSD videos, not 4 —
   sent in two messages six weeks apart, and only the second batch was ever written up. The
   motherboard batch is **7**, not 6: **`BvtNCM5ms3U` was never fetched or read** by the earlier
   pass that recorded motherboards as complete. Non-YouTube links re-derive to **27**, not 22
   (six are Google shopping-redirect wrappers pasted inside a quoted AI answer).


### Opened by the source audit, part 2 (RAM, monitor, cooler, case, build technique)

Videos 14-36 of 99, all read end to end. Quotes for every line are in
[source_audit.md](pc_build/source_audit.md).

9. **The assembly instruction for the Red Devil's three 8-pin sockets is backwards, and both
   sources say so.** [psu.md](pc_build/components/psu.md) tells the shop: *"Use the dual-head
   cable for two of the card's three 8-pin sockets, and one single-head cable for the third."*
   PC Builder — the doc's own cited source — says *"one cable per connection **for the first
   two** eight-pin plugs, then you can daisy chain **the third**"*. JayzTwoCents goes further and
   argues against pigtails entirely, with the spec arithmetic: an 8-pin is rated **150W**, the
   PCIe slot supplies **75W**. **Singles first, daisy-chain last** — the reverse of what the doc
   instructs. This goes on the order, so it should be fixed before the build is placed.

10. **A single-fan tower cooler must be mounted in push, not pull.** JayzTwoCents measured *"up
    to 10 degrees celsius"* between the two configurations and says *"if you're running an air
    cooler and you only have one fan push is the only config"*. The AK400 is a single-fan tower
    and a shop assembles this machine. Handover item; not in [cooling.md](pc_build/components/cooling.md).

11. **ram.md cites LTT for "do not pay for CL30"; LTT names 6000 CL30 as the sweet spot.** The
    doc's sentence merges two CPUs. *"Anything with a tuned EXPO profile"* is said of the
    **9950X**; of the **9800X3D** he says *"6,000 mega transfer CL30 is still the sweet spot"*.
    **The decision survives on better grounds** — this build's 9700X is the non-X3D case, and
    the source that tests the exact question (Hardware Unboxed via PC Builder) puts CL30-vs-CL40
    at 8.5% at 1080p with a 4090 and calls 6000 CL36 fine. Fix the citation, not the pick.
    Related: PC Builder gives the absolute-latency formula — CL x 2000 / speed — which puts the
    build's **6000 CL36 at 12.0 ns against 10.0 ns** for CL30. That is the size of the
    compromise, in a number, for the first time.

12. **LTT's advice for this machine's stated workload points at the low-latency kit.** *"If
    you're making money with your machine, you might want to consider ponying up for a
    high-speed, low latency kit, even at today's extortionate pricing"* — and his one measured
    exception is a **compile test**, which is the half of the workload ram.md uses to justify
    32GB. The counterweight is Gamers Nexus, who measured memory tuning at **3.5% in Blender and
    1.6% in 7-zip** against 10-17% in games. Recorded as a genuine tension, resolved in the
    doc's favour by the only source that benchmarked production work.

13. **"Every source says the same thing about high refresh rates" — one of the six says the
    opposite.** [monitor.md](pc_build/components/monitor.md) opens the 240-vs-180 question that
    way. The split is **4-1-1**: RTINGS, Aman, The Tech Chap and JayzTwoCents support the lower
    refresh; **ECPU calls 240Hz "the sweet spot for high-end and competitive gaming"**; MikMat is
    silent. The 180Hz case is in fact **stronger** than the doc argues — Tech Chap's *"27 inch
    1440p 165hz IPS or VA is absolutely ideal"* and Jay's *"27 in 1440p ... 144 HZ"* describe the
    Q27G4XF exactly, and neither is quoted anywhere in the doc.

14. **monitor.md now contradicts itself on brightness.** Its characteristics table says *"Under
    ~400 nits is noticeably dim in a bright room"*; its Correction 1 retracts "dim at 365 nits"
    on RTINGS' 300-350 line. Aman, also in the six, gives **350 as a floor** (*"anything below
    that ... feels just dim"*) and **500 as the minimum near a window**. The synthesis: 365 nits
    clears the bar for a controlled room and not for a bright one. Resolve the two statements.

15. **The cooler pick's defence is the method its own source calls the weak one.** cooling.md
    defends the AK400 on the 9700X with a wattage argument. Tech Guided: *"there is no
    standardized way to calculate TDP"*, and the fix is expert benchmarks from **Gamers Nexus or
    Hardware Unboxed**. Read in full, PC Builder also puts the **9700X by name** in the
    dual-tower tier and gives the tier below (Ryzen 5, Lean's 7500F) a separate lighter
    recommendation — so he sorted the chip deliberately rather than generalising from the 7700X.
    Question 1 in cooling.md stays open and its balance shifts toward stepping up.

16. **Three Tech Guided budget heuristics, and they do not agree with each other.** Same channel,
    same 3-7% / 5-10% methodology, applied to the Working build (115 389): **SSD 10.7% (over),
    cooler 1.5% (under), case 4.3% (under)**. Together they describe a build that is heavy on
    storage and light on chassis and cooling. Stepping the cooler to a Phantom Spirit 120 SE
    (+1 146) is roughly what dropping the 990 PRO to the EVO Plus would free. An observation,
    not a recommendation.

17. **case.md discards evidence that supports its own pick.** It records that the five guides
    recommend US-market cases and that *"nothing in them changes the Lancool 216"*. The most
    current of them calls the Lancool 216 *"my favorite front intake PC case of all time"*, and
    the reason is the stated criterion: *"The two fans in the front are 160 mm ARGB ... You can
    spin these fans much slower and get similar air flow ... and they're almost silent."* Add it.
    Separately, "mesh front — all five" is **four of five**: the CORSAIR 2019 video is a vendor
    advertisement that never mentions mesh.

18. **A noise-and-thermals clearance rule nothing has checked.** Mr Matt Lee: **at least an inch
    of clearance between the PSU shroud and the GPU's fans**, because less *"increas[es] noise
    levels while simultaneously restricting the airflow"*. Checkable against both cases with a
    ~327mm Hellhound GRE. Not checked.

19. **The frame check pc_build.md claims for ScatterVolt and GamingScan left no artefacts.**
    Before this pass `frames/` held twelve PNGs, all from the four GPU videos. Three ScatterVolt
    frames are now saved, including `frames/PsqulPtiR3g_17m18s.png`, which confirms the
    "AM5 ideal RAM kits" card **word for word**. One correction: the doc calls it *"a claim the
    audio never states"* — the narration states the **6000 CL30** and **6400 CL32** lines
    outright. Only **6000 CL28** is on-screen only.

20. **"The most common build error in all four videos" appears in one of them.** The A2/B2
    dual-channel mistake is covered at length by JayzTwoCents alone; GamingScan mentions dual
    channel once in passing; ScatterVolt and optimum do not raise DIMM placement. Keep the
    handover item — Jay's own advice is *"consult your manual"* — and drop "all four".

21. **Fan-header mode may need setting by hand.** case.md resolves the CC560 V2's unlabelled fans
    with *"ASRock's headers auto-detect DC vs PWM, so speed control works either way"*. optimum:
    *"double check in the Bios whether your fans are set up for pwm or DC operation ... three pin
    fans are DC and 4 pin is pwm."* Worth verifying in BIOS on collection rather than assuming.

22. **Sponsorship is now the rule, not the exception.** Of the 36 videos read so far, **eleven**
    carry a paid sponsor and **no document discloses any**: Corsair (GeekaWhat PSU, ScatterVolt
    parts), ASUS (GeekaWhat PSU 2026, PC Centric motherboards), AMD (Tech Notice SSD), Seasonic
    (PC Builder RAM **and** PC Builder coolers — while psu.md weighs a SeaSonic unit),
    VIP-SCDKey (PC Builder SSD, PC Builder cases, and `VgWrOSG24Yg`), Gigabyte (GeekaWhat cases),
    Falcon Northwest (JayzTwoCents monitors). None of it changes a conclusion. It should be
    recorded as a matter of course when a guide is cited.


### Opened by the source audit, part 3 (motherboard, GPU, combo guide, UPS) — PC parts complete

Videos 37-55 of 99. With this pass **every PC-component video is read**; what remains is
peripherals and the non-YouTube links. Quotes in [source_audit.md](pc_build/source_audit.md).

23. **A motherboard video was never fetched, and another document was already citing it.**
    `BvtNCM5ms3U` arrived in the same message as the other six boards and was never transcribed
    by the pass that recorded motherboards "6 of 6 done". It is **GeekaWhat's 2026 parts guide** -
    the source [cooling.md](pc_build/components/cooling.md) quotes for *"recommends liquid cooling
    for a Ryzen 7"*. That citation was **accurate and unverifiable at the same time**; it is now
    quoted verbatim and on disk. Nothing to fix in cooling.md.

24. **The VRM tier list this project recommends does not cover this platform.** Tech Guided names
    a Reddit motherboard VRM spreadsheet, and the audit recorded it as a gap worth filling. The
    video itself says it *"hasn't been updated for over a year now, so it only lists am4 chipset
    motherboards and 12th generation Intel chipsets"* — as of **2023**. **Nothing on B850 or AM5.**
    The usable half stands: **Buildzoid, Gamers Nexus, Hardware Unboxed**, named by two sources
    independently.

25. **A brand argument for this exact workload, which the ASRock paragraph does not have.** The
    2026 brand survey on Gigabyte: *"a lot of their AM5 and Z-series boards run surprisingly cool
    under sustained workloads. That matters for people sitting in Blender, Unreal Engine, Premiere
    Pro, or **long compilation workloads** for hours at a time."* The brief is heavy repos and
    language servers. The same video notes lower-end ASRock boards *"cut back harder on onboard
    audio or rear USB connectivity"*. Not a measurement and not a reason to reopen the pick on its
    own — but if the ASRock brand-risk paragraph is revisited, this is the argument that bears on
    the work case rather than on reputation.

26. **Two board features nobody has checked, both one lookup away.** Socket-X: *"A board with only
    two fan headers is a trap"* (aim for four or five), and *"look for a BIOS flashback button"* —
    which matters when a board shipped before the CPU it will run. Neither is in
    [motherboard.md](pc_build/components/motherboard.md)'s criteria table.

27. **The onboard-Wi-Fi rule is 3:1, not 2:1.** GeekaWhat calls it *"a red line"* for his own build
    company, alongside Socket-X and PC Centric. Only Paul's Hardware (2020) offers the USB-dongle
    alternative. The 614 UAH on the WiFi SKU is well supported. Also: **the A2/B2 handover item has
    a second source** — PC Centric states *"you use slots 2 and slots 4"* independently.

28. **The GPU document's main source is sponsored by the shop this build buys from.** GECID's
    RX 9070 vs RTX 5070 review was recorded as *"cards supplied by Telemart"*. It is more than a
    loan: the video runs a **live promo code** — *"до 5 липня за промокодом GESID 500 ... знижка у
    500 грн на всі відеоприскорювачі від ASUS"* — a paid promotion for **Telemart**, and for **ASUS
    cards**, which are the two cards under test. Telemart is one of the two assemblers this build
    is priced against. Nothing in the review reads as bought (it ends by recommending the **RTX
    5070** for buyers who want no surprises), and all fourteen of its claims are verbatim accurate.
    But the relationship belongs on the page — it is the only sponsorship in this audit that
    touches a **shop** rather than a component vendor.

29. **A char count that matches nothing.** The earlier GPU section states the GECID transcript is
    *"37 953 chars, read end to end"*. Measured: **21 497** body, **26 456** total, 44 105 bytes.
    The read was real — every claim checks out — but the number was not measured. Re-done in the
    verifiable format; **GPU and motherboard now pass the script**, which they did not before.

30. **ScatterVolt's two videos disagree about RAM, and the newer one supports Lean's 16GB.**
    pc_build.md cites him as a *"third independent source"* for **32GB**. That quote is from his
    **parts guide (2025-09)**. In the **combo guide (2026-08)**, eleven months later and after the
    price event the RAM section is about, he says of this build's tier: *"I really think 16 GB of
    DDR5 memory is still very much doable. But if you wanted 32 and you have the budget for it,
    then go for it."* Same source, different date — the citation needs dating, the decision does
    not change.

31. **UPS stays parked — but the batch contains one line that supports a live pick.** Dave's
    Garage: an offline UPS's transfer gap can reboot a PC *"even though it never fully loses
    power"*, because the PSU cannot bridge it. Transfer times in these videos are **5-20 ms**
    (offline) and **2-8 ms** (line-interactive); [psu.md](pc_build/components/psu.md) records
    **21.8 ms hold-up** for the chosen be quiet! platform. **The PSU covers a line-interactive unit
    with margin** — and line-interactive is the type all these sources name for a PC. If the item
    is ever unparked, the sizing arithmetic and the shutdown-over-USB requirement are already
    worked out in the audit; **do not re-research it.**


### Opened by the source audit, part 4 (peripherals — mouse)

Videos 56-63 of 99. Quotes in [source_audit.md](pc_build/source_audit.md); every correction is
made in [peripherals/mouse.md](pc_build/peripherals/mouse.md) in place. **The mouse pick is closed
and none of this reopens it** — the Razer Cobra at 2 499 stands.

32. **Three counts in mouse.md were wrong, and the wireless one was the worst.** *"Wireless 2.4G
    is not a compromise. **Six sources agree**"* — counted off the transcripts, **three** do:
    Rocket Jump Ninja 2025, DiamondLobby 2024, Hardware Canucks. Kimmy and DiamondLobby 2026 never
    mention wireless; Rocket Jump Ninja 2020 argues the other side of it. Also *"unanimous among
    the seven"* on shape → **six of seven** (the LTT video is a clone comparison and never
    discusses shape), and *"five of the eight open on"* fit → **four**. That is **seven wrong
    counts** this audit has now found across eleven components.

33. **"21 years of FPS reviews" is 10, and the 21 is a different thing.** The number came off
    Rocket Jump Ninja's site banner — *"100+ mouse reviews from over 21 years of FPS/Quake
    Experience"*, now saved as
    [`frames/QVI3mepUHuE_01m05s.png`](pc_build/frames/QVI3mepUHuE_01m05s.png). He says in the video:
    *"10 years ago, I started doing mouse reviews."* Right number, wrong noun — the same pattern as
    Tech Notice's 20% and Aman on response time.

34. **All eight mouse guides are monetised; none was disclosed.** Two carry a named paid sponsor —
    **Thermaltake** (Hardware Canucks, who also discloses free review units) and **Pulseway**
    (Linus Tech Tips). DiamondLobby's descriptions are Amazon affiliate links to the exact $45-65
    mice quoted in the doc as *"endgame level"*. Kimmy states it plainly: *"These are all my
    amazing affiliate links."* **Rocket Jump Ninja sells his own mouse design** (Xtrfy MZ1) while
    the doc leans on his 60% rule harder than on anything else, and he plugs a third party's mouse
    inside his price chapter. Running total: **13 of 63 videos read carry a paid sponsor**, and the
    mouse set is the first where *every* source has a commercial interest.

35. **The doc claimed frame checks with no frames on disk.** Five were pulled and they confirm the
    claims rather than overturning them — including Kimmy's **17.5 cm** boundary, which the
    auto-caption mangles to "70.5 cm" and which the transcript therefore could not prove. The
    frame paragraph now cites filenames.

36. **A 19.0 cm hand is "large" by the doc's own source, and the doc used the medium band.**
    Kimmy: *"large is like 19 plus"*, and for large hands *"anything above [125 mm] is okay"*. The
    file used her **medium** 115-125 mm band as a fence and marked the 128 mm DeathAdder V3 and
    125.8 mm Superlight 2 Dex as outside it. On her rule they are not. **The pick does not move** —
    three millimetres off a shell already known to fit beats any band — but the fence was doing
    work it cannot do. Also newly recorded: DiamondLobby measures the hand **relaxed**, not flat,
    and his own hand goes from 18 cm to 15 cm that way, so the two-source "consensus" on the
    measuring method is really two of three.

37. **Both mouse finalists have a failure mode; the doc only carried one.** LTT caught Razer
    Synapse forcing an install mid-match (*"Razer is the only one that successfully got me killed
    so far"*) and Hardware Canucks names Synapse and iCUE as the two suites that *"get a lot of
    heat"* — that is the Cobra's side, better evidenced than the Reddit aggregate the doc had. But
    the same reviewer: *"after your Logitech starts to double-click. We all know it's true"*, and
    *"Logitech G Hub just simply failing to start"*. The Logitech alternate is not the safe option
    the file implied.

38. **Two usable rules the doc had dropped.** Rocket Jump Ninja gives the only pass/fail number in
    the eight — click latency *"under 4 milliseconds"*, which sorts LTT's own lab results exactly
    (Attack Shark 10.8 ms fails, DeathAdder sub-2 ms passes). DiamondLobby: never plug a wireless
    dongle into the case, use the supplied desk adapter. Both added.


### Opened by the source audit, part 5 (peripherals — keyboard)

Videos 64-69 of 99. Corrections made in
[peripherals/keyboard.md](pc_build/peripherals/keyboard.md) in place. **The AULA F75 at 1 699
stands**; nothing below reopens it.

39. **Two statements in keyboard.md were backwards.** The mouse-collision row said a TKL makes the
    mouse hit *"the **left** edge of the keyboard"* — the mouse is to the **right** of the
    keyboard and hits its right edge; the source says only "the side". And the housing-plastic row
    put **POM with nylon** as the low-pitched plastics when the switch guide groups *"polycarbonate
    and POM"* together as the **high**-pitched, clacky ones. The second is the row you would use to
    predict how a board sounds, and it pointed the wrong way.

40. **"Every one of the six guides recommends" a switch tester — three do.** KeebNews never
    mentions one; PC Gamer says read reviews and listen to sound tests instead. **Eighth wrong
    count** of the audit.

41. **Four of the six keyboard sources are tied to Keychron.** The layout chapter's only source
    runs Keychron referral links and Keychron boards on camera. The low-profile row's only source
    was **sent** his board by Keychron — and it is the **K3 Max listed in the doc's own price table
    at 8 999**. KeebNews carries a Keychron referral and recommends the brand on camera. Only **PC
    Gamer** has no commercial tie. Paid-sponsor count stays **13 of 69**; gifted hardware and
    vendor referral now run through five of these six.

42. **Two sources put the board that was bought below their own quality floor, and the doc's
    justification misquoted all six.** KeebNews's sweet spot is *"80 to 120"* dollars, below which
    *"way too much plastic, which makes it feel a little cheaper and sound a little more hollow"*;
    Brad Colbow's $35 board *"sound[ed] really hollow"*. **1 699 UAH ≈ $41.** The doc closed with
    *"every beginner guide consulted says the same thing: buy cheap first"* — **one** of them tells
    that story. Recorded, not raised as a decision: Justin Tech says good boards exist under $50,
    the 63 owner reviews measure the very thing the heuristic guesses at, and the exposure is
    capped at 1 699 on a board Dmytro chose on looks and feel.

43. **Two small gains.** The 75% choice has a **second** independent source — Justin Tech:
    *"I wouldn't really recommend a TKL keyboard as 75% is basically the same thing"* — where the
    doc had called mouse collision *"the one concrete reason"* (and that reason is stated for
    *competitive* play, which is outside this build's case). And the switch guide's own
    *"generally, your keyboard is much more important than the switch"* is the line that makes
    closing the switch row without a tester defensible; it was never recorded.


### Opened by the source audit, part 6 (laptop-as-display)

Videos 70-73 of 99 plus one. This batch was previously recorded "done" and **had no document at
all** — the answer was given in chat on 2026-09-12 and never written down. Now written up as
[peripherals/laptop_display.md](pc_build/peripherals/laptop_display.md).

44. **The question had a clean answer nobody recorded: no cable can do it.** *"Laptops do not have
    a video input port, so you cannot directly connect it to your desktop via VGA or HDMI cable and
    use it as a monitor."* The built-in route is Windows Wireless Display over Wi-Fi; the fallback
    is spacedesk. The only cable that helps is an **Ethernet** one — *"if you use a wired ethernet
    connection, it'll be even smoother."*

45. **Three of the five videos answer a different question.** Two are *"connect your laptop to a
    monitor"* — the reverse direction, where a cable is exactly what you need — and one is about
    KVM sharing. The batch was marked done without that being noticed, which is why nothing could
    be written from it.

46. **The monitor already bought can do the better version of this, and nobody had noticed.** The
    fifth video shares one monitor between a PC and a laptop using *"multiple HDMI inputs"* plus a
    USB switch for the keyboard and mouse. **The AOC Q27G4ZR has two HDMI 2.0 inputs** beside the
    DisplayPort the desktop should use. So the laptop gets a real 27" 1440p screen for the price of
    an HDMI cable — one machine at a time. **No change to the monitor decision; a capability it
    already bought.** Unpriced: a USB/KVM switch, if the peripherals are to be shared too.

47. **A frame corrected a keystroke before it got written into a how-to.** The caption says *"press
    Windows plus B"*; the pane on screen is the **Connect** flyout (Win+K), and Win+P is the
    projection-mode switch. The same frame shows an option neither transcript mentions — *"Allow
    mouse, keyboard, touch, and pen input from this device"* — which is what lets the laptop's own
    keyboard and trackpad drive the desktop.


### Opened by the source audit, part 7 (headphones — all 16)

Videos 74-85 of 99 and four more. [peripherals/headphones.md](pc_build/peripherals/headphones.md)
is the most careful file in the repo — it corrects itself five times unprompted — and **the verdict
survives all sixteen full reads.** The Arctis Nova 5 stands. What follows are corrections to how it
is argued, plus the commercial position of the sources.

48. **The rival's microphone was oversold, and that favours the headset that was bought.** The file
    credits the BlackShark V2 HyperSpeed with the *"best wireless mic in the only listening test"*.
    In that test the winner is the **V2 Pro**, and the reviewer separates them: *"it's almost like
    the Pro version has more bandwidth in the microphone department"*, and *"the sidetone on the
    HyperSpeed is way worse versus the Pro. It's not as loud."* Corrected to second-best.

49. **A source was mined for its parameters and its verdict was never reported.** Kimmy supplies
    three of the file's spec rows. Her video is called *"Stop Buying Headsets from Gaming
    Companies"* and concludes *"you're paying for one product that does two things at 60%, when the
    same money gets you two products that each do their job at 100%"* — studio headphones plus a
    $30 cardioid mic. **The third cherry-pick of this audit, and the largest**: a verdict against
    the whole product category the file buys from. **The decision survives on her own terms** —
    *"if wireless and all-in-one convenience matters more than audio accuracy, a gaming headset is
    still a valid choice"* — which is this brief exactly. **Not raised as a decision**, because the
    requirement that settled the file (a mic endorsed for conference calls, wireless, one box) is
    not in dispute. Recorded as a gap: **the two-box path has never been priced in Ukraine.**

50. **Three of the sixteen sources are shops, and one of them supplies the file's rule about where
    to buy.** The Headphone Show is **headphones.com's own channel**, and its *"buy from somewhere
    with a reasonable return policy"* — quoted in the file as neutral research discipline — is a
    retailer's advice that also warns off a competitor. Audio Advice and Smart Home Sounds sell
    headphones too. Fourteen of the sixteen carry affiliate links; only PC Gamer and The Headphone
    Show do not.

51. **The file's own scepticism runs one way.** It discounts the negative Razer Insider threads as
    *"a complaint-selected sample"* — correctly — and then rests its final tie on **59 positive
    Reddit owner reports per headset**. The Headphone Show, its named authority on method, says
    forum product threads *"turn into support groups for product owners"*. Same bias, opposite
    sign. The tie does not move; the confidence in it should.

52. **Five sponsors, and for once none of them sells a headset.** Thermaltake, **be quiet!** (the
    PSU vendor of this build, sponsoring the headset buying guide), Freepik, Storyblocks, Fit Nexa.
    **Four of the five are disclosed on camera by the creator**, and This is Tech Today gives the
    cleanest disclosure in all 85 videos read: *"No brand had prior review, editorial control, or
    influence over this video or my choices."* **The disclosure failure here was the document's,
    not the creators'.** Running total: **18 of 85 read carry a paid sponsor.**

53. **A 2022 video is titled "The Best Headphones To Buy in 2026".** Ali Abdaal's, uploaded
    **2022-03-16**, testing the Sony XM4 and the first-generation AirPods Max. The mouse file marks
    a 2019 guide stale and discounts it; this one was listed undated. Now discounted on the same
    grounds.

54. **Two findings that support what was bought, which the file never made.** Three separate
    listening tests of consumer ANC microphones describe them identically — *"my voice sounds like
    it's underwater a little bit"*, *"it just sounds like right now I'm wearing headphones"*. That
    is a three-source argument **for** a boom mic. And PC Gamer independently ties a badly judged
    clamp to *"a nasty headache"* after a couple of hours, which is the exact comfort argument the
    Nova 5 won on.

55. **The "Sony XM6 has the best microphone on any headphone" claim is narrower than stated** —
    the source says *"amongst flagships that I've used"*, with no boom-mic headset in the
    comparison. And the file's *"the written outlets the guides themselves name as trustworthy"*
    lists seven; **three** are actually named by a guide.


### Opened by the source audit, part 8 (earbuds — separate task) — ALL 99 VIDEOS NOW READ

Videos 86-94 of 99, plus the five already counted. **`verify_audit.py` now prints 99/99 PASS.**
Every video Dmytro has sent across every session has been read end to end and quoted.
[earbuds.md](earbuds.md) is a separate matter from this build; its corrections are made there.

56. **A model was withdrawn using another product's verdict.** The CMF Buds Pro 2 at 2 499 was
    dropped because *"the same review is explicit that it loses on sound to every competitor in its
    class"*. Andro-news says that about the **$35 CMF Buds**; about the **Buds Pro 2** it says the
    tuning is *"the most balanced and high-quality"* in its class and its weak point is **ANC**.
    **Two products merged into one claim — the fourth instance of that pattern, and the first that
    changed a recommendation.** Decision 6 above.

57. **"Nothing added" was wrong again — the third such dismissal this audit has overturned.** Those
    four videos raise the **Creative Aurvana Ace 3 at $150** (SoundGuys' measured mid-range
    champion, in the line the file had withdrawn), the **Marshall Motif 2 ANC at ~$200** (inside
    budget), and two JLab models below the budget floor.

58. **A misattributed measurement.** The Sony WF-C710N's *"85% measured noise reduction, 9 h"* is
    credited to Tom's Guide, which says something else entirely — *"about 80 to 85% of the XM6
    experience"*. **Both numbers are SoundGuys' lab measurements**, from a video filed as adding
    nothing. Right numbers, wrong source, and the 85% meant two different things.

59. **hotline does not overturn the sponsored reviewer on ANC — it agrees with him.** On hotline's
    own per-model scores the Soundcore Liberty 5 Pro's ANC is **joint third of five**, which is
    exactly where the other reviewer's on-screen tier puts it. And **the only two sources ranking
    that model's microphone first are a Soundcore-sponsored video and a shop channel reviewing a
    shop-loaned unit**, whose 9/10 rests on *"not once did the interlocutor complain"*.

60. **The recommendation's battery is the optimistic figure of two.** Nothing Ear (3): 9.5 h
    *"taking into account the codec"* against *"about 5 to 5.5 hours with ANC"*. The file's own
    spec row warns about exactly this and sets a 5 h+ target — with ANC on, the pick sits at the
    bottom of its own band.

61. **A best-for-calls pick was never priced**, on a purchase whose stated point is the microphone:
    the **Samsung Galaxy Buds 3 Pro**, named by a reviewer as the non-Apple answer to *"best for
    work and for calls"*. No row, no price.

62. **Frames settled four words that were quoted as if spoken.** The sponsored reviewer's
    microphone tiers — *"perfect"*, *"great"*, *"fair"*, *"not good"* — appear nowhere in the
    transcript; they are on-screen labels, and
    [`frames/44zG1beMWfg_11m20s.png`](pc_build/frames/44zG1beMWfg_11m20s.png) confirms all four
    exactly. The ANC frame shows the file's table dropped one of five tiers.


### Opened by the source audit, part 9 (the 27 non-YouTube links) — THE AUDIT IS COMPLETE

All 27 checked over verified TLS on 2026-09-13, **no redirect followed**. Twenty are real sources
Dmytro sent; **six are Google redirect wrappers pasted inside a quoted AI answer and one is
boilerplate from a skill's own template**. Three pages returned unreadable bodies and are recorded
as *not read* rather than guessed at. Quotes in [source_audit.md](pc_build/source_audit.md).

63. **Two prices in the docs have moved, and both move in Dmytro's favour.** **Rozetka now sells
    the AULA F75 Black first-party at 1 699 — and 1 614 with a Rozetka card — in stock.**
    [keyboard.md](pc_build/peripherals/keyboard.md) said *"Rozetka is not a source for the Aula …
    marketplace sellers at 2 100-3 800"* and that the black SKU was out of stock there. **1 614
    would be the cheapest price anywhere for the chosen keyboard.**

64. **A price in cpu.md has no shop and no date, and is now too low.** Dmytro asked whether the
    9700X is tray-only on click.ua. **It is** — 12 892 ₴, and no BOX SKU exists there although nine
    other AM5 chips have one. That is **above the 12 599 "box" figure** in
    [cpu.md](pc_build/components/cpu.md), which was read somewhere else on an unrecorded day. Same
    failure as the hotline floors.

65. **Both aggregator criticisms hold, and two sentences of them were too broad.**
    technical.city really does say *"Games benchmarked by notebookcheck.net"* and really does rank
    the RTX 5070 above the 9070 XT (68.78 vs 64.58). But [tools.md](pc_build/tools.md) called its
    suite *"2015-2018 titles"* — **five of the thirteen are 2020 or later**. And its
    gamingpc.com.ua example, *"Valorant 327/327/327 … identical at 1080p, 1440p and 4K"*, does not
    describe the page today, where 1080p and 1440p match and 4K differs. Both narrowed.

66. **gamingpc.com.ua concedes the point itself, and nobody quoted it.** *"Показники FPS є
    усередненими і служать для демонстрації"* — averaged, for demonstration. The site's own
    disclaimer is the strongest line available against its numbers. Its per-build FPS widget now
    reads **0fps**, so the *"22 FPS vs 190 on the same page"* contradiction can no longer be
    reproduced — written down, not quietly dropped.

67. **Two direct questions from Dmytro were never answered anywhere.** *"What do you think about
    this pc, price and components"* (Vision 5 Pro, **119 073**) and *"what about this one"* (ASGARD
    Hel, **96 099**). Both are now priced and itemised. **Neither is proposed** — prebuilts with
    fixed CPUs, and the Hel's Ryzen 5 8400F is below anything in cpu.md's table. What they do
    supply is the evidence [ram.md](pc_build/components/ram.md) lacked: it argues 32GB from the
    prebuilt market citing **only US builders**, and **both Ukrainian machines ship 32GB
    DDR5-5600**, one beside an RX 9070 XT and one beside an RTX 5070.

68. **Two AeroCool cases he asked about had no answer in the repo.** Now priced and specified in
    [case.md](pc_build/components/case.md) — and the **D502A's front USB-C is verified**, a claim
    this project has asserted twice without checking. **The case decision is closed and stays
    closed.**

69. **The monitor listing confirms every figure and adds three the file never quoted** — 300 cd/m²,
    5000:1, and **four inputs** (2× HDMI, 2× DisplayPort). Dmytro was right that the measurements
    were on the page. The pick is closed; the spare input is what lets the laptop share the screen.

70. **The RAM guide names this build's exact risk and then declines to cover it.** *"I may be
    convinced to add a section about the pitfalls of **DDR5 RAM wrt XMP problems with four slot
    boards**, but I thought I would stick to DDR4 for now."* All four of its embedded citations are
    DDR4-only as well.

71. **The six Google wrappers are the citations of a pasted AI answer** claiming the BlackShark V2
    HyperSpeed is *"highly comfortable for glasses wearers"*. They are opaque redirects and were
    not followed. **The claim they were cited for was later settled the other way and then withdrawn
    entirely.** A pasted answer whose every citation is unopenable is the thing this audit exists
    to catch.

72. **`desk.md` survived word for word**, including the one thing it hedged: the seller's *"400 /
    435"* delivery blurb against Rozetka's own block, which still says only *"Тариф перевізника"*.
    It is the most careful sourcing in the repo.


## DECISIONS WAITING ON DMYTRO (opened by the source audit, 2026-09-13)

Everything below is a **choice**, not an error. All the documentation errors the audit found have
been fixed in place - see the "Opened by the source audit" items above for the record of what
changed. These five are what is left, with the evidence and the money.

**None of them reopens a decision Dmytro has already closed.** The case and monitor picks stay as
they are; the UPS stays parked. Four of the five are storage and cooling, which were never closed.

**Updated 2026-09-13:** two more were added at the end. **6** is the earbuds, a separate task,
where a model was removed from the running on evidence belonging to a different product. **7** is
the two prebuilts Dmytro sent and asked about directly, which no document ever answered — one of
them is 14 333 under the Max build with the better GPU. Both were first written up as "recorded,
not proposed", which was the wrong call: a choice with money attached is his, not mine.

---

### 1. CLOSED 2026-09-13: Working ships the 990 PRO - at click.ua it is the cheaper drive

**Option (c) was taken — the plain 990 EVO is priced, and it closes.** Two offers in the whole
country, both from one seller (1SERVER), **11 589 – 11 622**, stock to be confirmed with the
seller. **Telemart, Brain, ITbox and Foxtrot do not stock it at all**, so it cannot be part of a
one-shop basket, which assembly requires. It is **910 more than the EVO Plus**, only **573 under
the 990 PRO at Brain**, is DRAM-less like the Plus, and at 1TB is the slower part on paper:
**5 000 / 4 200 MB/s against 7 150 / 6 300**. Full price table and quotes in
[storage.md](pc_build/components/storage.md) → "The plain 990 EVO, priced and settled".

**And Tech Notice's sweeping line does not survive the full read.** He tested **2TB** samples of
both — *"I have the two terab model of both Evo and Evo plus"* (`kmxVz5jmG7A` @ 0:33). The EVO
wins the quick-system-drive, data and consistency charts; **the EVO Plus wins the full-system-drive
chart — the one this document picked it on**, and the one he calls the most important for OS and
programs. The second source on the plain EVO is against it outright: NASCompares puts it *"notably
lower in terms of performance across the board"* (`auaAty99KM0` @ 1:43) and aims it at mini PCs and
slim laptops, not this machine.

**What is actually on the table, and it now depends on the shop:**

| Basket | 990 EVO Plus 1TB | 990 PRO 1TB | The PRO costs |
|---|---:|---:|---|
| **Telemart** (current build sheet) | **10 679**, in stock | **12 399**, in stock | **+1 720** |
| **Brain / ITbox** (36-month assembly warranty) | 12 581 | **12 162**, in stock | **−419** — cheaper *and* it has the DRAM |

**The justification, rebuilt on measurements (2026-09-13, second pass).** The first version of this
recommendation leaned on a *"~3 000-4 000 MB/s"* sustained-write figure for the 990 PRO that
[storage.md](pc_build/components/storage.md) carried **with no source**. It is withdrawn. The
measured picture:

| | pSLC cache | Post-cache write | 4K QD1 random read | Price |
|---|---|---|---|---|
| **990 PRO 1TB** | ~115 GB | **≈1 350 MB/s** (ssd-tester.com: 200 GB at 2 436 MB/s average, cache full after 115 GB) | **best Gen 4 measured** — Tom's: *"the 990 Pro is the best we've yet tested here"* | 12 162 Brain / 12 399 Telemart |
| **990 EVO Plus 1TB** | ~12% of capacity | **~850 MB/s**, cache recovery *"не всегда стабильные"* (proSSD, exact SKU) | middling — Tom's: *"middling 4KB QD1 random read and write latencies"* | 12 581 Brain / 10 679 Telemart |

At **2TB**, where both were measured on the same bench, **the EVO Plus actually out-writes the
PRO** post-cache — 1.5-1.8 GB/s against *"around 1.4 GBps ... slower than expected"* (Tom's
Hardware, both reviews). So the DRAM does **not** buy sustained sequential write. At 1TB the PRO
leads ~1 350 to ~850, **~1.6x, not the 3-4x this repo claimed**, and those two numbers come from
different testers on different methods.

**What the DRAM does buy** is the FTL lookup table: 4K QD1 random read — the metric storage.md
chose on, where the PRO is the best Gen 4 drive Tom's has tested — and holding up as the drive
fills.

**CLOSED 2026-09-13 — Working ships the Samsung 990 PRO 1TB (MZ-V9P1T0BW), 12 162 at click.ua.**

Dmytro buys at **click.ua**, not Brain or Telemart, which settles it without any benchmark: click
lists the **990 PRO at 12 162** and the **990 EVO Plus at 12 581**, both in stock, both 60-month
warranty (his screenshots, 2026-09-13). The PRO is **419 cheaper** and ahead on every listed spec —
7 450/6 900 against 7 150/6 300, PCIe 4.0 x4 against PCIe 5.0 **x2**, DRAM against HMB, same 600
TBW. **The cheaper part is also the better one; there is nothing left to weigh.**

The EVO Plus, the plain EVO and the whole sustained-write argument are moot for this build. They
stay on record in [storage.md](pc_build/components/storage.md) because the reasoning was wrong in
places and should not be re-derived from the old text.

**Build sheet:** the Working row still reads *990 EVO Plus 10 679, Telemart*. It must become
**990 PRO 12 162, click.ua** when the click.ua repricing pass lands — not edited here, so the two
passes do not collide.

**Two warnings about click.ua's own spec tables**, found while checking his screenshots: they
print **read and write labels swapped** (the EVO Plus page calls 7 150 MB/s "Швидкість запису"; it
is the *read* figure), and the 990 PRO page lists IOPS as **"22 000/80 000"**, wrong by roughly a
factor of fifty. Use the page for price and stock, never for specs.

---

### 2. The Kingston Renegade G5 - the audit's two numbers were wrong, the shop reopened it

**What changed.** storage.md justified the G5 with *"Tech Notice measured Gen 5 at ~20% faster on
the full-system-drive random test - the one chart that matters here."* Read in full, he speaks the
20% over the **quick** system-drive benchmark, which he defines as *"a secondary drive on your PC
... where you store your little documents"*. Over the **full** system-drive chart he gives **no
figure at all**. **That claim is struck from storage.md.**

**What it does not change.** Two things in the earlier version of this entry were wrong:

| Claim | Correction |
|---|---|
| The G5 costs **+1 899** | That was 11 999 against the 990 PRO's **hotline floor** of 10 100 - the floor-against-shop comparison this project banned after Dmytro caught it once. **Same shop: Telemart, G5 11 999 against PRO 12 399 - the G5 is 400 cheaper.** There is no premium |
| **Nothing quantifies** the speed gain | Nothing *in the supplied videos* does. storage.md carries a measured, like-for-like figure that never came from a video: **PCMark 10 Storage, 990 PRO 4 651 / 743 MB/s against the G5's 8 062 / 1 178** (StorageReview). Its caveat - the sample was the 2TB, the 1TB is rated lower - is already recorded there |

The two other voices against Gen 5 (GeekaWhat *"Gen 5 is wildly overkill for gaming"*, Tech Notice
*"for most people 99% of the people Gen 5 drives are waste money"*) both argue against **paying a
premium** for Gen 5. At Telemart there was no premium to pay. At click.ua there is - below.

**On the performance argument, nothing to decide. On price, the shop changed the answer
(2026-09-13):** Dmytro buys at **click.ua**, where the G5 is **16 700** and the 990 PRO
**12 162** - a **4 538** premium, where at Telemart the G5 was the cheaper drive. **Settled
2026-09-13: the G5 stays in Max**, and Max is not being built. See [click_basket.md](pc_build/click_basket.md).

*(Telemart's own G5 price has since moved to **13 999**, read 2026-09-13. Every Telemart figure
in this entry is 2026-09-11 and is kept only to show what the audit was arguing about.)*

---

### 3. CLOSED 2026-09-13: the AK400 stays on Working and Max - the measurement clears it

**This was already cooling.md's open question 1.** The audit did not settle it; it weakened the
argument on the AK400's side.

- The doc's defence was that PC Builder's dual-tower recommendation targets the **105W/142W
  7700X**, and the 9700X is a 65W/88W part. Read in context, **he lists the 7700X and the 9700X
  together by name** in the dual-tower tier, and gives the tier below - Ryzen 5, which is Lean's
  7500F - a separate, explicitly lighter rule. He sorted the chip deliberately.
- **GeekaWhat goes further still**, and this is the video that was never fetched until now:
  *"a Ryzen 7 or Core Ultra 7 or higher is going to be recommended with a liquid cooler."*
- **Tech Guided says the doc's method is the unreliable one:** *"there is no standardized way to
  calculate TDP"* - use benchmarks, from **Gamers Nexus or Hardware Unboxed**.
- **Against all that:** Hardware Whisperer rates tower coolers at *"150W to over 250W"* and calls
  them *"an excellent choice for high-performance CPUs where overclocking is not required"* -
  which is a non-overclocked 88W 9700X exactly. And **no one has measured an AK400 on a 65W AM5
  part**, which is still the only thing that would close this.

**Cost if you step up:** Thermalright Phantom Spirit 120 SE **2 845** against the AK400's
**1 699** = **+1 146 per build** on Working and Max.

**Decided 2026-09-13: option (c) was taken, the measurement was found, and the AK400 stays.**
Nobody had measured an AK400 on a 65W AM5 chip - and nobody has - but the cooler's **capacity** has
been measured, which answers the same question:

| Measured | Result |
|---|---|
| AK400 on a **Ryzen 9 5950X at 220 W package power** (OC 4.45 GHz @ 1.312V) | **delta 68 °C** at full fan, 69 °C at a noise-normalised 40 dBA — [KitGuru](https://www.kitguru.net/components/cooling/luke-hill/deepcool-ak400-cpu-cooler-review/all/1/) |
| **9700X** under Blender, on air | *"The max operating temperature is set at 95°C ... I was way below that with a good air cooler"* — [Hardware Busters](https://hwbusters.com/cpu/amd-ryzen-7-9700x-cpu-review-performance-thermals-power-analysis/11/) |

A **second, independent measurement** was added after Dmytro asked whether one source was closing
this: Basic Tutorials ran the AK400 on a **Ryzen 5 3600X** (95 W TDP / 128 W PPT) under Cinebench
R23, **in a case**, and measured **delta 48.0 °C at 100% PWM (41 dB)** and 50.0 °C at 50% PWM
(38 dB). That also **kills the °C/W extrapolation** the first version of this entry used - 68 °C at
220 W and 48 °C at ~100 W are not the same ratio, because delta depends on heat density and IHS,
not watts alone. Read them as a bracket:

| Load measured | Delta | In a 22 °C room |
|---|---:|---:|
| ~95-125 W chip, in a case | **48-50 °C** | **~70-72 °C** |
| 220 W chip, open bench | 68-69 °C | ~90 °C |

The 9700X's **88 W** sits at or below the lower bracket, on a newer IHS. **Worst honest reading:
~70 °C sustained, 25 °C under the 95 °C limit**, with the optional 105 W / 142 W mode landing
between the brackets rather than above them.

**The three guides pointing at liquid cooling sort by product tier, not by watts.** The 9700X is a
65 W part in a tier defined by 105 W and 170 W chips. **What the +1 146 buys is noise, not
capability** — KitGuru measured the AK400's fan at **42 dBA at 1850 RPM** and called it
*"mediocre"*. Step up to the Phantom Spirit only if quiet under load is worth 1 146 x2; nothing
thermal requires it.

**Two notes from the configurator screenshot**, both recorded in
[cooling.md](pc_build/components/cooling.md):

- The cart holds **AK400 Digital SE `R-AK400-BKADMN-GJD`**, while the docs specify the plain
  **`R-AK400-BKNNMN-G-1`**. Same price, and APH Networks measured the Digital at *"exactly the same
  peak load temperature as the original AK400"*, so it is not an objection — but the LCD block
  needs power and **how it is powered was not confirmed**. Check the box.
- click.ua's *"менше 35%"* warning is a margin rule run on two numbers in the shop's database,
  neither of them published, on a page whose spec tables were separately found to swap read/write
  and misstate IOPS by ~50x. It is not a thermal test.

---

### 4. MOOT 2026-09-13: Lean is not the build being bought

**Dmytro: "lean is indeed not relevant."** He is buying Working/Max, so the AK400-on-Lean question
is parked, not answered, and the documents are deliberately left as they are.

**Known inconsistency, left standing on his instruction:**
[cooling.md](pc_build/components/cooling.md) records *"DECISION (2026-09-11): the Lean build buys
no cooler"*, while [builds.md](pc_build/builds.md) still lists the AK400 at 1 699 in Lean and
totals **92 192** with it. If Lean is ever revived, that is 1 699 of double-counting - the correct
total would be **90 493** - and one of the two files has to move. Do not "fix" it silently; ask
first.

**The original entry, kept for the reasoning:**

**Unchanged by this audit and now supported twice over.** The 7500F MPK bundles a Wraith Stealth.
PC Builder: *"It's fine, but given how cheap budget tower air coolers are, I'd switch it out"* -
i.e. the swap buys **noise, not capability**. Tech Guided adds the budget rule: *"if your budget
is under $800 we typically recommend that you get a processor that doesn't require a third-party
cooler."*

**Decide:** keep the AK400 on Lean for quiet, or drop it and take the **-1 699** - the single
largest saving still available in that build.

---

### 5. CLOSED 2026-09-13: the budget-share heuristics are withdrawn as out of date

**Dmytro's objection, and it is correct:** *"his video was like 4 years ago, the prices have
risen, how is this relevant?"* Tech Guided's three share bands come from videos dated
**2023-12-24** (cooler, motherboard) and **2024-01-03** (SSD), all pegged to a **$1 000 build** of
that era. Since then this repo's own headline finding is the **2026 memory crisis** - RAM and NAND
prices structurally higher, with no relief expected before 2027. A percentage-of-budget rule
computed before that shift cannot be applied after it: the same drive is a bigger share of the
same build for reasons that have nothing to do with whether it is the right drive.

**Withdrawn on both ends anyway:**

- **Cooler "under band"** - answered by decision 3. The AK400 is ~25 °C under its limit on the
  9700X. Being 1.5% of the build costs nothing.
- **SSD "over band"** - answered by decision 1. The 990 PRO was picked because at click.ua it is
  **cheaper** than the alternative. There is no step down to take.

**Nothing here is actionable and nothing should be re-derived from it.** The one cross-check worth
keeping is GeekaWhat's *"the board shouldn't be costing more than the CPU"* - 8 642 against
15 099, which passes.

**The original entry, kept for the record:**

Three heuristics from the **same channel**, same methodology, applied to the Working build
(115 389). They do not agree with each other, and that is the interesting part:

| Part | Cost | Share | Tech Guided's band | |
|---|---:|---:|---|---|
| Samsung 990 PRO 1TB | 12 399 | **10.7%** | 3-7% | **over** |
| DeepCool AK400 | 1 699 | **1.5%** | 3-7% | **under** |
| Lian Li Lancool 216 | 4 949 | **4.3%** | 5-10% | under |
| ASRock B850 Pro RS WiFi | 8 642 | **7.5%** | 8-12% | just under |

Read together they describe a build that is **heavy on storage and light on chassis and cooling**.
Note the arithmetic is suggestive, not binding - the heuristics come from a $1 000 build and both
the drive and the cooler were chosen on stronger grounds than a percentage. But **stepping the
cooler up (+1 146) is roughly what moving the drive down would free**, and that is the one place
the shape and the evidence point the same way.

GeekaWhat's cross-check passes cleanly, for what it is worth: *"The board shouldn't be costing
more than the CPU"* - 8 642 against 15 099.

---

### 6. CLOSED 2026-09-13 on Dmytro's instruction - earbuds are not being decided here

**He closed it: "just fuck off with 6, close."** No pick was made and none should be inferred. The
analysis was **not finished** - he said so and he was right: three shortlisted models
(Samsung Galaxy Buds 3 Pro, Creative Aurvana Ace 3, Huawei FreeBuds Pro 4) have **never been
priced and never assessed**, and the CMF-vs-Realme comparison rests on sources with known defects.

**State of the file:** [earbuds.md](earbuds.md) still shows the **Realme Buds Air 7 Pro 3 490** as
the pick and the **CMF Buds Pro 2 2 499** with its withdrawal retracted and awaiting a decision
that is not coming from this entry. Leave both as they are. **Do not reopen this without him
asking**, and if it is reopened, start by pricing the three unpriced models, not by re-arguing the
two that are priced.

**The original entry, kept for the evidence:**

**Opened 2026-09-13 by the source audit.** This is in [earbuds.md](earbuds.md), not the PC build,
but it belongs in the same list because it changes what gets bought.

**What happened.** [earbuds.md](earbuds.md) withdrew the **CMF Buds Pro 2 at 2 499** with:
*"the same review is explicit that it loses on sound to every competitor in its class —
bass-forward with suppressed mids and highs."*

**Andro-news says that about the CMF Buds at $35** — a different model, in the up-to-$40 class.
About the **CMF Buds Pro 2**, which won the up-to-$60 class, the same reviewer says the opposite:

> *"Without it [the gold sound profile], the CMF headphones sounded the **most balanced and
> high-quality**."*
> *"We decided to give one extra point to the CMF headphones just because they **play well out of
> the box**, without any additional settings."*
> *"The microphones are nice and feel good even on the street."*
> *"The only thing that let me down a bit was **the ANC**."*

Both axes are inverted: it won its class partly **on sound**, and its weak point there is **ANC**.

**What is still true against it.** RTINGS measures it at **+8 dB bass / −3 dB treble**, total
deviation **11 dB** — the worst in the table, and that measurement stands on its own. What does
not stand is the claim that a second, subjective source agreed with it. The only reviewer on
record who listened to this exact model says the opposite.

**And one qualification, added after the transcript was re-read in full — it is owed to the
Realme.** The CMF's sound win in that review is smaller than the quotes above suggest on their own:

> *"After using the gold profile settings, Realme and OnePlus, which have identical hardware,
> started to play almost the same and **no worse than CMF**. In the end, we decided to give **one
> extra point** to the CMF headphones just because they play well **out of the box**, without any
> additional settings."*

So it is a **one-point, out-of-the-box win**, and after a setup the reviewer says *"literally
everyone can follow"* the Realme matches it. That narrows the gap without closing it: the
withdrawal was still made using another product's verdict, and the RTINGS measurement is still the
only hard evidence on either side.

**The options and the money:**

| | UAH | What you get |
|---|---:|---|
| **Put the CMF Buds Pro 2 back on the list** | **2 499** | The cheapest thing here, RTINGS' budget pick for calls, winner of its class against OnePlus Buds 3, Redmi Buds 6 Pro, Oppo Enco Free 3 and Realme Buds T6 Pro, with microphones that *"feel good even on the street"*. Against it: the worst measured tuning of the shortlist, and weak ANC by its own reviewer. **Saves 991 against the current pick.** |
| **Leave the pick where it is** | **3 490** | Realme Buds Air 7 Pro — *"flagship-level"* sound, won the tier above, and the measured-tuning objection to the CMF does not apply to it. |
| **Buy nothing yet and close three gaps first** | — | Three things were never priced. The **Samsung Galaxy Buds 3 Pro**, a reviewer's explicit *best for work and calls* pick for a non-Apple user. The **Creative Aurvana Ace 3** ($150, ~6 200), whose measured review names transparency mode — not the microphone — as its weakness. And the **Huawei FreeBuds Pro 4** ($200, ~8 300), called *"the best microphone in their class"* and *"a reference microphone"* — the strongest mic claim made about anything near this budget, on a purchase whose stated point is the microphone. Its cost: several features, including its own codec, need a Huawei phone. |

**I have not re-picked it.** The withdrawal is retracted in [earbuds.md](earbuds.md) and the row is
marked as awaiting this decision. If 991 UAH is not worth a conversation, say so and the Realme
stands.

### 7. CLOSED 2026-09-13: both prebuilts rejected - "i dont care about those"

**Dmytro's answer, after being shown the money and the trade:** he is not buying either. The
**ASGARD Hel** (110 196 all-in, 14 333 under Max, 6-core 8400F, unnamed 650 W PSU) and the
**Vision 5 Pro** (133 170 all-in, 8 641 over Max for a lower-tier GPU) are both out. **The build
stays a parts build.** Do not raise prebuilts again unless he does.

**The original entry, kept for the pricing work:**

**Opened 2026-09-13.** You sent both and asked directly — *"what do you think about this pc, price
and components"* and *"what about this one"* — and **no document ever answered.** The source audit
priced and itemised them. I initially recorded them as "not proposed", which was me making a call
with your money in it; that was not mine to make. Here it is instead.

**ASGARD Hel — click.ua, 96 099 (from 106 979), in stock, 36-month warranty**

| | |
|---|---|
| CPU | **Ryzen 5 8400F** — 6 cores, 4.2-4.7 GHz, Zen 4, no iGPU |
| GPU | **RX 9070 XT 16GB** |
| RAM | 32GB DDR5-5600 | 
| Board / storage / PSU | B650 / 1TB NVMe / **650W, brand not stated** |
| Case, cooling | 1stPlayer T3-BK-4F1, air |

**Like for like against the build sheet.** The prebuilt is a tower only, so add the monitor and
Windows this sheet carries:

| | Tower | + monitor 6 999 + Win 7 098 | vs sheet |
|---|---:|---:|---|
| **ASGARD Hel** | 96 099 | **110 196** | **14 333 under Max**, and Max's 9070 XT is the one in the availability crisis above |
| **MAX build** | — | **124 529** | 9700X + 9070 XT |
| **WORKING build** | — | **115 389** | 9700X + 9070 **GRE** — the prebuilt is **5 193 cheaper with a higher GPU tier** |
| **Vision 5 Pro** (gamingpc.com.ua) | 119 073 | **133 170** | **8 641 OVER Max**, for an RTX 5070 — a lower tier than Max's 9070 XT. **That is the answer to your question about it: it is poor value against this sheet.** |

**What you give up on the Hel, and it is not small.** The **Ryzen 5 8400F is a 6-core Zen 4 part
that appears nowhere in [cpu.md](pc_build/components/cpu.md)'s table** — click.ua sells it at
7 100. Against the 9700X's 8 Zen 5 cores that is the exact axis this build was specified on:
heavy repos, language servers, parallel tooling. A **650W PSU of unstated make** on a 9070 XT
undoes the entire [psu.md](pc_build/components/psu.md) analysis — hold-up time, platform, the
21.8 ms figure that also decides the UPS question. **1TB only**, against
[storage.md](pc_build/components/storage.md). Case and cooler unmeasured. And you cannot apply any
of the research in this repo to a fixed configuration.

**What you gain.** 14 333, a single 36-month warranty against a dozen separate ones, assembly
included, and **an RX 9070 XT that is actually in stock** — which the Max build currently is not,
per the URGENT section above.

**Not used here, deliberately:** gamingpc.com.ua's per-build FPS figures. The site's own
disclaimer calls them *"averaged and for demonstration"*, and
[tools.md](pc_build/tools.md) documents why they cannot be trusted. The comparison above is on
parts and price only.

**The honest shape of it:** this is not a cheaper version of your build, it is a different
purchase — a mid-range CPU carrying a high-end GPU, which is the opposite balance to the one this
sheet argues for. I am not recommending it and I am not ruling it out. **If the 14 333 matters
more than the four cores, say so and I will price the delta properly; if not, say so and it
closes.**

### Not a decision, but worth knowing before you buy

**The GPU document's main source is sponsored by the shop you would buy from.** GECID's review
runs a live **Telemart** promo code for **ASUS** cards, and the two cards under test are ASUS.
All fourteen of its claims are verbatim accurate and it ends by recommending the *RTX 5070*, so
nothing reads as bought - but it is now disclosed in
[gpu.md](pc_build/components/gpu.md). **Eleven of the 55 videos read so far carry a paid
sponsor**, and no document disclosed any of them before this audit; they are disclosed now.

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
| [monitor.md](pc_build/components/monitor.md) | **Closed 2026-09-12: ASGARD AS275QC, 6 999** (click.ua; Foxtrot matches, Rozetka 7 799). 27" VA curved 1440p 200Hz, no height adjustment. Chosen by Dmytro after two rules this file applied were found unsound: height adjustment was never his requirement, and "must be independently measured" admits only 1 of 11 monitors at the shop being bought from. AOC Q27G4ZR 8 669 / Q27G4XF 6 899 remain the fallback |

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

1. **Which of the three builds?** Lean 92 192, Working 115 389 (the recommendation) or Max
   124 529. **Only one item in "Still open" above is still open** - item 4, the written quotes
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

**Confirmed - 16GB is the weak point, but the citation needs a date** (corrected 2026-09-13).
ScatterVolt's flat answer for DDR5 is **"32GB, that's all you need"** - stated as the target,
with no budget exception offered. That is verbatim, and it is from his **parts guide of
2025-09**.

**His combo guide of 2026-08 - eleven months later, after the DRAM price spike this whole
section is about - says the opposite for this build's tier:** *"I really think 16 GB of DDR5
memory is still very much doable. But if you wanted 32 and you have the budget for it, then go
for it."* So he is **not** a third independent source for 32GB; he is the same source at two
dates, and his current position is "16GB is doable, 32GB if you can afford it" - which is the
Lean-versus-Working split this project already runs. **The tiering is unchanged and now better
supported; the "third independent source" line is withdrawn.**

**Correction - the 750W PSU is not over-specified.** The audit called it "the least Lean-like
line in the Lean build". GamingScan's rule is that **power supplies are at their best operating
between 50% and 80% of maximum capacity**; Lean's measured ~373W peak against 750W is **~50%** -
the bottom edge of that band, not outside it. ScatterVolt's rule points the same way: take the
GPU maker's recommended wattage and add ~100W for safety. The 750W is correctly sized, and the
earlier remark is withdrawn.

**Frame check (not transcript-only) - re-done and corrected 2026-09-13.** The stills this
paragraph originally claimed were **never saved**; `pc_build/frames/` held twelve PNGs, all from
the four GPU videos, so the claim was not re-checkable. Three ScatterVolt frames are now on disk.
`frames/PsqulPtiR3g_17m18s.png` **confirms the card word for word**: "AM5 ideal RAM kits:
6000mhz CL30 DDR5 / 6000mhz CL28 DDR5", "LGA 1851 ideal RAM kits: 6400mhz CL32 DDR5". One
correction to what follows: this was called *"a claim the audio never states"*, and the narration
**does** state two of the three lines - *"For an AM5 gaming PC, choose a RAM kit that is 6,000
MHz for the [CL]30"* and the 6400 CL32 line. Only **6000 CL28** is on-screen only. The
substantive point is unchanged: an
on-screen card reading **"AM5 ideal RAM kits: 6000MHz CL30 DDR5 / 6000MHz CL28 DDR5"**. This
build buys **6000 CL36** on Working and Max. It is not an oversight - [ram.md](pc_build/components/ram.md)
does the arithmetic (CL36 at 6000 = **12.0 ns**, CL30 = **10.0 ns**) and prices the 2 ns at
**1-4% in games, mostly in 1% lows, near nothing in tooling, for 1 750**. Recorded as a third
source preferring CL30, and overruled on the same measured grounds as before.

**Added to the handover, because a shop assembles this machine:** a 2-stick DDR5 kit **must go
in the second and fourth DIMM slots** (A2/B2) or it runs single-channel - the build error with
the largest silent performance cost. Worth stating explicitly on the order, and worth verifying
in BIOS on collection. (Corrected 2026-09-13: this said *"the most common build error in all
four videos"*. It is covered at length by **JayzTwoCents alone**; GamingScan mentions dual
channel once in passing, and ScatterVolt and optimum do not raise DIMM placement. Jay's own
advice is *"consult your manual"*, which every board ships with.)

**Two more handover items, added 2026-09-13 from the same four videos:**

- **The AK400 must be mounted in push, not pull.** JayzTwoCents measured *"up to 10 degrees
  celsius"* between the two on an air cooler, and *"if you're running an air cooler and you only
  have one fan push is the only config"*. The AK400 is a single-fan tower.
- **Check the fan-header mode in BIOS.** optimum: *"double check in the Bios whether your fans
  are set up for pwm or DC operation ... three pin fans are DC and 4 pin is pwm."* This is the
  open question in [case.md](pc_build/components/case.md) about the CC560 V2's unlabelled fans -
  verify rather than assume the board auto-detects.

The remaining mistakes these videos cover - thermal paste quantity, paste in the socket,
standoffs, front panel headers, GPU clearance against drive cages, and removing the clear
protective film from the cooler's coldplate - are the assembler's responsibility under the
warranty, not ours.

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
