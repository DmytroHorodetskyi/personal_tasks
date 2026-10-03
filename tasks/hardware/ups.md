# UPS (ДБЖ) for the desktop build

Opened 2026-09-14, when Dmytro sent a click.ua listing for an **nJoy Horus Plus 1500** and asked
what it was worth. No UPS had been specified for this build before.

## What a UPS does here, in one line

It is a battery between the wall and the PC. On an outage it holds the machine up long enough to
**save and shut down cleanly** — it is not a way to keep working through a blackout, and nothing
at this price is.

## The characteristics that matter

| # | Spec (unit) | What it means, plainly |
|---|---|---|
| 1 | **Output waveform on battery** | **The one that disqualifies units.** "Pure sine" reproduces mains; "simulated / stepped sine" is a squared-off approximation. Modern PC power supplies use **active PFC**, which can fail to recognise a stepped wave — see below. |
| 2 | **Real watts (W), not VA** | The box leads with VA. A 1500 VA unit is typically **900–1200 W**. Size against **W**, never VA. |
| 3 | **Load as a fraction of rated W** | Runtime collapses non-linearly. 50 % load gives roughly 4× the runtime of 100 % load, not 2×. |
| 4 | **Transfer time (ms)** | How long the output is dead during the switch to battery. Under ~10 ms an ATX PSU rides it out on its own capacitors. |
| 5 | **Battery included?** | Some "sinusoidal" units at tempting prices ship **without batteries** — they are designed for external banks. |
| 6 | **Sockets** | Schuko (євро) vs IEC. IEC-only means buying cables. |

## What this machine actually draws

*(Revised 2026-09-30. The earlier version used psu.md's figures as if they were drawn at the wall.
They are what the parts draw from the PSU, on its DC side. The wall draw is higher by the PSU's
losses, ÷ ~0.9 for a Gold unit. It also sized only for Max, which is not being built.)*

The ordered build is **Working at click.ua**: Ryzen 7 9700X, Sapphire RX 9070 PURE, Cougar GEX X2
850 ([click_basket.md](pc_build/click_basket.md)). Max is kept only as upgrade headroom.

| | Ordered: **Working** | Max (not built) |
|---|---:|---:|
| CPU, AMD PPT | 88 W | 88 W |
| GPU | **247 W** (9070 PURE, ComputerBase measured; 220 W TBP) | 310–330 W (9070 XT limit, psu.md) |
| Board, RAM, SSD, fans, USB | ~65 W | ~65 W |
| **PC, DC side** | **~400 W** | 463–483 W |
| At the wall, ÷ 0.9 | ~445 W | ~515–535 W |
| + monitor (~30 W, unsourced estimate) | **~475 W** | **~545–565 W** |

