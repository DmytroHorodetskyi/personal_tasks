# CPU cooler and fans

## What cooling does for this machine

Modern CPUs do not overheat and die - they *throttle* and they *get loud*. Since you will sit
at this desk for eight hours a day, cooling is really a **noise** purchase: the goal is a
machine that stays inaudible while an LSP re-indexes and stays civil during a two-hour gaming
session. A good air cooler is the cheapest way to buy silence in the whole build.

## The characteristics that matter, and how to read them

Two rows decide it: how loud it is at a given temperature, and whether it fits. The wattage
rating printed on the box is near the bottom for a reason.

| # | Spec (unit) | What it means, plainly | What it is here |
|---|---|---|---|
| 1 | **Noise at a normalised temperature (dBA)** | The only honest cooling measurement. **Any cooler can be made quiet by letting the CPU run hotter**, so a dB figure with no temperature attached says nothing. Good reviews fix one and report the other. | ~25 dBA under load is quiet; above 30 dBA you hear it in a quiet room. The Phantom Spirit measures **36.4 dBA while holding 124W** on AM5. |
| 2 | **Height (mm)** | Cooler height against the case's stated maximum. Get this wrong and the side panel does not close. | **Phantom Spirit 120 SE = 154mm** on Thermalright's sheet (some retailers say 157mm). The Lancool 216 clears **180.5mm**, so there is wide margin. Budget 160mm to be safe. |
| 3 | **Tower design and heatpipe count** | More heatpipes and two towers mean more surface area - which buys **the same temperature at a lower fan speed**, i.e. less noise, not lower temperatures. | Dual-tower with 6-7 heatpipes is the value sweet spot. The pick is dual-tower, **7x 6mm**. |
| 4 | **RAM clearance (mm)** | Whether the front fan overhangs the DIMM slots. | ~42mm under the Phantom Spirit's front fan. Fine with plain kits (~34mm); tall RGB (~44mm) forces the fan upward. See [ram.md](ram.md). |
| 5 | **Air or AIO (liquid)** | An AIO moves the heat to a radiator. That adds a pump: one more moving part, one more noise source, and a finite service life. | **Air**, for a work machine. AIOs earn their place on 170W+ CPUs or for a specific look - not on a 120W chip. |
| 6 | **Mounting hardware** | The AM5 bracket, and whether fitting it means taking the board out of the case. | Thermalright's AM5 mount is a spring-loaded backplate - straightforward, even-pressure. |
| 7 | **Rated TDP capability (W)** | A marketing number: roughly "watts of heat it can move", with no standard behind it. Treat it as a rough class, never a promise. | The pick claims 105-280W. What actually matters is row 1. Any dual-tower 120mm cooler handles both CPUs on the list with margin. |
| 8 | **Thermal paste** | Included with every cooler here. | Do not buy it separately. Re-pasting a new cooler gains nothing measurable. |

**Ignore:** the rated wattage as a comparison between coolers, ARGB, fan CFM quoted without a
static-pressure figure, and "supports up to 280W" claims generally.

## Specifications

| | **Thermalright Phantom Spirit 120 SE** | Deepcool AK400 | Arctic Liquid Freezer III Pro 360 |
|---|---|---|---|
| Type | dual tower, air | single tower, air | 360mm AIO |
| Heatpipes | **7x 6mm**, AGHP 4th gen | 4x 6mm | - |
| Fans | 2x 120x25mm PWM | 1x 120mm PWM | 3x 120mm PWM |
| Fan speed | up to ~1 500 rpm | up to ~1 850 rpm | up to ~2 000 rpm |
| Airflow | 66.17 CFM per fan | ~66 CFM | - |
| Rated noise | 25.6 dB(A) | ~29 dB(A) | - |
| **Height** | **154mm** (125 x 110 x 154) | 155mm | radiator 398 x 120 x 38mm |
| RAM clearance | ~42mm under the front fan | fine | n/a |
| Rated capability | **105-280W** | ~150W | 300W+ |
| Sockets | AM4 / **AM5** / LGA1700 / 1200 / 115x | same | same |
| Thermal paste | included | included | pre-applied |

