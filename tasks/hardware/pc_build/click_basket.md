# The basket at click.ua, 2026-09-13

**This is the shop Dmytro buys from.** He said so on 2026-09-13, after every price
table in this project had been written around Telemart. Telemart, Brain, ITbox and
Foxtrot stay in [price_check.md](price_check.md) as a cross-check on whether a
click.ua price is fair - they are not places the basket is ordered from.

Read direct from click.ua's own search (`code/ua_prices.py`, `click.ua` adapter),
every row stock-checked on the shop's own page.

## What click.ua sells, and at what

| Part in the build sheet | click.ua | Stock | Best other shop, for reference | click.ua costs |
|---|---:|---|---:|---:|
| CPU Ryzen 5 7500F (Lean) | **6 938** Tray / 7 085 Multipack | in stock | 6 519 Brain/ITbox (Tray) | +419 |
| CPU Ryzen 7 9700X (Working, Max) | **12 892 Tray only** | in stock | 14 499 Telemart (BOX/WOF) | **no BOX SKU** |
| GPU RX 9070 GRE Hellhound 12GB | **not stocked** | - | 32 179 Telemart | - |
| GPU Sapphire RX 9070 PURE 16GB (Max) | **43 908** | in stock | 39 999 Telemart | +3 909 |
| MB ASRock B850M Pro RS WiFi (Lean) | **7 632** | in stock | 6 989 Telemart | +643 |
| MB ASRock B850 Pro RS WiFi (Working, Max) | **9 168** | in stock | 8 829 Telemart | +339 |
| MB ASUS TUF B850-PLUS WIFI (Max alt) | **9 976** | in stock | 9 399 Telemart | +577 |
| RAM Kingston FURY 16GB 2x8 DDR5-6000 (Lean) | **17 974** | in stock | 16 562 Brain/ITbox | +1 412 |
| RAM Crucial Pro 32GB 2x16 CL36 (Working, Max) | **not stocked** - nearest is a single 32GB stick at 27 268, or 2x16 **6400** White at 29 251 | - | 21 094 Brain (no stock) / 24 099 Telemart | - |
| SSD WD Green SN3000 1TB (Lean) | **7 483** | in stock | 6 999 Telemart | +484 |
| SSD Samsung 990 EVO Plus 1TB (Working) | **12 581** | in stock | 10 679 Telemart | +1 902 |
| SSD Samsung 990 PRO 1TB | **12 162** | in stock | 12 399 Telemart | **-237** |
| SSD Kingston FURY Renegade G5 1TB (Max) | **16 700** | in stock | 13 999 Telemart | **+2 701** |
| Cooler Deepcool AK400 | **1 699** | in stock | 1 699 everywhere | 0 |
| PSU be quiet! Pure Power 13 M 750W | **not stocked** - 550W 4 729 and 1200W 8 649 only | - | 5 419 Telemart/Brain | - |
| Case Deepcool CC560 Limited V2 (Lean) | **not stocked** - CC560 V2 3 029, Mesh V2 3 459 | in stock | 2 399 Telemart | +630 on the V2 |
| Case Lian Li Lancool 216 (Working, Max) | **not stocked** - Lancool 207 4 799-4 999, 217 7 234-8 332 | - | 4 699 Brain / 4 949 Telemart | - |
| Monitor AOC Q27G4XF / Q27G4ZR | **not stocked** | - | 7 820 / 10 034 Brain | - |
| Monitor ASGARD AS275QC (the pick) | **6 999** | in stock | 6 999 Foxtrot | 0 |
| Windows 11 Home ESD KW9-00664 | **8 799** | in stock | 7 098 Brain/ITbox | +1 701 |

## What this changes

**Five parts of the current sheet cannot be bought at click.ua at all:** the
9070 GRE Hellhound, the Crucial Pro 2x16 CL36 kit, the Pure Power 13 M 750W, the
Lancool 216 and both AOC monitors. Two more exist only as a different SKU: the
9700X is **Tray only** (no BOX, already recorded in
[cpu.md](components/cpu.md)), and the CC560 comes as the plain **V2**, not the
Limited V2.

