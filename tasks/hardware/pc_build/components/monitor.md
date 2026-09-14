# Monitor

**Status: closed 2026-09-12 — ASGARD Gaming AS275QC, 6 999 UAH at click.ua** (Foxtrot matches
at 6 999; Rozetka wants 7 799). 27" VA curved, WQHD 2560x1440, 200Hz, 5000:1 claimed,
FreeSync + G-Sync, VESA 100x100, **no height adjustment**. Chosen by Dmytro.

**This overturns the AOC Q27G4ZR verdict recorded below, and two rules this file was applying.**

1. **"Height adjustment is not a luxury at eight hours a day"** was written by this research,
   **not stated by Dmytro**. His monitor requirements were 27", 1440p and no 4K. The rule was
   then used to reject monitors - the same failure as the XXL mousemat and the 70 cm desk
   depth, where an inference hardened into a requirement.
2. **"Reject any panel with no independent measurements"** turns out to eliminate *almost the
   entire catalogue* at the shop actually being bought from. Checked 2026-09-12: of eleven
   monitors offered there, exactly **one** - the Gigabyte G27Q2 - has a measured review of
   that specific model. Even the Samsung Odyssey G5 S27CG550 has none (RTINGS tested other
   G5 variants, not this one). A rule that admits one product is a rule about availability,
   not about quality.

**What the AS275QC does have:** two owner reviews, both positive and both specific -
Comfy 4/5 (27 Aug 2026): 1440p at 27" is sharp, *"текстові документи та сайти читати
одне задоволення"*, adapted to the curve in two hours, no dead pixels or bleed;
click.ua 5/5: used for work and games, no complaints. Thin, but real owners.

**Accepted trade-offs:** VA smears on dark transitions and shifts gamma at the corners more
than IPS; the curve bows straight lines; fixed height; 8-bit colour (16.7M) against the
Gigabyte's 10-bit and 94% DCI-P3; and the 5000:1 and "1 ms" figures are the manufacturer's,
where "1 ms" on VA is an MPRT number rather than grey-to-grey. **14-day return covers the
panel lottery.**

**ASGARD is a Ukrainian brand**, not a shop label - also stocked by Foxtrot, Comfy, Rozetka
and MOYO. An earlier draft of this file called it a house brand; that was wrong.

**The AOC research below stands as the record of the alternative** and is still the answer if
the AS275QC disappoints: Q27G4ZR 8 669 or Q27G4XF 6 899, both at Rozetka.

## What the monitor does for this machine

It is the only component you look at, it outlives every other part (a good panel serves two
PCs), and it has to satisfy two conflicting jobs:

- **Work**: eight hours of small text - code, terminals, documents. Wants high pixel
  density, clean subpixel rendering, no eye strain, no burn-in risk from static UI.
- **Gaming at 1440p**: wants high refresh, low response time, adaptive sync.

The good news is that 27" 1440p is one of the rare specs where both jobs agree.

## The characteristics that matter, and how to read them

The monitor outlives the PC, and it is the part you look at for eight hours a day - so the
work-facing rows come first, ahead of the gaming ones.