Reading these: the **rated wattage is marketing** - treat it as a rough class, not a promise.
The numbers that decide the purchase are **height** (against the case's clearance) and
**measured noise at a fixed temperature** (from reviews, not the box). A cooler can always be
made quiet by letting the CPU run hotter, so a stock dB figure with no temperature attached
says nothing.

Height caution: Thermalright's own spec sheet says **154mm**; some retailers list 157mm for
this cooler and the near-identical Phantom Spirit 120 EVO. Budget **160mm** of case clearance
and the distinction stops mattering - the Lancool 216 allows 180.5mm.

Why air rather than an AIO for this machine: an AIO adds a pump, which is one more moving
part, one more noise source and a finite service life, in exchange for cooling a 120W CPU
does not need.

## Options - CPU cooler

Prices: lowest hotline.ua offer, 2026-09-09, UAH.

| Model | UAH | Type | Verdict |
|---|---:|---|---|
| Deepcool GAMMAXX 300 | 615 | single tower | Not for a 120W CPU. |
| ID-COOLING SE-224-XTS | 944 | single tower | Adequate for a 65W 9700X only. |
| **Deepcool AK400** | **1 515** | single tower, 4 pipes | **The right cooler if you buy a 9700X.** Quiet at 65W. |
| Arctic Freezer 36 | 970-2 702 | dual 120 | Great value, watch RAM clearance. |
| Thermalright Peerless Assassin 120 SE | 2 713 | dual tower, 6 pipes | The old value champion. |
| **Thermalright Phantom Spirit 120 SE** | **2 845** | dual tower, **7 pipes** | **The right cooler if you buy a 9800X3D.** |
| Deepcool AK620 Digital Pro | 3 235 | dual tower | Same class plus a temperature display. Pay for the display if you want it. |
| be quiet! PURE ROCK PRO 3 | 2 105 | dual tower | Quiet-focused, slightly less capable. |
| be quiet! Dark Rock Pro 6 | 5 289 | dual tower | Premium silence. Twice the price for ~1-2 dBA. |
| Noctua NH-D15 G2 | 7 047 | dual tower | The best air cooler made, and completely unjustified at 2.5x the Phantom Spirit. |
| Arctic Liquid Freezer III Pro 360 | 3 863 | 360 AIO | **Best AIO value on the market** by a wide margin. Only if you want liquid; needs a 360mm mount. |
| ASUS TUF Gaming LC III 360 ARGB LCD | 6 861 | 360 AIO | Paying for the screen. |

## Evidence (revised after the deep review pass, 2026-09-09)

**Correction first.** I earlier stated the Phantom Spirit runs "1.5-2.0 dBA quieter and 2-4 C
cooler" than the Peerless Assassin as though it were measured. The deep pass found **no
lab-measured head-to-head between the two** - that figure traces only to spec-aggregator and
SEO pages. What *is* verifiable from Thermalright's own specification: the Phantom Spirit
120 SE has **7 heatpipes to the Peerless Assassin's 6** and the newer TL-C12B V2 fans. It is
not a rebadge, but the size of the advantage is unproven.

**Is it enough for a 9800X3D? Yes, with margin - measured.** On the same 7-pipe stack:

- On AM5 (a 7700X) it held **124W at just 36.4 dBA - the second-strongest air result** in
  Tom's Hardware's chart, and at a 75W limit it tied third-quietest at 37.3 dBA.
- On an unlimited i7-13700K it sustained **234W at 41.9 dBA**, and **224W noise-normalised
  to 38.2 dBA**.

A 9800X3D's ~120W sits comfortably inside the AM5-measured envelope. This chip is
hotspot-density-limited rather than wattage-limited, so a bigger cooler buys very little.

**Height, corrected:** Thermalright's own spec for the **SE is 154mm**; the non-SE Phantom
Spirit 120 SE measures **154mm** on Thermalright's own spec sheet (some retailers list
157mm) with 42mm RAM clearance. Budget 160mm if you are near a case
limit.

**The cheaper option is measured too:** the **Arctic Freezer 36** handled 219W unlimited at
40.3 dBA and **214W noise-normalised at 38.2 dBA** - within ~5-10W of the Phantom Spirit -
and at 125W it ran **quieter than the system fans at idle**.