**The Max SSD flips.** At Telemart the Renegade G5 was the cheaper drive; at
click.ua it is **16 700 against the 990 PRO's 12 162 - a 4 538 premium** for the
Gen 5 drive. See [storage.md](components/storage.md).

**Nothing here is a single-shop basket yet.** Either the parts that click.ua does
not stock get substituted for what it does, or the order splits. That is a
decision for the build sheet, not for this file.

## The settled build, priced at click.ua (2026-09-13)

Same three builds as [builds.md](builds.md), with click.ua's SKU wherever it does not carry
the exact part. **Tray CPUs accepted** (Dmytro, 2026-09-13) - click.ua carries no BOX AM5 SKU
at all. Lean takes the **Multipack** instead of Tray: 147 more, and it bundles the Wraith
Stealth, which is 1 552 cheaper than Tray plus an AK400 and is the cooler cooling.md already
specified for that build.

### Lean - 94 475 UAH (was 92 192 at Telemart)

| Part | Model at click.ua | UAH |
|---|---|---:|
| CPU | Ryzen 5 7500F **Multipack** (100-100000597MPK) - bundles the Wraith Stealth | 7 085 |
| Motherboard | ASRock B850M Pro RS WiFi | 7 632 |
| RAM | Kingston Fury Beast 2x8GB DDR5-6000 CL30 (KF560C30BBEK2-16) | 17 974 |
| GPU | **PowerColor RX 9060 XT 16GB Hellhound** | 29 659 |
| SSD | WD Green SN3000 1TB (WDS100T4G0E) | 7 483 |
| PSU | Cougar GEX X2 850 850W | 5 799 |
| Cooler | *none* - the Multipack's bundled cooler, per cooling.md | 0 |
| Case | AeroCool P500C-G-WT-v1 | 3 045 |
| Monitor | ASGARD Gaming AS275QC 27" 1440p 200Hz VA | 6 999 |
| OS | Windows 11 Home 64-bit | 8 799 |
| | **Total** | **94 475** |

### Working - 129 581 UAH (was 115 389)

| Part | Model at click.ua | UAH |
|---|---|---:|
| CPU | Ryzen 7 9700X **Tray** (100-000001404) | 12 892 |
| Motherboard | ASRock B850 Pro RS WiFi | 9 168 |
| RAM | Kingston Fury Beast 2x16GB DDR5-6000 **CL36** (KF560C36BBE2K2-32) | 25 099 |
| GPU | **Sapphire RX 9070 PURE Gaming OC 16GB** (11349-02-20G) | 43 908 |
| SSD | Samsung 990 PRO 1TB (MZ-V9P1T0BW) | 12 162 |
| PSU | Cougar GEX X2 850 850W | 5 799 |
| Cooler | Deepcool AK400 | 1 699 |
| Case | AeroCool D502A-G-WT-v1 | 3 056 |
| Monitor | ASGARD Gaming AS275QC 27" 1440p 200Hz VA | 6 999 |
| OS | Windows 11 Home 64-bit | 8 799 |
| | **Total** | **129 581** |

### Max - 142 245 UAH (was 124 529)

| Part | Model at click.ua | UAH |
|---|---|---:|
| CPU | Ryzen 7 9700X **Tray** (100-000001404) | 12 892 |
| Motherboard | ASRock B850 Pro RS WiFi | 9 168 |
| RAM | Kingston Fury Beast 2x16GB DDR5-6000 **CL36** (KF560C36BBE2K2-32) | 25 099 |
| GPU | **Gigabyte RX 9070 XT Gaming 16GB** (GV-R9070XTGAMING-16GD) | 52 034 |
| SSD | Kingston FURY Renegade G5 1TB (SFYR2S/1T0) | 16 700 |
| PSU | Cougar GEX X2 850 850W | 5 799 |
| Cooler | Deepcool AK400 | 1 699 |
| Case | AeroCool D502A-G-WT-v1 | 3 056 |
| Monitor | ASGARD Gaming AS275QC 27" 1440p 200Hz VA | 6 999 |
| OS | Windows 11 Home 64-bit | 8 799 |
| | **Total** | **142 245** |