| # | Spec (unit) | What it means, plainly | What it is here |
|---|---|---|---|
| 1 | **Resolution + size = pixel density (PPI)** | Neither number means anything alone. Together they decide whether **text is pixel-aligned** in your IDE and terminal. | 27" 1440p = **109 PPI**: Windows at 100% scaling, crisp text everywhere. 27" 4K = 163 PPI and needs 150% scaling, where DirectWrite still misaligns glyphs in some tools. This is why 27"/1440p is the standard dev monitor, not a compromise. |
| 2 | **Panel type** | **IPS**: accurate colour, wide angles, decent speed, mediocre contrast (~1000:1). **VA**: better contrast, slower, smears in motion. **OLED**: perfect blacks, instant response, **burn-in risk** and text fringing. **mini-LED**: IPS plus hundreds of backlight zones - real HDR. | **IPS.** The static IDE layout you stare at all day is the exact worst case for OLED burn-in. |
| 3 | **Ports and their versions** | Not all inputs carry all refresh rates. A monitor's headline Hz often applies to **one port only**. | The pick does 240Hz on **DisplayPort 1.4 (with DSC) only** - its HDMI is 2.0 and **caps at 144Hz**. Use DisplayPort or silently lose 40% of what you paid for. |
| 4 | **Refresh rate (Hz)** | Frames per second the panel can display. | 60 -> 165 is a huge jump. 165 -> 240 is clearly visible. 240 -> 300+ is competitive-play territory, which you said this is not. **180-240Hz is the target.** |
| 5 | **Ergonomics: height range (mm) and VESA** | Height adjustment is not a luxury at eight hours a day; a 100x100 VESA mount lets you add an arm later. | The pick gives **130mm of height travel**, tilt, swivel and pivot. **Both withdrawn monitors failed on this row alone** - tilt only. |
| 6 | **Measured response time (ms) + overshoot (%)** | How fast a pixel changes, and whether it overcorrects. **Manufacturer "1ms" numbers are fiction on every monitor ever made.** Overshoot shows as a bright halo trailing moving objects, and matters as much as the millisecond figure. | Look for a review measurement. Any modern 180Hz+ IPS is adequate; the budget AOC's **0.1% average overshoot** is unusually clean tuning. |
| 7 | **Measured brightness (nits) and contrast** | What the panel actually does, as opposed to the spec sheet. | Measured on the shortlist: 545 nits / 1 410:1 (the pick), 434 / 1 262:1, 365 / 1 198:1. Under ~400 nits is noticeably dim in a bright room. |
| 8 | **Adaptive sync** | FreeSync Premium / G-Sync Compatible: the panel matches the GPU's frame rate, removing tearing without V-Sync input lag. | Present on everything listed, and it works with the RX 9070 XT over DisplayPort. Not a differentiator. |
| 9 | **Subpixel layout** | Standard **RGB stripe** renders text the way Windows expects. QD-OLED's triangular layout causes colour fringing on small text. | RGB stripe on every IPS panel here. A second reason the OLEDs are wrong for this machine. |

**Ignore:** "1ms response", **DisplayHDR 400** (it is SDR brightness with a badge - real HDR
needs local dimming and 600+ nits), dynamic/"mega" contrast ratios, %NTSC colour claims, and
built-in speakers.

## Specifications

| | **AOC Q27G4ZR** (the pick) | AOC Q27G4XF (budget) | GIGABYTE M27Q3 (upgrade) |
|---|---|---|---|
| Size / panel | 27" **Fast IPS**, matte | 27" Fast IPS | 27" IPS |
| Resolution | **2560x1440** | 2560x1440 | 2560x1440 |
| **Pixel density** | **109 PPI** | 109 PPI | 109 PPI |
| **Refresh rate** | **240Hz** (260Hz OC) | 180Hz | 300Hz (320 OC) |
| Response (measured) | ~1ms GtG rated | **4.6ms G2G, 0.1% overshoot** | 4.5ms, variable overdrive |
| Input lag | low (KitGuru) | 2.7ms | 0.3ms |
| Brightness (measured) | **545 nits peak** | 365 nits | 434 nits |
| Contrast (measured) | 1 410:1 | 1 198:1 | 1 262:1 |
| Colour | 100% sRGB, 86% DCI-P3, 80% AdobeRGB | dE 1.4 | - |
| HDR | DisplayHDR 400, **no local dimming** | - | - |
| Ports | **1x DisplayPort 1.4** (240Hz via DSC), 2x HDMI 2.0 (**144Hz cap**), 3.5mm | DP 1.4, HDMI | DP, HDMI 2.1, USB-C PD, KVM |
| Speakers | 2x 2W | - | - |
| VESA | **100x100** | 100x100 | 100x100 |
| Stand | **130mm height**, 24 deg tilt, +/-28 deg swivel, +/-90 deg pivot | height adjustable | full |
| Power | 16-38W | - | - |
| Warranty | 3 years | 3 years | - |

The rows to actually read:

- **Resolution and size together = PPI.** 109 PPI is why 27" 1440p is the standard dev
  monitor: Windows runs at 100% scaling with pixel-aligned text in every IDE and terminal.
  27" 4K is 163 PPI and needs 150% scaling, where DirectWrite still misaligns glyphs in some
  tools.
- **Ports, carefully.** This panel does 240Hz on **DisplayPort only** - its HDMI is 2.0 and
  caps at 144Hz. Use DisplayPort or you silently lose 40% of what you paid for.
- **Measured response, not "1ms".** The box number is fiction on every monitor ever made.
  Overshoot percentage matters as much as the millisecond figure: overshoot is the pixel
  overcorrecting, which shows as a bright halo trailing moving objects.
- **DisplayHDR 400 is not HDR.** It is SDR brightness with a badge. Real HDR needs local
  dimming; nothing at this price has it. Ignore the row.
