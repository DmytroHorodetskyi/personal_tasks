# Motherboard

## CURRENT ANSWER (2026-09-11)

| Tier | Board | Price | Status |
|---|---|---:|---|
| **Lean** | ASRock **B850M Pro RS WiFi** | **6 965** | Telemart, marked «Закінчується» - running low |
| **Working** | ASRock **B850 Pro RS WiFi** | **8 829** | Telemart, in stock |
| **Max** | **conditional on the quote** - the same ASRock **8 829** if Telemart supplies the build, **ASUS TUF B850-PLUS WIFI 9 399** if Brain does | | Brain stocks no ASRock B850 but this TUF |

Everything below is layered by date and the later layer wins. Reading order if you only want the
reasoning: the criteria table next, then **the 2026-09-11 research pass**, then the sections after
it. The 2026-09-09 decision and the 2026-09-10 stock section are kept for their arguments and are
marked where they are out of date.

## What the motherboard does for this machine

It adds no performance. What it buys is **connectivity, power delivery, and the option to
upgrade later** - and since AM5 is supported through 2029 with Zen 6 landing on the same
socket, "later" is a real consideration here rather than a theoretical one. The board is
also the part that decides how annoying the machine is to live with: enough USB, front
USB-C, a second M.2 slot for the SSD you will add, working Wi-Fi.

The rule for this build: buy the cheapest board that has every port you need and a VRM
comfortably above the CPU's needs. Do not buy chipset tiers.

## The characteristics that matter, and how to read them

A motherboard does not make a machine faster - it decides whether it stays stable, how many
drives it takes, and what still plugs in three years from now. Rows ordered accordingly.

| # | Spec (unit) | What it means, plainly | What it is here |
|---|---|---|---|
| 1 | **Measured VRM temperature (C)** | The VRM converts 12V into the ~1.2V the CPU wants. Under-built ones run hot and throttle. **Stage counts on the box are marketing; the measured temperature is not.** | The spread on this list is enormous: **54 C** on the best boards against **110 C and 128 C** on two ASUS Prime boards. Insist on a review with a number. |
| 2 | **Brand reliability record** | Not a spec, but it outranks most of them here: the 9800X3D has a documented failure cluster, **~82% of it on one vendor's boards**. | Steers the choice to MSI - see the reliability section below. This is why the best-VRM board on the list is not the pick. |
| 3 | **M.2 slots: count and lane source** | Each takes one NVMe drive. Some slots share lanes with the GPU slot or the SATA ports, so filling them disables something. | **2 minimum** - boot drive now, games drive later. The pick has 3 (one Gen5, two Gen4). Check the manual for lane sharing before filling the last one. |
| 4 | **LAN speed** | Wired ethernet. | 2.5GbE is the sane floor in 2026; the pick has **5GbE**. One board here is still on **1 GbE**, which is a 2015 spec. |
| 5 | **Front-panel USB-C header** | The internal connector that makes the *case's* front USB-C port work. | **The thing people forget.** Without it that port is dead. Present on the pick, at 20Gbps. |
| 6 | **BIOS support: flashback and update life** | Flashback updates the BIOS with no CPU installed. Longer-term, whether the vendor keeps shipping BIOSes decides if a Zen 6 chip ever drops in. | Flash the board **before first real use** - the worst 9800X3D outcomes cluster on stale firmware. No vendor has committed to Zen 6 on B650. |
| 7 | **Wi-Fi and Bluetooth** | Onboard module or nothing. **Corroborated 3:1** (2026-09-13): Socket-X, PC Centric and GeekaWhat all require it - GeekaWhat calls it *"a red line"* for his own build company; only Paul's Hardware (2020) offers the USB-dongle alternative. | If you want Wi-Fi, buy it onboard - a card afterwards costs more than the board difference. Bluetooth rides along, which is how a headset or controller connects. |
| 8 | **Audio codec** | ALC897 is basic; ALC1220 / **ALC4080** are audibly better. | Only matters with desktop headphones rather than USB ones. The pick has ALC4080; most of the list is ALC897. |
| 9 | **Chipset (B650 / B850 / X870)** | Sets features and lane counts, **not speed**. B850 gives PCIe 5.0 to the GPU slot; X870 mainly adds USB4. | **B850** is the sane default. X870 costs ~4 700 more here for a port you will not use. |
| 10 | **Form factor** | ATX / mATX / ITX. | **ATX** - cheaper per feature, better cooling, easier to build in. |
| 11 | **Fan headers (count)** | Every case and CPU fan plugs into one. Too few and you are buying splitters and hubs. Socket-X, 2026: *"A board with only two fan headers is a trap ... Aim for at least four or five."* | **Not checked** on the pick (added 2026-09-13). The Lancool 216 ships 3 fans and the AK400 adds one, so four headers is the floor. One lookup on ASRock's spec page settles it. |
| 12 | **Rear I/O port count** | You run out of USB faster than you expect. The same brand survey notes lower-end **ASRock** boards *"cut back harder on onboard audio or rear USB connectivity to hit aggressive pricing"*. | **Not checked** on the pick (added 2026-09-13). Worth counting against keyboard, mouse, headset, webcam and an external drive. |

**Ignore:** PCIe 5.0 to the GPU (an RX 9070 XT loses nothing on 4.0 x16), advertised phase
counts with no thermal test behind them, armour and heatsink styling, and RGB headers.

**And read the SKU carefully.** This category is full of near-identical names that are not
near-identical boards: ASUS **TUF** B850-PLUS vs ASUS **PRIME** B850-PLUS (the 110 C one), and
MSI MAG B850 TOMAHAWK **WIFI** vs TOMAHAWK **MAX** WIFI.

## Specifications