**Three different cards, one per build.** The GRE's disappearance moved the ladder up a rung;
it did not collapse it. Max is not being built (Dmytro, 2026-09-13) and is kept for the record.

## GPU: the RX 9070 GRE does not exist at click.ua, in any brand

The measured ladder, ComputerBase May 2026, 23 games, average FPS at 1440p (from
[components/gpu.md](components/gpu.md)), against what click.ua sells:

| Card | 1440p raster | RT | click.ua | vs the GRE |
|---|---:|---:|---:|---|
| RX 9070 GRE 12GB *(the settled card)* | 77.2 | 58.2 | **not sold** | baseline |
| **RX 9060 XT 16GB** PowerColor Hellhound | 59.2 | 45.2 | **29 659** | **-23%**, +4GB |
| RTX 5060 Ti 16GB Asus Dual OC | 61.0 | 49.3 | 38 999 | -21%, and **9 340 above the 9060 XT for 3%** |
| **RX 9070 16GB** Sapphire PURE | 90.7 | 68.3 | **43 908** | **+18%**, +4GB |
| **RX 9070 XT 16GB** Gigabyte Gaming | 100.5 | 77.1 | **52 034** | **+30%**, +4GB |

**Lean: PowerColor RX 9060 XT 16GB, 29 659.** 2 520 below what the GRE cost, 23% slower, and
16GB instead of 12. Lean is the build allowed to compromise, and this is the compromise.

**Working: Sapphire RX 9070 PURE 16GB, 43 908.** gpu.md already vetted this exact card. Same
**220W** on the same **2x 8-pin** as the GRE, so nothing else in the build moves - not the PSU,
not the case, not the cooling. **+11 729** over the GRE's Telemart price.

**Max: Gigabyte RX 9070 XT Gaming 16GB, 52 034**, the cheapest XT there. **304W on 3x 8-pin**
- the PSU below carries four, so it fits. gpu.md has not assessed this particular Gigabyte
model's cooler or acoustics; that check is owed only if Max is ever built.

**Nothing sits between the 9060 XT and the 9070 at click.ua.** The only card in the gap is the
RTX 5060 Ti 16GB at 38 999, which gpu.md measures *below* the GRE and barely above the
9060 XT. It is not a Working card.

## PSU: none of psu.md's picks are at click.ua, so the shelf was checked against its criteria

The be quiet! Pure Power 13 M 750W is not sold there (only 550W and 1200W), nor is the Super
Flower Leadex VII XG that psu.md names as the fallback, nor the Montech Century 2. Every
750W-class unit click.ua does stock, against this document's own bars - Cybenetics entry,
measured dBA, fan stop, ATX 3.1, connector count:

| Unit | UAH | Cybenetics | Measured dBA | Fan stop | Verdict |
|---|---:|---|---:|---|---|
| **Cougar GEX X2 850** | **5 799** | ETA Gold / LAMBDA Gold | **19.01 / 19.15** | **yes** | **The pick - Dmytro's call, 2026-09-13.** 4x PCIe 6+2-pin, SCP verified on every rail including -12V, 850W of headroom, the fullest published test record of the shortlist. ATX 3.0, 7-year warranty |
| Lian Li EDGE750 (EG0750G) | 5 854 | ETA Gold / LAMBDA Gold | 15.40 / 15.69 | yes | **Runner-up.** Quieter, ATX 3.1, 10-year warranty, but 3x PCIe 6+2-pin and no independent review of this model. See below |
| MSI MAG A750GLS PCIE5 | 6 999 | ETA Gold both voltages | 24.46 / 24.42 | yes | **The runner-up**, and the answer if ATX 3.1 and the 10-year warranty are worth 1 200. 4x PCIe 6+2-pin on 3 cables, 135mm FDB fan |
| Seasonic Focus GX-750 ATX 3.1 | 7 023 | ETA Gold / LAMBDA Silver | 29.33 / 29.41 | selectable | Louder than the ASUS TUF EVO this doc withdrew at 29.37. No |
| Gigabyte GP-UD750GM PG5 V2 | 4 499 | **no ETA at 230V** (PF 0.908) | 31.13 / 30.25 | yes | Uncertified at the voltage it will run on. No |
| MSI MAG A750GL PCIE5 | 5 600 | low badges | **36.13 / 35.42** | **no** | The A850GL's flaw exactly. Hard no |
| ~~DeepCool GamerStorm PN750M~~ | 5 199 | ETA Gold / LAMBDA **Standard+** | **~37** | **no** | **Hard no** - two samples died in short-circuit testing. See below |
| Lian Li SP750G | 6 052 | Platinum / **Standard+** | - | ? | SFX unit, Standard+ noise. No |
| Seasonic Core GC-750 | 5 179 | **absent from the database** | - | ? | No lab data. The standing rule rejects it |
| ~~Gigabyte GP-P850GM~~ | 4 999 | - | - | ? | **Hard no - asked about 2026-09-13.** Gamers Nexus tested ten of this unit and its GP-P750GM sibling: **five failed "in an explosive capacity"**. Gigabyte's response was to lower the OPP trip point from 120-150% to 110-120% and exchange a serial range; Cybenetics' own Aris Mpitziopoulos said the fault was **the overall design**, not the OPP setting. It is also ATX 2.x with no 12V-2x6, and 850W is the size psu.md already ruled one too large |
| 1stPlayer HA-750BA4 (NGDP Gold 750W) | 5 947 | ETA Gold / LAMBDA Gold | **22.42 / 22.43** | yes | **Close second, rejected on connectors** - only **2x PCIe 6+2-pin**. See below |
| ~~1stPlayer PS-850SFX (SFX-GLD-850-BK-EU)~~ | 5 240 | **absent from the database** | - | 0 RPM claimed | **No - wrong form factor.** It is an **SFX** unit with an **80mm fan**; the AeroCool cases take ATX and would need a bracket, and an 80mm fan cannot be as quiet as the 120-135mm units above. No lab data either |
| ~~Asus Prime 750W Gold (PRIME-750G, 90YE00U3)~~ | 5 486 | ETA Gold / **LAMBDA S++** (Standard++, the ~30-35 dBA tier), per ASUS' own spec sheet | - | **no** - ASUS: *"without 0dB technology"* | **No.** Also only **2x PCIe 6+2-pin**. ATX 3.1, 8-year warranty, 135mm fan |
| Asus Prime AP-750G (90YE00U1) | 6 021 | - | - | ? | ATX **3.0**, CWT, 3x PCIe 8-pin, 8-year warranty. Tom's Hardware: *"component quality and ripple suppression fall short of premium standards"*. No |
| ~~DeepCool GamerStorm PN850D~~ | 5 349 | ETA Gold / LAMBDA **Standard++** | **over 33** | **no** | **Hard no - asked about 2026-09-13.** Same -12V defect as the PN750M, tested on this line too: *"we tried two samples from this line at '-12V to Earth' SCP, and both died"*; the protection table prints **-12V to Earth: x**. Also **non-modular** (every cable permanently attached) and *"mediocre transient response on all rails"* |
| ~~Chieftec GPX-850FC (PowerUP)~~ | 4 855 | **absent from the database** | - | not claimed | **No - it is a previous-generation unit.** Chieftec's own spec sheet: **ATX12V 2.53**, so no ATX 3.x transient tolerance and **no 12V-2x6 connector at all**. 5-year warranty. Its 6x PCIe 6+2-pin and 140mm depth are the good parts |
| APNX Deluxe G1, Corsair CX750, other Chieftec, Prologix | 1 966-4 949 | **no entry found** | - | ? | No |

**Buy the Cougar GEX X2 850 at 5 799** - **+380** over the be quiet! this build was costed on.
Dmytro's call on 2026-09-13, after the whole shelf was checked unit by unit. Aris' review
(hwbusters, 2023-06-26): *"a dead silent PSU"*, semi-passive, **4x PCIe 6+2-pin**, 140mm deep,
XHY platform, seven-year warranty. Measured **19.01 / 19.15 dBA**, and *"dead silent at up to
530-620W load"* - this build peaks near 490W in Max and ~370W in Working, so the fan never leaves
that region. Its protection table shows **SCP present on every rail, -12V included** - the test
two DeepCool samples died on.

