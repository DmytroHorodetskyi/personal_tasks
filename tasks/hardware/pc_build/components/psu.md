# Power supply

## What the PSU does for this machine

It is the only component whose failure can take other components with it, and the one where
the marketing sticker (80 PLUS) tells you the least about the thing you will actually
notice - noise. It is also the part most people economise on to fund the GPU, which is the
wrong trade: a 40 000 UAH graphics card sitting behind a 2 900 UAH power supply is a bad bet.

## Power budget - is 750W actually enough? (verified 2026-09-11)

Yes, with margin, in all three builds. This section replaces the earlier estimate, which was
a single ~455W figure with no worst case and no transient treatment. Every number below is a
manufacturer power limit or a measured review figure, not a rule of thumb.

### Where the watts come from

| Part | Figure used | Source |
|---|---:|---|
| Ryzen 7 9700X / Ryzen 5 7500F, default | **88W** | AMD **PPT** for a 65W-TDP AM5 part. Not the 65W TDP - that is a cooling-design figure. |
| Ryzen 7 9700X, **105W cTDP mode** | **142W** | AMD's optional mode, exposed in MSI/ASRock BIOS. Phoronix measured 102W average, **143W peak**. |
| RX 9070 GRE (Hellhound) | **220W** | AMD TBP; PCGH measured ~222-225W peak in games. 2x 8-pin. |
| RX 9070 XT, **Hellhound** (the merit pick) | **310W** | PowerColor's limit over AMD's 304W reference. **2x 8-pin.** |
| RX 9070 XT, **Red Devil** (Telemart's stock) | **330W** | PowerColor's raised limit; factory OC to 3060MHz. **3x 8-pin.** |
| Board, RAM, SSD, fans, USB devices | **~65W** | B850 VRM + chipset ~30W, DDR5 ~10W, 990 PRO ~9W peak, fans ~8W, peripherals ~10W. |

### The three builds

| | **Lean** | **Working** | **Max** |
|---|---:|---:|---:|
| CPU (PPT) | 7500F 88W | 9700X 88W | 9700X 88W |
| GPU (board power limit) | GRE 220W | GRE 220W | **XT 310W Hellhound / 330W Red Devil** |
| Everything else | 65W | 65W | 65W |
| **Sustained peak** | **373W** | **373W** | **463W / 483W** |
| **Load on 750W** | **50%** | **50%** | **62% / 64%** |
| Worst case, **CPU in 105W mode** | 427W (57%) | 427W (57%) | **517-537W (69-72%)** |

The Max GPU is still undecided between the **Hellhound XT** (the merit pick, 41 800) and the
**Red Devil** (42 805, what Telemart stocks) - see [gpu.md](gpu.md) and
[../build_specs.md](../build_specs.md). **It does not change the PSU:** the two cards are 20W
apart and both land in the same load band.

**50-64% is the target band**, not a squeeze: it is where Gold efficiency peaks and where this
unit's fan is still stopped. Even the pessimistic case - a 9700X manually put in 105W mode
*and* a factory-overclocked XT at its limit *simultaneously*, which no real workload does
(gaming does not load eight cores to PPT) - lands at 72%.

### Transients - the part wattage headroom does not answer

A GPU's real risk is not its average draw but microsecond spikes that trip a PSU's
over-current protection. Headroom in the continuous rating is the wrong tool for this; the
**ATX 3.1 certification is the right one**, and it is what the pick carries: the unit must
survive **2x rated power (1 500W) for 100 microseconds** and 1.1-1.8x for longer windows.
Hardware Busters confirms this unit "handles power excursions up to double its rated power".

RDNA4 is also well-behaved here compared with the RDNA2 cards that built the transient
reputation. Igor's Lab measured the 9070 XT peaking at **~345W against its 304W nominal**
(~13%) and the RX 9070 at 330W peaks over 250W sustained. Apply the worse ratio to the Red
Devil's 330W limit and the spike is ~375W - **an excursion of ~45W over the sustained figure,
against 1 500W of certified excursion capacity.**

### What the box says, and why it is ignored

**The Red Devil's packaging asks for a 900W PSU.** That is a model claim covering the worst
system a buyer might pair it with, not a measurement - AMD's Frank Azor said publicly that
custom cards carry lower real requirements than that packaging implies. **AMD's own official
recommendation for the RX 9070 XT is 750W**, and 650W for the 9070/GRE. PowerColor's own
Hellhound GRE page says 700W minimum. Listicle sites recommending 1000W cite no measurement
and are the kind of source [tools.md](../tools.md) says to distrust.

The honest summary: **750W is AMD's own number for the largest card here, and this build draws
less than the reference system that number assumes**, because a 9700X at 88W PPT is a far
lighter CPU than the one vendors size against.

### Connectors - checked, and one correction

| Build | Card needs | PSU supplies |
|---|---|---|
| Lean, Working | 9070 GRE Hellhound: **2x 8-pin** | 4x PCIe 6+2-pin |
| Max, Hellhound XT | **2x 8-pin** | 4x PCIe 6+2-pin |
| Max, Red Devil XT | **3x 8-pin** | 4x PCIe 6+2-pin |

**Correction:** this documentation previously stated that "the cards here need 2x 8-pin". That
is true of the GRE but **not of the Red Devil XT, which takes three**. The 750W covers it with
one spare, and its 12V-2x6 (600W-rated, unused by an AMD card) is separate. Single +12V rail,
**62.5A = the full 750W**, so there are no per-rail limits to plan around.

**Answered (see the video cross-check below), and corrected 2026-09-13 by the source audit:**
PC Builder counts **three 6+2-pin connectors** on this unit, not "three cables carrying four" -
*"it comes with three PCIE 6+2 pins"* - and adds a constraint recorded nowhere here before:
*"One of them you have to not use the 12 V high power for."* That is a shared-port exclusion. It
does not block this build, because **no AMD card here uses the 12V-2x6** - but that is now the
reason the Red Devil fits, and the margin is thinner than the retailer's "four connectors"
implies. Verify against the unit's own manual before ordering.

**Cabling a 3x 8-pin card: one cable per connector, daisy-chain last.** An earlier version of
this line said the opposite. Both sources put the singles first:

- PC Builder: *"one cable per connection **for the first two** eight-pin plugs, then you can
  daisy chain **the third**"*.
- JayzTwoCents argues against pigtails entirely, with the spec arithmetic: an 8-pin PCIe
  connector is rated **150W** and the slot supplies **75W**, so a daisy-chained pair is asked for
  more than one cable's share. *"If you go with a power supply that has individual cables for
  your pcie you are now operating perfectly within spec."*

The card's three connectors carry ~255W between them (75W comes from the slot).

### Cross-check against online PSU calculators (2026-09-11)

Asked for, and run. Three independent sources, none of which contradicts the budget above.

| Source | What it says | Verdict on 750W |
|---|---|---|
| **Seasonic Wattage Calculator** - run directly, all three configs | **Lean 550W / Working 550W / Max 700W** recommended PSU | Comfortable in all three |
| **AMD**, official product page | **750W for the RX 9070 XT**, 650W for the 9070/GRE | Exactly the pick |
| **PowerColor**, Hellhound GRE product page | **700W minimum system power** | Comfortable |
| PCPartPicker estimated wattage, 9700X + 9070 XT | ~**535W** max system draw (reported in its forums; **not read directly** - the site is behind a bot check) | Matches this doc's 537W worst case almost exactly |

Two points on how to read these:

- **A calculator's output is a PSU size, not a power draw.** Seasonic's 700W for Max already
  contains its own safety margin on top of the actual ~483W. Its number and this doc's number
  are not the same quantity, and they agree in the only way that matters: both land under 750.
- **The spread between calculators is wide and upward-biased.** Seasonic says 550W where this
  doc computes 373W for the Working build. Vendor calculators assume a worse CPU, more drives
  and more fans than this machine has, and they are selling power supplies. That bias is the
  reason to treat 750W as generous rather than tight - not a reason to buy more.

Two calculators could not be made to produce a figure and are recorded as attempted, not as
evidence: **be quiet!'s own calculator** (computes server-side on submit; its component API
carries no wattages) and **Cooler Master's** and **MSI's** (both render their inputs in a way
that could not be driven in this session). If a second opinion matters later, Seasonic's is
the one that works.