| **MSI MAG B850 TOMAHAWK WIFI** | |
|---|---|
| Socket / chipset | AM5 / **B850** |
| Form factor | ATX, 8-layer PCB, 2oz copper |
| **VRM** | **14+2+1, 80A MPS stages**, dual 8-pin EPS - measured **64 C** (TechSpot, 170W 9950X; the 58 C once quoted here was a lighter in-build test) |
| Memory | 4x DDR5 UDIMM, up to 256GB, **8200+ MT/s (OC)**, EXPO |
| GPU slot | **PCIe 5.0 x16** (from CPU) |
| Other slots | 1x PCIe 4.0 x4, 1x PCIe 3.0 x1 |
| **M.2** | **3x**: 1x PCIe 5.0 x4 (CPU) + 2x PCIe 4.0 x4, with heatsinks |
| SATA | 4x 6Gb/s |
| **LAN** | **Realtek 5GbE** |
| Wi-Fi | **Wi-Fi 7** (2.4/5/6GHz, up to 2.9Gbps) + Bluetooth |
| **Audio** | **Realtek ALC4080** 7.1 |
| Rear USB | 1x USB-C 20Gbps, 1x USB-C 10Gbps, 4x USB-A (10 and 5Gbps), 4x USB 2.0 |
| Front headers | **USB-C 20Gbps header**, USB 3.2 header, 2x USB 2.0 headers |
| BIOS | Flash BIOS Button (update with no CPU installed) |

How to read the rows that decide a board:

- **VRM stages and measured temperature.** The VRM is the circuitry converting 12V into the
  ~1.2V the CPU wants. Under-built ones throttle or cook - and this list contains boards
  measured at **110 C and 128 C** against this one's 64 C. Stage counts on the box are
  marketing; the measured temperature is not.
- **M.2 count and lane source.** One drive now, one later, without unplugging anything.
  Watch for lane sharing - filling some slots disables SATA ports; check the manual.
- **The front USB-C header.** Without it the case's front USB-C port is dead. Easy to miss.
- **Chipset** sets features, not speed. B850 gives PCIe 5.0 to the GPU; X870 mainly adds
  USB4, which costs ~4 700 here and does nothing for this build.

Note the exact SKU: **MAG B850 TOMAHAWK WIFI**. MSI also sells a **TOMAHAWK MAX WIFI**
(different board, 4x M.2) and the ASUS list contains a **PRIME** B850-PLUS that must not be
confused with the **TUF** - the Prime is the 110 C board.

## Options

Prices: lowest hotline.ua offer, 2026-09-09, UAH.

| Model | UAH | Notes | Verdict |
|---|---:|---|---|
Measured VRM temperatures below are from Hardware Unboxed's B850 roundup: one hour of
Cinebench R23 on a **170W Ryzen 9 9950X**, i.e. a far harsher test than a 120W 9800X3D. Over
30 of the 47 boards stayed under 80 C.

| Model | UAH | VRM | Measured VRM temp | Audio | LAN | Verdict |
|---|---:|---|---|---|---|---|
| ASRock B650M-HDV/M.2 | 4 326 | thin | - | ALC897 | 1G | mATX, 1x M.2. No. |
| ASUS PRIME B650M-K | 4 530 | thin | **128 C** | ALC897 | 1G | Hardware Unboxed's worst-in-class result. **Avoid.** |
| ~~GIGABYTE B650 GAMING X AX V2~~ | 6 199 | unknown | no data | ALC897 | 2.5G | **Withdrawn.** No tier-1 review exists; every "review" online is a content farm with contradictory specs. Owner reports of random shutdowns fixed only by RMA. Oldest platform of the group and the least likely to get a Zen 6 BIOS. |
| GIGABYTE B850 EAGLE WIFI6E | 6 899 | 8+2+2, 60A | **over 80 C** | ALC897 | **1 GbE only** | Passed, but bottom third. Also the only board here stuck on gigabit ethernet. Acceptable for a 120W CPU; no longer my pick. |
| ASRock B850 Pro RS | 6 993 | 14+2+1, 80A | **54 C - best in class** | ALC897 | 2.5G | **Withdrawal scoped 2026-09-13: it applied to a 9800X3D build and this is not one** - see reliability below. The plain SKU has no Wi-Fi; the builds take the **WiFi** variant. |
| MSI B850 GAMING PLUS WIFI | 7 979 | - | no data | - | 2.5G | Fine, undocumented. |
| **ASUS TUF GAMING B850-PLUS WIFI** | **9 295** | 14+2+1, 80A | **54 C - 2nd of 47** | mid-tier | 2.5G | The cheaper *and* the cooler of the two good picks. 3x M.2, screw-in heatsinks, Wi-Fi 7. |
| ~~**MSI MAG B850 TOMAHAWK WIFI**~~ | 10 293 | 14+2+1, 80A MPS | **64 C** (was quoted here as 58 C) | **ALC4080** | **5 GbE** | **No longer the pick.** Warmer than the TUF, six-layer PCB, and 11 299 at Telemart today. Best audio and networking of the group. |
| ASUS PRIME B850-PLUS WIFI | - | weak | **110 C** | - | 2.5G | Note the name: this is the *Prime*, not the TUF. **Avoid.** |
| MSI MAG X870 TOMAHAWK WIFI | 14 999 | | | | | Adds USB4. No. |
| MSI MAG Z890 TOMAHAWK WIFI | 16 499 | Intel LGA1851 | | | | Only relevant if you had chosen Intel. |

## Scope correction 2026-09-13: the brand risk below is a 9800X3D finding, not a board finding

**The contradiction that forced this.** This file withdrew the ASRock B850 Pro RS *"on brand
risk, not hardware"*, while all three builds in [../../pc_build.md](../../pc_build.md) ship an
**ASRock B850 Pro RS WiFi**. One of the two had to move. **The withdrawal moves**, for a reason
stated in this file's own reliability section:

> *"The **9700X and 9600X show no failure pattern at all** - non-X3D Zen 5 looks clean."*