**What it costs, stated:**

- **ATX v3.0, not 3.1.** The 3.x rules are about riding out GPU transient spikes and about the
  16-pin connector; neither the 9070 PURE nor the 9070 XT has a 16-pin, so only the transient
  half applies, and ATX 3.0 already covers it.
- *"Protection features need more tuning"* - the 5VSB OCP is set too high or absent, and OPP is
  not lowered at high temperature. 12V OCP and OPP are set correctly.
- *"Not tight load regulation at 12V"*, and the 12V rail drops low in the 200% transient test.
- Seven-year warranty against the Lian Li's ten, and 850W is one size above what psu.md sized -
  which costs nothing and leaves room for a bigger card later.

**Runner-up: Lian Li EDGE750 (EG0750G) at 5 854** - 3.5 dBA quieter, ATX 3.1, ten-year warranty.
It loses on a fourth 8-pin, on having no independent review of this model at all, and on
Cybenetics' first sample failing ATX 3.1 on protection features where the second passed.

**Third: MSI MAG A750GLS PCIE5 at 6 999** - 24.46 dBA, ATX 3.1, ten-year warranty, 4x PCIe
6+2-pin. Beaten on price and noise by both of the above.

### The Lian Li EDGE750, checked on request (2026-09-13)

Sold at click.ua as *EDGE750, 80 Plus Gold, Black (G9P.EG0750G.B000.EU)*, **5 854**, in stock.