**The one cooler measured on an actual X3D chip:** the **DeepCool AK620 G2**, tested on a
9950X3D, cooled **242.5W at a noise-normalised 38.9 dBA - second-best air cooler tested** -
and sat at 38.9 dBA in a gaming simulation. Its smaller sibling the AK400 G2 posted the best
RAM temperatures of any air cooler. Neither appeared on hotline.ua when checked.

**Unverified in this pass:** the Peerless Assassin 120 SE itself, the AK620 Digital Pro, be
quiet! Pure Rock Pro 3 and Dark Rock Pro 6, and the Arctic Liquid Freezer III Pro 360 - no
measured data retrieved for any of them. Also completely unresearched: AM5 mounting-hardware
quality and fan-bearing complaints, because the owner-report sources were unreachable.

**Avoid: the Montech NX600** - Tom's Hardware calls it "the loudest air cooler I've *ever*
tested" at 50 dBA.

An X3D chip is a dense heat source but a modest one in absolute terms; it does not need
liquid cooling.

## Options - case fans

Most of the recommended cases already ship with 3-4 fans, so this is usually an optional
line item.

| Model | UAH | Note |
|---|---:|---|
| Arctic P12 Pro LN 5-pack | 882 | Low-noise variant, five fans. The best value in the category. |
| Arctic P12 Pro PST (each) | 325 | 120mm, PWM daisy-chain, pressure-optimised (good behind filters/radiators). |
| be quiet! Pure Wings 3 120 PWM | 299 | Quiet and cheap. |
| GameMax FN12A-N2 | 259 | Filler. |
| Noctua NF-A12x25 PWM | 1 286 | The reference 120mm fan. 4x the price for a couple of dB. |
| Arctic P8 Max / P9 Silent | 339 / 239 | Only for small cases. |

**Static pressure vs airflow**: "P" series (pressure) fans belong on radiators and behind
dust filters; "F"/airflow fans belong in open positions. It is a small effect - do not
over-think it, but do not put a low-pressure fan behind a fine filter.

## Verdict

> **CURRENT ANSWER (2026-09-11): Working + Max buy a Deepcool AK400 at 1 699; Lean buys no
> cooler at all** and uses the Wraith Stealth bundled with its 7500F MPK. Full reasoning in the
> DECISION section at the end of this file.
>
> **Open option, 2026-09-14:** the click.ua consultant proposed a **DeepCool AG620 G2 WH
> ARGB at 2 559, +860 same-shop** - a real dual tower that fits, priced and measured in the
> AG620 section below. It buys noise headroom, not capability; the AK400 stays the pick
> until Dmytro says otherwise.
>
> **Simplified 2026-09-10:** all three builds in [../../pc_build.md](../../pc_build.md) use a
> 65W CPU (7500F or 9700X), so the Phantom Spirit line below applies to no current
> configuration.
>
> **Price-checked at the two assembling shops, 2026-09-11 - it costs more than the doc said.**
> The 1 515 was the lowest hotline offer, from shops that do not assemble. At both candidate
> stores the AK400 (R-AK400-BKNNMN-G-1) is **1 699**: Telemart 1 699, Brain 1 699 and in stock.
> **+184 per build.** Watch the SKU - Deepcool sells AK400 ZERO DARK (1 899), DIGITAL (2 099-
> 2 229) and DIGITAL PRO (2 289) under the same AK400 name; the plain black one is the pick and
> the digital variants only add a temperature display.


- **With the 9800X3D: Thermalright Phantom Spirit 120 SE, 2 845.** Documented as quieter and
  cooler than its own cheaper sibling, fits every case here, and leaves nothing on the table
  for a 120W CPU.
- **With the 9700X: Deepcool AK400, 1 515.** A 65W chip does not need more.
- **Fans: buy none initially.** Build it with the case's own fans, then add an Arctic P12 Pro
  5-pack (882) only if temperatures or noise actually bother you. Spending 3 000 on fans
  before hearing the machine is the classic first-build mistake.
- **Better but pricier, if silence is a priority: be quiet! Dark Rock Pro 6 (5 289)** or the
  **Arctic Liquid Freezer III Pro 360 (3 863)** if you would rather move the heat out of the
  top of the case. Neither is necessary.

## Cross-check against three cooler guides (2026-09-11)