The section below was written when [cpu.md](cpu.md)'s pick was the **9800X3D**. It is not any
more: Working and Max take the **9700X**, Lean the **7500F**. Every documented failure in that
section is an X3D chip - 108 cases on the 9800X3D, ~2 on the 9950X3D, one on the 9850X3D, **none
on the non-X3D parts these builds buy**. A May 2026 brand survey (Socket-X, 406k views) separately
says the old ASRock reputation *"doesn't really fit anymore"* and raises no reliability concern in
its ASRock section.

**So the board stays**, on its measured merits: 14+2+1 80A VRM, **54 °C - best in class** of the 47
boards Hardware Unboxed tested, 2.5G LAN, Wi-Fi 6E on the WiFi SKU. **If the CPU ever changes to an
X3D part, this scope correction expires and the section below applies again in full.**

## Reliability: the 9800X3D board question (this changes the pick)

There is a documented, still-unclosed pattern of **Ryzen 7 9800X3D CPUs dying**, and it is
concentrated by board brand. This matters because the CPU verdict in [cpu.md](cpu.md) is the
9800X3D.

**The timeline, verified:**

- Feb-Apr 2025: a Reddit megathread grows to ~108 documented cases. Gamers Nexus' snapshot of
  the first 42 was **ASRock 34, ASUS 6, Gigabyte 1, MSI 1**; Tom's Hardware and TechSpot's
  count of ~108 put **98 (82%) on ASRock**.
- May 2025: ASRock pulls BIOS 3.20 without explanation, ships 3.25 lowering PBO TDC/EDC
  limits, and blames a mix of memory compatibility, aggressive PBO and user mishandling. It
  has **never published a root-cause analysis**.
- Jan 2026: a fresh wave on **ASUS 800-series** boards - five dead CPUs in two weeks, mostly
  high-end X870E (ROG Crosshair Hero, Strix X870E-E). ASUS announces an "immediate internal
  review" with AMD and has published nothing since.
- Feb 2026: ASRock ships a new BIOS base with AMD - **BIOS 4.10 / AGESA ComboAM5 PI 1.3.0.0a**
  - explicitly addressing "boot failure occurring on certain CPUs".
- Mar-Apr 2026: **failures continue on 4.10.** Igor's Lab documents three fresh cases on
  systems running stock or EXPO-only. One user reportedly lost **three 9800X3D chips in four
  months on an ASRock B850M Pro RS WiFi**.