- **130mm of height adjustment** is not a luxury at eight hours a day, and it is exactly what
  the two withdrawn monitors lacked.

## Options

Prices: lowest hotline.ua offer, 2026-09-09, UAH. All 27" 2560x1440 unless noted.

The deep pass established something that reshaped this table: **most cheap 1440p monitors
have never been measured by anyone credible.** RTINGS and TFTCentral have reviewed none of
the four models I originally shortlisted. Where a model has no lab data, that is now stated
as a defect in the purchase, because it means the overdrive tuning, contrast, brightness and
VRR behaviour are all unknown until the box is open.

| Model | UAH | Spec | Independent measurements? | Verdict |
|---|---:|---|---|---|
| Samsung Odyssey G5 | 7 241 | 165Hz VA | - | VA smearing. No. |
| **AOC Q27G4XF** | **6 757** | 180Hz Fast IPS | **Yes** (DisplaysTested) | **The budget pick.** 4.6 ms G2G, **0.1% average overshoot** - unusually clean tuning - 2.7 ms lag, 1198:1, dE 1.4. Dim at 365 nits measured. |
| ~~GIGABYTE G27Q20~~ | 7 816 | 200Hz (210 OC) | **None found anywhere** | **Withdrawn as my "bargain pick".** No RTINGS, TFTCentral, PC Monitors or Monitors Unboxed review exists. Height+tilt only, HDMI 2.0. You would be buying blind. |
| ~~ASUS TUF VG27AQ5A~~ | 8 784 | 210Hz Fast IPS | **None found anywhere** | **Withdrawn.** No credible review exists, and ASUS's own spec sheet confirms **no height adjustment - tilt only**. Wrong monitor for eight hours a day. |
| Philips 27M2N3501PA | 9 139 | 260Hz IPS | not checked | Unassessed. |
| MSI MAG 274QRFW E20 | 9 230 | 200Hz IPS | not checked | Unassessed. |
| **AOC Q27G4ZR** | **9 551** | 240Hz (260 OC) Fast IPS | **Yes** (KitGuru 9/10, Club386) | **The recommendation.** See the measurements below. |
| ~~AOC Q27G3XMN~~ | 13 499 | 180Hz mini-LED **VA**, 336 zones | Yes (TFTCentral, RTINGS) | **Withdrawn - and it is not IPS, it is VA.** Reasons below; this is the biggest correction in this document. |
| **GIGABYTE M27Q3** | **13 169** | 300Hz (320 OC) IPS | **Yes** (Monitors Unboxed) | **The better-but-pricier pick**, with one caveat to verify. 1262:1, 434 nits, 4.5 ms with *working* variable overdrive, 0.3 ms lag, KVM, USB-C PD, HDMI 2.1. |
| **GIGABYTE M27UP** | **16 999** | 27" **4K** 160Hz + FHD dual-mode | **Yes** (Monitors Unboxed + PC Monitors) | The 4K option, and better supported by evidence than I first gave it credit for. 405 nits, 1280:1, PWM-free, full-bandwidth HDMI 2.1, hardware KVM. |
| MSI MAG 274QPF X30MV | 17 859 | 300Hz IPS | not checked | The M27Q3 is measured and cheaper. |
| MSI MAG 271QP QD-OLED X24 | 22 407 | 26.5" 240Hz QD-OLED | yes | Best image in gaming, worst fit for 8h of static IDE. |
| Samsung Odyssey OLED G6 | 25 989 | 240Hz OLED | yes | Same. |
| ASUS ROG Strix XG27AQDMGR Gen2 | 24 599 | 240Hz WOLED | yes | Same; better text than QD-OLED, still not RGB stripe. |
| Alienware AW2725DF | 30 596 | 360Hz QD-OLED | yes | Same, plus refresh you will not use. |
| ASUS ROG Swift PG27AQWP-W | 48 329 | 540Hz | yes | Absurd for this brief. |

## Evidence (revised after the deep review pass, 2026-09-09)

**AOC Q27G4ZR - measured, and the flaws are specific.** KitGuru scored it 9/10 at £179:
response 4.21 ms G2G in the "Faster" overdrive mode with "next to no overshoot", input lag
2.14 ms, brightness 66-450 nits, contrast ~1160:1, greyscale dE 1.11, gamut 123.7% sRGB /
95.1% DCI-P3. Club386's separate unit measured 1410:1 contrast, 545 nits, dE 0.52 out of the
box, and a fully adjustable stand (130 mm height, pivot, swivel, tilt). Factory calibration
is unusually good for the price.