| | **Lian Li EDGE750** | Cougar GEX X2 850 |
|---|---:|---:|
| UAH | **5 854** | 5 799 |
| Measured noise | **15.40 / 15.69 dBA** | 19.01 / 19.15 |
| Fan stop | yes | yes |
| PCIe 6+2-pin | 3 (2 cables) | **4** |
| 12V-2x6 | **600W** per the Cybenetics report (Lian Li's own page says 450W) | 450W |
| ATX | **3.1** | 3.0 |
| Warranty | **10 years** | 7 |
| SCP, every rail incl. -12V | yes | yes |
| Capacity | 750W - the size psu.md sized | 850W, one above |

**It wins on everything the Cougar was compromising on** - ATX 3.1 instead of 3.0, ten years
instead of seven, the right capacity rather than a size up, and it is **3.5 dBA quieter** on the
same measurement. For 55 UAH more.

**Two things it does not have, stated:**

- **No full independent review of this model.** Aris has tested the EG1000G and EG1200G of the
  same line, not the 750W. So there is no published ripple, transient or hold-up figure for it -
  only Cybenetics' own efficiency, noise and protection measurements, which is less than the
  Cougar has.
- **Cybenetics tested it twice and the samples differ.** The first
  ([evaluation 2697](https://www.cybenetics.com/evaluations/psus/2697/), 14.27 / 13.38 dBA) is
  recorded as *"Cannot get ATX v3.1 because of issues in the Protection Features"*; the second
  ([2748](https://www.cybenetics.com/evaluations/psus/2748/), 15.40 / 15.69 dBA) passes ATX v3.1
  and shows SCP good on every rail. So there is a revision, and click.ua's listing does not say
  which one is on the shelf. **The shortfall was ATX 3.1 compliance, not a failure under test** -
  nothing died, unlike the DeepCool - and this build drives no 12V-2x6 card, which is what the
  3.1 rules govern.

**Settled: the Cougar.** Dmytro's call on 2026-09-13. The Lian Li's wins - 3.5 dBA and three
years of warranty - did not outweigh a fourth 8-pin, a published test record, and an ATX 3.1
badge that one of its two samples could not earn.

### If 850W is wanted anyway (2026-09-13)

psu.md sized this build at 750W and that still holds: Working peaks near **370W** (49% of 750W),
Max with the 9070 XT near **454W** (60%). 850W is the answer only if a 400W-class card is a real
plan. If it is, **it is not the Lian Li EDGE850** - the same-line step-up is measurably worse
than the 750W:

| | Lian Li EDGE750 | Lian Li EDGE850 | Cougar GEX X2 850 |
|---|---:|---:|---:|
| UAH | **5 854** | 6 968 | 5 799 |
| Measured noise | **15.40 / 15.69** | 19.05 / 19.34 | 19.01 / 19.15 |
| ATX 3.1 | **yes** (sample #2) | **no** - *"cannot achieve ATX v3.1 certification because of issues in the Protection Features & Short Power Ok Inactive to DC Loss Delay Period"* | no (3.0) |
| SCP per rail | **all rails ✓** | **not confirmed in testing** | **all rails ✓** |
| PCIe 6+2-pin | 3 | 4 | 4 |

**So the 850W to buy, if one is bought, is the Cougar at 5 799** - 1 169 cheaper than the
EDGE850, the same noise, and short-circuit protection actually verified.

### The 1stPlayer HA-750BA4, checked on request (2026-09-13)

Sold at click.ua as *HA-750BA4 (NGDP-GLD-750-BK-EU)*, **5 947**. It is the **1st Player NGDP
750W**, reviewed by Aris (hwbusters, 2024-04-15), OEM **Helly Technology**. This corrects
psu.md's blanket "1STPLAYER has no Cybenetics entry" - that was written about the **850W**
SKU; this one is measured.

| | **Cougar GEX X2 850** | 1stPlayer HA-750BA4 |
|---|---:|---:|
| UAH | **5 799** | 5 947 |
| Measured noise | **19.01 / 19.15 dBA** | 22.42 / 22.43 dBA |
| **PCIe 6+2-pin** | **4** | **2** |
| 12V-2x6 | 450W | **600W** |
| ATX | 3.0 | **3.1** |
| Warranty | 7 years | **10 years** |
| 12V load regulation | *"not tight"* | **within 1%** |
| SCP, all rails incl. -12V | yes | yes |
| Minor-rail OCP | 5VSB set too high | *"sky-high ... they jeopardize the platform's reliability"* |

**It loses on the connector count, which is the same reason psu.md rejected the Pure Power 13 M
650W.** Two 6+2-pin is exactly what the Sapphire 9070 PURE needs and not one more; the 9070 XT
in Max needs **three** and would not be powered at all. On a part meant to survive every later
change to the build, buying the one with no spare connector is the wrong saving - and it is not
even a saving, it costs 148 more.

It genuinely beats the Cougar on four things: ATX 3.1, a 600W 12V-2x6, ten years of warranty and
tight 12V regulation - Aris: *"Good overall performance at 230V ... tight load regulation at 12V,
the good ripple suppression, the long hold-up time"*. **If Max is definitively never built and a
future GPU will never need a third 8-pin, it is a defensible swap.** Otherwise the Cougar stands.

### The DeepCool PN750M, checked on request (2026-09-13)

Reviewed by **Aris Mpitziopoulos** (hwbusters.com, 2024-03-08) - the same tester whose
Cybenetics figures this table rests on. Two things end it:

- **"We tried two samples, and both died during the 12V Short Circuit Protection evaluation
  testing."** He adds that DeepCool and CWT *"should remove the completely unnecessary 12V rail
  from this platform. If shorted, it can also kill this specific PSU."* The cons list also
  carries **"No SCP at -12V"**. psu.md already deprioritises the Chieftec Vega M for a
  supervisor IC listed without short-circuit protection; this is the same defect, demonstrated.
- **Noise: "close to 37 dBA average"**, **no semi-passive operation**, and *"the fan starts at
  high speeds, which will be a problem for users concerned about noise output"* - 35 dBA at
  520W, over 40 dBA at 580W. Cons: *"The cooling fan's quality is so-so"* (120mm rifle bearing).

Verdict quote: *"Like the PN850M, the PN750M doesn't register top performance"*. Asked in the
comments whether to buy it over a Super Flower Leadex III Gold 650W, Aris answered
**"Superflower leadex III GOLD 650watt"**. It is fully modular, ATX v3.1, 10-year warranty and
has 3x PCIe 6+2-pin - mechanically it would run this build. It is rejected on the SCP result.

## Max SSD: settled

The Renegade G5 stays in Max (Dmytro, 2026-09-13), at **16 700**. Max is not being built.