Sources: Tech Guided *How to Choose A CPU Cooler for Beginners* (2023), Hardware Whisperer
*CPU Coolers Explained* (2025-01), and **PC Builder *Best CPU Cooler 2026 for Ryzen & Intel***
(2026-03) - the last of which is current and makes per-CPU recommendations, so it is the only
one that bears on this build.

### The finding that challenges the pick

**PC Builder recommends a dual-tower air cooler as the *minimum* for any Ryzen 7 7000/9000
chip**, naming the 7700X and **9700X** explicitly alongside the X3D parts: "a little tougher to
cool than the regular Ryzen 7 CPUs... I recommend a minimum of a dual tower air cooler for both
performance and noise." GeekaWhat's 2026 parts guide goes further and recommends liquid cooling
for a Ryzen 7. **This build puts a single-tower AK400 on the 9700X in the Working and Max
builds.**

The counter-argument, stated so it can be judged rather than assumed - and **weakened
2026-09-13 when the video was read in full**:

- Both recommendations are made for the **Ryzen 7 class**, whose best-known member is the
  **105W / 142W PPT** 7700X. The **9700X ships at 65W / 88W PPT** - the same envelope this
  document already calls "a 65W chip does not need more".
- **But he is not generalising from the 7700X.** In context he lists *"the Ryzen 7700X, **9700X**,
  and the big X3D CPUs"* together and gives that whole tier the dual-tower minimum, while giving
  the tier below - *"Ryzen 5 7000 9000 series CPUs"*, which is Lean's 7500F - a separate and
  explicitly lighter rule: *"at least a budget tower air cooler. And honestly, this is probably
  all you really need as long as your case has good airflow."* He sorted the 9700X deliberately.
- **And the method this document uses to defend the pick is the one its own source calls
  unreliable.** Tech Guided: *"there is no standardized way to calculate TDP, Intel and AMD
  calculate differently"*, and the fix is expert benchmarks - he names **Gamers Nexus and
  Hardware Unboxed**. That is exactly the search needed to close question 1 below.
- **A third source points the other way.** Hardware Whisperer rates tower coolers at *"150W to
  over 250W"* and calls them *"an excellent choice for high-performance CPUs where overclocking
  is not required"* - which describes a non-overclocked 9700X at 88W PPT. Generic rather than
  measured, so it does not close the question either.
- The tier below, which PC Builder says a **budget single tower** handles comfortably, is the
  Ryzen 5 7000/9000 series - and the **Lean build's 7500F is exactly that**, so the AK400 is
  already above requirement there.

**But the honest gap: this repo has no measured data for the AK400 on a 9700X.** The Evidence
section above measures the Phantom Spirit, the Arctic Freezer 36, and the **AK620 G2 / AK400 G2**
- the G2 is a *different cooler* from the AK400 in the build table. The pick currently rests on
a wattage argument, not a measurement, against two independent 2026 recommendations pointing the
other way.

### Stepping up to a dual tower costs far more here than the video implies

PC Builder's cheap dual-tower champion is the **ID-COOLING FROZN A620 Pro SE** at $27, "tied
with the Phantom Spirit" and "always the cheapest" - with an explicit warning to buy the
**Pro SE**, not the original A620. Checked in Ukraine, 2026-09-11:

| | Brain | Telemart |
|---|---|---|
| FROZN A620 **Pro SE** | listed but **«Знятий з виробництва»** - discontinued | **not stocked** |
| FROZN A620 (plain - the one the video says to avoid) | A620 ARGB 3 099 | 2 749 black / 2 799 ARGB / 2 899 GDL |

So the American "dual tower for $5 more" does not exist on this market. The real cost of moving
the Working and Max builds to a dual tower is the **Thermalright Phantom Spirit 120 SE at
2 845**, or the plain A620 at 2 749 - **roughly +1 050-1 150 per build over the AK400's 1 699.**

### The Lean build may not need a cooler at all

The **7500F MPK bundles a Wraith Stealth** ([cpu.md](cpu.md) records this; the video confirms
the 7500F ships with a stock cooler). PC Builder's view: it "is fine, but given how cheap budget
tower air coolers are, I'd switch it out" - i.e. the swap buys noise, not capability. **Dropping
the AK400 from Lean saves the full 1 699** and is the single largest saving still available in
that build.