GPU transients add ~13% of card power for microseconds (psu.md, Igor's Lab): **~30 W** on the
PURE, ~45 W on an XT. They need headroom in the UPS rating, not capacity.

## The minimum wattage to shop by

Sizing is on **active watts (Вт)**, never VA. Only a clean shutdown is needed, not runtime.

| Rated W of the UPS | Ordered build (~475 W) | Max (~555 W) | Verdict |
|---:|---:|---:|---|
| 360 W | 132 % | 154 % | overload — trips at transfer (the Horus Plus 600) |
| 600 W | 79 % | 93 % | carries today's build; no margin for transients, battery ageing or a bigger GPU |
| **700 W** | **68 %** | **79 %** | **the floor** |
| 800 W | 59 % | 69 % | Echo Pro 1000 |
| 900 W | 53 % | 62 % | Horus Plus 1500 |
| 1200 W | 40 % | 46 % | Powercom SPT-1500-II |

**Floor: 700 W.** Anything above it buys headroom for a future bigger GPU, not required runtime.
Three reasons not to go below it: the ~30–45 W GPU transients; a battery that loses capacity with
age while the shutdown still has to complete; and the overload failures in the video batch below,
which were the failure actually seen on camera.

In VA terms, cheap units run a 0.6 power factor, so **1200 VA ≈ 700 W** and **1500 VA ≈ 900 W** —
but always read the Вт figure off the listing rather than converting. Better units (APC, Powercom
SPT) run 0.7–0.8, so their VA number understates them.

## The unit he asked about

**nJoy Horus Plus 1500 (PWUP-LI150H1-AZ01B)** — [click.ua, 6 399 ₴, in stock, 2026-09-14](https://click.ua/shop/dzherelo-bezperebiynogo-zhivlennya-njoy-horus-plus-1500-left-parenthesispwupminusli150h1minusaz01bright-parenthesis-lindotintdotcomma-avrcomma-4-x-evrocomma-usbcomma-lcdcomma-plastik-p45978).
Telemart the same 6 399, in stock. hotline shows 15 sellers advertising 5 573 – 6 398; COMFY's
5 573 is the usual cheapest-of-fifteen and was not stock-checked.

| Spec | Value |
|---|---|
| Rating | **1500 VA / 900 W** |
| Topology | line-interactive, AVR, microprocessor, LCD |
| **Output waveform** | **simulated sine wave** |
| Transfer time | 2–6 ms |
| Runtime (maker's own figures) | 19 min @ 25 % · **7.5 min @ 50 %** · 4 min @ 75 % · <2 min @ 100 % |
| Recharge | 4–6 h to 90 % |
| Sockets | 4 × Schuko, USB, cold start |

Specs from [nJoy's own datasheet](https://cdn.njoy.global/hive_files/wp/products/16167712072zx2Zd.pdf).

**On watts it is correctly sized.** ~475 W on a 900 W unit is ~53 %. The maker's own 50 % row gives
**7.5 minutes**, which is ample to save and shut down.

## The problem: simulated sine wave against an active-PFC PSU

The build's PSU is a **Cougar GEX X2 850** (settled 2026-09-13 at click.ua, see
[click_basket.md](pc_build/click_basket.md)), an ATX 3.x unit — like every modern PSU, active PFC.
The first pass rested on one vendor note; the cross-check is in the next section. CyberPower
states it in its own technical note:

> "Simulated sine wave power ... momentarily creates a zero power gap. When power is interrupted, a
> computer with an Active PFC power supply may not recognize incoming simulated sine wave power due
> to the zero output present in the approximated wave."
> — [CyberPower, *Active Power Factor Correction Supplies for IT Equipment*](https://www.cyberpowersystems.com/feature_focus/active-power-factor-correction-supplies-for-it-equipment/)

The failure mode is the one that defeats the purpose: at the moment of transfer the PSU may buzz
loudly, shut down, or trip the UPS into an error — **so the machine dies on the outage the UPS was
bought to survive**.

**Stated honestly: it is a risk, not a certainty.** Plenty of active-PFC PSUs run on stepped-sine
units for years without incident, and it cannot be predicted from the spec sheets — it depends on
the particular PSU's undervoltage detection. But it can only be discovered by having a blackout,
which is a bad way to find out, and a UPS is the one component in the build whose entire job is
not being a gamble.

## Cross-check of the pure-sine requirement, 2026-09-30

Opened because the section above rested on **one** source, CyberPower, which sells pure-sine
UPSes. Goal: find out whether the risk is real, how often it bites, and whether anything covers
this PSU.

| Source | Kind | Read | Verbatim quote | Bearing |
|---|---|---|---|---|
| [Seasonic knowledge base](https://knowledge.seasonic.com/article/7-what-type-of-ups-does-seasonic-recommend) | **PSU maker** | full (2 sentences) | "Seasonic recommends a UPS with a pure sinewave output; however, a high quality simulated sinewave UPS from a reputable manufacturer could also be a possible solution" | Prefers pure sine but doesn't rule out a good stepped unit |
| [Intel, UPS FAQ for server boards](https://www.intel.com/content/www/us/en/support/articles/000006100/server-products.html) | System maker, **sells no UPSes** | full | "Unpredictable results may occur using UPS devices that use a simulated sine wave output, or a stepped approximation." | Confirms the risk, independently of any UPS seller |
| [LTT Labs, *Sine Waves and Spec. Sheets*, 2026-09-10](https://www.lttlabs.com/articles/2026/09/10/ups-considerations) | **Independent lab**, oscilloscope | full | "Modified sine waves are easier to implement and are 'good enough' for most equipment" · "testing a few 450-650 W loads on a Seasonic Prime TX-1300 … we didn't hear any buzzing, but this could vary with lower capacity or less expensive power supplies" | The only hands-on test found: **one** premium PSU, no failure. It only checked for buzzing, not for shutdowns across many PSUs. Its own recommended UPS is pure sine (BR1500MS2). |
| [hwbusters, Pure Power 13 M 750W, p. 6](https://hwbusters.com/psus/be-quiet-pure-power-13-m-750w-atx-v3-1-psu-review/6/) | Lab review of **this PSU** | page 6 | "The hold-up time is close to 19 ms, and the power OK signal is accurate." | Rides through the 2–6 ms transfer of both nJoy units several times over. That covers the transfer gap, not the waveform question. |
| [CyberPower tech note](https://www.cyberpowersystems.com/feature_focus/active-power-factor-correction-supplies-for-it-equipment/) | UPS maker, sells pure sine | quoted above | "may not recognize incoming simulated sine wave power" | The original source; still self-interested |
| Dave's Garage `JL71IH5HShI` @ 12:41 ([sources/](pc_build/sources/ups_JL71IH5HShI.md)) | Video | transcript, prior audit | "you want to look for a UPS that has what is known as a sine wave inverter" | Pro pure sine; the argument is about square waves and doesn't mention PFC |
| MOYO `fiKra9BXqoA` @ 3:21 ([sources/](pc_build/sources/ups_fiKra9BXqoA.md)) | Retailer video | transcript, prior audit | "in a computer there is a power supply which still converts alternating voltage into constant and for it it is no longer critical" | **Contra**: says stepped sine is fine for a PC; doesn't consider active PFC |
| E-Katalog `gFCOowZV3Cw` @ 3:21 ([sources/](pc_build/sources/ups_gFCOowZV3Cw.md)) | Catalogue video | transcript, prior audit | stepped sine "is something more about computers and devices with pulsed power supply" | **Contra**: same view, same omission |
| APC staff posts, community.se.com | UPS maker | **not read**: forum "closed for maintenance" 2026-09-30, archive.org blocked | — | A search summary attributes to APC staff that post-2008 Back-UPS units "handle most (not all) PFC loads". That is unverified, so nothing here rests on it. |

Forum anecdotes (Tom's Hardware, TrueNAS, techenclave, Linus Tech Tips) turned up in search in
both directions and were **not read**. Searches found no PSU-by-PSU shutdown test.

**What this establishes**

1. **The mechanism is real, not marketing.** A PSU maker (Seasonic) and a system maker that sells
   no UPSes (Intel) both acknowledge it. Every primary source says "may" or "unpredictable";
   none says it will happen.
2. **How often it happens is unknown.** Only one hands-on test was found, with one PSU, and it
   showed no problem. The two Ukrainian retail videos that call stepped sine fine for a PC never
   consider active PFC.
3. **Nothing covers this PSU.** be quiet! publishes no UPS guidance that search could find. The
   ~19 ms hold-up rules out the *transfer-gap* failure (a reboot on the switch). It says nothing
   about whether the PFC stage accepts a stepped wave.

**Effect on the decision:** it doesn't overturn it, but it downgrades the claim. "Documented
incompatibility" becomes **"a recognised risk that nobody has measured for this PSU."** Pure
sine stays the safe buy. The alternative is to **test it**: buy the Horus Plus 1500
(6 399 ₴), then pull its plug with the PC under a gaming load, several times, inside the return
window. If the PC stays up without buzzing, the 5 000 ₴ saving is real. *(My inference, not a
sourced claim: a pulled plug reproduces the exact transfer a blackout causes.)*

## The 12-video batch, 2026-09-30

Dmytro sent 12 videos to check. **All 12 transcripts were read in full**:
`audit_tools/coverage.py --missing <id>` reports "fully covered" for each one. **Frames were checked
for all 12**, as 2×2 contact sheets with one frame every 20 s, plus full-resolution grabs where a
sheet showed data. Transcripts are in [pc_build/sources/](pc_build/sources/) as `ups_<id>.md`;
full-resolution grabs are in `pc_build/frames/`. Two videos have only Ukrainian auto-captions
(`t2KTsxX5sUQ`, `xbTqJinXcYU`), fetched with `--lang uk`.

| Video | Chars read / total | Verbatim quote | Bearing on the decision |
|---|---:|---|---|
| Geerling Eng. `ovZAbCqh_A0` | 11 167 / 11 167 | @4:25 "you want clean sine wave power … for a lot of equipment you're going to be fine with any of them" | Prefers sine, not a hard rule. On-screen caption @2:40–3:40: **"50-70% load max"** |
| Dave's Garage `JL71IH5HShI` | 27 453 / 27 453 | @12:41 "you want to look for a UPS that has what is known as a sine wave inverter" | Pro sine, but argued against *square* waves; PFC never mentioned. Frame @8:00–9:00: APC display **"Load:101%"** with an RTX 4080 at 100% → overload alarm |
| Tech Overwrite `2TTzck8j3bE` | 15 651 / 15 651 | @5:00 "gracefully turns off after 2 minutes" | Waveform not mentioned. Frame of APC's own spec page: Back-UPS 850, **520 W, "2min 17s" at 520 W** (full load) |
| DoItForMe `F4MCSbmHmLQ` | 35 269 / 35 269 | @16:21 "Look for a UPS that clearly states it produces pure sinewave AC output" | Pro sine: computers "may not tolerate the ragged step". Slide: **"Graceful shutdown: 10 to 15 minutes"**. Sponsored (GoldenMate, pure sine, spec **"Conversion Time ≤20ms"**) |
| Venom's Tech `FToZpH9WH84` | 9 303 / 9 303 | @6:07 "They claim that they will handle around 600W load. But it couldn't carry the load of 430W" | **The only live test of a gaming PC on cheap units**: 13600K + 3060 system, 435 W with monitor (wattmeter frame 372.9 W PC). 600/650 VA overloaded; Luminous 1000 VA overloaded; APC BX1100C ran **2:40, then overloaded**. Spec-table frame @2:55: all five line-interactive, transfer 8–13 ms, **waveform not listed**. Every failure was overload, none attributed to waveform |
| ShortCircuit `cxkoAmJJbAo` | 8 212 / 8 212 | @1:07 "it is a pure sine wave unit that means it tends to be more reliable and efficient and transition more seamlessly" | Eaton-sponsored. Pulled the plug under Cyberpunk load: PC stayed up, on a **pure-sine** unit. No stepped comparison |
| MOYO `fiKra9BXqoA` | 9 587 / 9 587 | @3:21 "in a computer there is a power supply which still converts alternating voltage into constant and for it it is no longer critical" | **Contra**: stepped is fine for a PC. PFC never considered |
| Казімір `hebLFKBSEd4` | 4 328 / 4 328 | @3:33 "I will look for a device with a power mainly in the range of 700-800 W" | Wattmeter frames: i7-14700KF + RTX 4080 **peak 582.4 W, PF 0.93**. Waveform not discussed |
| Інструмент Центр `NyfoqRIFg4k` | 14 430 / 14 430 | @5:15 "for some devices, a pure sine wave is simply a necessity. These include medical equipment, audio and video equipment, servers" | Pro sine for servers; PCs not named either way. Line-interactive "2 to 8 ms" (caption frame) |
| E-Katalog `gFCOowZV3Cw` | 11 140 / 11 140 | @3:21 stepped sine "is something more about computers and devices with pulsed power supply" | **Contra**: stepped suits computers. Switching "no more than 5 ms". Catalogue tooltip frame: active W "приблизно 0,6" of VA |
| ВольтМаркет `t2KTsxX5sUQ` | 4 883 / 4 883 | @2:15 «наскрізний ноль … котел буде запалювати газову горілку тільки тоді коли буде бачити підключений нульовий провідник» | **Not applicable**: how to test a UPS for a gas boiler (neutral pass-through, phasing). Nothing on PCs or waveform |
| electro100 `xbTqJinXcYU` | 4 663 / 4 663 | @4:26 «офлайн-тип - це виключно для стаціонарного комп'ютера для того щоб завершити роботу зберегти проект» | Offline type is for saving work and shutting down a PC; claims line-interactive "має … чисту синусоїду" as a rule, which the nJoy Horus (line-interactive, stepped) contradicts |

**What the batch adds**

1. **None of the 12 tests the question that matters.** Nobody runs an active-PFC PSU on a
   stepped-sine unit and reports whether it survives. The split is the same as before: three
   Western videos lean pure sine (one of them sponsored by a pure-sine maker), and two Ukrainian
   retail videos say stepped is fine for a PC. None of them mentions active PFC. **The decision
   stands as written above: recognised risk, unmeasured for this PSU.**
2. **Overload, not waveform, is the failure that actually shows up on camera.** Venom's Tech
   killed four of five cheap units with a ~435 W PC, including a "1000 VA / 600 W" one, and
   Dave's 1500 VA APC hit 101%. That supports the **700 W real-watt floor** for this ~475 W load (the ordered build, at the wall).
   A unit's VA label is not a load rating.
3. **Казімір's measured 582 W peak** (14700KF + 4080) measured at the wall, is a real-world check on this
   doc's wall estimates: ~475 W for the ordered build and ~545–565 W for Max. That PC has a
   heavier CPU and GPU than either, so the estimates are plausible. It does not change the floor.
4. **Transfer times in the batch (2–13 ms) are all inside the PSU's ~19 ms hold-up**, so the
   switch-over gap is not the risk. That matches the earlier finding.

## The smaller sibling he asked about next: Horus Plus 600

**nJoy Horus Plus 600 (PWUP-LI060H1-AZ01B)** — [click.ua, 2 899 ₴, в наявності, price stamped
"актуальна на 14.09.26" on the listing](https://click.ua/shop/dzherelo-bezperebiynogo-zhivlennya-njoy-horus-plus-600-left-parenthesispwupminusli060h1minusaz01bright-parenthesis-lindotintdotcomma-avrcomma-2-x-evrocomma-usbcomma-lcdcomma-plastik-p45975).

| Spec | Value (from the click.ua characteristics table) |
|---|---|
| Rating | **600 VA / 360 Вт** |
| Topology | лінійно-інтерактивний, AVR, LCD, USB |
| **Output waveform** | **«апроксимована (ступінчаста) синусоїда»** — stepped, same as the 1500 |
| Transfer time | 2–6 мс |
| Runtime @ 50 % load (180 W) | 7 хв |
| Sockets | 2 × Schuko |
| Size / weight | 101 × 142 × 300 мм · 4.35 кг · 24 міс warranty |

It fails on **two** counts, not one:

1. **Same stepped-sine waveform** as the 1500 — the whole Horus Plus series is stepped. The
   active-PFC objection above applies unchanged.
2. **Undersized.** The ordered build draws **~475 W at the wall**; the unit is rated **360 W**.
   That is ~132 % of rating, so it does not "give a short runtime" — it **overloads and cuts out at
   the moment of transfer**. This unit is
   sized for a router, a NAS or an office PC, not for a 850 W-PSU gaming machine.

Nothing in it changes the decision below; it is the 1500's disqualifier plus a wattage one.

## Pure-sine alternatives, priced 2026-09-14

| Model | VA / W | Waveform | Price, shop | Stock |
|---|---|---|---:|---|
| **nJoy Horus Plus 600** (asked about) | 600 / **360** | **simulated** — and under-rated for this PC | **2 899 click.ua** | in stock |
| **nJoy Horus Plus 1500** (asked about) | 1500 / **900** | **simulated** | **6 399 click.ua** | in stock |
| **Powercom SPT-1500-II LCD** | 1500 / **1200** | **pure sine** | **12 375 Foxtrot** | in stock |
| APC Back-UPS Pro BR1200**SI** | 1200 / 720 | **pure sine** | 23 899 ITbox / 23 900 Telemart | in stock |
| APC Back-UPS Pro BR1600**SI** | 1600 / 1000 | **pure sine** | 31 500 Foxtrot | in stock |
| APC Back-UPS Pro BR1600**MI** | 1600 / 960 | **stepped** — the cheap lookalike | 21 880 Telemart / Brain / ITbox | in stock |
| Powercom INF-1500 | 1500 / 1000 | pure sine **but batteries NOT included** | 8 999 Foxtrot | in stock |

**Two traps in that table.** APC's **SI** suffix means Sinewave and **MI** does not — BR1600MI at
21 880 is 10 000 cheaper than BR1600SI and is *stepped*, so the cheaper APC solves nothing. And
Powercom's **INF-1500 at 8 999 ships with no batteries** ([Powercom](https://www.upspowercom.com/UPS-INF.jsp) —
designed for an external bank), so its real cost is well above the Powercom SPT.

~~**click.ua stocks neither pure-sine option.**~~ **Wrong — corrected below.** That was written from
the price script's model list rather than from click.ua's own catalogue. The shop stocks 28
pure-sine units; see the sweep.

## What click.ua actually stocks: the full pure-sine sweep, 2026-09-14

The earlier "click.ua stocks neither pure-sine option" line was written from the price script's
model list, not from the shop's own catalogue, and it was wrong. The category filter
[«Форма вихідного сигналу → правильна (чиста) синусоїда»](https://click.ua/shop/istochniki-bespereboynogo-pitaniya-ibp/328=pravilnaya-sinusoida)
returns **28 units, all listed in stock**. Every one was opened and its characteristics table
read; below are all of them that clear **700 W**, plus the traps.

| Model | VA / W | Topology | Battery | Schuko | Price, click.ua |
|---|---|---|---|---|---:|
| **NJOY Echo Pro 1000** (UPOL-OL100EP-CG01B) | 1000 / **800** | on-line | **2 × 7 Ah internal** | **3** | **11 399** |
| EnerGenie EG-UPSO-1000 | 1000 / 900 | on-line | internal | **1 only** | 11 999 |
| EnerGenie EG-UPS-PS3000-01 | 3000 / 2400 | line-int. | 4 | 0 (4 × IEC) | 16 999 |
| Eaton 5E G2 2200 (5E2200UI) | 2200 / 1200 | line-int. | 2 internal | 0 (6 × C13) | 17 474 |
| EnerGenie EG-UPSRACK-13 | 3000 / 2400 | line-int. | 4 | 1 | 18 999 |
| EnerGenie EG-UPSO-2000 | 2000 / 1800 | on-line | 6 | 2 | 21 005 |
| **APC Back-UPS Pro Gaming BGM2200B-GR** | 2200 / **1320** | line-int. | internal | **4** (+2 × C13) | **28 855** |
| NJOY Aten Pro 3000 | 3000 / 2700 | on-line | 6 | 4 | 28 999 |
| Njoy Balder 6000 · Marsriva MR-US6K · Eaton 5P/5PX/9SX · APC SMT | — | — | — | — | 30 999 – 123 889 |

**The traps in that filter, every one of them «Кількість батарей: без батареї»** — priced to look
like bargains because the battery is not in the box:

| Model | VA / W | Price | Why not |
|---|---|---:|---|
| Marsriva MR-UF1500P-H | 1500 / 1200 | 7 099 | **no battery**, terminals for an external bank, 2 × IEC only |
| Marsriva MR-UF2000P-H | 2000 / 1450 | 8 405 | **no battery** («батарея: зовнішня») |
| Njoy Aira 600 | 600 / 500 | 7 359 | **no battery**, and it is a boiler UPS |
| EnerGenie EG-HI-PS3000-02 / PS5000-02 | 3000 / 1800 · 5000 / 3000 | 9 998 · 13 999 | **no battery** — inverters |

Two more that are real but too small: **LogicPower LPM-U825VA, 3 126 ₴** — pure sine, 2 × Schuko,
but **577 W**, so ~89 % load; and **Marsriva MR-UF600P-H, 3 441 ₴** at 360 W.

**The Echo Pro 1000's numbers are the maker's own**
([nJoy datasheet, PN UPOL-OL100EP-CG01B](https://cdn.njoy.global/hive_files/wp/products/16182403846N5kJd.pdf)):

> «Waveform (Batt. Mode) **Pure Sine wave**» · «Transfer time Typical **0 ms**» · «Outlets type
> **3 x Schuko**» · «Noise level **Less than 40dB**» · «Efficiency To AC Mode **88%** · ECO Mode 96%»
> · running time 25 % — 19 min, **50 % — 6 min**, 75 % — 2 min, 100 % — 1 min

Two consequences worth naming before buying it. It is **double-conversion on-line**, so the fan
runs constantly at up to 40 dB next to the desk, and at 88 % efficiency it burns **~65 W
continuously** at full gaming load, and far less at desktop idle (ECO mode raises efficiency to
96 %, at the cost of a 4 ms transfer). At ~475 W it sits at **59 % load — roughly 4–5 minutes**,
between the maker's 6 min (50 %) and 2 min (75 %) rows.

**Unverified:** click.ua lists the Eaton 5E G2 as pure sine, but Eaton's own
[5E2200UI specification page](https://www.eaton.com/gb/en-gb/skuPage.5E2200UI.html) states no
waveform at all, and the 5E is the cheap IEC-only tier. Treat that row's waveform as unconfirmed —
it is IEC-only and dearer than the Echo Pro either way, so nothing rests on it.

## Rozetka, full sweep, 2026-09-30

Dmytro will buy at another shop with an OK reputation, not necessarily click.ua. First link he
sent: **Volt Polska SINUS PRO 800 E (3SP080012E), 3 899 ₴ — rejected**. It is **500 W** rated
(the 800 is VA or peak), which is ~95% of the ordered build's ~475 W, and its battery is
**«Зовнішня»**, not in the box. It is a boiler inverter.

**Method.** Rozetka category filter: pure sine + built-in battery + 501–3000 W →
**255 listings**, every one collected across all 5 pages. Each listing's own characteristics page
was then read, **255 of 255**, and filtered on Rozetka's own fields:

| Step | Left |
|---|---:|
| Nominal ≥700 W | 226 |
| Battery «Вбудована», no «без АКБ» in the name | 225 |
| «Є в наявності» | 103 |
| ≥1 Schuko socket | **37** |

66 in-stock units were dropped for IEC-only outlets; those work, but they need cables. Units
without an explicit «Є в наявності» were dropped. Rozetka's fields are seller-entered. The shortlist was compared
against **web-search summaries** of other retailers' listings; those pages were not opened
([Green Cell UPS09](https://www.proshop.nl/UPS/Green-Cell-UPS09-Pure-Sine-2000VA1400W/3224874),
[UPSLP700](https://arvutitark.ee/en/accessories/ups/greencell-ups-power-supply-700w1000va-pure-sine-1501474),
[PowerWalker VI 1500 CSW](https://www.proshop.nl/UPS/BlueWalker-10121114-PowerWalker-VI-CSW-1500VA900W-Line-Interactive-UPS/2771051),
[Qoltec 50721](https://www.dateks.lv/en/cenas/ups/942482-qoltec-pure-sine-wave-ups-1000va-700w)).
**The makers' own pages were not read.**

| | Green Cell UPS09 | PowerWalker VI 1500 CSW | Green Cell UPSLP700 | Qoltec 50721 | APC BGM2200B-GR |
|---|---|---|---|---|---|
| Price, Rozetka | **9 880** | 13 339 | 7 743 | 3 950 | 21 896 |
| Seller / delivery | RozetkaEU, from EU, ~12 Oct | **Rozetka**, pickup 4 Oct | RozetkaEU, from EU | third party, from EU | Діамант |
| Real W | **1400** | 900 | 700 | 700 | 1320 |
| Load at ~475 W | **34 %** | 53 % | 68 % | 68 % | 36 % |
| Topology | line-interactive | line-interactive | line-interactive | line-interactive | line-interactive |
| Battery | 2 × 12 V 9 Ah | 9 Ah (Rozetka field) | 2 × 12 V 7 Ah | built-in | internal |
| Schuko | 4 | 4 | 4 | 2 | 4 (+2 C13) |
| Transfer | 2–6 ms | 6 ms (Rozetka) / 10 ms (retailer) | 2–6 ms | 8 ms | — |
| Rozetka rating | 4.33 / 4 reviews | 3.6 / 31 | 4 / 1 | none | none |

Also passing all four filters: SVC SL-1.5KS-LCD 1200 W 7 649 (3.2 / 6, no transfer time
listed), Qoltec 52640 800 W 6 746, Greencell/Qoltec/EnerGenie online units at 7 652–11 999, and
Powercom, CyberPower, Eaton and Tescom from 17 955 up. Qoltec's online 53042 rates **2.62 / 34**,
the weakest record in the list.

**The APC BGM2200B-GR is 21 896 here against 28 855 at click.ua**, the same unit for 6 959 less.

## All shops, sweep, 2026-09-30

Asked for: every reputable Ukrainian shop, not only Rozetka. Criteria for each shop: **≥700 W
real, built-in battery, in stock, Schuko**, with the waveform recorded. Read in the browser from
each shop's own catalogue. Spec fields are the shop's own.

| Shop | What was read | Result |
|---|---|---|
| **Rozetka** | 255 listings, filtered pure sine + built-in + 501–3000 W, each spec page read | above |
| **click.ua** | all 248 listings; pure-sine filter (22) and stepped filter (41) read tile by tile; product pages opened for ≥700 W | Pure: Echo Pro 1000 **11 399**, FSP Champ 1K 900 W **16 500**. Stepped: **LPM-U1100VA-P 770 W 4 745**, Prologix 1500 900 W 4 749, Keen 1500 900 W 5 599. **Horus Plus 1500 now «Немає в наявності».** |
| **Epicentr** | «Продавець: Епіцентр К» only (53 own listings; the rest is marketplace), every page read | Nothing competitive. Orvaldi KC1000/KC2000 show price 0, not buyable; Westech 1000 is 9 360 for 700 W |
| **Comfy** | — | **Not read**: Cloudflare challenge, not bypassed |
| **Foxtrot** | all 169 UPS listings, each page read. **Foxtrot lists no waveform field** | Stepped (from model series): Ritar RTP1200 Proxima-L 720 W 2 × 7 Ah **4 400**, E-RTM1200 **4 399**, Powercom RPT-1500AP 900 W 6 480. No pure-sine unit beat Rozetka |
| **Brain / ITbox** (one catalogue) | pure + built-in (229 tiles) and stepped + built-in (338 tiles), specs from tiles, price from product data | Pure: **SVC SL-1KS-LCD 800 W, 2 × 7 Ah, 2 Schuko, 2–6 ms, 24 mo — 6 704**. Stepped: **SVC VP-1250-LCD 750 W, 2 × 7.5 Ah, 3 Schuko — 3 809**; Vinga VPE-1200PRM2 720 W 3 999; Gear GU-1200PL 720 W 4 Schuko 4 180 |
| **Telemart** | all 311 listings, each page read | Pure: best is EnerGenie PS1000-01 800 W **8 499**. Stepped: EnerGenie EG-UPS-033 720 W 4 999, Keen 1500 5 599 |
| **Moyo** | pure-sine subcategory (143), each page read; all 729 tiles, pages opened for everything ≤5 000 | Pure: cheap ones are all external-battery (36/48 V, «без АКБ»). Stepped: Vinga VPE-1200PU 720 W **3 899** |
| **Allo** | «Алло +» own stock only (177 tiles; 2 484 are marketplace sellers) | No pure sine ≥700 W. Stepped: Ritar from 4 630 |
| **LogicPower** (maker store) | line-interactive category, 25 models | All stepped. LPM-U1100VA-P **4 745**, LPM-U1250VA 5 477, UL1250VA 5 938, U1550VA 6 251 |
| **Citrus** | catalogue first page, sorted ascending | EnerGenie PS1000-01 8 499 pure; EG-UPS-033 4 999 stepped. Nothing new |
| **Voltmarket** | pure + built-in filter (304), sorted by price | Only 3 in stock under 11 000, and none beats the above; the rest are «Уточнити наявність» |

**A retailer states the waveform risk outright.** Brain's own listings for stepped units
(SVC VP-1250-LCD, Vinga VPE-1200PRM2, Gear GU-1200PL) carry **«Додатково: не сумісний з БЖ з
APFC»**, i.e. "not compatible with PSUs with active PFC". This is the concern argued above,
printed by a shop on the exact cheap units under consideration.

**Best per route, across all shops, 2026-09-30**

| | Pure: SVC SL-1KS-LCD | Pure: Green Cell UPSLP700 | Pure: Green Cell UPS09 | Stepped: SVC VP-1250-LCD | Stepped: LogicPower LPM-U1100VA-P |
|---|---:|---:|---:|---:|---:|
| Price | **6 704** Brain | 7 743 Rozetka | 9 880 Rozetka | **3 809** Brain | 4 745 click.ua / LogicPower |
| Real W | 800 | 700 | 1400 | 750 | 770 |
| Load at ~475 W | 59 % | 68 % | 34 % | 63 % | 62 % |
| Battery | 2 × 7 Ah | 2 × 7 Ah | 2 × 9 Ah | 2 × 7.5 Ah | 2 × 7.5 Ah |
| Schuko | 2 | 4 | 4 | 3 | 4 |
| Transfer | 2–6 ms | 2–6 ms | 2–6 ms | 2–6 ms | — |
| Warranty | 24 mo | 24 mo (retailer summary) | — | 24 mo | not read |

SVC's reputation is the open question: Rozetka rates the SL-1.5KS-LCD **3.2 / 6 reviews**, and no
independent review of the SL-1KS was read.

## Verdict

**Do not buy the nJoy Horus Plus 1500 for this machine.** It is not a bad UPS and its wattage suits
the build — the disqualifier is the single spec that matters most, and it is the one the listing
does not put in the title.

**Revised 2026-09-14 after the click.ua catalogue sweep.** click.ua does stock pure-sine units; the
choice is between his own shop and Foxtrot.

- **The pick, at his shop: NJOY Echo Pro 1000, 11 399 ₴ at click.ua.** Pure sine, on-line (0 ms
  transfer), 3 × Schuko, internal batteries, ~4–5 min at this build's full load. The cheapest honest
  pure-sine unit over 700 W in the whole category. Costs up to ~65 W in conversion loss and up to 40 dB of fan.
- **The quieter equivalent, at another shop: Powercom SPT-1500-II LCD, 12 375 at Foxtrot.** 1200 W
  line-interactive, so ~40 % load and longer runtime, no always-on fan or conversion loss, for
  **976 ₴ more at a shop he does not otherwise use**. Both prices are shop prices, so the gap is
  real; the shops are not.
- **Cheaper:** nothing honest. Everything under 11 399 in the pure-sine filter is either under
  700 W (LogicPower LPM-U825VA at 577 W) or sold without a battery (the two Marsrivas).
- **Better but pricier: APC Back-UPS Pro Gaming BGM2200B-GR, 28 855 at click.ua.** 1320 W pure
  sine, line-interactive, 4 × Schuko + 2 × C13, APC's service network — [Schneider's own listing
  says «Pure Sine Wave» in the product title](https://www.se.com/uk/en/product/BGM2200B-GR/). It is
  the right unit if the budget is indifferent; it is 2.5× the Echo Pro for a machine that needs
  four minutes of runtime. Better value than the BR1600SI at 31 500, which is 1000 W for more money.

**Unverified in this pass:** no lab review of the Powercom SPT-1500-II was read, only the maker's
specification; and the nJoy's runtime figures are the maker's own, not measured. Neither gap
changes the waveform conclusion, which is what decides it.

## Connecting it: wall socket, power strip, monitor, 2026-09-30

Dmytro's desk has **one wall socket**. His current strip feeds a laptop and chargers. He asked
whether a new strip is needed and how the UPS fits in.

**The setup:** wall socket → UPS only. UPS battery outlets → PC and monitor (there is no router at
this desk). The strip goes to a **different wall socket** elsewhere, for laptops and chargers,
which carry their own batteries. No new strip is needed. On the Echo Pro 1000 (3 × Schuko) that
leaves **one outlet free**, fine for one phone or laptop charger at a time (~20 W / ~65–100 W, a
light load). The charger drains the battery during an outage, so the PC's shutdown time shortens
slightly. To charge both from that outlet, use one multi-port USB-C charger, never a strip.

| Source | Kind | Read | Verbatim quote | Bearing |
|---|---|---|---|---|
| [APC/Schneider FA158852](https://www.se.com/us/en/faqs/FA158852/), modified 2026-04-01 | UPS maker | full (via fetch summary) | "Schneider Electric recommends against the use of any surge protector, power strip or extension cord being plugged into the output of any APC Back-UPS and Smart-UPS products." · "plug your UPS directly into the wall receptacle" | **Both rules.** No strip after the UPS: its filter can hide load and cause an overload on battery. No strip before it: it can compromise the ground and cause needless switches to battery. |
| [CyberPower ST425/ST625U/ST900U manual](https://inquirecontent2.ingrammicro.com/User-Manual/1049803838.pdf) | UPS maker | full, 7 pp. (16 052 chars) | "Plug the UPS into a 2-pole, 3-wire grounded receptacle (wall outlet)… The warranty prohibits the use of extension cords, outlet strips, and surge strips." · "DO NOT plug a laser printer, paper shredder, copier, space heater, vacuum… into the 'Battery and Surge Protected Outlets'" | A second maker agrees: wall socket, grounded, no strip. Also: the socket's circuit should not also feed an air conditioner or fridge. |
| [APC/Schneider FA158811](https://www.se.com/us/en/faqs/FA158811/), modified 2026-04-22 | UPS maker | full (via fetch summary) | "APC NEVER RECOMMENDS BATTERY BACKING UP A LASER PRINTER." · "Communication Cable Without Software" can cause unexplained shutdowns | Big loads stay off the UPS. Plug in the USB cable only with a driver or software handling it. |
| [APC/Schneider FA159743](https://www.se.com/us/en/faqs/FA159743/), modified 2026-08-03 | UPS maker | full (via fetch summary) | "roll back / revert the HID Driver to HID UPS" to restore native battery shutdown configuration | Windows can shut the PC down over USB with no vendor software (Power Options → Battery → critical battery action). |
| [ESFI, *Extension Cord Safety Tips*](https://www.esfi.org/extension-cord-safety-tips/) | Safety NGO (US) | full, browser | "Multiple plug outlets must be plugged directly into mounted electrical receptacles; they cannot be chained together." · "Make sure the extension cord or temporary power strip you use is rated for the products to be plugged in" | Strip rules: never chain one into another; rating must cover the load. |
| [Electrical Safety First, *Extensions and leads*](https://www.electricalsafetyfirst.org.uk/guidance/safety-around-the-home/extensions-and-leads/) | Safety charity (UK) | full (via fetch summary) | "Only use one socket extension device per socket. Don't plug an extension lead into another extension lead" · "Buy from a reputable retailer rather than a third-party seller online." | Same rules. Its 13 A figure is for UK plugs; Schuko strips are 16 A. |
| [iXBT Live, test of the Атлант/Атом strip](https://www.ixbt.com/live/supply/test-udlinitelya-atlant-atom.html), 2022-09-14 | Independent hands-on test (lab measurements) | full, browser, incl. comments | "Такое сопротивление соответствует сечению медной жилы 0.685 мм²." · "долговременно лучше не нагружать его токами более 10 А (мощность не более 2300 Вт)" | A strip sold as **16 A / 3500 W** measured **~0.7 mm²** and hit 65–73 °C at 16 A. The rating on the box is not proof. |
| [Distrelec RND 465-01012 datasheet](https://docs.rs-online.com/5e66/A700000013590617.pdf) | Maker datasheet | full, 2 pp. | "Cross-Section 1.5 mm² · Current Rating 16 A" · "Cable:H05VV-F 3G1.5 mm2" | What an honest 16 A Schuko lead specifies: H05VV-F 3G1.5. |

**Not read:**
- Tripp Lite's manual on manualslib: Cloudflare challenge, not bypassed. A search snippet says
  "Do not connect surge suppressors or extension cords to the output of your UPS".
- IEC 60884-2-7 Table 101 (wire size vs current for extension leads): the only copy found is
  encrypted.
- APC's install FAQ FA158879 no longer exists ("missing-faq"). "Monitor on the battery outlets"
  therefore rests on reasoning, not a quote: without it you can't see to save work.
- No manual for the nJoy Echo Pro 1000 or Powercom SPT-1500-II was found online. Read the one
  in the box for anything brand-specific.

**What this settles**

1. **UPS straight into the wall socket.** Two UPS makers agree, and CyberPower's warranty
   depends on it.
2. **Nothing plugged into the UPS except the PC, the monitor and, at most, one charger.** No
   strip, no laser printer, no heater.
3. **The strip goes in another wall socket, never chained to a second strip.** If it is ever
   replaced: Schuko with ground, 16 A, cable marked **H05VV-F 3G1.5** (or ПВС 3×1.5) printed on
   the jacket, from a known brand. A "3500 W" label alone proves nothing.
4. **Connect the USB cable and set automatic shutdown**, either through Windows' native battery
   settings or the maker's software. Never leave the cable connected with nothing handling it.

## Green Cell UPSLP700 in depth, 2026-09-30

Brief: [ups_greencell_brief.md](ups_greencell_brief.md). Dmytro likes the **Green Cell PowerProof
1000VA/700W (UPSLP700)**, 7 743 ₴ at RozetkaEU. The requirements (pure sine, ≥700 W, built-in
battery, Schuko, <10 ms) and the ~475 W load are settled above and not reopened here.

### What it is, maker-confirmed

A line-interactive UPS with a pure-sine inverter, from the **new PowerProof series (UPSLP480 /
700 / 1050 / 1400)**, listed on ek.ua since October 2025.

| Spec | Value | Where it's stated |
|---|---|---|
| Rating | **1000 VA / 700 W** → **68 %** at ~475 W | maker page + manual |
| Waveform | **pure sine** (manual table, OUTPUT row) | maker page + manual |
| Distortion (THD) | **not published** anywhere found | — |
| Transfer | **2–6 ms** (Ceneo seller copy: "maksymalny 10 ms") | maker page + manual |
| Battery | **2 × 12 V 7 Ah AGM**, 6–8 h to 90 % | maker page + manual |
| Battery replaceable? | Front cover "easy removal … better access to batteries"; manual: replace with "the same number and type" | maker page, manual p. 7 |
| Sockets | **4 × Schuko**, no IEC; RJ45 in/out, USB-B, fixed input cord, reset button | manual rear drawing p. 4, unboxing frames |
| Fan | **none drawn** on the 480/700 rear (the 1050/1400 have one); reviewers confirm no fan | manual p. 4, `AfYHfsgoBws`, `oIZ4qQdr8NI` |
| Noise | "below 55 dB" | manual |
| Alarms | battery mode every 10 s, low battery every 1 s, overload every 0.5 s, error continuous | manual p. 4 |
| Runtime at ~475 W | **not published.** Estimate below | — |
| Weight / size | 8 kg (page) / 9 kg (manual); 353 × 149 × 162 mm | maker page, manual |
| USB | GC UPS app (Windows 10/11, Linux, Intel Mac), auto shutdown, e-mail alerts | manual p. 8, gcups.greencell.global |
| Warranty | 24 mo (maker page adds "12 months for battery"); maker's territory **includes Ukraine** | maker page, manual p. 8 |
| EAN | 5904326375642 | maker page, Rozetka, Allegro |

**UPSLP700 and UPS08 are different units.** UPS08 is the older "Microsine" pure-sine model with
**2 × Schuko + 2 × IEC** (EAN 5902701419745). The UPSLP700 is the new design with 4 × Schuko. The
"2 sockets" result in the earlier sweep was the UPS08. Ceneo's UPSLP700 page also says "2x Schuko
+ 2x IEC", which is a seller copy error: the maker's drawing, Morele's spec table ("Gniazda schuko
4", "IEC C13 0") and the unboxing video all show four Schuko.

**Naming trap:** "PowerProof 1000VA" also names the older **UPS03 (1000 VA / 600 W, modified
sine)**. That series' manual says "output waveform … modified sin wave". Order by code
**UPSLP700**, never by name.

**Runtime estimate (my inference, not a sourced figure).** ~475 W out at ~85 % inverter efficiency
is ~560 W from the batteries, ~280 W per 12 V block. CSB's GP1272 datasheet gives 329–352 W per
battery for 5 min and 219–230 W for 10 min, so a new CSB-grade pair lasts **~5–7 min**. The only
runtime test of a Green Cell unit found (UPS05, `Q68xX7HmLA8`) got about half its expected time,
so **plan on ~3–5 min**. That is enough for a clean shutdown, not for waiting out an outage.

### Active PFC

**The maker says nothing about PFC.** Its page even claims modified sine suits "older generation
laptops and desktop computers", the opposite of Brain's «не сумісний з БЖ з APFC» (see "All
shops" above). The only first-hand remark is one Amazon Vine reviewer: "Gerade bei moderner
Hardware mit Active PFC merkt man den Unterschied, da läuft alles stabil". It is an anecdote, not
a test. What does bear on it is that the waveform is a real sine: the UPS08 predecessor's scope
trace on battery (`oIZ4qQdr8NI` @ 8:15) is a sine with flattened peaks near full load, not a
stepped wave. Whether the UPSLP700's inverter is the same is **not known**.

### USB shutdown: the weak point

- **Probably not HID.** Every older Green Cell unit on record talks the Megatec/Q1 protocol through
  a generic USB chip (NUT issue #2727: "VID=0001 PID=0000", driver `nutdrv_qx`). For the UPSLP700,
  one reviewer found "Auch die Verbindung über die integrierte USV-Steuerung des Betriebssystems
  ist nicht realisierbar" (macOS). **Not verified on Windows.** Plan on Green Cell's app, not on
  Windows' battery settings.
- **The app works for most buyers.** "funktioniert auch unter Windows11" (Amazon DE). The Rozetka
  reviewer can "налаштувати автоматичне вимкнення комп'ютера через застосунок". Two Vine
  reviewers run it through NUT.
- **But one buyer returned two units over USB.** "dwie testowane sztuki czasami połączą się po USB
  a najczęściej nie łączą się. Zwrot." (Allegro, 25 Oct 2025, the month of launch; the app is now
  v1.1.10).
- **Don't trust the battery %.** The UPS05 app showed 100 → 45 % within 15–40 s of a cut
  (`Q68xX7HmLA8` @ 1:50). Set shutdown to trigger **after N seconds on battery**, not at a percentage.
- The app forgets mute when the UPS loses power: "Не запам'ятовує тихий режим" (Rozetka), and
  the manual says "The settings will reset to default after turning the UPS off".

### Warranty and returns via RozetkaEU

- **Rozetka:** "Гарантія. 24 місяці. Повернення товару впродовж 30 днів." Rozetka's help page adds
  that a return must be «Товар не був у використанні», the buyer pays return shipping, and the
  money comes back within 14 days. **The 35 ₴ customs payment is not refunded.**
- **Implication:** the earlier idea of testing by pulling the plug with the PC under load inside
  the return window **uses the unit**. A failure on that test is a defect claim, not a no-questions
  return.
- **Maker:** warranty territory "covers the European Union, … Russia, Ukraine, Turkey and Albania".
  Claims go by e-mail to support@greencell.global. The maker covers "the cost of delivery of the
  defective product to the Guarantor service" and back, and a battery qualifies when capacity falls
  "below 80% of the nominal value". **No Ukrainian service centre found.** The official UA dealers
  IBIS (no UPSes listed) and Solarex (site blank) don't carry this model.
- **Nobody reports an actual RozetkaEU warranty claim** (Overclockers.ua thread, 18 posts). One
  buyer notes a receipt but no warranty card.

### Price and stock, 2026-09-30

| Shop | Price | Stock |
|---|---:|---|
| **Rozetka (seller RozetkaEU, from the EU)** | **7 743 ₴ + 35 ₴ customs + 319 ₴ Meest** (free with the 50 ₴/mo subscription) | «Є в наявності», 5–9 days |
| click.ua, Telemart, Brain/ITbox, Foxtrot, Allo, Citrus, Comfy | — | **not listed** (own site search) |
| Epicentr | — | search shows no product |
| Moyo | — | search returned no product text; not established |
| hotline | — | no entry; ek.ua: «Очікується у продажу», last seen 7 291 ₴ |
| Poland, for scale: Ceneo, 28 offers | from **531 zł** (Morele, Amazon) | in stock |

Rozetka is the only Ukrainian seller. It is not a markup the doc can quantify like-for-like: the
Polish price excludes delivery and customs.

### Coverage table

| Source | Read | Verbatim quote | Bearing |
|---|---|---|---|
| greencell.global product page ([archive 2026-06-11](https://web.archive.org/web/20260611064223/https://greencell.global/en/new-release/6172-uninterruptible-power-supply-ups-greencell-1000va-700w-powerproof-with-lcd-display.html)) | full page, via Wayback (live site 403) | "Sine wave type Pure sine wave" · "Sockets 4x Schuko" · "Warranty 24 months (12 months for battery)" | Maker spec confirmed |
| Maker manual, PowerProof 750–2000 VA pure sine ([docs.greencell.global](https://docs.greencell.global/manuals/UPS_Power_Proof/pure_sine_manual.pdf); same text as [Amazon's copy](https://m.media-amazon.com/images/I/D1dRiWCCB1L.pdf)) | EN section in full (pp. 1–9 of the Amazon copy, image pages read visually); other 25 languages not read | "Output waveform pure sine wave" · "Territorial scope of warranty protection covers … Ukraine" | Spec, alarms, app, warranty path |
| Maker manual, older PowerProof 600–2000 VA ([batna24](https://www.batna24.com/products/DNXGFQISKRMNH/Green%20Cell%20Manual%20UPS01-05.pdf)) | EN section in full | "output waveform … modified sin wave" | The naming trap: older series, stepped |
| Maker manual `ups_en.pdf` (archived) | in full | "1KVA-3KVA series on-line UPS" | **Not this unit**: online series |
| [gcups.greencell.global](https://gcups.greencell.global/en) | full (fetch summary) | "Works with all GC UPS devices" · version 1.1.10 | Official app, Windows/Intel Mac |
| [NUT issue #2727](https://github.com/networkupstools/nut/issues/2727) | full (fetch summary) | "VID=0001 PID=0000" · `nutdrv_qx` megatec | Older GC units are not HID |
| [Rozetka p569712112](https://hard.rozetka.com.ua/ua/green-cell-upslp700/p569712112/) | specs, 2 reviews, 1 question, all | "Продавець: RozetkaEU" · "35 ₴ митних платежів" · review tagged "Номінальна потужність: 1400 Вт" | Price. **The one review is for the 1400 W variant**, so the 700 W has none there. The AI summary on that page (mentions IEC ports) is ignored |
| [Rozetka help: return from EU](https://help.rozetka.com.ua/p/84-yak-povernuty-zamovlenyj-tovar-z-yevropy-rozetka-eu/) | full (fetch summary) | "Товар не був у використанні та не має слідів зносу" | Return only if unused |
| [Overclockers.ua, RozetkaEU warranty](https://forum.overclockers.ua/viewtopic.php?t=273817) | 18/18 posts | "чек є, а гарантійного талону, як такого, немає" | No claim experience on record |
| [Amazon DE B0FQ5WVZ6K](https://www.amazon.de/dp/B0FQ5WVZ6K) (same pool on .pl/.it/.fr/.es) | 8 visible reviews in full; 31 ratings, **4.4 / 5**; the other 23 are star-only or behind sign-in, **not read** | "Threadripper Pro server, which normally draws about 350 to 400 W … several power cuts … kept the server running" · "vier 230-Volt-Steckdosen" | Real outages survived at a load like ours; 3 of the 8 note plastic smell or a bright screen; 5 are Vine (free product) |
| [Ceneo 188818453](https://www.ceneo.pl/188818453) | full page | "Gniazda:2x Schuko + 2x IEC" (seller copy) · from 531,00 zł | PL price; socket error explained above; no reviews |
| [Morele](https://www.morele.net/ups-green-cell-powerproof-1000va-upslp700-15498948/) | 3/3 reviews (2 are UPSLM360) | "trzyma napięcie ale po 9 miesiącach zaczął głośno buczeć" | One verified buyer, loud buzzing after 9 months |
| [Allegro product](https://allegro.pl/produkt/zasilacz-ups-greencell-upslp700-1000-va-700-w-35ad081d-b375-40b2-9c1d-5584a837452d) | 1/1 written review; 7 ratings, **4.71 / 5** | "dwie testowane sztuki czasami połączą się po USB a najczęściej nie łączą się. Zwrot." | **USB unreliable on 2 units** |
| ek.ua UPSLP700 | full | «Очікується у продажу» · «Дата додавання на E-Katalog жовтень 2025» | No UA seller besides Rozetka |
| Xipe `AfYHfsgoBws` ([sources/](pc_build/sources/ups_AfYHfsgoBws.md)) | 2 349 / 2 349 chars + 4 frames | @0:00 "Da ist kein Lüfter, der jetzt sich die ganze Zeit dreht" | Affiliate unboxing. Frames @0:42–1:08 show 4 Schuko, USB-B, 2 × RJ45, fixed cord |
| Ss4Net `oIZ4qQdr8NI` ([sources/](pc_build/sources/ups_oIZ4qQdr8NI.md)) — **UPS08, predecessor** | 9 446 / 9 446 chars + 5 frames | @6:40 "lo spariamo a 695 … rimane acceso" · @12:50 "non ha una dissipazione attiva quindi non ha una ventola … andrà in protezione termica" · description "indicato per apparecchi con assorbimento massimo di circa 500W" | Held 700 W on battery with a real sine. Fanless, so not for sustained near-full load. AVR boost at ~205 V, battery below ~168–170 V |
| HiMiK13 `Q68xX7HmLA8` ([sources/](pc_build/sources/ups_Q68xX7HmLA8.md)) — **UPS05, old stepped model** | no captions; 7 frames (every ~20–30 s) | frame @1:50: «при нагрузці не більше 250-300 ват він тримає 8-10 хв (а повинен 15-20)» | GC battery underdelivers; the app's battery % is unreliable |
| [CSB GP1272 datasheet](https://csb-battery.com/wp-content/uploads/2026/03/CSB-Datasheet-GP1272-01312026.pdf) | discharge tables | "10.50V (1.75 VPC) 329 219 168" W at 5/10/15 min | Basis of the runtime estimate |

**Not read:** greencell.global live (HTTP 403 on every page; WebFetch and browser); manuals.plus
UPSLP700 manual and Heureka.cz reviews (Cloudflare, not bypassed); the Amazon reviews behind
sign-in; the older UPS08 maker page (not archived). **No lab review of the UPSLP700 exists** that
search could find: no written test, no scope trace, no THD. Search on YouTube in EN/PL/DE/UA found
only the maker's 2021 promo `2R3sBEpaa-E` (old series, not read) and the videos above.

### Verdict on the UPSLP700

**Buy it, with the USB risk managed.** It meets every settled requirement on the maker's own
spec: pure sine, 700 W real (68 %), 4 × Schuko, 2–6 ms, batteries in the box. Buyers report
real outages survived, one at a 350–400 W load like this PC's.

- **Open risk 1, USB auto-shutdown.** One buyer got two units whose USB mostly failed to connect,
  and Windows native shutdown probably won't work. **Test the app on day one**, before the 30 days
  run out and before relying on it. If it won't hold a connection, that is a defect claim.
- **Open risk 2, a fanless unit.** It is fine for a few minutes at 475 W, but don't expand the
  load toward 700 W. The Max build (~555 W, 79 %) would be near what the UPS08 reviewer advised
  against.
- **Open risk 3, service.** Warranty runs through RozetkaEU or by e-mail to Green Cell in Poland.
  No Ukrainian service centre was found, and nobody reports a claim being handled.
- **Minor:** plastic smell for the first days (3 reports), a bright screen with no dimming (2),
  buzzing after 9 months (1), a relay click when the UPS is off but plugged in (1).

Alternatives were not re-examined: nothing above fails a requirement. They stand as priced in
"All shops, sweep": SVC SL-1KS-LCD (6 704 Brain, cheaper, 2 Schuko, no review read) and
Green Cell UPS09 (9 880 Rozetka, 1400 W).