Its real flaws:
- **No variable overdrive.** "Faster" is correct at 240Hz but overshoots at 120Hz and 60Hz,
  so you must drop to "Fast" manually when playing capped or slower games. This is the
  model's main weakness and the M27Q3 fixes it.
- **HDMI 2.0 only** - 1440p caps at 144Hz over HDMI. You must use DisplayPort for 240Hz.
- Effective refresh measures ~237Hz against the 260Hz OC claim.
- No USB hub, no KVM, 5-button OSD rather than a joystick.
- Club386's unit showed **IPS bleed on the left and bottom-left with 15-18% luminance
  deviation** - panel lottery is real here.
- HDR is DisplayHDR 400 with no local dimming: nominal only.

**GIGABYTE M27Q3 - the best-tuned panel of the group.** Monitors Unboxed measured 4.5 ms
average with **Smart OD variable overdrive holding up across the refresh range** (the thing
the AOC cannot do), contrast 1262:1, peak 434 nits, processing lag 0.3 ms, 96% DCI-P3, and
called it "one of the best-tuned 1440p LCDs on the market". It adds a KVM switch, USB-C with
power delivery, HDMI 2.1 and a fully adjustable stand. Weaknesses: HDR is nominal
(DisplayHDR 400, no dimming), the strobe mode is useless (artifacts, no better clarity than
native 320Hz), and no sRGB clamp is active by default with a slight red tint out of the box.

**The one thing to verify before buying the M27Q3:** its **subpixel layout is undocumented**,
and this panel family has history - the original M27Q used a Sharp panel with a **BGR**
subpixel order, which makes small text render with colour fringing on Windows, and a later
revision silently switched to Innolux panels. No reviewer states the M27Q3's layout.
Reviewers normally flag BGR, so silence is weak evidence of standard RGB - not proof. For a
machine that displays code all day this is the difference between a great buy and a daily
irritation. Check ClearType or a magnified photo of the panel before committing.

**Why the mini-LED recommendation is withdrawn.** The AOC Q27G3XMN is a **VA panel, not
IPS** - my earlier claim that it kept an RGB-stripe IPS panel was simply wrong. Worse, the
defect list is severe for an all-day work display:
- **RTINGS ranked it the worst VRR flicker of the 38 monitors it had tested**, describing it
  as "terrible". TFTCentral, by contrast, saw no flicker in dynamic content - the sources
  genuinely conflict, and owner reports land in between (flicker in static and dark uniform
  screens, two games needing VRR off entirely).
- **Coil whine audible at 60-70% brightness**, unit-dependent.
- **DDC/CI broken over DisplayPort** - roughly half of brightness commands ignored; it works
  over HDMI, which caps at 144Hz.
- The monitor drops off the bus when powered off, so Windows rearranges your windows.
- **No firmware updates are available**, so none of this gets fixed.
- Reports of dead subpixels and panel tinting lottery; viewing angles poor even for VA.
- Its HDR hardware is real (1365 nits measured, 336 zones) but the dimming *algorithm* is
  where it falls apart - haloing around subtitles and desktop UI, and aggregated owner
  reports describe SDR local dimming as erratic.