### Confirmed, no action

- **Thermal paste:** every cooler in 2026 ships with enough for one application - **buy none**.
  Paste degrades in **3-5 years** and wants cleaning and reapplying then. Premium paste
  (Kryonaut, ~$20) is explicitly not worth it below high-end builds: "spend that $20 getting a
  better cooler".
- **CPU contact frame: not needed on AMD.** It addresses Intel's uneven socket pressure on
  13th/14th-gen i7/i9 only, and fitting one risks the board's pins.
- **Socket, clearance and RAM overhang** are covered in the criteria table above; the guides add
  nothing to them.
- **Avoid 280mm AIOs** on case-fitment grounds (PC Builder: go 240 or 360). Moot - this build is
  air-cooled.

### Net

**No change forced, one question opened and one saving found:**

1. **Working/Max: is the single-tower AK400 right for a 9700X?** Two 2026 guides say dual tower
   minimum for that CPU class; this document says 65W does not need one and has no AK400 + 9700X
   measurement either way. Closing it needs a measured AK400 review on a 65W AM5 part, not
   another opinion. Cost if the answer is "step up": **+1 050-1 150 per build**.
2. **Lean: drop the cooler entirely, -1 699** - the MPK's Wraith Stealth is adequate for a 65W
   Ryzen 5, at a noise cost.

### Verified against AMD's own specifications (2026-09-11)

Both open points above were checked at the primary source - AMD's product pages - rather than
against more opinion.

| AMD spec page | Default TDP | Thermal solution in the box | AMD's "Recommended Cooler" line |
|---|---|---|---|
| **Ryzen 7 9700X** | 65W | **Not Included** | "Premium air cooler recommended for optimal performance" |
| **Ryzen 5 9600X** | 65W | Not Included | **the identical sentence** |
| **Ryzen 5 7500F** | 65W | **AMD Wraith Stealth - listed for both PIB *and* MPK** | *(no such line - it ships with a cooler)* |

**What this settles:**

1. **The Lean saving is real and sourced.** AMD lists the Wraith Stealth for the **MPK** SKU
   explicitly, which is the SKU [cpu.md](cpu.md) buys. Dropping the AK400 from Lean saves
   **1 699** with no compatibility question at all.
2. **"Premium air cooler" is boilerplate, not a 9700X requirement.** AMD prints the same sentence
   on the **9600X** - a 6-core 65W chip nobody argues needs a dual tower. It appears on every
   Zen 5 part shipped without a cooler, so it carries no information about the 9700X specifically
   and **cannot be used to support the dual-tower recommendation**.
3. **No measured AK400-on-9700X test was found** in this pass either. The reviewer consensus for
   the 9700X names dual towers (Peerless Assassin, Phantom Spirit) and 240mm AIOs; community
   load temperatures for the chip average **~58 C**, which is nowhere near the 95 C limit and is
   consistent with the wattage argument.

**Conclusion: the AK400 stays.** The case against it is two generic class-level recommendations
and one boilerplate line that AMD also prints on a 6-core chip. The case for it is the measured
65W / 88W PPT envelope. If the 9700X is ever switched into its optional **105W / 142W PPT** mode,
this conclusion does not hold and the Phantom Spirit at 2 845 becomes the right cooler.

## CLOSED 2026-09-13: the measured AK400 test exists, and it clears the 9700X

Every earlier pass ended on *"no measured AK400-on-9700X test was found"*, which left the question
to class-level opinion. **A measurement of the cooler's actual capacity does exist**, and it
settles the question the only way Tech Guided said it could be settled - *"there is no
standardized way to calculate TDP ... use benchmarks"*.