### Video cross-check, five buying guides (2026-09-11)

Five PSU guides supplied by Dmytro, read in full via `code/yt_transcript.py`: GeekaWhat 2026
and 2023, PC Builder "Best PSU 2026", JayzTwoCents 2021, Tech Guided 2024. **Nothing in them
overturns the 750W conclusion**, and three gaps in this document came out of them.

**Sponsorship, added 2026-09-13.** Two of the five are vendor-sponsored and this was not
recorded: **GeekaWhat 2023 is sponsored by Corsair** - a PSU manufacturer, in a PSU buying guide
that then walks through Corsair units - and **GeekaWhat 2026 by ASUS**. Neither changes anything
below; both are quoted for general rules rather than for product picks. Weigh the Corsair one
accordingly. (Separately: the two PC Builder guides cited elsewhere in this project are
sponsored by **Seasonic**, whose Focus GX-850 appears in the options table.)

**Gap 1 - the SPL PSU tier list, which this document was not using.** Two of the five guides
treat it as the primary quality source, and they are right to: it is a maintained, public
teardown-based grading of nearly every unit on the market, with the OEM named. Read directly
at [psutierlist.org](https://psutierlist.org/) (mirror:
[tuerie.github.io/psu-tier-list](https://tuerie.github.io/psu-tier-list/)). What it says about
this family:

| Unit | Tier | The list's own note |
|---|---|---|
| Pure Power 13 M **750/850W** | **A** | "Excellent noise profile." FSP, ATX 3.x, Gold, fully modular |
| Pure Power 13 M 550/650W | **B+** | "**85C bulk caps**, excellent noise profile" |
| Pure Power 13 M 1000W | **A-** | "**Poor excursion response in the 200% excursion test; platform is being pushed close to its limits**" |

Three things fall out of that. **The pick is A tier** - independent confirmation from a source
this doc had not consulted. **The 650W is B+, not A**, which is a second and better reason to
reject it than the connector count. And **the 1000W is graded *below* the 750W** because the
platform runs out of excursion headroom - so in this family, buying bigger is worse, not safer.
That is the exact opposite of the "when in doubt buy more watts" instinct, and it is measured.

**Gap 2 - how to cable a 3x 8-pin card, which this doc had left as an open question.** Now
answered, and **corrected 2026-09-13**: the reconciliation written here previously ("retailers
quote four *connectors*, the video quoted three *cables*") was not what the video says. PC
Builder counts **three 6+2-pin connectors**, and says one of them cannot be used alongside the
12V-2x6. For a Red Devil XT:

> **One cable per connector. Daisy-chain only if you run out of cables, and then only for the
> third socket.** Do not run the first two from one daisy-chained cable.

PC Builder gives the same rule generally - one cable per connector for the first two, daisy
chain only the third if you must. Also noted: **the 12V-2x6 cable occupies two PSU-side sockets
and both plugs must be connected**, an ATX 3.1 requirement. Irrelevant here, since no AMD card
in these builds uses it, but it is why the PSU-side port count looks tighter than the connector
count suggests.

**Gap 3 - a build-time safety rule this doc never stated.** Both JayzTwoCents and PC Builder
raise it independently, and be quiet!'s own manual says it outright: **never reuse a modular
cable from a different power supply.** The PSU-side pinouts are not standardised between units
or even between series from the same brand; Jay describes an SSD destroyed exactly this way.
The unit's own cables, and nothing else. A related troubleshooting note from PC Builder worth
keeping: **black screens and crashes in games are more often a loose GPU power cable or a
third-party cable extension than a bad GPU or driver** - reseat before diagnosing.

**The one genuine disagreement, recorded rather than buried.** PC Builder's sizing rule is
**1.5x the PCPartPicker rated draw**. Applied to the Max build that is 535 x 1.5 = ~800W, so
his rule would put Max on an 850W unit, not 750W. Against it: AMD's own figure for the 9070 XT
is 750W, Seasonic's calculator says 700W, and the 1.5x multiplier exists to cover transients
*without relying on ATX 3.1 certification* - which this unit holds and which is tested to 2x
rated power. It is a deliberately conservative blanket rule for readers who will not check a
certification. It is the reason the Max build's 64% load is worth knowing rather than a detail:
if the number had come out at 75-80%, the rule would deserve to win.

**Corrected 2026-09-13:** this paragraph previously said the 1.5x rule was *"the only source of
the five that would size this build above 750W"*. It is **two of five**. JayzTwoCents does not
stop at his blanket 850W - for a card of this class he says *"i usually recommend uh a thousand
watt power supply for anyone running any sort of high-end components ... something that's like an
80 series gpu or higher or something like a 6800 xt or higher."* An RX 9070 XT is above that
line.

**JayzTwoCents' blanket "buy an 850W Gold" is the habit this document already corrected** - it
is a 2021 video, predates ATX 3.x entirely, and he argues from efficiency-curve and future-GPU
reasoning rather than from this build. His underlying points hold and are already here: the
efficiency bell curve, over-current protection shutting the system down rather than frying it,
and a PSU being the most reusable part across upgrades.

**Confirmed, not new:** every guide says a GPU vendor's recommended wattage is sized for the
*whole hypothetical system* and overestimates deliberately (GeekaWhat, Jay, Tech Guided, all
independently); calculators read below vendor recommendations by design - Tech Guided's own
worked example has OuterVision at 469W against AMD's 700W recommendation for the same build,
the same gap this doc found between Seasonic's 550W and AMD's 750W; 80 PLUS on its own is
near-meaningless and Cybernetics is the measurement that matters; fully modular, fan-stop and
ATX 3.1 are the right asks. Two guides also name **ASRock Phantom Gaming / Steel Legend**,
**Montech Century 2** and **MSI MAG A GLS** as A-tier alternatives at this wattage - none
checked for Ukrainian availability, and none displaces a unit already measured at 6.51 dBA.

### Why the same PSU in all three builds (asked 2026-09-11)

The tiers differ on the parts you experience - cores, memory, refresh rate, case noise, the
card. The PSU is not one of those; it is a safety and acoustics part, and spending less on it
buys nothing you notice except risk. But that is an argument, not evidence, so the cheaper
options were actually priced.

**Lean and Working cannot differ on sizing at all.** Both run a 65W-class CPU at 88W PPT and
**the same RX 9070 GRE**. Their peak is the same 373W. Any difference between them would have
to be a difference in unit quality, deliberately buying a worse power supply for the cheaper
build.

**And there is nothing cheaper worth having.** Every candidate at 650-750W was checked against
the SPL tier list and Ukrainian pricing:

| Candidate | UAH | Tier | Why not |
|---|---:|---|---|
| **Pure Power 13 M 750W** | **5 419** | **A** | **The pick** |
| Pure Power 13 M 650W | 4 921 | B+ | Saves 500. 85C bulk caps, 2x 6+2-pin only, 450W 12V-2x6 |
| be quiet! Pure Power 12 M 750W | **10 240** | A | Previous generation, ATX 3.0, 2x 6+2-pin - and **one shop, at nearly double the price**. End of life |
| MSI MAG A850GLS | 6 349 | A- | **930 more expensive**, and a grade lower |
| ASRock Steel Legend 650-1000W | - | B+ | The list's own note: "other models mediocre" |
| Super Flower Leadex VII XG 750W | 6 277 | **A+** | The one graded *higher* - but +858, so it is the upgrade, not the saving |

The saving available on Lean is **500 UAH, for a B+ part with a connector constraint**, on the
one component whose failure can take the graphics card with it. That is 0.5% of the Lean build.
**One unit across all three is the answer**, and it also means the PSU survives every later
change to the ladder.

### When 750W would stop being enough

Only on a GPU upgrade. A 5080-class or 9070-XT-successor card at 400W+ would put Max at ~600W
and past 80% load. Nothing else in this machine can move the number: the CPU is capped at
142W even abused, and storage and fans are rounding errors. If a much larger card is a real
plan within the warranty period, that is the argument for the 850W - not anything in the
builds as specified.

## The characteristics that matter, and how to read them

The PSU is the component with the widest gap between marketing and measurement, so the top
rows are all independent lab data rather than anything printed on the box.

| # | Spec (unit) | What it means, plainly | What it is here |
|---|---|---|---|
| 1 | **Cybenetics LAMBDA (dBA)** | An independent lab's **noise** measurement, on a voluntary scheme - so a unit's *absence* from the database is itself information. | **Look the exact unit up before buying.** A++ is under ~20 dBA. The pick measures **10.65 dBA**; three rejected options here have no entry at all, and one measures 38.49. |
| 2 | **ATX 3.0 / 3.1 compliance** | The standard defining **transient tolerance**: the unit must survive 2x rated power for 100 microseconds. Modern GPUs spike to roughly double their rating for exactly that long. | **ATX 3.1 preferred**, 3.0 acceptable. This is the spec that stops "the PC shuts off mid-game". Check the SKU - some models exist in both revisions. |
| 3 | **Continuous output (W)** | Sustained wattage. Sizing is not about the peak; it is about sitting near 50-60% load where efficiency peaks and the fan stays off. | Build peak ~368W (Working) / ~488W (Max) -> **750W**. Above 1000W is wasted money and slightly worse idle efficiency. |
| 4 | **Protections (OCP / OPP / OTP / SCP)** | What shuts the unit down instead of frying the motherboard. Tested by Cybenetics SAFE and Hardware Busters. | Unbranded units frequently fail these outright. One option here is listed **without short-circuit protection** - that alone disqualifies it. |
| 5 | **Cybenetics ETA / 80 PLUS (efficiency)** | How much wall power becomes DC. ETA is measured across the real load range; 80 PLUS tests three points. | Gold is correct here. **Platinum and Titanium pay back over a decade, not a warranty period.** The pick is 80 PLUS Gold but measures Cybenetics Platinum. |
| 6 | **Fan-stop (semi-passive)** | The fan stops entirely below a load threshold - so the machine is silent at idle, which is most of a work day. | **Yes** on the pick. Two of the cheaper options have none. |
| 7 | **Modularity** | Fully modular means only the cables you use get plugged in. | Fully modular, for airflow and for building in a case without a cable nest. |
| 8 | **Connectors** | Native 12V-2x6 versus an adapter, and the PCIe 8-pin count. | The RX 9070 XT needs **2x 8-pin**, so 12V-2x6 only matters for a future NVIDIA card. The pick has a native 600W one anyway. |
| 9 | **Warranty (years)** | The manufacturer betting its own money on the unit. | **10 years** on the pick. Under 7 at this tier is a signal. |

| 10 | **SPL PSU tier list grade** | A public, maintained grading built on teardown reviews - component quality, protections, ripple, excursion behaviour - with the OEM named. A/A+ is best, C is the floor for a gaming build. | **A** for the pick. Free at [psutierlist.org](https://psutierlist.org/). Added 2026-09-11 after five buying guides treated it as the primary quality source; it is the fastest way to check a shop's proposed substitute. |

**Ignore:** the 80 PLUS badge on its own, peak/"max" wattage claims, RGB, and the wattage
arms race - a bigger unit is not a safer one if it has no lab data behind it.

## Specifications

Both wattages of the same unit, because the size is the live question. **They are the same
platform, the same 160mm depth and the same cable set** - the 750W is a drop-in for the 850W.

| | **Pure Power 13 M 750W** (the pick) | **Pure Power 13 M 850W** (superseded) |
|---|---|---|
| Continuous output | 750W, **single +12V rail** | 850W, single +12V rail |
| Standard | **ATX 3.1 / PCIe 5.1** | ATX 3.1 / PCIe 5.1 |
| Efficiency | 80 PLUS Gold; **Cybenetics ETA Platinum**, 90.77% @115V / **92.77% @230V** | 80 PLUS Gold; ETA Platinum, up to 94.4% |
| Noise | **LAMBDA A++, 6.51 / 6.21 dBA measured** - at the lab's noise floor | LAMBDA A++, **10.65 / 10.60 dBA** |
| Fan | 120mm, **semi-passive** (stops entirely at low load) | same |
| Modularity | **fully modular** | same |
| GPU connectors | 1x native **12V-2x6** + **4x PCIe 6+2-pin** | same |
| Dimensions (W x H x D) | 150 x 86 x **160mm** | 150 x 85 x 160mm |
| Warranty | **10 years** | 10 years |
| OEM | FSP | FSP |
| Telemart, 2026-09-11 | **5 419** | 5 796 |

**The 750W measures quieter than the 850W** - 6.51 dBA against 10.65 - on the same platform.
Both are inaudible in practice; the point is that dropping a size costs nothing on the axis
this whole document is built around.

## Options

Prices: lowest hotline.ua offer, 2026-09-09, UAH.

Cybenetics measures noise in a hemi-anechoic chamber across the full load range. **LAMBDA
A++ is roughly 10 dBA; Standard+ is roughly 38 dBA.** That is the difference between a PSU
you never hear and one that is the loudest thing in the case. Figures below are the measured
average dBA at 115V/230V.

| Model | UAH | Cybenetics ETA / LAMBDA | Measured dBA | Fan stop | OEM | Verdict |
|---|---:|---|---:|---|---|---|
| Ocypus Iota P850S | 2 939 | **none - absent from the 1 169-unit database** | - | ? | ? | No lab data anywhere. No. |
| 1STPLAYER HA-850BA4 | 6 809 | **none for this SKU** | - | ? | ? | Brand's tested units range 24-37 dBA. Tells you nothing. No. |
| Chieftec Vega M 850W | 4 067 | Gold / A- | 24.96 | **no** | High Power | Best ripple at 230V, but 1.38% load regulation and its supervisor is listed **without short-circuit protection**. |
| ~~ASUS TUF-GAMING-850G~~ | 5 026 | **absent from the database** | - | ? | Great Wall | **Withdrawn.** No lab data, and ASUS's page now claims ATX 3.1 for a unit that launched as 3.0 - unresolved. |
| **be quiet! Pure Power 13 M 750W** | **5 291** | **Platinum / A++** | **6.51 / 6.21** | **yes** | FSP | **The pick, 2026-09-11.** Same platform as the 850W, quieter, 5 419 at Telemart. |
| be quiet! Pure Power 13 M 650W | 4 921 | Platinum / **A++** | 6.34 / 6.32 | yes | FSP | Rejected: only **2x PCIe 6+2-pin** and a **450W** 12V-2x6, for 370-500 less. See below. |
| be quiet! Pure Power 13 M 850W | 5 759 | Platinum / A++ | 10.65 / 10.60 | yes | FSP | **Superseded.** The former pick; correct unit, one size too large. |
| ~~MSI MAG A850GL PCIE5~~ | 5 596 | Platinum / **Standard+** | **38.49** | **no** | CWT | **Hard no.** Loudest unit here, no fan stop, and its 16-pin GPU cable is rated **450W only**. |
| ~~ASUS TUF Gaming 850W Gold EVO~~ | 6 139 | Gold-Plat / **A-** | **29.37** | **no** | Great Wall | **Withdrawn - my previous pick, and it was wrong.** See below. |
| Corsair RM850x (2024 ATX 3.1) | 6 340 | Gold / A | 21.34 | selectable | CWT | Fine, but 101.7A inrush at 230V - above Cybenetics' bar, which matters on a shared breaker or a UPS. |
| Super Flower Leadex VII XG 850W | 6 277 | Gold / **A++** | **9.71** | yes | Super Flower | Excellent all-rounder: 19.85 mV ripple, 25.1 ms hold-up. The best alternative to the pick. |
| SeaSonic Focus GX-850 **ATX 3.1** | 7 398 | Platinum / A | 22.76 / 21.09 | selectable | SeaSonic | Best load regulation measured (0.16%). **Only the 3.1 SKU** - the 3.0 version is 30.7 dBA. |
| be quiet! Dark Power 14 850W | 8 956 | Titanium / **A++** | **10.46** | yes | - | The ceiling. Nothing here needs it. |
| ASUS TUF-GAMING-1000G | 7 329 | - | - | - | - | Only if a 5080-class GPU is a real plan. |

## Evidence (revised after the deep review pass, 2026-09-09)

I got this component wrong twice, and the Cybenetics database is why:

- **be quiet! Pure Power 13 M 850W**: **ETA Platinum, LAMBDA A++, 10.65 dBA measured**, with
  fan stop, built by **FSP**. It also posts the best transient behaviour of anything on the
  list - 12V holds **11.56V at 200% load** - with 21.8 ms hold-up and 27.3 mV ripple. ATX
  3.1, 12V-2x6, rear-mounted connectors. Its one compromise is Elite 2000h bulk caps rather
  than Japanese ones.

  **Why the 21.8 ms hold-up is worth more than it looks** (added 2026-09-13, from the UPS video
  batch). A UPS does not switch to battery instantly; it has a **transfer time**, and if that
  gap exceeds the PSU's hold-up the machine reboots *"even though it never fully loses power"*
  (Dave's Garage). Transfer times from those sources: **offline/standby 5-20 ms**,
  **line-interactive 2-8 ms**, with E-Katalog's rule of thumb being *"no more than 5 ms"*.
  **21.8 ms covers a line-interactive unit with a wide margin** and would be marginal against a
  slow offline one - and line-interactive is the type every source in that batch names for a PC.
  The UPS itself stays **parked** by Dmytro; this is recorded because it is a point in favour of
  the PSU already chosen.
- **ASUS TUF Gaming 850W Gold EVO** - the unit I recommended - measures **LAMBDA A- at
  29.37 dBA**, has **no 0dB fan-stop mode at all** (ASUS states this itself), **12V ripple of
  55.5 mV** with the lab flagging high ripple at the 5V OCP trip, 1.64% load regulation, and
  its warranty is **8 years, down from the non-EVO's 10**. It is a *regression* on exactly
  the axis I bought it for. My earlier "Cybenetics Platinum + A-" line was accurate but I
  read A- as good; against A++ at 10.65 dBA it is three times the noise.
- **MSI MAG A850GL PCIE5**: **38.49 dBA, LAMBDA Standard+, no fan stop**, and - the detail
  that settles it - **its 16-pin GPU cable is rated 450W**, not 600W. Note the near-identical
  **A850GLS** is a *different CWT platform*: 18.07 dBA, A+, 600W 16-pin. Same brand, same
  family name, wildly different unit.
- **ASUS TUF-GAMING-850G** (non-EVO): **absent from the Cybenetics database entirely**, and
  ASUS's current page claims ATX 3.1 for a unit that launched as ATX 3.0 - either a silent
  revision or marketing copy. No lab data means no pick.
- **Fanless exists at this power level**: the Cooler Master X Silent Edge Platinum 850 is
  **completely fanless at 6.00 dBA** (the lab's noise floor). For a 490W desk-side machine
  that is the categorically correct answer if you can find one and your case has airflow.

> **Shop change, 2026-09-13.** Dmytro buys at **click.ua**, which sells no be quiet! Pure
> Power 13 M 750W, no Super Flower Leadex VII XG and no Montech Century 2. Its whole 750W shelf
> was checked unit by unit against the criteria below and the answer is the **Cougar GEX X2 850
> at 5 799** (+380), Dmytro's call 2026-09-13: ETA Gold / LAMBDA Gold, **19.01 / 19.15 dBA
> measured**, semi-passive, **4x PCIe 6+2-pin**, SCP verified on every rail including -12V,
> seven-year warranty. It costs ATX **3.0** rather than 3.1 and looser 12V load regulation.
> Runner-up **Lian Li EDGE750 at 5 854** (15.40 dBA, ATX 3.1, ten years, but 3x 6+2-pin and no
> independent review); third **MSI MAG A750GLS at 6 999**. Also checked and rejected by name:
> DeepCool PN750M and PN850D (two samples each died in -12V short-circuit testing), Gigabyte
> GP-P850GM (the Gamers Nexus exploding-PSU batch), 1stPlayer HA-750BA4 (only 2x 6+2-pin),
> 1stPlayer PS-850SFX (SFX form factor, 80mm fan), Asus Prime 750W Gold (LAMBDA S++, no fan
> stop), Asus Prime AP-750G, Chieftec GPX-850FC (ATX 2.53), Seasonic Focus GX-750 and Core
> GC-750, Gigabyte UD750GM PG5 V2, MSI MAG A750GL, Lian Li SP750G. Table and rejections: [../click_basket.md](../click_basket.md) - including the
> **DeepCool PN750M (5 199)**, asked about by name and rejected on a safety result: Aris tried
> **two samples and both died during 12V short-circuit-protection testing**, and the review
> lists no SCP at -12V. Same defect class as the Chieftec Vega M below, but demonstrated.

## Verdict (revised 2026-09-11: the 750W, not the 850W)

**Buy the be quiet! Pure Power 13 M 750W - 5 419 at Telemart, 5 291 at hotline floor.** Same
FSP platform, same ATX 3.1, same 600W-class 12V-2x6 and four 6+2-pin, same 160mm depth, same
10-year warranty as the 850W this document previously picked - and it **measures quieter**,
6.51 dBA against 10.65. It sits at ~49% load in the Working build and ~65% in Max, which is
the band the fan stays stopped in.

**The saving is 377, not the ~1 300 the open item estimated.** be quiet! prices this range
almost flat: 650W 4 921, 750W 5 291, 850W 5 759 at hotline floor. The reason to drop a size
is therefore correctness, not money - the 850W was sized against a 9800X3D build that no
longer exists. 377 x 3 builds is real but it is not a lever.

- **Cheaper: the 650W at 4 921** (-370) is **rejected**, now on two grounds. It carries only
  **2x PCIe 6+2-pin** where the Red Devil XT wants three, and its 12V-2x6 is rated **450W** -
  the exact flaw that disqualified the MSI MAG A850GL here. And the SPL tier list grades it
  **B+ against the 750W's A**, citing 85C bulk caps. 370 buys a worse part.
- **Better but pricier: Super Flower Leadex VII Gold (XG) 750W at 6 277** (+858) - the only
  unit found that is graded **above** the pick: **A+** on the SPL list, A++ at 9.71 dBA,
  19.85 mV ripple, 25.1 ms hold-up. Buy it if the be quiet! is out of stock, or if the extra
  858 is worth the top grade. The **850W of the same be quiet! family at 5 796** (+377) is
  also A tier and is the answer only if a 400W-class GPU upgrade is a real plan. The **Dark
  Power 14** is Titanium/A++ overkill.
- **Avoid:** unchanged from the list below - the MSI MAG A850GL (38 dBA, 450W cable), the
  ASUS TUF EVO (no fan stop, high ripple, 8-year warranty), the SeaSonic Focus GX-850 in its
  ATX 3.0 SKU, and anything with **no Cybenetics entry at all**: Ocypus, 1STPLAYER, the
  non-EVO ASUS TUF.
- **Deprioritise: Chieftec Vega M 850W** - its supervisor IC is listed without short-circuit
  protection.

### Why the 850W was picked in the first place

It was not wrong at the time. The sizing table used a **9800X3D at 162W PPT** and a flat 304W
card, giving ~530W and making 850W the ~60%-load answer. Both builds that survive use a
**9700X at 88W PPT**, and the Working build's GPU is a 220W GRE. The peak fell by 160W and
the PSU never followed.

## Closed: sizing, 2026-09-11

The open item is settled - **750W across all three builds**, priced and specified above.
Independent support for the split: ScatterVolt's 2026 combo guide puts 650-750W on a
9070/GRE build and reserves 850W for the 9070 XT tier
([../scattervolt_2026.md](../scattervolt_2026.md)); the Max build's ~488W peak sits inside
750W comfortably and ATX 3.1 covers the transients by standard.

**Prices, 2026-09-11:** Pure Power 13 M 750W **5 419 at Telemart** (in stock), 5 291 at
hotline floor across 29 offers. The 850W is 5 796 at Telemart. Both are among the few lines
where hotline's floor and a real store price agree to within ~2%.

## Every video behind this document

**Added 2026-09-13 by the source audit.** This file named its videos by channel and year only — **no id, no link** — which is the exact complaint the audit was started over: *"the docs were found to cite videos by channel name with no ID and no timestamp, leaving nothing Dmytro could re-check."* 5 of the 5 PSU videos could not be traced from this page at all. The full set, with the transcript on disk and the quote-by-quote record in [source_audit.md](../source_audit.md):

| Video | Channel | Date | Title |
|---|---|---|---|
| [`Xx6rFaKaqp0`](https://www.youtube.com/watch?v=Xx6rFaKaqp0) | GeekaWhat | 2023-12-29 | How to Pick the Right PSU for Your Next Gaming PC Build! 🛠️ [Options for All Budgets] |
| [`4et8XC9QG00`](https://www.youtube.com/watch?v=4et8XC9QG00) | GeekaWhat | 2026-03-26 | How to Pick the Best PSU for a PC Build in 2026! |
| [`bUh2EZzJZRU`](https://www.youtube.com/watch?v=bUh2EZzJZRU) | JayzTwoCents | 2021-03-13 | Beginners Guide to Power Supplies... How to understand the ratings |
| [`SrNIbt703jo`](https://www.youtube.com/watch?v=SrNIbt703jo) | PC Builder | 2026-03-05 | 🛑STOP🛑 Buying BAD PSUs! Best Power Supply for PC 2026 / Best PSU 2026 |
| [`SS7P63fLE_8`](https://www.youtube.com/watch?v=SS7P63fLE_8) | Tech Guided | 2024-01-11 | How to Choose A Power Supply for Beginners |