Its successor, the **AOC Q27G40XMN** (1152 zones, 1357 nits measured by Tom's Hardware),
fixes the zone count at a similar price - but it is **not listed on hotline.ua**, so it is
not currently buyable here, and it regresses to a **tilt-only stand**. It also still shows
VRR brightness flicker in some games.

- At 27", **1440p = 109 PPI and 4K = 163 PPI**. For code specifically, 109 PPI is the density
  where 100-125% scaling yields crisp pixel-aligned rendering across development tools, while
  4K at 27" demands 150% scaling, where Windows' text rendering can misalign glyphs and blur
  hinting. Reviewers who prefer 4K note it looks crisper *at 150% scaling* - both statements
  are true; the difference is whether you want to manage scaling.
- OLED text: QD-OLED's non-standard subpixel layout produces colour fringing on small text,
  and static UI elements are the burn-in scenario. This is a work machine with a fixed IDE
  layout on screen for hours.
- "DisplayHDR 400" panels have no local dimming; only mini-LED or OLED deliver HDR that
  looks like HDR.

## Verdict (revised)

> **Price note, 2026-09-12.** The figures in this section (9 551, 6 757) are the 2026-09-09
> hotline sweep. The named-shop pass of 2026-09-11 supersedes them: **Q27G4ZR 8 669 and
> Q27G4XF 6 899, both at Rozetka, both in stock** - see
> [../price_check.md](../price_check.md). The build table in
> [../../pc_build.md](../../pc_build.md) uses the newer numbers. **The pick itself does not
> change**, and neither does the 2 794-vs-1 770 gap's direction; only the amounts do.

**Buy the AOC Q27G4ZR, 240Hz Fast IPS, 9 551.** It survives the deep pass: two independent
reviews, genuinely good measured response and near-best-in-class factory calibration for the
money, a fully adjustable stand, and no serious defect beyond the manual-overdrive quirk and
the usual IPS bleed lottery. Use DisplayPort, set overdrive to "Faster", and drop it to
"Fast" if you ever play something locked at 60.

**Cheaper: AOC Q27G4XF at 6 757** (-2 794) - and note this replaces the GIGABYTE G27Q20 as
the budget pick, because unlike the Gigabyte it has actually been measured: 4.6 ms with only
**0.1% overshoot**, 1198:1, dE 1.4. You give up 60Hz of refresh and it is dim at 365 nits.

**Better but pricier: GIGABYTE M27Q3 at 13 169** (+3 618) - the best-tuned panel here, with
working variable overdrive across the whole refresh range, better contrast, a KVM switch and
USB-C power delivery that would let a laptop share the screen. **Conditional on verifying it
is RGB and not BGR subpixel order** - see the evidence above. If it is RGB, this is the buy.

**The 4K option is now stronger than I said: GIGABYTE M27UP at 16 999** (+7 448). The deep
pass found two credible reviews with good results (405 nits, 1280:1, PWM-free, competent
responses across the VRR range, full-bandwidth HDMI 2.1, hardware KVM button), plus a
dual-mode 1080p/320Hz escape hatch for competitive titles. At 163 PPI it is the best monitor
here *for reading code*, which is what you do most. The costs are real: it needs 150% Windows
scaling, it demands much more GPU at 4K, its HDR has zero dimming zones, and the dual-mode
switch is clunky. **If you tell me text quality outranks frame rate, this becomes my
recommendation and I will re-cost the build around it.**

**Withdrawn: the mini-LED AOC Q27G3XMN.** I recommended it as "real HDR with an IPS panel
for text". It is VA, it has the worst VRR flicker RTINGS had measured at the time, coil
whine, broken DDC/CI over DisplayPort, and no firmware support. That was my worst call in
the first pass.

**Also withdrawn: GIGABYTE G27Q20 and ASUS TUF VG27AQ5A** - no credible measurements exist
for either, and the ASUS has no height adjustment at all.

**On OLED:** unchanged. The right time to buy one is as a *second* monitor for games only.

**On OLED:** the right time to buy one is as a *second* monitor for games only, once this
machine exists. Not as the single all-day display.


## Price movement and build assignment (2026-09-10)

The Q27G4ZR has **fallen**: hotline now shows it from **9 233** against the 9 551 recorded above.
It is **out of stock at Telemart**, and Rozetka appears to be near 8 658 (unverified - Rozetka
returns HTTP 403 to automated requests). Monitors are the one category in this build where the
price moved in the right direction.

**Assigned:** Q27G4ZR to the Working and Max builds; the **Q27G4XF at 6 757** to Lean, where the
2 794 saving is part of what makes that build a genuinely different machine rather than the same
one with a cheaper card.

## Cross-check against six monitor guides (2026-09-11)

Sources: **RTINGS *How to Buy The Right Gaming Monitor*** (2026-05 - the only lab among them),
ECPU *How to Choose a Monitor in 2026* (2026-03), Aman *If You're About to Buy a Monitor*
(2026-04), The Tech Chap (2023), JayzTwoCents (2024-12), MikMat Tech (2022).

**4K is refused.** Dmytro, 2026-09-11: "no 4K, nope, not happening." The M27UP line in the
Verdict above is therefore closed, and the PPI argument these videos make for work use - Aman:
pixel density "way more important for work than something like refresh rate" - is noted and
overruled by the owner. **Do not reopen it.**

### Corrections to this document

**1. "Dim at 365 nits" overstates it - but so did this correction, and the two are reconciled
here (2026-09-13).** RTINGS' stated threshold is that **monitors brighter than 300-350 nits are
good enough for most well-lit rooms**, so the Q27G4XF's measured **365 nits is above that line**.
But Aman, also among the six, treats **350 as a floor rather than a comfort point** - *"anything
below that is basically cheap office-level brightness that feels just dim"* - and sets **500 nits
as the minimum for a bright room or a desk near a window**.

**The synthesis: 365 nits clears the bar for a controlled room and does not clear it for a bright
one.** That is what the criteria table above means by "under ~400 nits is noticeably dim in a
bright room", and the two statements no longer contradict each other. For a desk-bound work
machine indoors this is adequate; it is not headroom.

**2. Single response-time figures are not how the best lab measures motion.** RTINGS uses
**CAD (cumulative absolute deviation)** across 72 grey-to-grey transitions in every overdrive
mode - "the best LCDs struggle to have a CAD lower than 100" against OLED's under 15. The
"4.6 ms G2G, 0.1% overshoot" quoted for the Q27G4XF comes from DisplaysTested and is a good
sign, but it is one transition set, not CAD. **Neither AOC has an RTINGS review**, so no CAD
figure exists for either - consistent with what this document already says about cheap 1440p
panels being under-measured.

**3. Input lag has a floor, and ours clears it.** RTINGS: a 240Hz panel cannot measure below
~2.08 ms, and "anything under 3-4 ms is great". The Q27G4XF's **2.7 ms** is inside that band.

### The question this pass actually opens: 240Hz or 180Hz on Working and Max

**Four of the six say the same thing about high refresh rates, one says the opposite, and one is
silent** (corrected 2026-09-13 - this previously read "every source"):

- **RTINGS:** diminishing returns - "you'll notice a bigger change between 120 and 240 Hz than
  between 240 and 360 Hz", and the frame rate has to be there to use it.
- **Aman:** for work "60 Hz or even 120 Hz is completely fine... higher refresh rates don't
  really make a difference in most work apps". His rule is to match the panel to your actual
  frame rate: *"if your system can't reach those numbers, then there's no reason to spend extra."*
  (The "only really matters if you're playing at a high competitive level" line quoted here
  before is his, but it is about **response time**, not refresh rate.)
- **The Tech Chap:** *"I think 144 or 165 Hertz is The Sweet Spot"*, and his closing
  recommendation is *"a 27 inch 1440p 165hz IPS or VA is absolutely ideal"* - the Q27G4XF exactly.
- **JayzTwoCents:** his sweet spot is *"27 in 1440p resolution 144 HZ refresh rate with a 1
  millisecond response time"*.
- **ECPU dissents:** *"240 Hz is the sweet spot for high-end and competitive gaming"*, and his
  all-round recommendation is **144-240 Hz** at 1440p/27".
- **MikMat Tech** does not address it, and is a 2022 video whose OLED and TN claims are obsolete.

| | AOC Q27G4XF | AOC Q27G4ZR |
|---|---|---|
| Price | **6 757** | **9 233** |
| Refresh | 180Hz Fast IPS | 240Hz (260 OC) Fast IPS |
| Measured by | DisplaysTested | KitGuru (9/10), Club386 |
| Brightness | 365 nits | - |
| Stock | - | **out of stock at Telemart** |

The gap is **+2 476 for 60Hz** on a machine that spends most of its hours in an IDE, driven by a
9070 GRE that will not hold 240 fps in modern titles at 1440p anyway. Both are the same panel
family, both measured, both with adjustable stands. **Putting the Q27G4XF in all three builds
saves 2 476 per build** and costs refresh headroom that only competitive play would use.

This is a preference, not an error - the 240Hz pick is defensible and nothing new contradicts
its measurements. But it is now the single largest unforced spend left in the Working and Max
builds, and the assigned unit is out of stock at the shop that would assemble it.

### Confirmed, no action

- **OLED is wrong for this brief** - Aman: "not great for working with text because of colour
  fringing", and ECPU warns of "text clarity issues depending on their specific subpixel layout,
  making them kind of annoying for office type work". This is the same reasoning this document
  already uses to keep OLED as a games-only second screen, and the same reason the **M27Q3's
  RGB-vs-BGR subpixel order still has to be verified** before paying its 13 169.
- **IPS contrast is low and that is inherent** (RTINGS); VA has better contrast but smears;
  mini-LED is the LCD answer for dark rooms. All already reflected above, including the
  withdrawal of the mini-LED VA panel.
- **Matte vs glossy coating** and VRR flicker vary per unit and must come from reviews, not spec
  sheets - which is what this document already does.

## Stock check (2026-09-11): out at the two assemblers, widely available elsewhere

Found while frame-checking the guide videos, then verified market-wide.

| Model | Telemart | Brain | **Rest of the market (hotline)** |
|---|---|---|---|
| **AOC Q27G4ZR** (Working + Max) | Немає в наявності | Немає в наявності, 9 998 listed | **12 offers, 9 687 - 11 651** |
| **AOC Q27G4XF** (Lean) | Немає в наявності | Немає в наявності, 7 820 listed | **9 offers, 6 757 - 8 565** |

**Correction to a first reading of this: neither monitor is scarce.** Both are stocked by a
dozen shops between them - Сенюшко, DENIKA.UA, TehnoExpert, Redprice, Сафік, WOX, Tomdom,
TimeSport, AT-shop, Semtech. What is true is narrower: **neither is available from Brain or
Telemart**, the two stores that could assemble the machine.

**And that does not matter for a monitor.** The single-store constraint in
[../../pc_build.md](../../pc_build.md) exists because *the machine* has to be assembled and
warranted by one shop - it binds the parts that go inside the case. A monitor is a peripheral:
it is plugged in, not built in, and it carries its own manufacturer warranty (3 years on the
Q27G4ZR per Telemart's own listing). **It can be bought from any shop, and the same is true of
the keyboard, mouse and desk.**

**So the picks stand.** The only real change is price: the Q27G4ZR floor has risen from 9 233 to
**9 687** (+454), while the Q27G4XF is unchanged at **6 757**. Budget the higher figure.

**What the two assemblers do have**, kept only as fallbacks if buying the monitor separately
turns out to be unwelcome (none checked against this document's criteria):

| Model | Price | Panel | Note |
|---|---:|---|---|
| AOC **Q27G42XNE** | **7 508** | VA 180Hz | cheapest; VA, so smearing is the question |
| AOC **Q27G42ZE** | **8 982** | **IPS 260Hz** | marked «Закінчується» - running low |
| GIGABYTE **M27Q3** | 13 176 | IPS 300Hz | already the "better but pricier" pick above; **still needs the RGB/BGR subpixel check** |
| AOC Q27G4SRU | 15 519 | IPS 320Hz | unassessed |
| AOC **Q27G3XMN** | 14 304 | mini-LED VA | **the model this document withdrew** - see the evidence section |

Of these the **AOC Q27G42ZE at 8 982** would be the one to check first - same family, IPS,
260Hz, priced between the two originals - but on the reasoning above **no substitution is
needed**, so no measurement search has been run for it.

### A lead the transcripts did not contain: AOC Q27G40XMN

RTINGS' video shows an on-screen scorecard - **AOC Q27G40XMN, Local Dimming 8.0** - that is
spoken nowhere in the audio and would have been missed by a transcript-only pass. This is the
**successor to the Q27G3XMN this document withdrew**, and it fixes the specific defect that got
its predecessor withdrawn: **1 152 dimming zones against 336**, contrast over **33 000:1** with
dimming on, HDR1000, quantum-dot film, 180Hz. Reviewed by Tom's Hardware, TechSpot and RTINGS -
far better measured than anything else in this price class.

**Two reasons it is still not the pick:** it remains a **VA panel** (the transcript-level
objection to the G3XMN was partly that it is VA, not IPS, and VA smears), it still shows VRR
brightness flicker in some titles, and - decisively - **neither Telemart nor Brain stocks it.**
Recorded so the next pass does not have to rediscover it.

### 180Hz vs 240Hz: what the 2 930 actually buys (checked 2026-09-11)

Dmytro's rule, restated: **the three builds must differ from each other** - a single monitor
across all three is not an option, regardless of value. So the question is only what the step
from the Lean panel to the Working/Max panel is worth.

**Refresh rate.** Frame time goes from **5.6 ms to 4.2 ms** - about 1.4 ms. The jump everyone
remembers, 60 to 144Hz, is **16 ms to 7 ms**; 144 to 240 is 7 ms to 4 ms, and this step is
smaller still. In a blind side-by-side reported on the Blur Busters forums a subject identified
the 240Hz panel **about 60% of the time - barely above chance**. The consensus phrasing is
"noticeable to experts, imperceptible to many".

**And the frames have to exist to use it.** A 9070 GRE at 1440p runs modern titles well under
180 fps; only esports titles clear 240. For eight hours of IDE work the refresh difference is
**zero**.

**What is not zero:** the panels differ in more than hertz.

| | Q27G4XF | Q27G4ZR |
|---|---|---|
| Rated brightness | **300** cd/m² (measured 365) | **400** cd/m² |
| Rated response | 0.5 ms | 0.3 ms |
| Extras | - | speakers, more ports |

**The brightness is the part that will actually be noticed while working** in a lit room - more
so than the 60Hz. Worth recording plainly: the Q27G4ZR is defensible on this build, but it earns
its 2 930 on panel quality, not on the number in its marketing.

## DECISION (2026-09-11): both monitors confirmed, question closed

**Lean: AOC Q27G4XF, 6 757. Working + Max: AOC Q27G4ZR, 9 687** (the floor rose 454 from the
9 233 recorded above - budget the new figure).

Settled with the evidence above: the 4K path is refused, the tiers must differ, and the
Q27G4ZR's 2 930 is accepted as buying panel quality (400 cd/m2 against 300, 0.3 ms against
0.5 ms) rather than the 60Hz of refresh, which is near-imperceptible and unreachable on a
9070 GRE outside esports titles.

**Buy the monitor from any shop.** Neither is stocked at Brain or Telemart, both are stocked by
a dozen others, and a monitor is a peripheral rather than a part that gets assembled into the
machine - the single-store constraint does not reach it. Same for keyboard, mouse and desk.

## The click.ua listing, re-read 2026-09-13 by the source audit

Dmytro sent the listing with *"did you do proper research? … there are measurements on the same
bloody site, did you bother to open them?"* **He was right that there are.** The page was read
again over verified TLS; **the decision is closed and nothing here reopens it.**

**Everything this file states is confirmed.** *"Монітор ASGARD Gaming 27" AS275QC VA Black Curved
200Hz"*, **8 599 ₴ → 6 999 ₴**, *"В наявності"* — the price has not moved and it is still in stock.
VA, WQHD 2560×1440, 200 Hz, 1 ms, curved. *"Регулювання по висоті: **відсутнє**"* — no height
adjustment, as recorded. And the single review this file called thin but real is still the only
one: Антон, 2026-07-28, *"Хорошее четкое изображение, плавная картинка без рывков в динамичных
играх"*.

**Three specifications on that page are not in this file:**

| | |
|---|---|
| **Brightness** | **300 cd/m²** — dimmer than the AOC Q27G4ZR's measured 365-434 nits recorded above, and low for a bright room |
| **Contrast** | **5000:1** — the VA advantage over the IPS alternatives' ~1200:1, and the reason blacks look better on this panel |
| **Inputs** | **2 × HDMI and 2 × DisplayPort** — four inputs, where the AOC has one DisplayPort. *(Relevant to [../peripherals/laptop_display.md](../peripherals/laptop_display.md): a spare input is how a laptop shares the desk screen.)* |
| Also | 2 × 2 W speakers, AMD FreeSync and Nvidia G-Sync |

**None of this changes the pick**, which was Dmytro's on stated criteria. It is recorded because
the file argued the monitor without ever quoting the numbers on the page he pointed at.

## Every video behind this document

**Added 2026-09-13 by the source audit.** This file named its videos by channel and year only — **no id, no link** — which is the exact complaint the audit was started over: *"the docs were found to cite videos by channel name with no ID and no timestamp, leaving nothing Dmytro could re-check."* 6 of the 6 monitor videos could not be traced from this page at all. The full set, with the transcript on disk and the quote-by-quote record in [source_audit.md](../source_audit.md):

| Video | Channel | Date | Title |
|---|---|---|---|
| [`6F0iI_OxU9E`](https://www.youtube.com/watch?v=6F0iI_OxU9E) | Aman | 2026-04-06 | If You’re About to Buy a Monitor, Watch This First |
| [`2adjvq793Dc`](https://www.youtube.com/watch?v=2adjvq793Dc) | ECPU | 2026-03-26 | How to Choose a Monitor in 2026 |
| [`mtA4hqZb4IE`](https://www.youtube.com/watch?v=mtA4hqZb4IE) | JayzTwoCents | 2024-12-31 | Ultimate Gaming Monitor Guide: Find the BEST Screen for Your Setup |
| [`yKvj63oG7D0`](https://www.youtube.com/watch?v=yKvj63oG7D0) | MikMat Tech | 2022-04-15 | You Bought The WRONG Monitor! (Monitor Panels Explained) |
| [`u2VbWEKHCWU`](https://www.youtube.com/watch?v=u2VbWEKHCWU) | RTINGS Computer | 2026-05-26 | How to Buy The Right Gaming Monitor (For Your Needs) |
| [`ptUchraop3c`](https://www.youtube.com/watch?v=ptUchraop3c) | The Tech Chap | 2023-05-20 | Monitor Buying Guide - What You NEED to Know! |