**What the cause actually is: still disputed.** AMD calls it a memory-compatibility issue in
older BIOSes that has been "rectified" - but many failed chips had POSTed and run for weeks,
and some show physical burn damage on the pads, which a POST-blocking bug does not explain.
Gamers Nexus found *insufficient* voltage (ASRock's fix raises the 9800X3D to 1.2V), while
German coverage attributes to ASRock a suspicion of *excessively high* SoC voltage. Those
readings contradict each other, and no vendor has settled it.

**Scale, honestly:** a few hundred cases against many hundreds of thousands of chips sold.
This is a low-probability risk, not a coin flip. But it is avoidable at zero cost by brand
choice, which makes it worth acting on.

**Other chips:** the 9850X3D has one credible case (an ASUS X870 that killed a 9800X3D and
then its 9850X3D replacement). The 9950X3D has ~2 cases against the 9800X3D's 108. The
**9700X and 9600X show no failure pattern at all** - non-X3D Zen 5 looks clean.

## The Zen 6 upgrade path is weaker than I implied

I earlier described the board as buying you a drop-in Zen 6 upgrade. The research pass
qualifies that materially:

- **The socket is safe.** AMD stated at Computex that **AM5 is supported through 2029**, and
  Zen 6 desktop ("Olympic Ridge") is assigned to AM5 in AMD's own technical documentation -
  spotted by InstLatX64 and reported by five outlets. Caveat: that AMD page is no longer
  publicly accessible, so the evidence is now archived screenshots, and AMD has still not
  formally announced the product. Expected launch ~**CES 2027**.
- **The board is the risk, not the socket.** Support depends on each vendor shipping a BIOS
  built on the right AGESA - it is **not automatic** for existing B650/B850 boards, and no
  vendor has publicly committed to a Zen 6 BIOS for B650.
- **BIOS flash capacity is the specific trap:** boards with 32MB BIOS chips have already hit
  space limits supporting *current* CPUs. Boards with smaller flash are the ones most likely
  to get no Zen 6 BIOS, or a stripped one that drops older CPU support. Flash capacity is
  not published for any of these boards - it is the single most valuable missing data point
  here, and it is not obtainable from spec sheets.

Practical read: treat a future Zen 6 upgrade as **plausible but unguaranteed**, and let it
push you toward a vendor that actively ships BIOS updates rather than toward the cheapest
board. It is a tiebreaker, not a reason to spend.

## DECISION (2026-09-09): per tier, and the expensive board is no longer needed - PRICES AND LEAN BOARD SUPERSEDED

> **Out of date in two places.** The ASRock is **8 829**, not ~9 400, and the Lean tier no
> longer uses an MSI board - see the 2026-09-11 sections. The reasoning below - why the VRM
> requirement relaxed at 65W, and what "cheaper" actually costs - still holds.

**New requirement, stated by Dmytro on 2026-09-09: Wi-Fi is required.** That rules out the
plain non-WiFi SKUs and narrows the price gaps below, because every ASRock "Pro RS" figure
quoted earlier in this doc was for the board *without* the wireless module.

| Tier | Board | Real price | Why |
|---|---|---:|---|
| **Ceiling** | **ASRock B850 Pro RS WiFi** | **~9 400** (8 802-10 623) | Best measured VRM of 47 boards (54 C), 2.5GbE, ATX |
| **Probable** | **ASRock B850 Pro RS WiFi** | **~9 400** | Same board - nothing above it earns its money at 65W |
| **Floor** | **MSI B650M GAMING PLUS WIFI** | **~7 100** | 2 300 back; mATX and B650, which is an acceptable trade at this tier |

### Why the MSI Tomahawk pick was dropped

It cost **~12 000** at real prices and was chosen almost entirely because the **9800X3D
failure cluster is ~82% ASRock**. **No tier contains a 9800X3D any more** - see
[cpu.md](cpu.md) - so that argument does not apply to a single build on the list. What the
Tomahawk's extra ~2 600 still buys is 5GbE and the ALC4080 codec; worth it only on a network
above gigabit or with desktop headphones driven off the board.

### The VRM requirement relaxed, and this is the real change

Every "must have a strong VRM" argument in this document was sized for a **120W / 162W PPT**
9800X3D. The chosen CPUs are a **9700X (65W / 88W PPT)** and a **9600X (65W / 88W)**. At half
the power the VRM stops being a differentiator - which is what makes the cheap boards
defensible now and did not before. The GIGABYTE B850 EAGLE's **>80 C** result, disqualifying
under a 120W chip, would be unremarkable under a 65W one.

It is **not** why the EAGLE is still rejected. That is **1 GbE**, a 2015 specification.

### What "cheaper" actually costs

| Trade | Consequence |
|---|---|
| B850 -> **B650** | PCIe 4.0 instead of 5.0 to the GPU - **costs the RX 9070 nothing measurable**. The real loss is that B650 is the oldest platform here and the **least likely to receive a Zen 6 BIOS**, quietly closing the upgrade path |
| ATX -> **mATX** | Fewer expansion slots, tighter build. Irrelevant to this parts list |
| 2.5GbE -> **1 GbE** | Not accepted at any tier |

The ~2 300 between the ASRock and the MSI B650M buys the better VRM, ATX, and the Zen 6 door
staying open. That last point is why the top two tiers pay it and the floor does not.

### Still ruled out, regardless of tier

| Board | Reason |
|---|---|
| ASUS PRIME B650M-K | **128 C VRM** - worst in class in Hardware Unboxed's test |
| ASUS PRIME B850-PLUS WIFI | **110 C**. Note this is the *Prime*, not the TUF |
| GIGABYTE B650 GAMING X AX V2 | No tier-1 review exists anywhere; owner reports of random shutdowns fixed only by RMA |
| GIGABYTE B850 EAGLE WIFI6E | **1 GbE only** |
| MSI MAG X870 TOMAHAWK WIFI | ~15 000 for USB4 this build will not use |

### Open check before purchase

The ASRock B850 Pro RS WiFi is believed to ship **Wi-Fi 6E**, not Wi-Fi 7 (its mATX sibling,
the B850M Pro RS WiFi, is documented as 6E + 2.5G LAN). The ASUS TUF B850-PLUS WIFI at
~10 500 **is** Wi-Fi 7. If Wi-Fi 7 matters, that is what the extra ~1 100 buys; if the router
is Wi-Fi 6, it is moot. **Confirm the ATX board's wireless standard at purchase.**

## Verdict (revised) - SUPERSEDED

> **Historical.** This verdict predates two things: the 2026-09-09 per-tier decision above
> (which dropped the Tomahawk when the CPU moved off the 9800X3D) and the 2026-09-11 research
> pass below (which measured the Tomahawk at 64 C and the TUF at 54 C). It is kept for the
> reasoning, not the conclusion. **The current picks are in the two dated sections that follow.**

**MSI MAG B850 TOMAHAWK WIFI, 10 293.** This replaces the GIGABYTE B850 EAGLE, and the
reasons are all measurements rather than preferences:

- **VRM**: 14+2+1 with 80A MPS stages, measured **64 C** under the 170W 9950X. (The 58 C
  in-build figure and the 69 C at 183W with *no case airflow* came from a lighter test.) The
  Eagle exceeded **80 C** in the same class of test and landed in the bottom third.
- **Networking**: 5 GbE plus Wi-Fi 7, versus the Eagle's **1 GbE**. On a machine that pulls
  large repos and container images, gigabit is the one spec here you would actually notice.
- **Audio**: ALC4080 with an isolated audio section, versus ALC897. Audible if you use
  desktop headphones.
- **Brand record**: in the 9800X3D failure saga MSI accounted for 1 case out of the first
  42 documented. That is the cleanest record of any brand named in this document, and it is
  the CPU this build uses.
- It is the only board of the five with a genuine tier-1 recommendation behind it, and it
  carries an auxiliary 8-pin PCIe power connector for the GPU slot.

One documented quirk to know: on the MAX variant, populating the third M.2 drops the third
PCIe slot to x2, and enabling Wi-Fi costs some M.2 bandwidth. Neither affects a build with
one GPU and two SSDs. The Wi-Fi module is a MediaTek part that does not support 320 MHz
channels, so it is Wi-Fi 7 branding with a bandwidth ceiling - irrelevant on a wired desk.

**Cheaper and defensible: ASUS TUF GAMING B850-PLUS WIFI, 9 295** (-1 000). 14+2+1 80A,
Wi-Fi 7, 2.5 GbE. Its VRM measures **54 C, second-best of 47 boards tested**,
and it has only three M.2 slots with screw-in heatsinks. **Important disambiguation:** the
ASUS boards that measured 110-128 C are the **Prime** B850-Plus and Prime B850M-K, *not*
the TUF - do not let a "avoid ASUS B850" headline talk you out of the wrong board.

**Cheapest acceptable: GIGABYTE B850 EAGLE WIFI6E, 6 899** (-3 394). Its >80 C result came
under a 170W chip; a 120W 9800X3D will not stress it the same way. You are accepting 1 GbE
ethernet and weak audio to save 3 400.

**Do not** buy the ASRock B850 Pro RS despite it having the best VRM in class (54 C, the
coolest of 47 boards tested) - see below. **Do not** buy the GIGABYTE B650 GAMING X AX V2
that I previously suggested as the budget option. **Do not** buy X870/X870E for USB4.


## The pick has to survive the store (2026-09-10) - SUPERSEDED 2026-09-11

> **This section's premise was wrong.** Telemart does stock the ASRock B850 Pro RS WiFi
> (8 829, in stock on 2026-09-11); **Brain** is the shop that carries no such board. The
> four boards below have since been checked. See the research pass at the end of this file.

**Telemart does not stock the ASRock B850 Pro RS at all.** Its B850 range on 2026-09-10:

| Board | Telemart |
|---|---:|
| MSI B850M GAMING PRO WIFI6E | **7 599** |
| Gigabyte B850M GAMING X WIFI6E | 7 999 |
| ASUS TUF GAMING B850-PLUS WIFI | 9 399 |
| MSI MAG B850 TOMAHAWK WIFI | 10 499 |

The ASRock stays this doc's pick - **stock at one shop is a purchase-time filter, not a
selection criterion**, and stock moves weekly. But one store has to supply and assemble the
whole machine, and which store that is has not been decided - Brain and Telemart are both
candidates and neither has quoted yet. Brain's ASRock stock is unchecked. **If Telemart wins
the quote a substitute is forced**, and **none of the four above has been checked against the
criteria in this doc** - VRM temperatures under sustained load, M.2 count, 2.5GbE,
audio codec. The MSI B850M GAMING PRO is carried in the Lean build on price alone, which is
exactly the kind of shortcut the rest of this document exists to avoid.

Do this check when the written quotes come back, since the quote decides which board is actually
on the table.

## Research pass, 2026-09-11: the stock claim above is wrong, and the VRM numbers are now measured

Three things came out of this pass. The first overturns the open question; the second replaces
two estimates with measurements; the third answers the Wi-Fi question left open above.

### 1. Telemart does stock the ASRock. Brain is the one that does not.

Checked 2026-09-11 on both shops' own B850 listings:

| | ASRock B850 Pro RS WiFi | Other ASRock B850 carried |
|---|---|---|
| **Telemart** | **8 829 UAH, «Є в наявності»**, 24-month manufacturer warranty | B850 Pro RS (non-WiFi), B850M Pro RS 7 499, B850M Pro-A 6 799, B850M Challenger WiFi White 7 909, B850 LiveMixer WiFi 9 799, B850 Steel Legend WiFi 9 969, B850M-X R2.0 6 039 |
| **Brain** | **not carried** | **B850 LiveMixer WiFi 9 499 - the only ASRock B850 Brain sells at all** (44 B850 boards listed, one of them ASRock) |

So the pick survives the store; it is Brain that would force a substitute, not Telemart. The
substitute at Brain is a good one: the **B850 LiveMixer WiFi**, 14+2+1 80A, **57 C measured**,
Wi-Fi 7, 2.5GbE, 3x M.2 - i.e. it beats the Pro RS on wireless and loses one M.2 slot, for
670 more.

Hotline shows 42 offers on the Pro RS WiFi between 7 866 and 10 938, so the ~9 400 figure used
in the tier table above is now high; **8 829 at Telemart is the number to plan with**.

### 2. Measured VRM temperatures, from the completed 47-board roundup

Earlier sections of this doc cite Hardware Unboxed's roundup second-hand. The primary source is
TechSpot's two-part publication of the same test - part 1 (23 boards, Aug 2025) and the
completed 47-board set (Nov 2025). Method: 170W Ryzen 9 9950X, Cinebench 2024 looped one hour,
ATX case, 21 C room, peak PCB-backside temperature by K-type thermocouple. Pass = under 100 C
without throttling the CPU; 30+ boards passed under 80 C.

| Board | Measured | Note |
|---|---:|---|
| Gigabyte B850 AI Top | 52 C | best of 47; irrelevant here (320 USD) |
| **ASUS TUF GAMING B850-PLUS WIFI** | **54 C** | **2nd of 47.** This replaces the "~57 C (unverified)" written above |
| ASRock B850 Pro RS | 54 C | as already recorded |
| MSI MAG B850 Tomahawk **MAX** WiFi | 55 C | the MAX, not the board this doc picked |
| ASRock B850 Steel Legend WiFi | 56 C | |
| ASRock B850 LiveMixer WiFi | 57 C | Brain's only ASRock |
| Gigabyte B850 Gaming X WiFi6E | 60 C | ATX |
| **Gigabyte B850M GAMING X WIFI6E** | **62 C** | 6th of 23 in part 1; comfortably fine |
| **MSI MAG B850 TOMAHAWK WIFI** | **64 C** | not the 58 C quoted above - see below |
| Gigabyte B850M Aorus Elite WiFi6E Ice | 68 C | |
| Gigabyte B850 Eagle WiFi6E | 83 C | as recorded |
| ASUS Prime B850-Plus WiFi / Prime B850M-K | 110 / 128 C | as recorded |

**Two corrections to earlier sections of this document:**

- The **58 C** attributed to the MSI MAG B850 TOMAHAWK WIFI is **64 C** in this test. The 58 C
  figure came from an in-build review of a different sample under a lighter load; against the
  ASUS TUF's 54 C in the same harness, the Tomahawk is the *warmer* of the two, not the cooler.
  The Tomahawk's remaining advantages - 5GbE, ALC4080 - are unaffected.
- The **TUF's VRM is now verified** and is the second-best result in the entire 47-board field.
  The line above calling it "~57 C (unverified)" and "the cheaper of the two good picks" should
  be read as: it is the cheaper *and* the cooler of the two.

Note also that TechSpot lists the non-MAX **B850 Tomahawk WiFi** as six-layer PCB, 3x M.2,
9x USB 3.2 - a cost-reduced version of the MAX. The "8-layer PCB" in this doc's specification
table is the MAX's figure.

### 3. The three unchecked Telemart substitutes, now checked

Prices are Telemart, 2026-09-11 (Brain in brackets where it carries the board).

| | **ASUS TUF GAMING B850-PLUS WIFI** | **Gigabyte B850M GAMING X WIFI6E** | **MSI B850M GAMING PRO WIFI6E** |
|---|---|---|---|
| Price | **9 399** (Brain 9 976) | **8 799** (Brain 8 599) | **7 599** |
| Form factor | **ATX** | mATX | mATX |
| VRM | **14x 80A, 8-layer** | 10+2+2, 60A | **not published** |
| Measured VRM temp | **54 C (2nd of 47)** | **62 C** | **never tested by anyone** |
| M.2 | **3** (1x Gen5 + 2x Gen4) | 2 (1x Gen5 + 1x Gen4) | 2 (1x Gen5 + 1x Gen4) |
| GPU slot | PCIe 5.0 x16 | PCIe 5.0 x16 | **PCIe 4.0 x16** |
| LAN | 2.5GbE | 2.5GbE (Realtek) | 2.5GbE (Realtek 8125D) |
| Wi-Fi | **Wi-Fi 7** | Wi-Fi 6E (RTL8852CE) | Wi-Fi 6E |
| Audio | mid-tier | Realtek, model not published | **ALC897** |
| Front USB-C header | yes | yes (10Gbps) | yes (10Gbps) |
| BIOS flashback | yes | Q-Flash Plus | Flash BIOS Button |
| EPS power | 8+4 | **single 8-pin** | 2x 8-pin |
| Verdict | **passes everything in this doc** | passes; mATX and 2x M.2 are the costs | **fails the documentation test** |

**On the MSI B850M GAMING PRO WIFI6E specifically.** It is the board the Lean build carries on
price alone, and it is the weakest-documented board on the table: MSI publishes no VRM
specification for it, no reviewer has tested it, and the wider pattern is against it - TechSpot
found MSI's other WIFI6E-suffixed mATX board (B850M Gaming Plus WiFi6E) to be a cost-reduced
version using **discrete MOSFETs instead of power stages**, and MSI's discrete-MOSFET boards are
exactly the ones that ran hot in this test (Pro B850M-P hit 121 C once its power limit was
lifted). Its own spec sheet also gives the GPU slot only **PCIe 4.0**, which costs the RX 9070
nothing but shows where the money was saved. At 65W this board will very probably be fine - but
"probably fine" is the standard this document exists to refuse.

**One more data point that matters for the Zen 6 question above.** The Gigabyte's BIOS chip is
**256 Mbit = 32MB** - published, unlike every other board here. That is exactly the capacity the
Zen 6 section names as the trap. It is not disqualifying, but it is the first hard number this
doc has on that question.

### Where this leaves the pick

Nothing forces a change at the Ceiling/Probable tier: **ASRock B850 Pro RS WiFi at 8 829,
in stock at Telemart**, cheaper than the ~9 400 assumed. The one board that would genuinely
compete is the **ASUS TUF GAMING B850-PLUS WIFI at 9 399** (+570): same 54 C class, ATX, 3x M.2,
and **Wi-Fi 7 rather than the ASRock's 6E** - which is the answer to the open Wi-Fi question
below. Both shops carry the TUF, so it is also the substitution-proof choice if the quote goes
to Brain.

For the Lean tier, **Gigabyte B850M GAMING X WIFI6E at 8 799 / 8 599** is measured and passes;
the MSI at 7 599 is 1 200 cheaper and undocumented. That is the actual trade, stated plainly.

**Wi-Fi question above: answered.** ASRock's own product copy for the B850 Pro RS WiFi
specifies **Wi-Fi 6E 802.11axe**, not Wi-Fi 7. The suspicion recorded above was right.

Sources for this pass: TechSpot [23-board part 1](https://www.techspot.com/review/3027-amd-b850-motherboards/)
and [47-board complete roundup](https://www.techspot.com/review/3050-amd-b850-motherboards-full/);
manufacturer specification pages for the
[MSI B850M GAMING PRO WIFI6E](https://www.msi.com/Motherboard/B850M-GAMING-PRO-WIFI6E/Specification)
and [Gigabyte B850M GAMING X WIFI6E](https://www.gigabyte.com/Motherboard/B850M-GAMING-X-WIFI6E-rev-10/sp);
Telemart and Brain B850 category listings and hotline.ua offer list, all read 2026-09-11.

## Cross-check against seven buying guides (2026-09-11)

Dmytro supplied seven videos: Tech Guided *How to Choose A Motherboard for Beginners* (2023),
PC Centric *How To Choose A Motherboard* (2021), Paul's Hardware *3 Levels of Skill* (2020),
Tech Notice *Ultimate Motherboard Guide* (2025), GeekaWhat *How to Pick Parts in 2026* (2025-12),
and two Socket-X explainers, *Every Motherboard Feature Explained* and *Every Motherboard Brand
Explained* (both 2026-05).

**These are general buying guides, not board reviews.** None tests a board, none names any board
on this list, and nothing in them contradicts a measurement recorded above. Their value is as a
checklist: every criterion they raise, against what this document already weighs.

**Already covered here, and they agree:** socket and chipset (B-series is the sweet spot; the
chipset adds connectivity, not speed), form factor, VRM quality with the explicit warning that
**phase counts on the box are marketing and only a review with a measured temperature settles
it**, M.2 count and lane sharing, front-panel USB-C header (PC Centric names it as the single
most common mistake), onboard Wi-Fi bought with the board rather than as a card afterwards,
2.5GbE as the floor, rear USB count, BIOS flashback, and "PCIe 5.0 to the GPU changes no frames".
Socket-X independently reaches this document's own conclusion: the gaming gap between brands is
now tiny, so buy the B-series board with adequate VRM cooling and the ports you need.

### Five things the criteria table above does not weigh

| # | Raised by | Where this build stands |
|---|---|---|
| 1 | **Fan headers** - "a board with two is a trap"; aim for 4-5 (Socket-X) | Fine, and now checked: **ASRock B850 Pro RS WiFi has 7** (2x CPU, 4x chassis, 1x AIO pump), MSI B850M GAMING PRO 5, Gigabyte B850M GAMING X 4. No candidate is short |
| 2 | **Debug LEDs / POST code readout** (PC Centric, Socket-X) | Not a criterion here, but it should be **on the Lean build specifically**: the 7500F has **no iGPU**, so with the card pulled there is no display to diagnose from. The MSI carries 4x EZ Debug LED + a memory-detection LED; the ASRock has a Post Status Checker. Worth confirming on whatever the Lean build actually buys |
| 3 | **BIOS quality and DDR5 memory training** (Socket-X brands video) | A real brand-level difference this doc never scored. ASUS's BIOS is the most-praised; MSI is credited with the smoothest DDR5 memory training; **Gigabyte's BIOS polish and ASRock's fan control are the two named as least refined**. A soft tiebreaker, and it points the same way as the measurements: toward the **ASUS TUF** |
| 4 | **Budget share: 8-12% of the build on the board** (Tech Guided) | Working 8 829/116 800 = **7.6%**; with the TUF, 8.0%; Lean 7 599/92 900 = **8.2%**. All inside the band - this build is not over- or under-spending on the board |
| 5 | **"The board should not cost more than the CPU"** (GeekaWhat) | **The Lean build breaks this rule:** board **7 599** against a 7500F at **6 589**. Not fatal - Wi-Fi is mandatory and AM5 has a floor - but it is the clearest sign that the Lean tier's money is in the wrong place, and it argues against paying the extra 1 200 for the Gigabyte at that tier |

**Ignore-list confirmed.** Socket-X's advice to skip the 12V RGB header and prefer 5V ARGB, and
to treat "premium" onboard audio as marketing next to a cheap external DAC, both match the
ignore list above. Nothing here promotes an ignored item back onto the list.

**One source this document has not used.** Tech Guided names **buildzoid (Actually Hardcore
Overclocking)** as the deepest VRM analysis available - he reads the actual power stages off the
PCB rather than repeating the box. That is exactly the gap on the **MSI B850M GAMING PRO
WIFI6E**, the one board here with no published VRM spec and no test. If the Lean build stays on
that board, a buildzoid segment is the only realistic way to close it.

**One cross-component note, outside this file.** GeekaWhat recommends liquid cooling for any
Ryzen 7. This build pairs a 9700X with an air AK400, which is correct for a **65W / 88W PPT**
part - his advice is sized for 105-170W chips. No change; recorded because it will look like a
contradiction next time someone reads that video. See [cooling.md](cooling.md).

**Net effect on the pick: none.** No video contains a measurement, and the two things they add
that genuinely bear on the choice - BIOS quality and the Lean tier's board-versus-CPU imbalance -
both push toward what the measurements already said: **ASUS TUF B850-PLUS WIFI at the top two
tiers, and no extra spending on the board at the Lean tier.**

## Boards written into the build table (2026-09-11)

| Tier | Board | Price | Why |
|---|---|---:|---|
| **Max** | **ASUS TUF GAMING B850-PLUS WIFI** | **9 399** | 54 C, 2nd of 47 tested. ATX, 3x M.2, **Wi-Fi 7**, the best-regarded BIOS of the four brands, and **stocked by both Telemart and Brain** - the only candidate immune to which shop wins the quote |
| **Working** | **ASRock B850 Pro RS WiFi** | **8 829** | Same 54 C class, ATX, **4x M.2**, 7 fan headers. Wi-Fi 6E rather than 7, Telemart-only. Saves 570 |
| **Lean** | **ASRock B850M Pro RS WiFi** | **6 965** | See below - this replaces the MSI |

Dmytro's instruction (2026-09-11): give Max and Working different boards rather than choosing
one. Note this is the first spec other than the GPU that differs between the two tiers; the
tiering rule stated at the top of [pc_build.md](../../pc_build.md) is that Max is the Working
build with the XT dropped in. The board is now a second difference, at +570.

### The Lean board changed, and the reason is that the MSI has no reviews

The MSI B850M GAMING PRO WIFI6E was carried at 7 599 on price alone. Searching for a review of
it in English, Ukrainian and Russian returns **nothing from any tier-1 outlet**: not TechSpot's
47-board roundup, not TechPowerUp, not TheFPSReview, not Tom's Hardware. What does come back is
the same pattern this document rejected for the GIGABYTE B650 GAMING X - **SEO content farms**
publishing "reviews" with invented test figures. One of them quotes 58 C for MSI's *B850M Gaming
Plus WiFi6E*; TechSpot examined that board and found it uses **discrete MOSFETs instead of power
stages**, which is the configuration that produced MSI's worst result in the whole roundup
(Pro B850M-P WiFi, 121 C with its power limit lifted). A number from a farm, about the wrong
board, in the direction the real data contradicts.

So the answer to "is it acceptable to buy untested" did not need answering, because there is a
**cheaper board that was tested**:

| | MSI B850M GAMING PRO WIFI6E | **ASRock B850M Pro RS WiFi** |
|---|---|---|
| Telemart price | 7 599 | **6 965** (from 7 999; marked «Закінчується» - running low) |
| Measured VRM | **none - never tested** | **77 C** under a 170W 9950X, no power limit |
| M.2 | 2 | **3** |
| GPU slot | PCIe 4.0 x16 | PCIe 5.0 x16 |
| LAN / Wi-Fi | 2.5GbE / 6E | 2.5GbE / 6E |
| Reviewer verdict | - | TechSpot: **"the best-value B850 motherboard available right now"** |

It is **634 cheaper, tested, and better specified**. 77 C is the warmest board in this document's
shortlist, but it was reached under a **170W** chip with no power limit; the Lean build's 7500F
is **65W**, and TechSpot's own note is that below 120W every board in the test performs
identically.

One caveat, recorded rather than hidden: TechSpot qualifies its ASRock recommendation with the
unresolved **X3D failure cluster** and says to buy ASRock only if you are sure you will not run
an X3D chip. The Lean build's CPU is a **7500F**, non-X3D, so the caveat does not apply - but it
does mean this board is the wrong one to keep if a future X3D upgrade is ever wanted. See the
reliability section above.

**Lean total drops 92 900 -> 92 300.** Working drops 116 800 -> 116 300. Max is unchanged at
127 400 - the TUF costs what the old estimate assumed.

## The router, identified 2026-09-11 - and it makes the LAN argument moot

Dmytro's router is a **Xiaomi Mi Router 4A, model R4AC**, made 04/2021. Its specification:

- **Wi-Fi 5** (802.11ac, AC1200: 300 Mbps at 2.4GHz, 867 Mbps at 5GHz). Not Wi-Fi 6, not 6E,
  not 7.
- **10/100 Mbit ethernet ports** - one WAN, two LAN. This is the non-Gigabit 4A; the separate
  "4A Gigabit Edition" is a different model.

**Consequences for this document:**

1. **Every wired-LAN argument above is currently academic.** 2.5GbE, the 5GbE on the Tomahawk,
   and the rejection of the GIGABYTE B850 EAGLE for being "1 GbE only" all concern speeds this
   network caps at **100 Mbit** - a quarter of gigabit. The board's ethernet cannot be the
   bottleneck while this router is in place; the router is.
2. **Wi-Fi 7 on the ASUS TUF buys nothing today.** It was half the reason for putting the TUF on
   the Max build. The remaining reason - it is the only shortlisted board stocked by **both**
   Telemart and Brain - still stands, and that is now the whole of its case at +570.
3. The specs stay worth having anyway: the board will outlive the router, and 2.5GbE remains the
   sane floor for a machine bought in 2026. Nothing here argues for buying *down* to 1 GbE.

**The cheapest real upgrade in this whole project is not a board.** A Wi-Fi 6 router with gigabit
ports costs roughly 1 000-1 500 UAH and would multiply this network's wired throughput by ten -
more practical difference than the 570 between the two top-tier boards, and more than the 1 200
the Lean tier was nearly spent on. Worth putting on the list; it is not part of the PC budget.

### The Max board is conditional on the quote (decided 2026-09-11)

With Wi-Fi 7 established as worthless on this network, the ASUS TUF and the ASRock B850 Pro RS
WiFi are near-equal: both 54 C, both ATX. The TUF keeps a better BIOS reputation and is stocked
by both shops; the ASRock has **4x M.2 against 3** and costs **570 less**. That is too close to
call in the abstract, so it is decided by the event that is coming anyway:

- **Telemart quotes the build** -> **ASRock B850 Pro RS WiFi on all three tiers.** Pocket the 570.
- **Brain quotes the build** -> **ASUS TUF B850-PLUS WIFI**, the only shortlisted board Brain
  stocks.

### Remaining open items on this component

1. **The Lean board's stock.** Telemart marks the ASRock B850M Pro RS WiFi «Закінчується» -
   running low at 6 965. If it is gone by quote time the next tested mATX option is the Gigabyte
   B850M GAMING X WIFI6E at 8 799 / 8 599, i.e. the 1 200 this swap just saved comes straight
   back.
2. **Lane sharing, per board, before the second SSD goes in.** Confirmed on the Lean board:
   **occupying M2_3 disables the PCIE2 slot** on the ASRock B850M Pro RS WiFi. The build uses one
   GPU and one SSD, so this bites only at upgrade time - check each board's manual then.
3. **Debug LEDs on the Lean build: resolved.** The 7500F has no iGPU, so with the graphics card
   out there is no display to diagnose from. The ASRock B850M Pro RS WiFi carries ASRock's
   **Post Status Checker** as part of its EZ Troubleshooter set, which covers that gap.
4. **BIOS flash capacity for a future Zen 6 chip: unresolvable.** Not published for any board
   here. Recorded in the Zen 6 section above; no action possible before purchase.
5. **Flash the BIOS before first real use**, then enable EXPO. Unchanged advice from the
   reliability section.

## Every video behind this document

**Added 2026-09-13 by the source audit.** This file named its videos by channel and year only — **no id, no link** — which is the exact complaint the audit was started over: *"the docs were found to cite videos by channel name with no ID and no timestamp, leaving nothing Dmytro could re-check."* 5 of the 7 motherboard videos could not be traced from this page at all. The full set, with the transcript on disk and the quote-by-quote record in [source_audit.md](../source_audit.md):

| Video | Channel | Date | Title |
|---|---|---|---|
| [`BvtNCM5ms3U`](https://www.youtube.com/watch?v=BvtNCM5ms3U) | GeekaWhat | 2025-12-30 | How to Pick Parts for a Gaming PC in 2026! 👀 |
| [`lP-pinlU-Ko`](https://www.youtube.com/watch?v=lP-pinlU-Ko) | Paul's Hardware | 2020-05-17 | How to Choose a Motherboard: 3 Levels of Skill |
| [`PfAsVb4Bza4`](https://www.youtube.com/watch?v=PfAsVb4Bza4) | PC Centric | 2021-09-09 | How To Choose A Motherboard for Your Gaming PC! 🔧(Ryzen & Alder Lake) / AD |
| [`7CVkfi0_mME`](https://www.youtube.com/watch?v=7CVkfi0_mME) | Socket-X | 2026-05-11 | Every Motherboard Feature Explained: What You Actually Need in 2026 |
| [`ITBy9ckvSFY`](https://www.youtube.com/watch?v=ITBy9ckvSFY) | Socket-X | 2026-05-15 | Every 2026 Motherboard Brand Explained. What’s the Real Difference? |
| [`fsIh2eoWLT4`](https://www.youtube.com/watch?v=fsIh2eoWLT4) | Tech Guided | 2023-12-24 | How to Choose A Motherboard for Beginners |
| [`VgWrOSG24Yg`](https://www.youtube.com/watch?v=VgWrOSG24Yg) | Tech Notice | 2025-09-14 | Ultimate Motherboard Guide - How to understand & Choose the BEST for YOU!? |