| What was measured | Result | Source |
|---|---|---|
| AK400 on a **Ryzen 9 5950X overclocked to 4.45 GHz @ 1.312V, 220W of CPU package power** | **delta 68 °C** over a 22 °C room at full fan; **69 °C** at a noise-normalised 40 dBA | [KitGuru](https://www.kitguru.net/components/cooling/luke-hill/deepcool-ak400-cpu-cooler-review/all/1/) |
| AK400 **Digital** on a Ryzen 5 5600X | *"peaking at 63 degrees Celsius ... exactly the same peak load temperature as the original AK400"* | [APH Networks](https://aphnetworks.com/reviews/deepcool-ak400-digital/3) |
| Ryzen 7 9700X under Blender | *"The max operating temperature is set at 95°C, but as you can see in the graph above, I was way below that with a good air cooler"* | [Hardware Busters](https://hwbusters.com/cpu/amd-ryzen-7-9700x-cpu-review-performance-thermals-power-analysis/11/) |

**A second, independent measurement - added after Dmytro asked whether one source was closing
this.** Basic Tutorials tested the AK400 on a **Ryzen 5 3600X** (95 W TDP, 128 W PPT) under
Cinebench R23 in a case, room baseline 36 dB:

| AK400 | Idle delta | Cinebench delta | Noise |
|---|---:|---:|---:|
| 100% PWM | 9.2 °C | **48.0 °C** | 41 dB |
| 50% PWM | 9.3 °C | **50.0 °C** | 38 dB |

[Basic Tutorials](https://basic-tutorials.com/reviews/hardware-reviews/deepcool-ak400/)

**And it kills the linear model an earlier version of this section used.** 68 °C at 220 W is
0.31 °C/W; 48 °C at a ~95-125 W chip is 0.38-0.50 °C/W. Delta does not scale with watts alone -
heat density, IHS and bench-versus-case all move it - so **do not extrapolate °C/W**. Read the two
measurements as a bracket instead:

| Load measured | Delta over ambient | In a 22 °C room |
|---|---:|---:|
| ~95-125 W chip (3600X, Cinebench, in a case) | 48-50 °C | **~70-72 °C** |
| 220 W chip (5950X OC, open bench) | 68-69 °C | ~90 °C |

The 9700X's 88 W PPT sits **at or below the lower bracket**, on a chip whose IHS Hardware Busters
credits with *"lower thermal resistance"* than earlier parts. So the worst honest reading is
**~70 °C under sustained all-core load, 25 °C below the 95 °C limit**, and the 105 W / 142 W mode
lands between the two brackets rather than above them.

**So the AK400 is not lacking, and it clears the 105 W mode too** - which the 2026-09-11
conclusion had explicitly excluded for want of a number. The three guides that point at liquid
cooling for *"a Ryzen 7 or higher"* are sorting by product tier, not by watts; the 9700X is a 65 W
part sitting in a tier defined by 105 W and 170 W chips.

**What the +1 146 for a Phantom Spirit 120 SE actually buys: noise, not capability.** KitGuru
measured the AK400's fan at **42 dBA at its 1850 RPM maximum** and called it *"mediocre"* against
competitors, and needed **90% duty cycle** to hold 40 dBA. On a 88 W chip the fan will rarely be
near maximum, but that is the axis on which the upgrade is defensible - not thermals.

### The cart has a different SKU than this document specifies

Dmytro's configurator shows **DeepCool AK400 Digital SE Black, `R-AK400-BKADMN-GJD`, 1 699**. This
document specifies the plain **`R-AK400-BKNNMN-G-1`**, *"not the ZERO DARK / DIGITAL / DIGITAL PRO
variants"*. Thermally it does not matter - APH Networks measured the Digital at the same peak load
temperature as the original - and the price is identical, so this is a note, not an objection. The
Digital carries an LCD display block that needs power; **how it is powered was not confirmed**
(the review page consulted does not say), so check the box contents before assuming a spare header
is not needed.

### The shop's warning is a heuristic, not a measurement

The click.ua configurator says *"Ваша збірка сумісна, проте система охолодження процесора не значно
перевищує його тепловиділення (менше 35%)"*. That is a margin rule applied to two numbers in the
shop's database - a cooler rating against a CPU TDP - and the shop does not publish either input.
It is not a thermal test and it does not override the measurements above. The same page's spec
tables were separately found to swap read/write figures and misstate IOPS by ~50x, so its
generated advice carries no weight here.

## The shop consultant's AG620 G2 (2026-09-14)

The consultant at click.ua proposed swapping the cooler to a **DeepCool AG620 G2 WH ARGB
(R-AG620-WHAMMG2-G)** — a dual-tower air cooler, i.e. the step this file priced on 2026-09-11 as
"+1 050-1 150 per build" and then declined. **The price is new: it is +860, not +1 146, and the
Phantom Spirit this file named as the step-up is not sold at click.ua at all.**

### Prices, all read direct at the shops, 2026-09-14

| Cooler | click.ua | Brain | ITbox | Telemart |
|---|---:|---:|---:|---:|
| **Deepcool AK400** (R-AK400-BKNNMN-G-1) — current pick | **1 699**, in stock | 1 699 | 1 699, in stock | 1 699, in stock |
| **AG620 G2 WH ARGB** (R-AG620-WHAMMG2-G) — proposed | **2 559**, in stock | 2 559 | not listed | not listed |
| AG620 G2 ARGB black (R-AG620-BKAMMG2-G) | not listed | 2 449 | 2 449, in stock | not listed |
| AG620 ARGB V2 (previous gen, R-AG620-WHAMMN-GJD) | 2 929, in stock | 2 929 | 2 929, in stock | 2 929, in stock |
| Thermalright Phantom Spirit 120 SE | **not stocked** | not stocked | not stocked | out of stock |

**The premium is same-shop and therefore real: +860 per build at click.ua**, 1 720 across Working
and Max. hotline's directory shows the black G2 advertised from 2 158 across 10 sellers; that is
the usual cheapest-of-forty figure and is not what click.ua charges.

### Specifications

| | **Deepcool AK400** (current) | **DeepCool AG620 G2 WH ARGB** (proposed) |
|---|---|---|
| Type | single tower, air | **dual tower, air** |
| Heatpipes | 4 × 6 mm | **6 × 6 mm** |
| Fans | 1 × 120 × 25 mm PWM | **2 × 120 × 25 mm PWM**, ARGB |
| Fan speed | up to ~1 850 rpm | 500–2 000 rpm / 500–2 200 rpm |
| Airflow | ~66 CFM | 62.16 / 68.85 CFM |
| Static pressure | not published | 1.75 / 2.10 mmAq |
| Rated noise | ~29 dB(A) | ≤28.10 / ≤30.93 dB(A) |
| **Height** | **155 mm** | **159 mm** (heatsink 156 mm; 129 × 136 × 159 mm assembled) |
| Weight | ~660 g | **1 046 g** |
| Sockets | AM4/AM5, LGA1700/1200/115x | AM5/AM4, **LGA1851/1700** |
| ARGB connector | none | 3-pin 5 V ARGB |
| **click.ua, 2026-09-14** | **1 699** | **2 559** |

Specs from [DeepCool's own page for the WH ARGB SKU](https://www.deepcool.com/products/Cooling/cpuaircoolers/AG620-G2-WH-ARGB-Superior-Performance-6-Heatpipe-Dual-Tower-CPU-Cooler/2026/22802.shtml).

### It fits, and it matches the case

- **Height 159 mm against the AeroCool D502A's 171 mm** — 12 mm of margin. Working and Max both
  use the D502A, so this is clear. (The P500C in the Lean build allows 162 mm, which would leave
  only 3 mm — but Lean buys no cooler at all, so it does not arise.)
- **RAM: Kingston Fury Beast non-RGB, ~34.9 mm** — under any dual tower's front fan. No conflict.
- The case is the **white** D502A-G-WT-v1 and the board (ASRock B850 Pro RS WiFi) has ARGB
  headers, so the WH ARGB SKU is the cosmetically consistent one. That is what the +110 over the
  black G2 buys.

### The measured case for it — and what it does not say

No lab test of the **G2** with a noise-normalised figure was found in this pass. What exists is
Tom's Hardware on the **previous-generation AG620** (same 6 × 6 mm dual-tower stack, different
fans and mount), tested on an i9-13900K:

> "a solid dual tower air cooler that pairs well with Intel's Core i9-13900K, handling loads of
> up to **277W** … at full fan speeds I found the noise produced by this cooler to be slightly
> annoying. The pitch of the fans is whiny"
> — [Tom's Hardware, 2023-01-15](https://www.tomshardware.com/reviews/deepcool-ag620-air-cooler/2)

and, at the power level that actually matters here:

> "When limited to **125W**, the AG620 **ran silently**; the noise profile is essentially
> indistinguishable from the rest of the system fans."

**Read honestly:** 277 W of capacity against the 9700X's **88 W PPT** is enormous overkill, and
this file already established the AK400 lands at **~70 °C in a 22 °C room, 25 °C below the 95 °C
limit**, on the same chip. The AG620 does not fix a thermal problem, because there is not one.
What it buys is the axis the CLOSED 2026-09-13 section named: **noise**. Two 120 mm fans on six
heatpipes hold 88 W far below their 2 000 rpm ceiling, where the AK400's single fan is already
the one KitGuru called *"mediocre"* at 42 dBA at its 1 850 rpm maximum.

**The caveats, stated rather than buried:**

1. The 277 W and "ran silently" figures are the **G1**, not the G2. The G2 changed the fans, which
   is precisely the part the reviewer complained about — the whine may be fixed or may not. Nobody
   has measured it.
2. **The consultant's own reason is not evidence.** click.ua's configurator warns that the cooler
   *"не значно перевищує його тепловиділення (менше 35%)"*. That is a margin rule over two numbers
   in the shop's database, not a thermal test, and this file already recorded that the same page's
   spec tables swap read/write figures and misstate IOPS by ~50×. The recommendation may simply be
   the configurator talking.

### Verdict

**No change forced. The AK400 is not undersized and the consultant has not produced a measurement.**
But at **+860 same-shop** — not the +1 146 this file declined on 2026-09-11 — the dual-tower step
is now the cheapest it has ever been here, and the white ARGB SKU is the one that matches the case.

- **Keep the AK400 (1 699)** if the money matters more than the last few dBA. Nothing in this pass
  weakens the 2026-09-13 closure.
- **Take the AG620 G2 WH ARGB (2 559, +860)** if a quieter machine under sustained all-core load
  and a matching white ARGB tower are worth 1 720 across the two builds. This is the honest version
  of the upgrade — a real dual tower, in stock, at his shop.
- **Cheaper way to the same thing:** the **black AG620 G2 ARGB at 2 449 (ITbox, in stock)** —
  identical cooler, −110, does not match the white case.
- **Do not buy** the AG620 **ARGB V2** at 2 929: it is the previous generation at +370 over the G2.

## DECISION (2026-09-11): the Lean build buys no cooler

Dmytro's call. The **7500F MPK ships with an AMD Wraith Stealth** - listed by AMD for the MPK
SKU specifically - so the Lean build takes it and **saves the AK400's 1 699**. On the tier whose
entire purpose is being cheap, 1 699 for a quieter idle is the wrong place for the money.

**Working and Max keep the Deepcool AK400 at 1 699** (plain black R-AK400-BKNNMN-G-1, not the
ZERO DARK / DIGITAL / DIGITAL PRO variants).

What is being accepted on Lean: the Wraith Stealth is audibly louder than a tower cooler under
load and has less headroom, though it is AMD's own bundled solution for this 65W chip. It is
also **reversible at any time** - the AK400 can be added later for the same 1 699, since the
cooler is the one part of the build that can be changed without touching anything else.

## Every video behind this document

**Added 2026-09-13 by the source audit.** This file named its videos by channel and year only — **no id, no link** — which is the exact complaint the audit was started over: *"the docs were found to cite videos by channel name with no ID and no timestamp, leaving nothing Dmytro could re-check."* 3 of the 3 CPU cooler videos could not be traced from this page at all. The full set, with the transcript on disk and the quote-by-quote record in [source_audit.md](../source_audit.md):

| Video | Channel | Date | Title |
|---|---|---|---|
| [`dwvlv7VPW_c`](https://www.youtube.com/watch?v=dwvlv7VPW_c) | Hardware Whisperer | 2025-01-08 | CPU Coolers Explained. Cooler types and how to choose the right one for you. |
| [`ju2OYF16RKA`](https://www.youtube.com/watch?v=ju2OYF16RKA) | PC Builder | 2026-03-22 | 🛑STOP🛑 Buying BAD Coolers! Best CPU Cooler 2026 for Ryzen & Intel Builds |
| [`7f-Guxj4kl0`](https://www.youtube.com/watch?v=7f-Guxj4kl0) | Tech Guided | 2023-12-24 | How to Choose A CPU Cooler for Beginners |

