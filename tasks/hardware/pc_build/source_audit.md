# Source audit: every link Dmytro sent, checked against the docs

Started 2026-09-13, after the docs were found to cite videos by channel name with no ID and no
timestamp — leaving nothing Dmytro could re-check. Scope: **every link sent across every session**,
verified against what the docs claim, video *and* audio.

Inventory taken from the raw session transcripts with two independent extractors (different regex
patterns, second one also covering `/shorts/`, `/embed/`, `/live/`). Both return the same totals.

| | Count |
|---|---:|
| YouTube videos sent | **99** |
| Non-YouTube links sent | **27** (see the note below) |
| **Total** | **126** |

**Corrected 2026-09-13.** An earlier figure of 113 links / 91 videos was wrong, and so was the
replacement: the non-YouTube count is **27**, not 22. Re-derived twice from the raw `.jsonl`
transcripts. Six of the 27 are Google shopping-redirect wrappers pasted inside a quoted AI answer
and one is skill boilerplate rather than a link Dmytro chose to send, which is where the lower
figure came from. **99 is confirmed and stable** across every derivation.

Transcripts are saved under [`sources/`](sources) and frames under [`frames/`](frames) so any line
below can be re-checked without re-fetching. The component map is
[`sources/GROUPS.tsv`](sources/GROUPS.tsv), re-derived from the transcripts, and
[`verify_audit.py`](verify_audit.py) re-derives the inventory from scratch on every run rather
than trusting either.

## Progress — run `verify_audit.py`, do not trust this table

`PYTHONUTF8=1 venv/Scripts/python.exe tasks/hardware/pc_build/verify_audit.py`

**As of 2026-09-13: 99 of 99 PASS. Every video sent across every session has been read end to end.**

| Component | Videos | Verified | Status |
|---|---:|---:|---|
| PSU | 5 | **5** | read in full, every row quoted |
| SSD / storage | **8** | **8** | **was recorded as 4** — two batches six weeks apart, only the second was ever written up |
| RAM | **5** | **5** | **was recorded as 10** — four of those ten are SSD videos, one is the combo guide |
| Monitor | 6 | **6** | read in full |
| CPU cooler | 3 | **3** | read in full |
| Case | 5 | **5** | read in full |
| Build technique / compatibility | 4 | **4** | read in full; ScatterVolt frames pulled, having never been saved |
| Motherboard | **7** | **7** | **was recorded as "6 of 6"** — `BvtNCM5ms3U` had never been fetched |
| GPU | 4 | **4** | re-done in the verifiable format; the earlier "37 953 chars" matched nothing on disk |
| CPU/GPU combo guide | 1 | **1** | the source behind `scattervolt_2026.md`; transcript now kept |
| UPS | 7 | **7** | **parked by Dmytro** — read and recorded, not researched |
| Mouse | 8 | **8** | read in full; three miscounts and a misattributed "21 years" fixed in the doc |
| Keyboard | 6 | **6** | read in full; two backwards statements fixed, a Keychron tie through four of the six |
| Headphones / headset | 16 | **16** | read in full; the rival mic was oversold, a source verdict was never reported, three of the sixteen are shops |
| Laptop-as-display | 5 | **5** | read in full; three of the five answer a different question, and the answer was never written down anywhere |
| Earbuds (separate task) | 9 | **9** | read in full; a withdrawal made on another product's verdict — see DECISIONS in pc_build.md |
| Non-YouTube links | 27 | **27** | 20 real sources checked over verified TLS; 6 are Google redirect wrappers in a pasted AI answer and 1 is skill boilerplate; 3 pages unreadable and recorded as unread |

## The audit did to itself what it was built to catch — recorded 2026-09-13

**Four of the 99 rows below were written from a partial read, and their char counts said otherwise.**
Dmytro asked directly whether every video had been read in full. It had not. The honest accounting,
computed from the line ranges actually printed against the line counts on disk:

| Video | What was actually read | The row claimed |
|---|---|---|
| `f7lnPrre2Wk` Andro-news, 123 lines | lines 1-22, a **grep window**, then 97-120 | 31 598 / 31 598 |
| `u0eyHbDMzU8` MyChooz, 69 lines | 1-26, a **grep window**, 47-62 | 20 432 / 20 432 |
| `4F0289jmqQs` Mike O'Brien, 71 lines | 1-24, a **grep window** over 24-50; 51-71 unread | 22 045 / 22 045 |
| `sBba4MGPc2U` Ali Abdaal, 55 lines | 1-28 and 38-55 — **head+tail**; 29-37 unread | 21 028 / 21 028 |
| `2hVk-4Timf0` hotline, 71 lines | 1-64 and 66-71 | one line short |

**Three used grep windows and one used head+tail — the two methods this audit's own brief names
first as not counting as a read.** Every other video was a genuine end-to-end dump; the ones read
in slices (`We6Ta36qJ_Q`, `MSBnVb5SoUE`, `ljV1iOJmE_E`, `zbClh_tBl6o`, `44zG1beMWfg`,
`ZpP3-fUWQew`) were checked and their ranges do cover the full body.

**`verify_audit.py` passed all five and always would have.** It checks that a row exists, carries a
verbatim quote, and that the number matches `measure.py`. The number came from `measure.py`, not
from reading. **A char count is evidence that the file was measured, not that it was read** — which
is exactly the hole the "37 953 chars, read end to end" finding in the GPU section describes.

**All five were then read in full and the rows re-checked.** Nothing already written turned out to
be false; two findings gained support and **three things were missed and are now recorded** —
see "What the partial reads had missed" at the end of the earbuds section.

**And the hole is now closed in the tooling rather than in a promise.**
[`audit_tools/coverage.py`](audit_tools/coverage.py) reconstructs, from the raw `.jsonl` logs,
every line of every transcript that was ever actually printed into a context, and
`verify_audit.py` fails any video whose body is not fully covered — it now reports
**`bodies proven read end to end : 99 of 99`** alongside the PASS count. `measure.py`'s output is
no longer admissible in a row; `coverage.py --emit` supplies the pair instead, derived from
evidence. A hook, [`.claude/hooks/no_partial_reads.py`](../../../.claude/hooks/no_partial_reads.py),
refuses `grep`/`head`/`tail`/byte-truncation against `sources/` outright, because the instruction
not to use them was already written in bold and was ignored anyway.

**The check paid for itself immediately: it found three more unread lines that had been passing
all along**, including two in `ups_JL71IH5HShI` from the very first sweep — one of which carried
the most practical sentence in the UPS batch. See the UPS section.

**Exactly one of the 99 has no caption track** — `2ufCzwK73GM` — re-confirmed after a rate-limit
bug in the fetcher was fixed. That bug would have silently recorded HTTP 429 responses as "no
captions"; it is fixed, and every fetch since ran clean.


## GPU - verified 2026-09-13

| Source | Doc claim | Frame | Verdict |
|---|---|---|---|
| BENCHMARKS FOR GAMERS `2ufCzwK73GM` @ 10:38 | "13% faster on average at 1440p" | "13% Faster on average at 1440p + DLSS 4.5 / FSR 4.1 Q" | **exact** |
| same | all 13 per-game deltas (25, 24, 20, 20, 19, 16, 13, 12, 12, 4, 3, 1, -6) | identical, all thirteen bars | **exact** |
| same @ 0:40 | Forza raw overlay 73.8 / 65.3 vs 92.4 / 81.2, VRAM 11 230 MB | 73.8 / 65.3, 92.4 / 81.2, VRAM 11230 | **exact** |
| Testing Games `4UqYr3nAj90` @ 3:59 | 9070 39, 5070 38, XT 48, 5070 Ti 52 | 39, 38, 48, 52 | **exact** |
| Jegs TV `hIZj4MOk6fo` @ 14:50 | 9070 1% low **41** | **37** | **WRONG - corrected** |

The single error leaned in the RX 9070's favour: the real 1% low deficit in path-traced Cyberpunk
is 32%, not 20%. It does not change the decision — path tracing was already the known worst case
and never the buying argument. Corrected in [gpu.md](components/gpu.md) with the timestamp recorded.

## GPU - the three benchmark videos, transcripts read in full 2026-09-13

These were previously recorded as "frame-checked only, their transcripts carry no data". That was
an **assumption, never tested.** Tested now:

| Video | Transcript chars | Content |
|---|---:|---|
| `2ufCzwK73GM` BENCHMARKS FOR GAMERS | **0** | No caption track at all. The assumption held here. |
| `4UqYr3nAj90` Testing Games | **450** | A G2A sponsor read and in-game dialogue. No technical content. |
| `hIZj4MOk6fo` Jegs TV | **1 798** | **Contains the test setup, which the doc does not record.** |

### What the Jegs TV intro adds

*"we're going to use **Sapphire's Pulse** RX 9070 and **Palit's RTX 5070 Infinity 3** ... a Ryzen 7
9800X3D with **64 gigs of 6,000 MHz RAM** ... 15 games in 1920x1080p, 2560x1440p, and 4K"*, and
*"the test will be free from any form of commentary, so you guys can interpret the data at your own
leisurely pace."*

Two things follow. First, **the card models were never recorded in
[gpu.md](components/gpu.md)** - it cites "Jegs TV, Cyberpunk 2077, 1440p, RT Overdrive" with no
mention that the cards are a **Sapphire Pulse** and a **Palit Infinity 3**. Model matters: a Pulse
is a near-reference card and an Infinity 3 is a budget partner design, so this is a like-for-like
pairing at the low end of both stacks, not the OC models GECID used. Worth adding. Second, the
video states outright that it carries no commentary, which **confirms the frame-reading method**
was the correct one for it rather than a convenient assumption.

### Scope limit on frames

Transcripts for all four GPU videos are now read in full. **Frames are not exhaustive**: 2 of
roughly 14 chart frames sampled from `2ufCzwK73GM` (the closing average chart covers all 13 games,
so the doc's claims are fully covered), 1 each from `4UqYr3nAj90` and `hIZj4MOk6fo`, and 8 of
roughly 18 per-game charts from GECID. Every figure the docs actually claim has been checked
against a frame; not every frame in every video has been looked at.

## GPU - GECID `cUSxa4PxI4I`, read in full 2026-09-13

Transcript [`sources/gpu_cUSxa4PxI4I.md`](sources/gpu_cUSxa4PxI4I.md), **37 953 chars, read end
to end.** Plus 8 frames in [`frames/`](frames).

**Result: every claim in [gpu.md](components/gpu.md)'s GECID section is verbatim accurate.**

| Doc claim | Transcript |
|---|---|
| "about 10-20% ahead in most modern projects" | *"У більшості сучасних проєктів вона випереджає RTX 5070 приблизно на 10-20%"* |
| Death Stranding 2 **+16%** | *"RX9070 перегнала RTX 5070 на 16% загальної продуктивності"* |
| S.T.A.L.K.E.R. 2 **+13%** | *"випереджаючи RTX 5070 приблизно на 13%"* |
| Resident Evil Requiem **+20 FPS** | *"випереджає RTX 5070 приблизно на 20 кадрів за секунду в середньому"* |
| AC Shadows **64 FPS against under 60** | *"стабільно втримувати планку у 60 кадрів за секунду їй все ж не вдається. Натомість RX 9070 забезпечує в середньому близько 64 FPS"* |
| Battlefield 6 **90+ FPS**, 5070 below 60 in firefights | *"допускає просідання нижче комфортної позначки у 60 FPS ... Більше 90 FPS в середньому"* |
| The Long Dark, 5070 by **~80 FPS** | *"близько 250 разів за секунду в середньому, що майже на 80 FPS перевищує результати RX 9070"* |
| 5070 also wins GTA 5, Dying Light, Witcher 3 | *"невелика перевага все ж залишається за RTX 5070"*; *"символічно виривається вперед"*; *"не вдається наздогнати свого зеленого опонента"* |
| 12GB "filled to the brim" | *"гра вже майже повністю освоює доступні 12 ГБ"* (Cyberpunk RT Ultra); *"12 ГБ ... фактично заповнюється під зав'язку"* (RE Requiem) |
| DOOM would not launch on the current AMD driver | *"на найновішому драйвері AMD гра на відріз відмовилася запускатися, тоді як на більш старій версії все запрацювало"* - and the on-screen Vulkan crash dialog at 28:05 |
| Pragmata / RE Requiem: no path tracing on the 9070 | *"На відеокарті неможливо активувати трасування шляху"*; *"RX 9070 позбавили підтримки цього режиму"* |
| Subnautica 2: no FSR | *"Підтримки FSR у грі наразі просто немає"* |
| Witcher 3: FSR 2 only | *"на RX 9070 доступний лише FSR-2"* |
| Cards supplied by Telemart | *"за надання цих відеокарт на тест ми дякуємо магазину Telemart"* |

### Retraction

An earlier version of this section recorded the AC Shadows line as **contradicted**, on the
grounds that the summary chart at 27:42 reads 96 against 121. That verdict was wrong, and it was
wrong for the same reason everything else in this audit has been wrong: it was formed from a
partial sample. The chart at 27:42 runs *with frame generation enabled*; the doc's figure comes
from the upscaling-only run, which the narration states exactly. **Both numbers are real and
describe different configurations.**

The same partial reading produced three "unlocated" claims - Death Stranding 2, S.T.A.L.K.E.R. 2
and The Long Dark. All three are stated outright in the narration. They were not missing; they
were unread.

**Conclusion on this source: the prior session did this one properly.** Fifteen claims, fifteen
verified, including four that required understanding which test configuration produced which
number. The only real defect is the one this audit was set up to fix - no timestamps recorded -
and on a source this accurate that is a documentation gap, not an accuracy problem.

**Action on [gpu.md](components/gpu.md):** add the chapter timestamps. Nothing needs correcting.

## Motherboard and part-choice guides - 6 of 6 read IN FULL, 2026-09-13

This heading was wrong twice before. It is now measured, not asserted:

| Video | Transcript chars | Read | Full? |
|---|---:|---:|:--:|
| `7CVkfi0_mME` | 9 550 | 9 550 | yes |
| `fsIh2eoWLT4` | 22 878 | 22 878 | yes |
| `lP-pinlU-Ko` | 19 621 | 19 621 | yes |
| `ITBy9ckvSFY` | 13 047 | 13 047 | yes |
| `VgWrOSG24Yg` | 21 535 | 12 000 + 11 000 overlapping | yes |
| `PfAsVb4Bza4` | 15 479 | 8 200 + 8 500 overlapping | yes |

Transcripts in [`sources/`](sources). None is a benchmark video, so no frames apply.

### What the previously unread halves contained

Three things that the partial reads had missed, all quoted:

- **`PfAsVb4Bza4` is sponsored by ASUS** - *"a massive thank you to asus for sponsoring this
  video"* - which its ASUS-range walkthrough should be weighed against. It also states the case
  for spending *less* on the board: *"motherboards don't usually result in better or worse frames
  per second in games"*, and *"I commonly see people overspending on their motherboards but then
  getting a cheaper processor or graphics card to compensate and ultimately this ends up lowering
  your gaming performance."* That supports the board sitting at 7.5% of the Working build rather
  than Tech Guided's 8-12%.
- **A third independent corroboration of the Wi-Fi SKU trap**: *"if you do need wi-fi make sure
  your motherboard does actually support this because especially at the budget ends not all of
  them do."* With `VgWrOSG24Yg`'s *"sometimes you have Wi-Fi or Wi-Fi missing"*, that is three
  sources on the exact trap hit in this session when the click.ua basket carried the non-WiFi
  ASRock.
- **`VgWrOSG24Yg` carries a sponsored segment for grey-market Windows OEM keys at $23.22.** The
  build budgets Windows 11 Home at **7 098**; that is roughly 1 000 UAH. Recorded as a thing that
  exists, **not** as a recommendation - these keys carry legitimacy and re-activation risk, and
  the doc's 7 098 is for a licence that will survive a motherboard change.

### Correction to a finding above

An earlier version of this section said `ITBy9ckvSFY` *"never mentions the AM5 CPU-failure saga
at all."* Read in full, it **does** mention an AM5 problem - but attributes it to **ASUS**:
*"the AM5 voltage controversy during early Ryzen 7000 launches."* That is a different event from
the 9800X3D burnout cluster that [motherboard.md:103](components/motherboard.md) pins on ASRock.
The substantive point survives - the video's ASRock section raises no reliability concern and says
the budget-brand reputation *"doesn't really fit anymore"* - but "never mentions the AM5 saga" was
too strong and is withdrawn.

| Video | Channel, date | What it actually contains that bears on this build |
|---|---|---|
| `ITBy9ckvSFY` | Socket-X, 2026-05-15 | **ASRock reframed:** *"originally started as a lower-cost ASUS spin-off ... that reputation doesn't really fit anymore"*, strength is *"value engineering"*. A full brand-by-brand 2026 survey that **never mentions the AM5 CPU-failure saga**. |
| `7CVkfi0_mME` | Socket-X, 2026-05-11 | *"A modern B650 or B760 offers effectively the same gaming performance as their more expensive siblings"* - backs B850 over X870. *"32 GB across two sticks is the technical golden zone"* and daisy-chain topology penalises four sticks - backs the 2x16 kit. *"Around 6,000 MT/s is the sweet spot"* - matches DDR5-6000. **Gen 5 NVMe drives *"run incredibly hot"*, heatsink *"isn't just for show"*.** 2.5GbE *"useless unless your router and internet plan actually support those speeds"*. |
| `lP-pinlU-Ko` | Paul's Hardware, 2020-05-17 | Five-feature checklist: BIOS flashback, LED post readout, clear CMOS button, fan control, surface-mount power buttons. Recommends **Hardware Unboxed and Buildzoid** for VRM analysis - the exact method [motherboard.md](components/motherboard.md) uses. Suggests a **USB Wi-Fi dongle** as an alternative to onboard. |
| `fsIh2eoWLT4` | Tech Guided, 2023-12-24 | **Board budget heuristic: 8-12% of total budget** on builds of $1 000+. Phase count is a weak VRM indicator; use Buildzoid / GN / HWU reviews. Names a **Reddit motherboard VRM tier spreadsheet** as a resource. |
| `VgWrOSG24Yg` | Tech Notice, 2025-09-14 | Compare **whole-platform cost** across generations, not just the board - previous-gen stock dries up and prices rise. Warns that the same model name appears **with and without Wi-Fi**. |
| `PfAsVb4Bza4` | PC Centric, 2021-09-09 | Onboard Wi-Fi over an add-in card: *"extra money and ultimately extra mess"*. Warns the **front USB-C header** must exist on the board if the case has a USB-C port. |

### What this changes

**1. The ASRock brand-risk paragraph needs a dated re-check.**
[motherboard.md:103](components/motherboard.md) withdrew the ASRock B850 Pro RS **"on brand risk,
not hardware"**, resting on a 2025 Reddit megathread of ~108 CPU failures. The most recent brand
survey in this set - May 2026, 406k views, full ASRock section - explicitly says the old reputation
*"doesn't really fit anymore"* and never raises the failures. That is an argument from silence, not
a refutation. But **the build ships an ASRock B850 Pro RS WiFi in all three tiers**, so the
paragraph and the pick already contradict each other. One of the two has to move.

**2. The onboard-Wi-Fi rule is corroborated 2:1.** [motherboard.md:40](components/motherboard.md)
says *"onboard module or nothing"*. Socket-X 2026 and PC Centric both agree; only Paul's Hardware
(2020) offers the USB-dongle alternative. The rule stands, and the 614 UAH paid for the WiFi SKU
this session was correctly spent.

**3. Two checks the docs do not currently make:**
- **Front USB-C header.** The AeroCool D502A has front USB-C. Nothing confirms the ASRock B850 Pro
  RS WiFi carries the matching header. Raised by PC Centric; flagged in
  [case.md:27](components/case.md) as a thing to check but never actually checked.
- **Gen 5 NVMe heat.** Max ships a Kingston Renegade G5, a PCIe 5.0 drive. Socket-X is explicit
  that Gen 5 drives run hot and need a heatsink. Needs confirming against
  [storage.md](components/storage.md) and against whether the board's primary M.2 slot has one.

**4. Two findings recorded but not acted on:**
- The board is **7.5% of the Working build** (8 642 of 115 389), just under Tech Guided's 8-12%
  heuristic. The heuristic comes from a $1 000-build context and degrades at higher budgets, so
  this is a cross-check that approximately passed, not a problem.
- The docs carry a **PSU tier list** but no **motherboard VRM tier list**. Tech Guided names one.


## PSU - 5 of 5 read IN FULL, 2026-09-13

Transcripts in [`sources/`](sources) as `psu_<id>.md`. "Chars" is the transcript **body** - the
`## Transcript` section, excluding title block, chapter list and description. Every row below
carries a verbatim quote; rows I could not quote say "not read" instead of a verdict.

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `SS7P63fLE_8` Tech Guided, 2024-01-11 | **16 871 / 16 871** | *"the calculator suggested a minimum PSU wattage of 469 Watts that is considerably less than the 700 Watts that AMD recommends to run a 7800 XT"* | **exact** - psu.md's worked example is verbatim |
| `SS7P63fLE_8` | 16 871 / 16 871 | *"the manufacturer's recommendation on your graphics card will likely overestimate that amount"* | **exact** - supports "vendor wattage overestimates" |
| `SS7P63fLE_8` | 16 871 / 16 871 | *"the 80 plus rating system isn't perfect and doesn't necessarily indicate that a power supply is a quality unit"*; *"where the 80 plus rating system will overrate some units the cybernetics rating program likely won't"* | **exact** - supports the Cybenetics-over-80-PLUS rule |
| `SrNIbt703jo` PC Builder, 2026-03-05 | **22 196 / 22 196** | *"I recommend sizing your PSU at least 1.5 times the max rated draw in PC Part Picker. If my rated draw is 500 W, then multiplying that by 1.5 gives you a 750 W minimum PSU."* | **exact** - the 1.5x rule is quoted correctly |
| `SrNIbt703jo` | 22 196 / 22 196 | *"For GPUs, I recommend using one cable per connection for the first two eight-pin plugs, then you can daisy chain the third one if your GPU requires that many."* | **exact** - the cabling rule is quoted correctly |
| `SrNIbt703jo` | 22 196 / 22 196 | *"For modular PSUs, you should never mix and match cables with another PSU"* | **exact** |
| `SrNIbt703jo` | 22 196 / 22 196 | *"most of the time, it's not their GPU at all, but a power delivery issue and reseating the power cables ... often fixes the issue"* | **exact** - the black-screen troubleshooting note |
| `SrNIbt703jo` | 22 196 / 22 196 | *"the be quiet Pure Power 13M ... only the 750, 850, and 1000 W units are actually A-tier rated. Anything over that is B-tier"* | **exact** - independent confirmation the pick is A tier |
| `SrNIbt703jo` | 22 196 / 22 196 | *"it comes with **three** PCIE 6+2 pins ... One of them you have to not use the 12 V high power for."* | **CONTRADICTS psu.md** - see below |
| `bUh2EZzJZRU` JayzTwoCents, 2021-03-13 | **19 728 / 19 728** | *"an 80 plus gold 850 watt power supply uh from any reputable brand"* | **exact** - his blanket recommendation |
| `bUh2EZzJZRU` | 19 728 / 19 728 | *"i usually recommend uh a thousand watt power supply for anyone running any sort of high-end components ... something that's like an 80 series gpu or higher or something like a 6800 xt or higher"* | **CONTRADICTS psu.md** - see below |
| `bUh2EZzJZRU` | 19 728 / 19 728 | *"nick actually blew up an ssd of mine because he used the plug from a wrong power supply"* | **exact** - the destroyed-SSD anecdote is real |
| `bUh2EZzJZRU` | 19 728 / 19 728 | *"it is actually a bell curve on the way the efficiency curve works"*; *"they're one of the most reusable components in your system"* | **exact** |
| `bUh2EZzJZRU` | 19 728 / 19 728 | *"the graphics card manufacturers are accounting for the hypothetical potential equipment that you're hooking up to it"* | **exact** |
| `Xx6rFaKaqp0` GeekaWhat, 2023-12-29 | **10 674 / 10 674** | *"one of the most fullprof ways of getting the right wattage is actually by looking at your gpu's recommended PSU"*; *"the GPU figure is always a good one to go off"* | **CONTRADICTS psu.md** - see below |
| `Xx6rFaKaqp0` | 10 674 / 10 674 | *"the idea is that both of these bodies are pretty independent so you can trust them"* (of 80 PLUS **and** Cybenetics) | **CONTRADICTS psu.md** - he does not call 80 PLUS meaningless |
| `Xx6rFaKaqp0` | 10 674 / 10 674 | *"a big thank you the Corsair for helping make this video possible"*; *"Corsair who kindly sponsored this video"* | **undisclosed in psu.md** - sponsored by a PSU vendor |
| `Xx6rFaKaqp0` | 10 674 / 10 674 | *"many have what we call a zero RPM mode"*; *"I always prefer a fully modular power supply"* | **exact** - fan-stop and modularity asks |
| `4et8XC9QG00` GeekaWhat, 2026-03-26 | **19 627 / 19 627** | *"it's not that's the power supply this GPU needs, it's that's the power supply we'd recommend for a build with this GPU that kind of sits in the expected region"* | **exact** - vendor wattage is a whole-system figure |
| `4et8XC9QG00` | 19 627 / 19 627 | *"The GPU recommended wattages are the most important thing to swear by in my opinion."* | **exact, and it supports the pick** - AMD's own number for a 9070 XT is 750W |
| `4et8XC9QG00` | 19 627 / 19 627 | *"there's some great testing that's done as part of what's known in the PC building world as the PSU tier list ... Big shout out to SP out for putting this together"* | **exact** - the second of the two guides that lead with the tier list |
| `4et8XC9QG00` | 19 627 / 19 627 | *"lots of power supplies nowadays will also come with silent features or semi-fanless operation"* | **exact** |
| `4et8XC9QG00` | 19 627 / 19 627 | *"a quick word from today's video sponsor ... this year marks the 20th anniversary of ASUS Republic of Gamers"* | **undisclosed in psu.md** - ASUS-sponsored |

### What the full reads changed

**1. The connector count on the pick is not what the doc says it is, and the video is the doc's
own cited source.** [psu.md](components/psu.md) states the Pure Power 13 M 750W's four 6+2-pin
connectors arrive on *"three cables - one dual-head and two single-head"*, and reconciles the
retailer count with the video by saying *"retailers quote four connectors, the video quoted three
cables"*. Read in full, the video says no such thing. It says **three connectors**, not three
cables - *"it comes with three PCIE 6+2 pins"* - and adds a constraint the doc never records:
*"One of them you have to not use the 12 V high power for."* That is a **shared-port exclusion**,
not a cable-count quirk.

This matters for exactly one build. The **Max build with the Red Devil XT needs 3x 8-pin.** On
PC Builder's reading that is the entire PCIe allocation of the unit, available only if the
12V-2x6 goes unused. It does go unused here - no AMD card in these builds uses it - so **the pick
still works**, but the doc's reasoning for why it works is wrong and the margin is thinner than
stated. Going into [pc_build.md](../pc_build.md) as open.

**2. JayzTwoCents is a second source that sizes this build above 750W, not the
only-one-is-PC-Builder the doc claims.** psu.md says of PC Builder's 1.5x rule: *"It is also the
only source of the five that would size this build above 750W"*. Jay's blanket answer is 850W,
which the doc does record - but his actual recommendation for a card of this class is **1000W**:
*"i usually recommend uh a thousand watt power supply for anyone running any sort of high-end
components ... something like a 6800 xt or higher."* An RX 9070 XT is above that line. So the
count is **two of five**, not one. The conclusion survives - Jay's 2021 reasoning predates ATX 3.x
and argues from the efficiency curve, which the doc already handles - but "the only source" is
withdrawn.

**3. "GeekaWhat says vendor wattage overestimates" is half right, and the wrong half matters.**
The 2026 video supports it. The **2023 video says the opposite**: *"the GPU figure is always a
good one to go off"*, and it tells you to add **more** on top for a high-end CPU. And the 2026
video's closing verdict is *"The GPU recommended wattages are the most important thing to swear
by."* Neither GeekaWhat video tells you to buy below the vendor figure. Since AMD's figure for the
9070 XT **is** 750W, this does not move the pick - it removes an argument the doc leaned on and
replaces it with a cleaner one.

**4. Two of the five guides are vendor-sponsored, and psu.md discloses neither.** GeekaWhat 2023
is **sponsored by Corsair**, a PSU manufacturer whose units the video then walks through - the
most direct conflict of interest in the set. GeekaWhat 2026 is **sponsored by ASUS**. The audit
already flagged this pattern on `PfAsVb4Bza4` (ASUS / motherboards); it recurs here.

**5. One claim in psu.md is sourced to these videos and is in none of them.** The doc states:
*"Also noted: the 12V-2x6 cable occupies two PSU-side sockets and both plugs must be connected, an
ATX 3.1 requirement."* It sits inside the "Video cross-check, five buying guides" section. **It
appears in none of the five transcripts.** Recorded here as **unsourced**, not as wrong.

**Not overturned: the 750W sizing itself.** Four of the five guides land on or below 750W for a
card of this class, AMD's own figure is 750W, and the one rule that sizes higher (1.5x
PCPartPicker) is explicitly a substitute for checking ATX 3.1 certification, which this unit holds.

**Frames:** none of the five guides is a benchmark video and no doc attributes a *figure* on
screen to any of them - every claim above is narration, quoted. One frame is still taken for
`SS7P63fLE_8` at 13:21, the only on-screen number a doc reuses (OuterVision's 469W), and is
recorded in the frames pass below.

## SSD - 8 of 8 read IN FULL, 2026-09-13

**There are eight SSD videos, not four.** Dmytro sent them in two separate messages, six weeks
apart, and [storage.md](components/storage.md) wrote up only the second batch:

| Batch | Sent | Videos | Written up in storage.md |
|---|---|---|---|
| `03d54ca8:1361` | *"well check online / also check these videos"* | `IqqarIpZET8`, `auaAty99KM0`, `kmxVz5jmG7A`, `hpXXptnlfFw` — four Samsung 990 comparisons | **no** — only `hpXXptnlfFw` is cited, and only for one number |
| `a43557ac:931` | *"pls check these videos whether there is anything useful or smth we missed"* | `3uG1hGXh5xU`, `3f9hEn5_QZw`, `pdyniBtGcDo`, `a_eea_JHGkM` | **yes** — this is the doc's "What four SSD videos changed" |

> **Retraction.** An earlier version of this section said *"three of the four videos storage.md
> credits to Dmytro were never sent by him."* That was **wrong**, and wrong for the usual reason:
> I had assigned every video to a component by the topic of the message it arrived in, and the
> message at `a43557ac:931` sits in the middle of a run of RAM questions. Its four videos are all
> SSD videos. They were sent, storage.md read them, and its citations are accurate. The real
> finding is the opposite one — **the first four were never written up at all.**

Transcripts in [`sources/`](sources) as `ssd_<id>.md`.

### Batch 2 — the four storage.md actually used

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `3uG1hGXh5xU` Linus Tech Tips, 2026-04-08 | **8 948 / 8 948** | *"there is one situation where I would strongly recommend a DRAM cache, and that's as an operating system drive"* | **exact** |
| `3uG1hGXh5xU` | 8 948 / 8 948 | *"especially true as your drive starts to get older and more full, but you will notice a difference in system responsiveness during background operations like system updates or virus scans"* | **exact** |
| `3uG1hGXh5xU` | 8 948 / 8 948 | *"Modern drives with host memory buffer can be perfectly performant, especially as a secondary storage drive"* | **exact** |
| `3uG1hGXh5xU` | 8 948 / 8 948 | *"The top end SN850X does, but the SN7100 and SN770 do not"* | **exact** — the WD correction is right |
| `3uG1hGXh5xU` | 8 948 / 8 948 | *"SanDisk, Seagate, MSI, Corsair, Crucial, and Netac have all been guilty"*; *"Samsung ... but also Kingston and Acer Predator all list whether their drives have a DRAM chip"* | **exact** — both brand lists are correct |
| `3uG1hGXh5xU` | 8 948 / 8 948 | *"resorting to a third-party resource like TechPowerUp"*; *"real world performance trumps whatever you can put on a spec sheet"* | **exact** |
| `3f9hEn5_QZw` Tech Notice, 2024-12-19 | **22 899 / 22 899** | *"for most people 99% of the people Gen 5 drives are waste money"* | **exact** |
| `3f9hEn5_QZw` | 22 899 / 22 899 | *"if you are buying a Gen 4 Drive I would say you don't need an extra cooler on it unless your motherboard doesn't have a cooler on the slot ... if your motherboard already has a slot on that has some kind of heat cover you'll be completely fine"* | **exact** — the conditional is stated as the doc reports |
| `3f9hEn5_QZw` | 22 899 / 22 899 | *"cooling on Gen 5 drives is very very important"* | **exact** — the doc's quoted "very very important" is real |
| `3f9hEn5_QZw` | 22 899 / 22 899 | *"gigabyte on their motherboards actually does very good heating cooling which often is both-sided ... whereas Asus ... only the top slot may have double-sided cooling"* | **exact** |
| `3f9hEn5_QZw` | 22 899 / 22 899 | *"the best bank for buck there is roughly the solid ip44 Pro and Samsung 990 Evo plus one of them with Dam one of them without"* | **exact** — the "one with DRAM, one without" quote is real |
| `3f9hEn5_QZw` | 22 899 / 22 899 | *"we're looking at the **quick** system Drive Benchmark ... the Gen 5 drives yes they are actually a bit faster about 20 plus% faster than the highest end Gen 4 Drive"* | **CONTRADICTS storage.md** — wrong chart, see below |
| `3f9hEn5_QZw` | 22 899 / 22 899 | *"the industry standard is 600 terab written per 1 tbyte"*; *"The Sweet Spot is the 1 tbte"* | **exact** — supports the 1TB decision |
| `3f9hEn5_QZw` | 22 899 / 22 899 | *"the Gen 5 drives or gen five slots on the motherboard share bandwidth with something else like your GPU slot"* | **exact** — the Renegade G5 caveat is sourced |
| `3f9hEn5_QZw` | 22 899 / 22 899 | *"this video is brought to you by AMD ryzen Pro"* | **undisclosed in storage.md** |
| `pdyniBtGcDo` Tech Guided, 2024-01-03 | **11 402 / 11 402** | *"we recommend that you spend anywhere between 3 to 7% of your total budget on your SSD"* | **CONTRADICTS storage.md's "nothing usable"** — see below |
| `pdyniBtGcDo` | 11 402 / 11 402 | *"as a general rule of thumb 1 tabt of space should be enough for most users"* | **exact** — supports 1TB |
| `a_eea_JHGkM` PC Builder, 2026-05-02 | **16 608 / 16 608** | *"don't waste money on a Gen 5 NVMe SSD unless you find a really insane deal"* | **exact** |
| `a_eea_JHGkM` | 16 608 / 16 608 | *"cache only affects write speeds, not game loading or reading speeds"* | **exact** |
| `a_eea_JHGkM` | 16 608 / 16 608 | *"we always want to keep at least 15% of the SSD empty at any given time because it slows down as the drive fills up"* | **exact** — and the source is PC Builder, which the doc leaves unattributed |
| `a_eea_JHGkM` | 16 608 / 16 608 | *"it seems unlikely to happen until early 2027 at the earliest. And even then, it might only get to around $100 per TB"* | **exact** — the price outlook is verbatim |
| `a_eea_JHGkM` | 16 608 / 16 608 | *"many motherboards come with their own built-in heatsinks. Some of them may not fit an SSD with a built-in heatsink of its own. And third, manufacturers can claim if you remove the built-in heatsink on the SSD that it voids the warranty."* | **exact** — both heat-sink-SKU arguments |
| `a_eea_JHGkM` | 16 608 / 16 608 | *"This video is sponsored by VIP-SCDKey ... get a Windows 11 OEM license for a great price"* | **undisclosed** — the same grey-market-key sponsor already flagged on `VgWrOSG24Yg` |

### Batch 1 — the four never written up

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `IqqarIpZET8` Gadget Rivalry, 2026-07-06 | **469 / 469** | *"Heat. Heat. [music] Ooh. [music] [music] [singing]"* — the whole caption track, 4:24 of music with no speech | **no spoken content.** 323 views, auto-generated. No doc cites it |
| `auaAty99KM0` NASCompares, 2024-02-26 | **12 218 / 12 218** | *"the 990 Pro is the one with the highest read highest write and highest recorded iops ... it has the best and highest quality nand on board"* | **independent support for the pick**, unused |
| `auaAty99KM0` | 12 218 / 12 218 | *"the 990 Pro is just the most future proof of all the drives there on the table"* | **independent support**, unused |
| `auaAty99KM0` | 12 218 / 12 218 | *"the Evo there lack something called drram ... it actually utilizes onboard memory of the machine"*; *"if you put it in some systems ... that don't have the provision ... it lowers its performance"* | **exact** mechanism — note this is the plain **990 EVO**, not the EVO Plus |
| `kmxVz5jmG7A` Tech Notice, 2024-11-11 | **10 963 / 10 963** | *"this right now here is the best system drive that Samsung has offered or what I have tested we've got the 990 Pro slightly slower okay we're talking about 2% 2.5% slower"* | **exact** — storage.md's "~2-2.5%" is verbatim |
| `kmxVz5jmG7A` | 10 963 / 10 963 | *"usually the drives that don't have DRM cache absolutely fall apart"*; *"the Samsung 990 Pro ... with 1 tbte capacity ... able to make a lot better performance than the 990 Evo plus 2 TB version"* | **exact** — the consistency finding is verbatim |
| `kmxVz5jmG7A` | 10 963 / 10 963 | *"it's probably best going with the Evo rather than the Evo plus because the Evo offers better performance in pretty much every case scenario"* | **CONTRADICTS storage.md** — see below |
| `kmxVz5jmG7A` | 10 963 / 10 963 | *"offers 600 terabyt per terabyte endurance rating"*; *"Samsung offers 5 years of warranty"* | **exact** |
| `hpXXptnlfFw` proSSD, 2025-01-29 | **14 869 / 14 869** | *"потом скорость снижается до 850 Мб в секунду"* | **exact** — the "~850 MB/s, on the exact 1TB SKU" figure |
| `hpXXptnlfFw` | 14 869 / 14 869 | *"есть ssc cash небольшой 12%"* | **exact** — the "~12% SLC cache" figure |
| `hpXXptnlfFw` | 14 869 / 14 869 | *"результаты не всегда стабильные"* ("the results are not always stable") | **exact** — quoted correctly |
| `hpXXptnlfFw` | 14 869 / 14 869 | *"несмотря на нагрев, несмотря на цифры по температуре, троттлинга нет ... данное SSD можно использовать без радиатора"*, peak 65.9 °C | **new, not in storage.md** |
| `hpXXptnlfFw` | 14 869 / 14 869 | *"не вижу я смысла в его покупке"* ("I see no reason to buy it") | **CONTRADICTS storage.md** — see below |

### What the full reads changed

**1. The ~20% Gen 5 figure is attached to the wrong chart.** storage.md: *"Tech Notice measured
Gen 5 at ~20% faster on the **full-system-drive** random test - the one chart that matters here."*
The 20% is spoken over the **quick** system-drive benchmark, which Tech Notice defines as *"a
secondary drive on your PC ... where you store your little documents"*. His full-system-drive
chart — the one he calls *"probably the most important graph for most people"* — is a different
chart, and over it he says only that Gen 5 drives *"are on top"*, with no figure. **The number is
real; the chart it is attached to is not.** That matters because the doc uses it to justify the
Renegade G5's +1 899, on the strength of the chart that models this machine's actual use.
Going into [pc_build.md](../pc_build.md) as open.

> **Resolved 2026-09-13.** The chart correction stands and the claim is struck from storage.md.
> The two conclusions drawn from it here do not: the **+1 899** was 11 999 against the 990 PRO's
> *hotline floor* of 10 100, and same-shop at Telemart the G5 is **400 cheaper** than the PRO
> (12 399); and the speed gain is quantified outside the videos - **PCMark 10 Storage, 4 651 / 743
> against 8 062 / 1 178 MB/s** (StorageReview), already in storage.md. **Max keeps the G5.**

**2. "Nothing usable came from Tech Guided" is wrong, and what it missed is unflattering.** The
video carries a budget heuristic of the same kind the doc accepts from this channel for
motherboards: *"we recommend that you spend anywhere between 3 to 7% of your total budget on your
SSD."* The 990 PRO 1TB at 12 399 in the 115 389 Working build is **10.7%** — well above the
range. That is a cross-check the doc never ran, and unlike the motherboard one it does not pass.
It is not decisive on its own — the heuristic comes from a $1 000 build and this machine's drive
is deliberately chosen on QD1 latency for a work load — but "nothing usable" should not have
been written. Going into the open list.

**3. Both reviewers who actually tested the 990 EVO Plus tell you not to buy it.** Tech Notice's
closing recommendation is the **plain 990 EVO**, which beats the Plus on his quick-system, data
and consistency charts. proSSD, testing the exact **1TB** SKU this build would buy, ends on *"I
see no reason to buy it"*. storage.md carries the EVO Plus as *"the documented cheaper option,
-1 720"* on the strength of the one chart where it wins, quoted accurately, without recording
that the same reviewer's overall verdict goes the other way. **The pick is unaffected — the doc
buys the 990 PRO** — but the EVO Plus's standing as the live alternative is not what the sources
say. This is the same cherry-picking failure the GECID AC Shadows chart produced. Open.

**4. A drive neither doc considers beats the one that is shortlisted.** The plain **990 EVO** is
faster than the EVO Plus on three of Tech Notice's four charts and is the drive he recommends;
NASCompares independently calls it the power-efficiency pick. It is absent from storage.md's
shortlist and its Ukrainian price was never checked. Worth checking before the EVO Plus is
offered as the saving. Open.

**5. Three of the eight are sponsored, and storage.md discloses none.** Tech Notice by **AMD
Ryzen Pro**, PC Builder by **VIP-SCDKey** (grey-market Windows keys — the same sponsor the audit
flagged on `VgWrOSG24Yg`), LTT by a chair company (no conflict). None of it touches the SSD
conclusions; it is recorded because the pattern now holds across PSU, motherboard and storage.

**Not overturned:** the 990 PRO pick and essentially all of storage.md's second-batch
citations, which are verbatim accurate — the LTT DRAM section in particular is quoted correctly
line for line. NASCompares adds a third independent voice for the 990 PRO. The Gen 5 thermal
rules, the 15%-empty rule, the 600 TBW/TB yardstick and the early-2027 price outlook are all
located and exact.

**Frames:** no doc attributes an on-screen *figure* to any of these eight except the ~20% Gen 5
claim on `3f9hEn5_QZw`, which is resolved above from narration. `IqqarIpZET8` carries no
narration at all, so its content is on-screen only; frames for both are in the frames pass below.

## RAM - 5 of 5 read IN FULL, 2026-09-13

Five RAM videos, not ten. The ten-video count in the order list bundles two batches that turned
out to be SSD videos (`a43557ac:931`, four of them, now in the SSD section above) and one
CPU/GPU-combo guide (`UyKvDu9dZUs`, ScatterVolt — its own section below). Transcripts in
[`sources/`](sources) as `ram_<id>.md`.

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `eFmQG4BuiGw` Socket-X, 2026-05-21 | **17 507 / 17 507** | *"Micron announced that the crucial consumer brand is being gradually wound down with consumer shipments ending through 2026 while warranty and support continue afterward"* | **exact** — ram.md's Crucial wind-down is verbatim |
| `eFmQG4BuiGw` | 17 507 / 17 507 | *"Crucial memory offers one of the lowest failure rates in the consumer market"*; *"The trade-off is limited overclocking headroom"* | **exact** |
| `eFmQG4BuiGw` | 17 507 / 17 507 | *"They source their silicon dynamically from SK Hynix, Samsung, and Micron, depending on current batch pricing ... two identical mid-range kits bought months apart can feature entirely different internal silicon"* | **exact** — the Kingston lottery claim |
| `eFmQG4BuiGw` | 17 507 / 17 507 | *"The Fury Beast features low-profile stamped aluminum heat spreaders designed to sit under large dual tower air coolers without clearance conflicts"* | **exact** — the AK400 clearance note |
| `eFmQG4BuiGw` | 17 507 / 17 507 | *"Corsair prints a tiny version number on the physical stick sticker. If a user attempts to combine two separate vengeance kits with different version numbers, the system will frequently encounter severe memory training errors and constant boot loops"* | **exact** — the mechanism behind "never mix kits" |
| `eFmQG4BuiGw` | 17 507 / 17 507 | *"they lean heavily on well-binned SK Hynix silicon"* (Patriot) | **exact** |
| `eFmQG4BuiGw` — the rank claim ("every DDR5 IC is 16Gb, so a 16GB module can only be single-rank; dual-rank worth ~9%"), the secondary-timings table (36-38-38-80 vs 36-44-44-96), the A2/B2 slot rule, "games allocate a percentage of installed RAM" | 17 507 / 17 507 | **none of it appears in this transcript.** The video defers: *"if you want a full breakdown of timings and memory specs, I already made a dedicated RAM guide for that"* | **not read** — sourced to a Socket-X video Dmytro never sent |
| `05HRLuU--jI` Linus Tech Tips, 2026-02-26 | **9 397 / 9 397** | *"we tested four CPUs at eight different speeds of DDR5 running as slow as 4,800 mega transfers per second"* | **exact** |
| `05HRLuU--jI` | 9 397 / 9 397 | *"as long as you can get your hands on something, anything with a tuned expo profile, you probably won't notice a difference"* | **exact** — but said of the **9950X**, see below |
| `05HRLuU--jI` | 9 397 / 9 397 | *"there is a little bit of variance. Our 4,800 megat transfer per second kit does sit in last place and **6,000 mega transfer CL30 is still the sweet spot**"* (9800X3D) | **CONTRADICTS ram.md** — see below |
| `05HRLuU--jI` | 9 397 / 9 397 | *"our GDAU compile test does see a decent improvement with higher speed memory on the 14900 K"* | **exact** — the compile exception is real |
| `05HRLuU--jI` | 9 397 / 9 397 | *"there are cases here where using 16 gig versus 24 gig modules is going to make as much of a difference or more"* | **exact** — the capacity-over-speed note |
| `05HRLuU--jI` | 9 397 / 9 397 | *"if you're making money with your machine, you might want to consider ponying up for a high-speed, low latency kit, even at today's extortionate pricing"* | **CONTRADICTS ram.md's use of this video** — see below |
| `9-yjwxhmr40` PC Builder, 2026-04-11 | **14 036 / 14 036** | *"testing done by TechSpot, aka Hardware Unboxed, with a Ryzen 7700X, the difference in performance at 1080p with an RTX 4090 across seven games was only 8 and 1/2% between the sweet spot DDR5 6000 CL30 kit and a DDR5 6000 CL40 slower kit"* | **exact** — the 8.5% figure is verbatim, including the test rig |
| `9-yjwxhmr40` | 14 036 / 14 036 | *"13th and 14th gen Intel platforms cared even less with only about a 5.6% difference between DDR5 6000 CL30 and even the slower DDR5 5200 CL40 kit"* | **exact** — the 5.6% figure is verbatim |
| `9-yjwxhmr40` | 14 036 / 14 036 | *"RAM prices are beginning to come down"* | **exact** — the April 2026 price dissent ram.md records |
| `9-yjwxhmr40` | 14 036 / 14 036 | *"many of the kits I'm seeing around 6000 CL38 or 36"*; *"DDR5 5200 CL40 or faster, that's likely fine"* | **exact — and it supports the CL36 pick directly** |
| `9-yjwxhmr40` | 14 036 / 14 036 | *"multiply the CAS latency by 2000, then divide that number by the RAM speed"* — 6000 CL30 = 10 ns, 6400 CL32 = 10 ns, 6000 CL28 = 9.33 ns | **new, not in ram.md** — see below |
| `9-yjwxhmr40` | 14 036 / 14 036 | *"because DDR5 memory controllers generally don't do well with four-stick configurations, I only recommend two sticks maximum for DDR5"* | **exact** — independent support for 2x16 |
| `9-yjwxhmr40` | 14 036 / 14 036 | *"Don't waste your money on more than 32 GB of RAM for a gaming PC build in 2026"* | **exact** — independent support for capping at 32GB |
| `9-yjwxhmr40` | 14 036 / 14 036 | *"This video is sponsored by Seasonic"* | **undisclosed** — and psu.md weighs a SeaSonic unit |
| `mkpCvaBBo-c` GamingScan, 2019-11-02 | **12 770 / 12 770** | *"we don't advise combining different RAM modules especially ones from different manufacturers ... it can lead to some unexpected compatibility issues crashes"* | **CONTRADICTS ram.md's "nothing usable"** — see below |
| `mkpCvaBBo-c` | 12 770 / 12 770 | *"rather its servers and workstations running memory hungry software ... to get a tangible performance boost from all the added bandwidth"* (of quad-channel) | **CONTRADICTS ram.md's characterisation** — see below |
| `mkpCvaBBo-c` | 12 770 / 12 770 | *"32 gigabytes is a bit too much for gaming at the moment ... you're better off sticking to 16 gigabytes"* | **genuinely obsolete** — ram.md is right that the capacity advice is DDR4-era |
| `vbHyF50m-rs` Gamers Nexus, 2020-05-22 | **16 698 / 16 698** | *"as far as the rain and the core you can expect a combined total somewhere between five and nine percent uplift ... and then once you throw memory in there you start going past the 10% barrier but still under 20%"* | **not cited by any doc** — see below |
| `vbHyF50m-rs` | 16 698 / 16 698 | *"once you get to the point where you're paying 100 bucks more for memory you're kind of approaching just the better class of CPU like a 10 700 K and now there's a question as to how much value does the uplift in the CPU provide versus the uplift in memory"* | **independent support for ram.md's verdict**, unused |
| `vbHyF50m-rs` | 16 698 / 16 698 | Blender: *"a reduction of 3.5% against the stand alone all core OC"*; 7-zip: *"another 1.6 percent improvement"* | **tension with LTT's compile finding** — see below |

### What the full reads changed

**1. ram.md cites LTT for "do not pay for CL30", and LTT names 6000 CL30 as the sweet spot.**
The doc's summary is *"On a 9800X3D and a 9950X, anything with a tuned EXPO profile is
indistinguishable"*. The "anything with a tuned EXPO profile" line is said of the **9950X**. Of
the **9800X3D** he says the opposite in the same breath: *"6,000 mega transfer CL30 is still the
sweet spot."* Merging the two CPUs into one sentence dropped the half that names CL30.

This does not overturn the pick, and the reason is worth stating because it is stronger than what
the doc currently argues: **this build's CPU is a 9700X — a non-X3D part, the 9950X case, not the
9800X3D case** — and the source that *does* test the exact question, PC Builder quoting Hardware
Unboxed, puts CL30-vs-CL40 at **8.5% at 1080p with a 4090** and says *"6000 CL38 or 36"* kits are
fine. The CL36 pick stands on that, not on LTT. Going into [pc_build.md](../pc_build.md) as open
— the citation needs fixing, not the decision.

**2. And LTT's advice for *this* machine's workload points the other way.** The doc uses the video
to justify not paying for tighter timings. The video's productivity conclusion is *"if you're
making money with your machine, you might want to consider ponying up for a high-speed, low
latency kit, even at today's extortionate pricing"*, and its one measured exception is a
**compile test**. ram.md's own justification for 32GB is *"IDE + language servers, Claude Code
over heavy repos"* — the compile half. So on the doc's own framing of the workload, LTT's
recommendation is the low-latency kit. Recorded as a real tension, not a decision: the counter-
evidence is Gamers Nexus below, and the cost delta in the current DRAM market is large.

**3. Gamers Nexus measures the production case and finds almost nothing.** The one source here
that actually benchmarked memory tuning against production applications got **3.5% in Blender**
and **1.6% in 7-zip**, against 10-17% in games. That is the direct counterweight to LTT's compile
result and it lands on the doc's side. It is also **cited by no document** — and it is the video
the Reddit RAM guide Dmytro supplied leans on for its headline claim.

**4. The Reddit guide's headline claim overstates its own cited source.** The guide says GN
*"tune an i5 10600k to match the far more expensive i9 10900k in gaming"* and that *"a large part
of it is down to the high end RAM"*. GN's own breakdown: core plus cache overclock alone give
**5-9%**, and adding the memory tune takes it *"past the 10% barrier but still under 20%"* — so
memory contributes roughly **4-6 points of a 17-point total**, not "a large part". GN's closing
advice is to spend the money on a better CPU instead. **The guide's conclusion is not what its
source says**, and the source agrees with ram.md.

**5. "Nothing usable came from GamingScan" is wrong twice.** It carries the *"never mix kits"*
rule independently — the same rule ram.md derives from Corsair version numbers — and its
multi-channel failsafe argument. More importantly the doc's stated reason for dismissing it is
inaccurate: *"its quad-channel and four-stick advice is actively wrong for AM5"*. The video
recommends **two sticks**, and explicitly confines quad-channel's benefit to *"servers and
workstations"*, not gaming. Its capacity advice is genuinely obsolete; its channel advice is not
wrong. Second instance of this pattern after Tech Guided's SSD guide. Going into the open list.

**6. A method ram.md does not have.** PC Builder gives the absolute-latency formula — CL x 2000 /
speed, in nanoseconds — which makes kits directly comparable. Applied here: the build's **DDR5-6000
CL36 is 12.0 ns**, against **10.0 ns** for 6000 CL30 and 6400 CL32, and 9.33 ns for 6000 CL28. So
the pick carries a **20% higher absolute latency** than the kit two sources call the sweet spot.
That is the size of the compromise, stated in a number for the first time. Worth adding to
[ram.md](components/ram.md) whichever way the decision goes.

**7. A block of ram.md's brand section is sourced to a video that was never sent.** The rank
claim, the secondary-timings table, the A2/B2 slot rule and the "games allocate a percentage"
note are all absent from `eFmQG4BuiGw`, which defers to *"a dedicated RAM guide"* of its own.
Recorded as **not read**, not as wrong.

**Not overturned:** the brand, die and sourcing section — every line of it is verbatim accurate.
The 8.5% and 5.6% figures, the Crucial wind-down, the Corsair version-number mechanism, the
Kingston silicon lottery, the Fury Beast clearance note and the two-stick rule are all exact.

**Frames:** no doc attributes an on-screen figure to any of the five; every claim above is
narration, quoted.

## Monitor - 6 of 6 read IN FULL, 2026-09-13

Transcripts in [`sources/`](sources) as `monitor_<id>.md`. The channel attributions in
[monitor.md](components/monitor.md) are all correct, and so are its dates.

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `u2VbWEKHCWU` RTINGS, 2026-05-26 | **12 126 / 12 126** | *"monitors that get brighter than 300 to 350 nits are good enough to use in most well-lit rooms"* | **exact** |
| `u2VbWEKHCWU` | 12 126 / 12 126 | *"we measure the monitor's first response time, total response time, and overshoot in 72 different gray-to-gray transitions. We do this in every overdrive setting"*; *"cumulative absolute deviation, or CAD"* | **exact** — the CAD method is reported correctly |
| `u2VbWEKHCWU` | 12 126 / 12 126 | *"OLED monitors have the best motion handling with CAD of less than 15. Even the best LCD monitors struggle to have a CAD lower than 100"* | **exact** — both figures verbatim |
| `u2VbWEKHCWU` | 12 126 / 12 126 | *"A 240 Hz refresh rate has a frame time of 4.17 milliseconds, so the minimum input lag we could measure would be 2.08 milliseconds. Anything under 3 to 4 milliseconds for a 240 Hz monitor would be great"* | **exact** — the input-lag floor is verbatim |
| `u2VbWEKHCWU` | 12 126 / 12 126 | *"you'll notice a bigger change between 120 and 240 hertz than between 240 and 360 hertz"* | **exact** |
| `u2VbWEKHCWU` | 12 126 / 12 126 | *"IPS and TN monitors have low contrast ratios, so blacks look gray"*; *"Mini LED monitors are the next best option"* | **exact** |
| `6F0iI_OxU9E` Aman, 2026-04-06 | **15 111 / 15 111** | *"this is actually way more important for work than something like refresh rate"* (pixel density) | **exact** |
| `6F0iI_OxU9E` | 15 111 / 15 111 | *"honestly 60 hertz or even 120 hertz is completely fine. Higher refresh rates don't really make a difference in most work apps"* | **exact** |
| `6F0iI_OxU9E` | 15 111 / 15 111 | *"It's not great for working with text because of color fringing"* (OLED) | **exact** |
| `6F0iI_OxU9E` — *"only really matters if you're playing at a high competitive level"* | 15 111 / 15 111 | the sentence exists, but in **Step 5, Response time**: *"These only really matters if you're playing at a high competitive level"* — not about refresh rate | **misattributed** — right quote, wrong spec |
| `6F0iI_OxU9E` | 15 111 / 15 111 | *"around 350 nits should be your minimum ... Anything below that is basically cheap office-level brightness that feels just dim"*; *"if your setup is near a window or you're in the really bright room, then 500 nits should be your minimum"* | **CONTRADICTS monitor.md's Correction 1** — see below |
| `6F0iI_OxU9E` | 15 111 / 15 111 | *"if your games runs at around 300 FPS, then getting up to 300 hertz refresh rate monitor actually makes sense. But if your system can't reach those numbers, then there's no reason to spend extra"* | **exact** — supports the 180Hz argument |
| `2adjvq793Dc` ECPU, 2026-03-26 | **8 988 / 8 988** | *"they can have text clarity issues depending on their specific subpixel layout, making them kind of annoying for office type work"* | **exact** |
| `2adjvq793Dc` | 8 988 / 8 988 | *"240 Hz is the sweet spot for high-end and competitive gaming"*; *"Best all-around monitor in 2026, 1440p resolution, 27-in screen size, **144 to 240 Hz** refresh rate ... and IPS panel"* | **CONTRADICTS monitor.md's "every source"** — see below |
| `ptUchraop3c` The Tech Chap, 2023-05-20 | **22 023 / 22 023** | *"for me I still think a 27 inch 1440p 165hz IPS or VA is absolutely ideal"*; *"I think 144 or 165 Hertz is The Sweet Spot"* | **supports the 180Hz argument**, uncited |
| `ptUchraop3c` | 22 023 / 22 023 | *"some manufacturers claim one or two millisecond response times but these are their best case results and they're tested using extreme overdrive modes that can then introduce reverse ghosting"* | **exact** — independent support for Correction 2 |
| `ptUchraop3c` | 22 023 / 22 023 | *"the base tier that display hdr400 certification is actually kind of rubbish it only requires 400 nits of brightness in HDR content without any kind of local dimming"* | **exact** — independent support for "DisplayHDR 400 is not HDR" |
| `ptUchraop3c` | 22 023 / 22 023 | *"ideally particularly for gamers you want anything under 5 milliseconds"* | **the pick passes** — Q27G4XF is 4.6 ms G2G |
| `mtA4hqZb4IE` JayzTwoCents, 2024-12-31 | **25 629 / 25 629** | *"the perfect sweet spot ... possibly 27 in 1440p resolution 144 HZ refresh rate with a 1 millisecond response time"* | **supports the 180Hz argument**, uncited |
| `mtA4hqZb4IE` | 25 629 / 25 629 | *"if you're going to go larger than say 27 in on a panel you really want to go with 4K otherwise 1440p the text starts to look very blocky"* | **exact** — supports 27" 1440p |
| `mtA4hqZb4IE` | 25 629 / 25 629 | *"follow the sponsored Link in the description"* (Falcon Northwest) | **undisclosed** |
| `yKvj63oG7D0` MikMat Tech, 2022-04-15 | **4 018 / 4 018** | *"oled panels ... are mainly 4k monitors with a 60 to 120 hertz refresh rate"*; *"tn panels ... have the fastest refresh rates on the market"* | **obsolete** — both false in 2026; nothing in the docs rests on it |

### What the full reads changed

**1. "Every source says the same thing about high refresh rates" is not true — one of the six
says the opposite.** monitor.md opens the 240-vs-180 question with that sentence. Read in full,
the six split **4-1-1**:

| Source | On high refresh |
|---|---|
| RTINGS | diminishing returns past 240 |
| Aman | match the monitor to your actual FPS; 120-144 is the start |
| The Tech Chap | *"144 or 165 Hertz is The Sweet Spot"*, and *"27 inch 1440p 165hz IPS or VA is absolutely ideal"* |
| JayzTwoCents | sweet spot is *"27 in 1440p ... 144 HZ"* |
| **ECPU** | ***"240 Hz is the sweet spot for high-end and competitive gaming"***, and its all-round recommendation is **144-240 Hz** |
| MikMat Tech | silent |

The argument for the 180Hz panel is **stronger than the doc makes it**, because two sources it
never quotes — Tech Chap and Jay — both name a 27" 1440p panel at 144-165Hz as their ideal, which
is the Q27G4XF exactly. But "every source" is wrong and should be "four of six, with one
dissenting". Going into [pc_build.md](../pc_build.md) as open — the recommendation is unchanged,
the claim behind it is overstated.

**2. Correction 1 (the "dim at 365 nits" retraction) rests on one source, and a second source in
the same set supports the original wording.** RTINGS' 300-350 line is quoted correctly. But Aman
gives **350 nits as a floor, not a comfort point** — *"anything below that is basically cheap
office-level brightness that feels just dim"* — and **500 nits as the minimum for a bright room
or a setup near a window.** monitor.md's own characteristics table still says *"Under ~400 nits is
noticeably dim in a bright room"*, so the document now contradicts itself: the table says one
thing and Correction 1 says another.

The honest synthesis is the one Correction 1 half-reaches: **365 nits clears the threshold for a
controlled room and does not clear it for a bright one.** Since this machine is a desk-bound work
machine, that is probably fine — but the retraction went further than the sources support, and
the internal contradiction should be resolved. Open.

**3. Two of the six sources are never quoted anywhere in the doc, and both support its
conclusions.** The Tech Chap's *"27 inch 1440p 165hz IPS or VA is absolutely ideal"* and Jay's
*"27 in 1440p ... 144 HZ"* are the most direct endorsements of the Lean pick in the entire set,
and neither appears in monitor.md. The Tech Chap also independently confirms **both** of the
doc's corrections — the overdrive-inflated 1 ms claim and DisplayHDR 400 being a badge rather
than HDR. Worth quoting rather than leaving as a name in a list.

**4. One of the six is obsolete and should be marked as such.** MikMat Tech (2022) states that
OLED panels are *"mainly 4k monitors with a 60 to 120 hertz refresh rate"* and that TN panels
*"have the fastest refresh rates on the market"*. Both were arguable in 2022 and are false in
2026. Nothing in monitor.md rests on it, but it is listed among the six without a date caveat
while the 2023 and 2024 sources are dated.

**Not overturned:** every RTINGS figure — the 300-350 nit line, CAD under 15 vs 100, the 2.08 ms
input-lag floor and the 3-4 ms band, the 120-240 vs 240-360 comparison. The ECPU and Aman OLED
text-fringing quotes. The 4K refusal is Dmytro's and stays closed.

**Frames:** no doc attributes an on-screen figure to any of the six; every claim above is
narration, quoted.

## CPU cooler - 3 of 3 read IN FULL, 2026-09-13

Transcripts in [`sources/`](sources) as `cooler_<id>.md`. Channel attributions and dates in
[cooling.md](components/cooling.md) are all correct.

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `ju2OYF16RKA` PC Builder, 2026-03-22 | **30 640 / 30 640** | *"we've got the Ryzen 7 CPUs in the 7000 and 9000 series. This is like the Ryzen 7700X, **9700X**, and the big X3D CPUs ... These are a little tougher to cool than the regular Ryzen 7 CPUs for sure. I recommend a minimum of a dual tower air cooler for both performance and noise."* | **exact** — the 9700X is named, and the quote is not taken out of context |
| `ju2OYF16RKA` | 30 640 / 30 640 | *"For Ryzen 5 7000 9000 series CPUs, I recommend at least a budget tower air cooler. And honestly, this is probably all you really need as long as your case has good airflow."* | **exact** — the AK400 is above requirement on Lean's 7500F |
| `ju2OYF16RKA` | 30 640 / 30 640 | *"The Ryzen 7500F and 7600 non-X do come with an included stock cooler. It's fine, but given how cheap budget tower air coolers are, I'd switch it out."* | **exact** |
| `ju2OYF16RKA` | 30 640 / 30 640 | *"the ID-COOLING Frozen A620 Pro SE. Don't get the original A620. Make sure you get the Pro SE version"*; *"It's tied with the Phantom Spirit"*; *"$27. It is always the cheapest."* | **exact** — all three fragments verbatim |
| `ju2OYF16RKA` | 30 640 / 30 640 | *"virtually every CPU cooler in 2026 will come with enough paste for at least one application"*; *"Thermal paste will typically degrade in 3 to 5 years"*; *"spend that $20 getting a better cooler"* | **exact** — though he then recommends a $7 tube of MX-4, so "buy none" is slightly firmer than he puts it |
| `ju2OYF16RKA` | 30 640 / 30 640 | *"Short answer, no for AMD"* (contact frames); *"Installing a contact frame means removing the motherboard retention mechanism, which carries a small risk of damaging the motherboard pins"* | **exact** |
| `ju2OYF16RKA` | 30 640 / 30 640 | *"Just go either 240 or 360"* | **exact** |
| `ju2OYF16RKA` | 30 640 / 30 640 | *"This video is sponsored by Seasonic"* | **undisclosed** — same sponsor as the RAM guide `9-yjwxhmr40` |
| `7f-Guxj4kl0` Tech Guided, 2023-12-24 | **14 206 / 14 206** | *"if your budget is $1,000 or more ... we recommend that you spend anywhere from 3 to 7% of your budget on your cooler"* | **new, not in cooling.md** — see below |
| `7f-Guxj4kl0` | 14 206 / 14 206 | *"there is no standardized way to calculate TDP Intel and AMD calculated differently"*; *"a better way would be to check benchmarks carried out by experts"*, naming **Gamers Nexus and Hardware Unboxed** | **undercuts the doc's own defence of the pick** — see below |
| `7f-Guxj4kl0` | 14 206 / 14 206 | *"if your budget is under $800 we typically recommend that you get a processor that doesn't require a third-party cooler"* | **supports dropping Lean's cooler** |
| `dwvlv7VPW_c` Hardware Whisperer, 2025-01-08 | **6 031 / 6 031** | *"Tower coolers usually have a higher TDP ... rating, ranging from 150W to over 250W"*; *"Tower coolers are an excellent choice for high-performance CPUs where overclocking is not required"* | **supports the single-tower pick**, uncited |

### What the full reads changed

**1. The dual-tower quote is accurate, and reading it in full makes the counter-argument weaker,
not stronger.** cooling.md's defence is that PC Builder's recommendation is aimed at the
**105W/142W 7700X** and that the 65W/88W 9700X sits below that class. Read in context, PC Builder
puts the 7700X **and the 9700X in the same tier by name**, and gives the tier below — Ryzen 5
7000/9000, which includes Lean's 7500F — a separate and explicitly lighter recommendation. He is
not generalising from the 7700X; he sorted the 9700X into the dual-tower tier deliberately. The
doc's reading of the quote is honest, but its inference about what the reviewer meant is not
supported by the surrounding text. Open question 1 in cooling.md stays open and its balance
shifts toward stepping up.

**2. Tech Guided says the doc's method is the wrong one — and names the right one.** cooling.md
already concedes *"the pick currently rests on a wattage argument, not a measurement"*. Tech
Guided makes that concession sharper: TDP matching is *"not the most perfect way"* because
*"there is no standardized way to calculate TDP"*, and the fix is expert benchmarks from
**Gamers Nexus or Hardware Unboxed**. That is exactly the search the doc says is needed to close
the question, from a source in the same batch. Worth recording as the method, not just as a gap.

**3. A budget heuristic that cuts the opposite way from the SSD one.** Tech Guided applies the
same **3-7% of total budget** rule to coolers that it applies to SSDs. On the Working build
(115 389):

| Part | Cost | Share | Tech Guided's 3-7% |
|---|---:|---:|---|
| Samsung 990 PRO 1TB | 12 399 | **10.7%** | **over** |
| DeepCool AK400 | 1 699 | **1.5%** | **under** |

Same channel, same methodology, opposite verdicts — and the two together point at a reallocation
rather than at either number in isolation. Stepping Working/Max up to a Phantom Spirit 120 SE
(2 845) moves the cooler to 2.5%, still under the band; the +1 146 is roughly what dropping the
990 PRO to the EVO Plus would free. Recorded as an observation, not a recommendation — the
heuristic comes from a $1 000 build and both parts were chosen on stronger grounds than a
percentage. Going into [pc_build.md](../pc_build.md) as open.

**4. The third guide is not useless, and it supports the pick.** cooling.md says PC Builder *"is
the only one that bears on this build"*. Hardware Whisperer rates **tower coolers at 150W to over
250W** and calls them *"an excellent choice for high-performance CPUs where overclocking is not
required"* — which is the 9700X at 88W PPT, not overclocked, exactly. It is a generic explainer
rather than a measurement, so it does not close question 1, but it is a third source and it
points the other way from PC Builder.

**Not overturned:** every PC Builder quote in cooling.md is verbatim, including the A620 Pro SE
warning, the Wraith Stealth line, the paste rules, the contact-frame rule and the 280mm advice.
The Lean decision to drop the cooler is supported twice over — by PC Builder's stock-cooler line
and by Tech Guided's under-$800 rule.

**Frames:** no doc attributes an on-screen figure to any of the three; every claim above is
narration, quoted.

## Case - 5 of 5 read IN FULL, 2026-09-13

Transcripts in [`sources/`](sources) as `case_<id>.md`. All five channel attributions and dates
in [case.md](components/case.md) are correct.

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `bT_SznZRKpA` PC Builder, 2026-03-12 | **29 913 / 29 913** | *"I recommend spending 5 to 10% of your overall PC budget on the case itself, including any additional fans"* | **exact** |
| `bT_SznZRKpA` | 29 913 / 29 913 | *"I recommend at least two intake fans and one exhaust fan as a minimum"* | **exact** |
| `bT_SznZRKpA` | 29 913 / 29 913 | *"with the increased use of metal mesh to intercept dust. I think negative pressure cases are absolutely fine in 2026"*; *"you don't need mesh filters at the exhaust points, just where the air is coming into the PC build"* | **exact** |
| `bT_SznZRKpA` | 29 913 / 29 913 | *"only the worst budget PC cases use uncontrollable Molex fans any longer"* | **exact** |
| `bT_SznZRKpA` | 29 913 / 29 913 | *"my favorite front intake PC case of all time, and that is the Leanly **Lancool 216**"*; *"The two fans in the front are 160 mm ARGB ... You can spin these fans much slower and get similar air flow ... and they're almost silent."* | **CONTRADICTS case.md's framing** — see below |
| `bT_SznZRKpA` | 29 913 / 29 913 | *"This video is sponsored by VIP SCed Key"* | **undisclosed** — third appearance of this sponsor |
| `fLxP3u4xho0` GeekaWhat, 2025-09-30 | **31 177 / 31 177** | *"the first thing I would look at with a case is airflow ... The first would be the mesh or lack of mesh ventilation on the front"* | **exact** — supports the mesh-front rule |
| `fLxP3u4xho0` | 31 177 / 31 177 | *"Spending an extra 20 or $30 ... on a case and getting extra fans in exchange can actually save you money down the line"* | **exact** — supports the included-fan-value criterion |
| `fLxP3u4xho0` | 31 177 / 31 177 | sponsor read for the **Gigabyte Aorus Master 16** laptop | **undisclosed** |
| `vhyqtZx0NHM` Tech Guided, 2024-01-06 | **15 862 / 15 862** | *"we recommend allocating around 5 to 10% of your total budget to your case"* | **exact** — the second source for the 5-10% rule |
| `vhyqtZx0NHM` | 15 862 / 15 862 | *"cases that have grilled or mesh panels are ideal ... try and choose a case that has grilled or meshed panels especially on the front of the case"* | **exact** — supports the mesh-front rule |
| `xhy4KrcbcQA` Mr Matt Lee, 2025-03-10 | **10 366 / 10 366** | *"An airflow focused ATX tower ... will have a mesh front panel for air intake along with a rear and top exhaust ... the front intake directly feeds the graphics card"* | **exact** — supports the mesh-front rule |
| `xhy4KrcbcQA` | 10 366 / 10 366 | *"ideally you want to aim for at least an inch of clearance between the power supply shroud and the fans on your graphics card any less than this you'd be increasing noise levels while simultaneously restricting the airflow"* | **new, not in case.md** — a checkable clearance rule |
| `sDqOUfqcLY0` CORSAIR, 2019-08-10 | **4 789 / 4 789** | *"however you want your case to look or perform Corsair has you covered"* — the video is a Corsair product ad throughout | **contains no mesh-front claim at all** — see below |

### What the full reads changed

**1. case.md says the five guides do not bear on the pick. One of them names the pick as its
favourite case, for the exact reason the pick was bought.** The document says: *"the
recommendations in them are US-market cases (Thermaltake V170, Okonos Aqua 3/7, Montech XR,
Gamdias Atlas M1) that are not sold here."* Those four are correctly identified — they are PC
Builder's **budget and mid-range** picks. The list stops before his premium section, where he
says: *"my favorite front intake PC case of all time, and that is the Leanly Lancool 216."*

And his reason is the stated criterion, not aesthetics: *"The two fans in the front are 160 mm
ARGB ... You can spin these fans much slower and get similar air flow to for instance 3 120
millimeter fans and they're almost silent."* That is an airflow-per-noise argument for the exact
two 160mm intakes case.md lists in its fan table.

**The decision does not change — it is already the Lancool 216.** What changes is that the doc
records "nothing in them changes the Lancool 216" as if the guides were silent, when the most
current of them independently endorses it. Under a thermals-and-noise-only brief that is
supporting evidence the doc threw away. Going into [pc_build.md](../pc_build.md) as open, to be
added rather than decided.

**2. "Mesh front is the single biggest thermal decision — all five" is four of five.** Tech
Guided, Mr Matt Lee, GeekaWhat and PC Builder all support it, and GeekaWhat's framing is the
closest to the doc's wording. **The CORSAIR 2019 video does not mention mesh once.** It is a
five-minute vendor advertisement that ends on *"Corsair has you covered"*, and its only cooling
content is "check how many fans your case supports" and "dust filters are good". case.md already
labels it `(2019, vendor)`; the attribution to "all five" should be narrowed to four.

**3. A clearance rule none of the docs carry.** Mr Matt Lee: **at least an inch of clearance
between the PSU shroud and the GPU's fans**, because less than that *"increas[es] noise levels
while simultaneously restricting the airflow"*. This is a noise-and-thermals rule, which is the
whole brief, and it is checkable against both picks with a ~300mm 9070 GRE. Not checked here —
recorded as a check to run. Open.

**4. The 5-10% budget rule is confirmed by two sources independently**, and case.md's arithmetic
against it is correct: Working 4.3%, Lean 2.5%, both under the band. Note this is the **third**
Tech Guided percentage heuristic in this audit, and the three do not point the same way — SSD
10.7% (over), cooler 1.5% (under), case 4.3%/2.5% (under). Taken together they describe a build
that is heavy on storage and light on chassis and cooling.

**Not overturned:** every fan-count, filter and pressure rule in case.md is verbatim accurate,
and the doc's central judgement — that **none of the five contains a thermal or noise
measurement**, so Gamers Nexus' noise-normalised data outranks them — is **correct and confirmed
by reading all five in full.** No measurement appears in any of them. The CC560 V2's lack of a
lab test is not closed by anything here, exactly as the doc says.

**Frames:** no doc attributes an on-screen figure to any of the five; every claim above is
narration, quoted.

## Build technique / compatibility - 4 of 4 read IN FULL, 2026-09-13

Transcripts in [`sources/`](sources) as `build_<id>.md`. All four attributions and dates in
[pc_build.md](../pc_build.md) are correct.

| Video ID | chars read / total | Verbatim quote or frame | Verdict |
|---|---:|---|---|
| `PsqulPtiR3g` ScatterVolt, 2025-09-19 | **28 463 / 28 463** | *"Most modern-day entry-level CPUs, whether it's like an Intel Core Ultra 235 or Ryzen 57500F or even 9600X, can handle pretty much any modern-day GPU that isn't an RTX 5090"* | **exact** |
| `PsqulPtiR3g` | 28 463 / 28 463 | *"Those of you who need to worry about bottlenecks are those of you who are going to exclusively play at 1080p on very easy to run PC games like Valerant, Counterstrike 2, or Fortnite"* | **exact** |
| `PsqulPtiR3g` | 28 463 / 28 463 | *"if you're working with DDR5, 32 GB, that's all you need"* | **exact** |
| `PsqulPtiR3g` | 28 463 / 28 463 | *"if you want to be safe, you can get something that's an additional 100 watts above that recommended number"* | **exact** |
| `PsqulPtiR3g` @ 17:18 | 28 463 / 28 463 | `frames/PsqulPtiR3g_17m18s.png` — on-screen card reads **"AM5 ideal RAM kits: 6000mhz CL30 DDR5 / 6000mhz CL28 DDR5"**, **"LGA 1851 ideal RAM kits: 6400mhz CL32 DDR5"** | **card transcribed exactly** — but see below on "the audio never states" |
| `PsqulPtiR3g` | 28 463 / 28 463 | *"the only thing I look out for ... is ensuring your SSD has a DRAM controller"* | **independent support for the 990 PRO**, unused |
| `PsqulPtiR3g` | 28 463 / 28 463 | *"while 1 TB of SSD storage may be fine now, it may not be fine in a few years time. So, 2 TB if you can get to that amount is appreciated"* | **CONTRADICTS the 1TB capacity decision** — see below |
| `PsqulPtiR3g` | 28 463 / 28 463 | *"I would say it's good to aim to at least have four case fans"* | **CONTRADICTS case.md's fan sufficiency** — see below |
| `PsqulPtiR3g` | 28 463 / 28 463 | *"Six cores is all you need for gaming in 2025 ... Eight is recommended"*; *"even your standard B850 motherboard ... can handle all CPUs other than those 12 and 16 core variants"* | **exact** — supports the 9700X and the B850 |
| `PsqulPtiR3g` | 28 463 / 28 463 | *"I got to give a thank you to Corsair for not only sponsoring this video series, but for also sponsoring the parts for the PC"* | **undisclosed** — and the video then demonstrates Corsair PSUs, coolers and fans throughout |
| `rwfjm7fSLWE` GamingScan, 2020-02-01 | **11 343 / 11 343** | *"power supplies are at their best when they operate between 50 and 80 percent of their maximum capacity"* | **exact** — the correction in pc_build.md is correctly sourced |
| `rwfjm7fSLWE` | 11 343 / 11 343 | AM4 / LGA1151 / PCIe 3.0 throughout; *"there are still no GPUs that require this newer interface"* (PCIe 4.0) | **obsolete** — 2020, DDR4-era; nothing else in it is usable |
| `-8LMML_EiMg` JayzTwoCents, 2021-01-22 | **25 386 / 25 386** | *"you've just occupied one channel with two sticks of ram ... you're forcing single channel"*; *"consult your manual to figure out which is the appropriate ... slots"* | **exact** — the dual-channel error, and it is this video that carries it |
| `-8LMML_EiMg` | 25 386 / 25 386 | *"the spec states that an 8-pin pci express power connector is rated to 150 watts ... 75 watts of power for the graphics card also comes from the socket"*; *"if you go with a power supply that has individual cables for your pcie you are now operating perfectly within spec"* | **CONTRADICTS psu.md's cabling rule** — see below |
| `-8LMML_EiMg` | 25 386 / 25 386 | *"I have seen up to 10 degrees celsius drop by moving from pool config on an air cooler to push config"*; *"if you're running an air cooler and you only have one fan push is the only config"* | **new, not in cooling.md** — the AK400 ships with one fan |
| `-8LMML_EiMg` | 25 386 / 25 386 | *"i still make the stupid mistake of forgetting to remove the clear plastic label"* (cooler coldplate film) | **handover item**, not recorded anywhere |
| `0L7SBpZXnsE` optimum, 2022-11-19 | **10 613 / 10 613** | *"mixing power supply cables ... that's a one-way ticket to potentially frying some of your Hardware"* | **exact** — a **third** independent source for the never-reuse-PSU-cables rule |
| `0L7SBpZXnsE` | 10 613 / 10 613 | *"double check in the Bios whether your fans are set up for pwm or DC operation ... three pin fans are DC and 4 pin is pwm"* | **qualifies case.md's auto-detect assumption** — see below |
| `0L7SBpZXnsE` | 10 613 / 10 613 | *"if you've just built a fresh PC build and it's blue screening out of the box then unstable memory is most likely why. The first thing that you can try ... is updating your motherboard's bios"* | **handover item**, not recorded |
| `0L7SBpZXnsE` | 10 613 / 10 613 | *"you simply don't need an i7 or an I9 or a ryzen 9 CPU when it comes to just gaming"* | **consistent** — the 9700X is justified on work, not games |

### What the full reads changed

**1. The frames pc_build.md says it pulled were never saved — and I have now pulled them.** The
document states: *"Frame check (not transcript-only). Stills pulled at the bottleneck, RAM and
PSU sections of the ScatterVolt video and the PSU section of GamingScan's."* Before this pass
[`frames/`](frames) contained **twelve PNGs, all four of them GPU videos.** No ScatterVolt or
GamingScan frame existed. The claim was not re-checkable, which is the exact defect this audit
was opened to fix. Three ScatterVolt frames are now on disk, including
`frames/PsqulPtiR3g_17m18s.png`.

**2. The card is transcribed exactly; "a claim the audio never states" is wrong.** The frame
confirms the card word for word. But the narration **does** state two of its three lines: *"For
an AM5 gaming PC, choose a RAM kit that is 6,000 MHz for the [CL]30"* and *"6400 MHz with a cast
latency 32 will work with these Intel Core Ultra CPUs"*. Only the **6000 CL28** line is
on-screen only. The substantive point survives untouched — this is a third source preferring
CL30, and ram.md overrules it on measured grounds — but the framing should be corrected.

**3. JayzTwoCents contradicts psu.md's cabling instruction, and so does psu.md's own source.**
psu.md tells the assembler: *"Use the dual-head cable for two of the card's three 8-pin sockets,
and one single-head cable for the third."* Jay's rule is the opposite — **one cable per
connector, pigtails avoided** — with the spec arithmetic behind it: an 8-pin is rated 150W, the
slot supplies 75W, so a daisy-chained pair is being asked for more than the single cable's share.
And PC Builder, the source psu.md actually cites, says *"one cable per connection **for the first
two** eight-pin plugs, then you can daisy chain **the third**"* — which is also the reverse of
what the doc instructs. **Both sources put the singles first and the daisy-chain last; the doc
puts the daisy-chain first.** With a 3x 8-pin Red Devil this is a real assembly instruction going
to a shop. Going into [pc_build.md](../pc_build.md) as open, and it compounds the connector-count
finding already open from the PSU pass.

**4. "The most common build error in all four videos" is in one of them.** The A2/B2
dual-channel mistake is covered at length by **JayzTwoCents only**. GamingScan mentions dual
channel once in passing (*"check whether the motherboard and the CPU support dual channel"*),
ScatterVolt does not raise DIMM slot placement at all, and optimum's list does not include it.
The handover item is right and worth keeping — Jay's own advice is *"consult your manual"* — but
"all four videos" is not accurate.

**5. Two ScatterVolt recommendations cut against settled decisions, and neither is recorded.**
He asks for **2TB** of SSD (*"1 TB ... may not be fine in a few years time"*) against the build's
1TB, and **at least four case fans** against the Lancool 216's three. Both are opinions rather
than measurements and neither is a reason to reopen a closed decision — but the same video is
cited three times in pc_build.md for the claims that agree with it, and these two were not
recorded. Noted for completeness.

**6. A single-fan tower cooler should be in push, not pull** — Jay measured *"up to 10 degrees
celsius"* between the two, and *"if you're running an air cooler and you only have one fan push is
the only config"*. The AK400 is a single-fan tower and a shop is assembling it. Handover item.

**Not overturned:** every ScatterVolt and GamingScan quote pc_build.md relies on is verbatim —
the 7500F/9600X bottleneck line, the "32GB, that's all you need" line, the +100W PSU rule and the
50-80% PSU band. The withdrawal of "the least Lean-like line in the Lean build" is correctly
reasoned: 373W of 750W is 50%, the bottom edge of GamingScan's stated band.

## Motherboard - 7 of 7 read IN FULL, 2026-09-13 (was recorded as "6 of 6")

**The batch is seven videos, not six.** `BvtNCM5ms3U` was sent in the same message as the other
six (`e569baa2:433`) and **was never fetched, never transcribed and never read** by the pass that
recorded this component complete. It is now in [`sources/`](sources) with the rest.

The six earlier char counts were each exactly **16 higher** than the figures below. That is the
length of the `\n## Transcript\n\n` marker, not a discrepancy - this audit counts the body after
the marker, stripped.

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `BvtNCM5ms3U` GeekaWhat, 2025-12-30 | **15 270 / 15 270** | *"A Ryzen 5 or Core Ultra 5 is going to be fine with a fairly basic air cooler, but a Ryzen 7 or Core Ultra 7 or higher is going to be recommended with a liquid cooler."* | **exact** - and this is the source [cooling.md](components/cooling.md) cites as "GeekaWhat's 2026 parts guide". It was **unverifiable until now** |
| `BvtNCM5ms3U` | 15 270 / 15 270 | *"one of my rules from the very start is that we'd never sell a build that didn't have motherboard Wi-Fi. For me, that's a red line."* | **third independent source** for the onboard-Wi-Fi rule |
| `BvtNCM5ms3U` | 15 270 / 15 270 | *"The board shouldn't be costing more than the CPU as if it is, you're probably better allocating your cash elsewhere."* | **new checkable rule - the build passes.** Working: board 8 642 against CPU 15 099 |
| `BvtNCM5ms3U` | 15 270 / 15 270 | *"for AMD builds, if you're shopping on the mid-range, the B series chipset is what I'd go for"* | **exact** - supports B850 |
| `BvtNCM5ms3U` | 15 270 / 15 270 | *"Gen 5 is wildly overkill for gaming and Gen 4 is going to be your best friend. I normally recommend a one or two terabyte Gen 4 NVMe."* | **bears on the Renegade G5 decision** - a fourth voice for Gen 4 |
| `BvtNCM5ms3U` | 15 270 / 15 270 | *"pick up the cheapest 6000 MHz CL30 kit you can find"* | **fourth source naming CL30** - see the RAM section |
| `BvtNCM5ms3U` | 15 270 / 15 270 | *"The ASUS winter sale has landed ... check out the ASUS winter sale at the first link in the description"* | **undisclosed** - ASUS-sponsored |
| `7CVkfi0_mME` Socket-X, 2026-05-11 | **9 534 / 9 534** | *"A modern B650 or B760 offers effectively the same gaming performance as their more expensive siblings"* | **exact** |
| `7CVkfi0_mME` | 9 534 / 9 534 | *"32 GB across two sticks is the technical golden zone"*; *"Populating all four slots increases the electrical strain on the CPU's memory controller"* | **exact** |
| `7CVkfi0_mME` | 9 534 / 9 534 | *"While Gen 5 drives are the new spec king, they run incredibly hot. A heat sink for your primary NVMe drive isn't just for show."* | **exact** |
| `7CVkfi0_mME` | 9 534 / 9 534 | *"2.5 gigabit Ethernet is the new standard, but it's useless unless your router and internet plan actually support those speeds"* | **exact** |
| `7CVkfi0_mME` | 9 534 / 9 534 | *"A board with only two fan headers is a trap ... Aim for at least four or five"*; *"look for a BIOS flashback button"* | **new, not in motherboard.md** - both checkable against the ASRock pick |
| `7CVkfi0_mME` | 9 534 / 9 534 | *"PCIe 4 is still more than enough for modern GPUs ... the generation won't change your gaming FPS"* | **disagrees with GeekaWhat's** *"I always recommend PCI Gen 5"* |
| `ITBy9ckvSFY` Socket-X, 2026-05-15 | **13 031 / 13 031** | *"ASRock originally started as a lower-cost ASUS spin-off ... That reputation doesn't really fit anymore"*; strength is *"value engineering"* | **exact** |
| `ITBy9ckvSFY` | 13 031 / 13 031 | *"the AM5 voltage controversy during early Ryzen 7000 launches"* - in the **ASUS** section | **confirms the earlier withdrawal** of "never mentions the AM5 saga". It is a different event from the 9800X3D cluster |
| `ITBy9ckvSFY` | 13 031 / 13 031 | Gigabyte: *"a lot of their AM5 and Z-series boards run surprisingly cool under sustained workloads. That matters for people sitting in Blender, Unreal Engine, Premiere Pro, or **long compilation workloads** for hours at a time."* | **new, and it is this build's exact workload** - see below |
| `ITBy9ckvSFY` | 13 031 / 13 031 | *"Some lower-end ASRock boards also cut back harder on onboard audio or rear USB connectivity to hit aggressive pricing"* | **new** - worth checking the B850 Pro RS WiFi's rear IO |
| `fsIh2eoWLT4` Tech Guided, 2023-12-24 | **22 862 / 22 862** | *"if you have a larger budget around $1,000 or more we recommend spending 8 to 12% of your budget on your motherboard"* | **exact** |
| `fsIh2eoWLT4` | 22 862 / 22 862 | *"more power phases doesn't automatically mean a quality vrm"*; *"read or watch reviews ... by reviewers like build Zoid ... Gamers Nexus and Hardware unboxed"* | **exact** |
| `fsIh2eoWLT4` | 22 862 / 22 862 | *"The list ... hasn't been updated for over a year now though so it only lists am4 chipset motherboards and 12th generation Intel chipsets"* | **CONTRADICTS the audit's own recommendation** - see below |
| `lP-pinlU-Ko` Paul's Hardware, 2020-05-17 | **19 605 / 19 605** | *"surface mounted power and reset buttons"*, *"an LED post readout"*, *"A BIOS flashback feature"*, *"a clear CMOS button on the rear i/o"*, *"fan stop mode ... or just simply advanced fan controls"* | **exact** - all five features confirmed |
| `lP-pinlU-Ko` | 19 605 / 19 605 | *"they are Hardware unboxed and build Zoids actually hardcore overclocking channel"* | **exact** |
| `lP-pinlU-Ko` | 19 605 / 19 605 | *"it is something that you can also easily add just with a USB plug in adapter so it's not something I mind going without"* | **exact** - the dongle alternative |
| `lP-pinlU-Ko` | 19 605 / 19 605 | *"The new asus VG 259 QM gaming monitor ... click the sponsor link in the description"* | **undisclosed** - ASUS-sponsored |
| `PfAsVb4Bza4` PC Centric, 2021-09-09 | **15 463 / 15 463** | *"a massive thank you to asus for sponsoring this video"* | **exact** - already recorded |
| `PfAsVb4Bza4` | 15 463 / 15 463 | *"motherboards don't usually result in better or worse frames per second in games"*; *"I commonly see people overspending on their motherboards but then getting a cheaper processor or graphics card to compensate"* | **exact** |
| `PfAsVb4Bza4` | 15 463 / 15 463 | *"if you do need wi-fi make sure your motherboard does actually support this because especially at the budget ends not all of them do"*; *"extra money and ultimately extra mess"* | **exact** |
| `PfAsVb4Bza4` | 15 463 / 15 463 | *"you usually buy two sticks and run them in dual channel operations so you use **slots 2 and slots 4**"* | **second independent source for the A2/B2 handover item** |
| `PfAsVb4Bza4` | 15 463 / 15 463 | *"maybe you're using a case with usbc but then it doesn't actually have the usbc header on it"* | **exact** - the front USB-C warning |
| `VgWrOSG24Yg` Tech Notice, 2025-09-14 | **21 519 / 21 519** | *"the Windows 11 Pro OEM key is just $23.22"* | **exact** - the grey-market sponsored segment |
| `VgWrOSG24Yg` | 21 519 / 21 519 | *"I highly recommend checking out the latest and the previous generation platform pricing, not just motherboard and CPU. See how much the whole platform is going to cost."* | **exact** |
| `VgWrOSG24Yg` | 21 519 / 21 519 | *"very often you see X870E but it doesn't tell you the full story. Sometimes you have Wi-Fi or Wi-Fi missing."* | **exact** - the Wi-Fi SKU trap |
| `VgWrOSG24Yg` | 21 519 / 21 519 | *"I always recommend going with the highest tier with the latest motherboard"* | **dissents from the B850 pick** - but 2:1 against him (Socket-X, GeekaWhat) |

### What the full reads changed

**1. The seventh video is the one another document was already citing.** [cooling.md](components/cooling.md)
supports its open question with *"GeekaWhat's 2026 parts guide goes further and recommends liquid
cooling for a Ryzen 7"*. That claim was **true and unverifiable at the same time** - the video had
never been fetched. It is now quoted verbatim above. This is the clearest possible case for why
the audit exists: the citation was accurate, and nothing in the repo could have shown that.

**2. The VRM tier list this project recommends does not cover this platform.** motherboard.md
carries Tech Guided's Reddit VRM spreadsheet as a resource, and the earlier audit recorded it as
a gap worth filling. The video itself says the list *"hasn't been updated for over a year ... so
it only lists am4 chipset motherboards and 12th generation Intel chipsets"* - as of **2023**. It
has **nothing on B850 or AM5**. Recommending it without that caveat sends you to a dead end. The
usable half of the same advice stands: **Buildzoid, Gamers Nexus and Hardware Unboxed**, named
independently by both Tech Guided and Paul's Hardware.

**3. A brand argument for this exact workload that no document has.** The ASRock brand-risk
paragraph in motherboard.md has been contradicting the pick for some time. The brand survey adds
a separate, non-reliability reason to look at Gigabyte: *"a lot of their AM5 and Z-series boards
run surprisingly cool under sustained workloads. That matters for people sitting in Blender,
Unreal Engine, Premiere Pro, or **long compilation workloads** for hours at a time."* Dmytro's
stated brief is *"IDE + language servers, Claude Code over heavy repos"*. The same video notes
lower-end ASRock boards *"cut back harder on onboard audio or rear USB connectivity"*. Neither is
a measurement, and neither reopens a settled pick on its own - but if the ASRock paragraph is
revisited, this is the argument that bears on the work case rather than on brand reputation.

**4. Two checkable board features nobody has checked.** Socket-X: *"A board with only two fan
headers is a trap"* - aim for four or five; and *"look for a BIOS flashback button"*, which
matters because a board manufactured before a CPU's launch needs one to boot. Both are one lookup
away on the ASRock B850 Pro RS WiFi and neither appears in motherboard.md's criteria table.

**5. The onboard-Wi-Fi rule is now 3:1, not 2:1.** Socket-X, PC Centric **and GeekaWhat** all
require it - GeekaWhat calls it *"a red line"* for his own build company. Only Paul's Hardware
(2020) offers the USB-dongle alternative. The 614 UAH spent on the WiFi SKU is well supported.

**6. The A2/B2 handover item has a second source.** PC Centric states it plainly - *"you use
slots 2 and slots 4"* - independently of JayzTwoCents. Worth noting alongside the correction in
[pc_build.md](../pc_build.md) that it is **not** in all four build-technique videos.

**7. Three of the seven are ASUS-sponsored** - PC Centric, Paul's Hardware and GeekaWhat - and a
fourth carries the grey-market Windows key segment. The ASUS concentration matters more here than
elsewhere, because this is the component category where ASUS is a vendor being compared.

**Not overturned:** every claim the earlier pass made from the six videos it did read is verbatim
accurate, including the corrections it made to itself. The B850-over-X870 reasoning, the 2x16
kit, the Gen 5 heat warning, the 2.5GbE caveat, the whole-platform-cost rule and the Wi-Fi SKU
trap are all exact.

**Frames:** none of the seven is a benchmark video and no doc attributes an on-screen figure to
any of them; every claim above is narration, quoted.

## GPU - 4 of 4 re-read IN FULL, 2026-09-13 (re-done in the verifiable format)

The earlier GPU pass was substantively good - **every one of its claims checks out below** - but
it recorded no per-claim char counts and one figure that matches nothing on disk, so it could not
be verified mechanically. Re-done here.

**The 37 953 char figure was wrong.** The earlier section states the GECID transcript is
*"37 953 chars, read end to end"*. Measured now:
[`sources/gpu_cUSxa4PxI4I.md`](sources/gpu_cUSxa4PxI4I.md) is **21 497** body chars, **26 456**
chars in total including title block and description, and 44 105 **bytes** (Cyrillic is
multi-byte in UTF-8). 37 953 is none of those. The read was real - all fourteen claims below are
verbatim - but the number attached to it was not measured.

| Video ID | chars read / total | Verbatim quote or frame | Verdict |
|---|---:|---|---|
| `cUSxa4PxI4I` GECID, Ukrainian | **21 497 / 21 497** | *"У більшості сучасних проєктів вона випереджає RTX 5070 приблизно на 10-20%"* | **exact** |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"RX9070 перегнала RTX 5070 на 16% загальної продуктивності"* (Death Stranding 2) | **exact** |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"випереджаючи RTX 5070 приблизно на 13%"* (S.T.A.L.K.E.R. 2) | **exact** |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"RX9070 випереджає RTX 5070 приблизно на 20 кадрів за секунду в середньому"* (RE Requiem) | **exact** |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"стабільно втримувати планку у 60 кадрів за секунду їй все ж не вдається. Натомість RX 9070 забезпечує в середньому близько 64 FPS"* (AC Shadows) | **exact** - and the retraction of the earlier "contradicted" verdict is confirmed correct |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"допускає просідання нижче комфортної позначки у 60 FPS"*; *"Більше 90 FPS в середньому"* (Battlefield 6) | **exact** |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"близько 250 разів за секунду в середньому, що майже на 80 FPS перевищує результати RX 9070"* (The Long Dark) | **exact** |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"невелика перевага все ж залишається за RTX 5070"* (GTA 5); *"символічно виривається вперед"* (Dying Light); *"не вдається наздогнати свого зеленого опонента"* (Witcher 3) | **exact** - all three 5070 wins |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"гра вже майже повністю освоює доступні 12 ГБ"*; *"12 ГБ у RTX 5070 тут вже фактично заповнюється під зав'язку"* | **exact** - the 12GB ceiling |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"на найновішому драйвері AMD гра на відріз відмовилася запускатися, тоді як на більш старій версії все запрацювало"* (DOOM) | **exact**, and `frames/cUSxa4PxI4I_28m05s.png` carries the Vulkan crash dialog |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"На відеокарті неможливо активувати трасування шляху"*; *"RX 9070 позбавили підтримки цього режиму"* | **exact** |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"Підтримки FSR у грі наразі просто немає"* (Subnautica 2); *"на RX 9070 доступний лише FSR-2"* (Witcher 3) | **exact** |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"Заявлений TDP Radon RX 9070 становить 220 Вт, тоді як GeForce RTX 5070 розрахована на 250"* | **exact** - confirms psu.md's 220W |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"за надання цих відеокарт на тест ми дякуємо магазину Telemart.ua ... до 5 липня за промокодом GESID 500 ви можете отримати додаткову знижку у 500 грн на всі відеоприскорювачі від ASUS"* | **deeper than "cards supplied"** - see below |
| `cUSxa4PxI4I` | 21 497 / 21 497 | *"Asus Prime GeForce RTX 5070 OC"* vs *"Asus Prime Radeon RX9070 Evo OC"*, chosen *"щоб мінімізувати вплив відмінностей у виконанні та системах охолодження"* | **good method, unrecorded** - same series both sides |
| `2ufCzwK73GM` BENCHMARKS FOR GAMERS | **0 / 0** - no caption track (re-confirmed after the fetcher's rate-limit bug was fixed; exactly one video of the 99) | `frames/2ufCzwK73GM_10m52s.png` reads **"13% Faster on average at 1440p + DLSS 4.5 / FSR 4.1 Q"** and thirteen bars: **25, 24, 20, 20, 19, 16, 13, 12, 12, 4, 3, 1, -6** | **exact** - header and all thirteen deltas match gpu.md |
| `2ufCzwK73GM` | 0 / 0, no caption track | `frames/2ufCzwK73GM_00m40s.png` - Forza raw overlay | **exact** per the earlier pass |
| `4UqYr3nAj90` Testing Games | **434 / 434** | *"Buy game keys, save money, and then just play ... CHECK G2A.COM"* plus in-game dialogue - the entire caption track | **no technical content**, as recorded. Data is in `frames/4UqYr3nAj90_04m40s.png` |
| `hIZj4MOk6fo` Jegs TV | **1 782 / 1 782** | *"we're going to use Sapphire's Pulse RX970 and Pallet's RTX 5070 Infinity 3 ... a Ryzen 7 9800 X3D with 64 gigs of 6,000 MHz RAM"*; *"the test will be free from any form of commentary"* | **exact** - the test setup and the no-commentary statement |
| `hIZj4MOk6fo` @ 15:10 | 1 782 / 1 782 | `frames/hIZj4MOk6fo_15m10s.png` - 2560x1440p, RT Overdrive, frame gen off: RTX 5070 **avg 59 / 1% low 49**, RX 9070 **avg 45 / 1% low 37** | **the earlier correction is confirmed.** The 1% low is **37**, not 41; the 5070's lead over it is 32% |

### What the re-read changed

**1. The GECID review is sponsored by the shop this build buys from.** The earlier pass recorded
*"cards supplied by Telemart"*. Read in full it is more than a hardware loan: the video carries a
**live discount code** - *"до 5 липня за промокодом GESID 500 ... додаткова знижка у 500 грн на
всі відеоприскорювачі від ASUS"* - a paid promotion for Telemart, and specifically for **ASUS
graphics cards**, which are the two cards under test. **Telemart is one of the two assemblers
this build is priced against** ([tools.md](tools.md)), and gpu.md leans on this review more than
on any other single source.

Nothing in the review reads as bought - its conclusion is genuinely balanced and it ends by
recommending the **RTX 5070** for buyers who want no compatibility surprises. But the
relationship should be on the page, and it is the one sponsorship in this audit that touches a
shop rather than a component vendor.

**2. The methodology is better than gpu.md records, and worth keeping.** GECID deliberately tested
**two cards from the same ASUS Prime series** - same coolers, same 30cm/2.5-slot dimensions - to
isolate the GPUs from the board partners. That is the control that the Jegs TV comparison
(Sapphire Pulse against Palit Infinity 3) does not have, and it is why these two sources can
disagree without either being wrong.

**3. Frame timestamps in the earlier pass are approximate.** It cites `2ufCzwK73GM` @ 10:38,
`4UqYr3nAj90` @ 3:59 and `hIZj4MOk6fo` @ 14:50; the frames on disk are at **10m52s**, **04m40s**
and **15m10s**. Same charts, same numbers - both frames re-read above confirm the figures
exactly - but a reader following the cited timestamp lands slightly early. The filenames are the
authority.

**Not overturned: nothing.** All fourteen GECID claims, both frame readings and the Jegs TV setup
are verbatim accurate, and the one correction the earlier pass made to itself - the 1% low of 37
- is confirmed against the frame. **This component was done properly; only its bookkeeping was
not.**

## CPU/GPU combo guide - 1 of 1 read IN FULL, 2026-09-13

`UyKvDu9dZUs`, ScatterVolt "Best CPU GPU Combo for Every Budget! (2026)". This is the single
source behind [scattervolt_2026.md](scattervolt_2026.md), which recorded *"transcript not kept"*.
**It is kept now**, at [`sources/combo_UyKvDu9dZUs.md`](sources/combo_UyKvDu9dZUs.md).

Metadata checks out exactly: **49:26**, published **2026-08-16**, 228 940 views against the
"220k" recorded then.

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `UyKvDu9dZUs` tier 9, the tier this build sits in | **47 476 / 47 476** | *"a 7700X for $220 is really hard to beat. Like really, really hard. And that's eight cores, 16 threads. It's not an X3D CPU, but it retails for at least $100 or more less"* | **exact** |
| `UyKvDu9dZUs` | 47 476 / 47 476 | *"a B850 motherboard, that's fine. **We don't need X870.**"* | **exact** - supports the B850 |
| `UyKvDu9dZUs` | 47 476 / 47 476 | *"RX 9070 GRE is your first option you should consider. That is **locked in right now at $550**. It has not gone up in price. It's probably going to be the one GPU that isn't going to go up in price"* | **exact** |
| `UyKvDu9dZUs` | 47 476 / 47 476 | *"If you can find a discounted RX[9]070 16 GB, that would be the absolute best GPU option ... the price premium for a RX[9]070 over that other GPU will not be worth it if it exceeds $100"* | **exact** |
| `UyKvDu9dZUs` | 47 476 / 47 476 | *"RX[9]070 XT is the best ... there's other comparable GPUs to it like the RTX [50]70 Ti 16 GB that retail for almost $300 more"*; the 5080 is *"$600 more ... You're getting a 1.2 at most faster GPU"* | **exact** |
| `UyKvDu9dZUs` | 47 476 / 47 476 | *"the best GPU of this generation from all the major brands ... The pricing is unmatched"* (9070 XT, tier 10) | **exact** |
| `UyKvDu9dZUs` tier 9 PSU | 47 476 / 47 476 | *"anything from 650 watts to 750 W is going to be supportive for any of our GPU options"*; tier 10: *"we have amped up ... some of our GPU options could ask of 850 watts at peak load"* | **exact** - psu.md's "650-750W on a 9070/GRE build, 850W for the 9070 XT tier" is verbatim |
| `UyKvDu9dZUs` | 47 476 / 47 476 | *"I really think **16 GB of D[DR]5 memory is still very much doable.** But if you wanted 32 and you have the budget for it, then go for it."* | **CONTRADICTS the "third source for 32GB" claim** - see below |
| `UyKvDu9dZUs` | 47 476 / 47 476 | *"you really shouldn't have to worry about bottlenecking ... It's not like Skyrim potions"*; *"as long as it's not the top tier CPU, it's going to work in whatever motherboard you put it in"* | **exact** - the bottleneck position |
| `UyKvDu9dZUs` | 47 476 / 47 476 | no sponsor read anywhere in 49 minutes; he promotes only his own **pcbuilds.gg** | **one of the few unsponsored sources in this audit** |

### What the full read changed

**1. ScatterVolt's two videos disagree about RAM, and the newer one supports Lean's 16GB.**
[pc_build.md](../pc_build.md) records: *"ScatterVolt's flat answer for DDR5 is **32GB, that's all
you need** - stated as the target, with no budget exception offered. Third independent source
saying the same thing."* That quote is real and verbatim - but it comes from his **parts guide
(`PsqulPtiR3g`, 2025-09)**. In this video, **eleven months later**, he says of the tier this
build sits in: *"I really think 16 GB of DDR5 memory is still very much doable. But if you wanted
32 and you have the budget for it, then go for it"* - and for the tier below, *"16 GB of DDR5
memory is what you're going to need"*. He is explicit about why: the memory shortage.

So the "third independent source" for 32GB is **the same source, at an earlier date, before the
price event that the whole RAM section is about.** His current position is closer to "16GB is
doable, 32GB if you can afford it" - which is exactly the Lean-versus-Working split this project
already runs. **Nothing changes; one citation needs dating.**

**2. Everything else in scattervolt_2026.md is verbatim accurate.** That document is a
49-minute video compressed into a table of twelve combos, written without keeping the transcript.
Read against the source in full, the tier 9 and tier 10 rows - the ones this build actually
depends on - are exact, including the $550 price lock, the $100 premium rule, the "B850, not
X870" line, the $300 and $600 GPU deltas and the 650-750W / 850W split. Its caption-artefact
decoding table ("RX970" = RX 9070, "LGA700" = LGA1700, "Rockheim" = ROCm) is also correct - the
ASR mangles those consistently.

**3. Its source-tier warning is right, and worth keeping.** scattervolt_2026.md calls this
*"opinion, not measurement ... good for direction and for what a builder would pair, and it is
not a source for any number."* Confirmed: across 49 minutes there is not one benchmark chart, not
one measured figure, and no methodology. Every number in it is a **US price**, mid-August 2026.
The GRE's "$550 locked" is a market observation, not a test result - and it is the line the
build's GPU tiering leans on hardest.

**Frames:** no doc attributes an on-screen figure to this video, and the claims above are all
narration. He does show part-list cards on screen, but nothing in the repo cites one.

## UPS - 7 of 7 read IN FULL, 2026-09-13

**No document in this repo cites any of these seven.** [pc_build.md](../pc_build.md) records the
component as *"**Parked** by Dmytro - to be discussed with a specialist, not researched here."*
That decision stands and nothing below reopens it. The videos are read because they were sent,
and recorded so the work is not repeated if the item is ever unparked.

Dmytro's brief when he sent them (`4d4f7b00:1803`): *"so i need just the safe shudown, not
autonomic runtime / just the correct one for this setup"*.

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `1oNdbI8NFgk` Techquickie, 2016-04-16 | **5 697 / 5 697** | *"pick up a UPS with a volt amp rating 50 to 75% above whatever the typical wattage load from your PC will be"* | **no doc cites it** - sizing rule recorded |
| `1oNdbI8NFgk` | 5 697 / 5 697 | *"they're designed to give you enough time to save your work and shut down your computer properly"*; *"many units will allow you to connect the UPS to your computer with a USB cable ... automatically shut down your computer properly once the battery gets low"* | **matches the brief exactly** |
| `JL71IH5HShI` Dave's Garage, 2023-04-01 | **27 453 / 27 453** | *"it usually requires a USB or serial connection from the UPS to the PC ... your PC can save its data flush the caches and do an orderly shutdown"* | **matches the brief exactly** |
| `JL71IH5HShI` | 27 453 / 27 453 | *"I bought a 1500 [VA] ups for my main workstation because my machine has a 1200 watt power supply ... the UPS started complaining"* - VA is apparent power, W is real power, the ratio is the power factor | **the sizing trap, from someone who fell into it** |
| `JL71IH5HShI` | 27 453 / 27 453 | *"many computer power supplies can't buffer or bridge that Gap and your system May reboot even though it never fully loses power"* (offline UPS transfer time) | **the one line that touches the PSU pick** - see below |
| `JL71IH5HShI` | 27 453 / 27 453 | *"The APC 1500 ... can supply 100 Watts for about three hours ... a more reasonable load like 1000 Watts for about ... 18 minutes. Not much time to get any real work done but plenty to provide a safe shutdown"* | **the runtime the brief actually asks for** |
| `JL71IH5HShI` | 27 453 / 27 453 | *"the most basic UPS units, which you should probably avoid at all costs, simply create a square wave ... such UPS's have no place in running sensitive Electronics"* | **exact** |
| `ovZAbCqh_A0` Geerling Engineering, 2022-02-25 | **11 167 / 11 167** | *"sizing a battery pack ... you want to get it like 50 to 75 [%] loaded at the most and 50 is a great space to load it"* | **exact** - the load-side of the same rule |
| `ovZAbCqh_A0` | 11 167 / 11 167 | *"you want clean sine wave power ... they have a triangular wave and they have a stepped wave"*; a first-hand account of an overloaded UPS cycling equipment on and off during an outage | **exact** |
| `fiKra9BXqoA` MOYO, 2023-02-23 (Ukrainian) | **9 587 / 9 587** | *"This type of uninterruptible power supply [line-interactive] is best suited for digital and computer equipment"*; online/double-conversion is for *"pumps or boilers"* | **exact** - the type recommendation for a PC |
| `fiKra9BXqoA` | 9 587 / 9 587 | *"20-30% must be added to this sum of our capacities"* (efficiency of the line-interactive transformer) | **exact** |
| `NyfoqRIFg4k` Інструмент Центр, 2024-08-25 (Ukrainian) | **14 430 / 14 430** | *"For the home, I repeat, the best option will be linear-interactive"*; switching time *"from 2 to 8 ms"* against offline's *"5 to 20 ms"* | **exact** |
| `NyfoqRIFg4k` | 14 430 / 14 430 | *"For computers and servers, this is 0.95"* (VA → W factor); *"we need to add another 25% on top for the reserve"* | **exact** |
| `NyfoqRIFg4k` | 14 430 / 14 430 | runtime formula: capacity (Ah) x voltage x 0.8 / load (W); worked example 150Ah x 12V x 0.8 / 250W = **5.75 h** | **exact** |
| `gFCOowZV3Cw` E-Katalog, 2023-10-08 (Ukrainian) | **11 140 / 11 140** | *"for computers it is 0.95"*; *"Add another 20% to this amount"*, plus another 20% if an upgrade is planned | **exact** - a third independent VA→W factor, all three agree on 0.95 |
| `gFCOowZV3Cw` | 11 140 / 11 140 | *"try to choose such an UPS so that its switching time is no more than 5 ms"*; *"for PCs you need sockets of the ... C13 C14 standard"* | **exact** |
| `hebLFKBSEd4` Владислав Казімір, 2024-07-02 (Ukrainian) | **4 328 / 4 328** | measured with a wattmeter on an i7-14700KF + RTX 4080: idle **187 W**, normal **~250 W**, work tasks **300-500 W**, stress-test maximum **~600 W** | **the only measured system in the set** |
| `hebLFKBSEd4` | 4 328 / 4 328 | *"It is recommended to choose a DBZ power of some 20-30% [that] exceeds the maximum consumption of your equipment"*; he lands on **700-800 W** for that ~600 W system | **exact** |

### What the reads found

**1. Every source agrees on the type, and it is the cheap-but-not-cheapest one.** For a PC, three
of the seven name **line-interactive** explicitly - MOYO (*"best suited for digital and computer
equipment"*), Інструмент Центр (*"for the home ... the best option will be linear-interactive"*)
and Dave's Garage, who prefers online but concedes line-interactive covers a PC. **Offline/standby
is ruled out by all of them** for a computer, on transfer time. Online/double-conversion is
described as overkill for a PC and reserved for boilers, medical and telecoms gear.

**2. The one line that touches a decision already made.** Dave's Garage: an offline UPS's transfer
gap can reboot a PC *"even though it never fully loses power"*, because the PSU cannot bridge it.
The relevant number is the PSU's **hold-up time**, and [psu.md](components/psu.md) records
**21.8 ms** for this be quiet! platform. Against the transfer times these videos give - offline
**5-20 ms**, line-interactive **2-8 ms**, E-Katalog's rule of thumb *"no more than 5 ms"* - the
chosen PSU covers a line-interactive unit with a wide margin and would be marginal on a slow
offline one. **This is a point in favour of the PSU already picked, and it is the only place the
UPS batch bears on a live decision.**

**3. The sizing arithmetic, if the item is ever unparked.** All three Ukrainian sources give the
same VA→W factor for computers - **0.95** - and headroom of **20-30%** over measured maximum.
Techquickie's older rule is 50-75% above typical load; Geerling puts it the other way round -
load the UPS to **50-75% of its rating at most**. Applied to this build's **373 W** measured peak
(Working) the two rules converge on roughly **500-750 VA**, and the Max build's 483 W on roughly
**650-950 VA**. Recorded as arithmetic, **not as a recommendation** - the component is parked and
the sizing depends on whether the monitor goes on the same unit.

**4. Runtime is not the question the brief asks.** Dave's Garage's worked figure - an APC 1500
sustaining 1000 W for about **18 minutes**, *"not much time to get any real work done but plenty
to provide a safe shutdown"* - is the direct answer to *"just the safe shutdown, not autonomic
runtime"*. Any unit sized by the rules above will clear that bar; the specification that matters
for the brief is the **USB/serial data link and its shutdown software**, named by Techquickie,
Dave's Garage, MOYO and E-Katalog alike.

> **Added 2026-09-13, and it is the first thing `coverage.py` caught.** The read-coverage check
> found **two body lines of `JL71IH5HShI` that no pass had ever printed** — the closing lines of
> Dave's Garage's video — while the row for it had been passing as a full read since the first
> sweep. They contain the verbatim this paragraph was asserting without one, and a detail nobody
> had:
>
> *"There's one essential component that I skimmed over earlier: a connection from the UPS to the
> PC so that the UPS can inform the PC when the power is going to go down … that advanced notice
> allows the PC to do an orderly shutdown."*
> *"**Now Windows itself can interface with most every common UPS**, and for those that it can't
> you're stuck with whatever comes with bundled software. But whichever route you go, make sure
> you get that one piece of communications working properly."*
>
> **The second sentence is new and useful if the UPS is ever unparked:** Windows speaks to most
> units natively, so vendor software may not be needed at all — and the one thing to verify at
> purchase is that the data cable and its shutdown signalling actually work, not which app ships
> in the box. The item stays parked; this is recorded so the check is not repeated.

**Sponsorship:** Techquickie carries an **Audible** read; the two Ukrainian retail channels (MOYO,
E-Katalog, Інструмент Центр) are shops publishing buying guides for stock they sell - not
sponsorship, but a commercial interest worth the same caution.

**Frames:** no doc attributes an on-screen figure to any of the seven; every claim above is
narration, quoted.


## Mouse - 8 of 8 read IN FULL, 2026-09-13

Sent in one message, `4d4f7b00:54`. The document is
[peripherals/mouse.md](peripherals/mouse.md), **closed 2026-09-11 on the Razer Cobra at 2 499 and
confirmed by Dmytro with the drawbacks accepted**. Nothing below reopens that pick; three of the
findings correct *how it is argued*, and the corrections are made in the doc in place.

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `ivZEp0J2wYg` Rocket Jump Ninja, 2025-07-01 | **14 676 / 14 676** | *"I recommend using a mouse about 60% of your hand measurements"*; *"the length is just the length of your middle finger. Just measure your middle finger all the way back to your knuckle"* | **exact** - the doc's 60% rule and the middle-finger length rule |
| `ivZEp0J2wYg` | 14 676 / 14 676 | *"Polling rate is a gimmick ... I can't even tell the difference with a high-speed camera"*; *"Under 60 g is generally pretty good"*; *"Wireless is as good as wired now"* | **exact** - all three used in the doc, all three verbatim |
| `ivZEp0J2wYg` | 14 676 / 14 676 | *"give it two to 3 weeks and then decide"* | **exact** - the doc's adaptation window |
| `ivZEp0J2wYg` | 14 676 / 14 676 | *"10 years ago, I started doing mouse reviews"*; his site banner reads *"100+ mouse reviews from over 21 years of FPS/Quake Experience"* - [`frames/QVI3mepUHuE_01m05s.png`](frames/QVI3mepUHuE_01m05s.png) | **wrong thing attached to a right number** - the doc credited him with *"21 years of FPS reviews"*. 21 years is his Quake *play*; the reviews are 10 years. **Fixed in the doc.** |
| `ivZEp0J2wYg` | 14 676 / 14 676 | *"I give a shout out to Orbital here. The Pathfinder mouse is a great way to find the right mouse for you"*; description: *"My products: Xtrfy MZ1 - My mouse design"* | **undisclosed conflict of interest** - the reviewer designs and sells mice and plugs a third party's inside the price chapter. Not recorded anywhere before this audit. |
| `QVI3mepUHuE` Rocket Jump Ninja, 2020-02-27 | **6 560 / 6 560** | *"we're basically after that measurement from the thumb knuckle over to the little finger knuckle"* | **exact** - the doc's "Rocket Jump Ninja includes the thumb knuckle" |
| `QVI3mepUHuE` | 6 560 / 6 560 | *"the most important measurement is the width you really want to get the right grip width ... I think that's the one that affects aim the most so not comfort but your aim potential"* | **exact** - the doc's "grip width decides aim; length decides comfort", verbatim from the source |
| `QVI3mepUHuE` | 6 560 / 6 560 | search form and results columns read off the screen: Hand Length / Hand Width / Search Leniency / Grip Type / Wireless / Left-handed / # of buttons, results carrying **Name, Weight (g), Size, Length (cm), Grip Width (cm), Review** - [`frames/QVI3mepUHuE_03m45s.png`](frames/QVI3mepUHuE_03m45s.png) | **exact, and now on disk** - the doc asserted this from prose timestamps with no frame saved |
| `QVI3mepUHuE` | 6 560 / 6 560 | *"as for the button latency I do test it ... as long as it's under 4 milliseconds it should be ok"* | **a threshold the doc never recorded** - it is the pass/fail line LTT's 10.8 ms clone fails and its sub-2 ms Razer clears. **Added to the doc.** |
| `6RlGpvcW51s` Kimmy, 2026-03-24 | **11 653 / 11 653** | *"measure across your knuckles from the outside of your index finger to the outside of your pinky. And this is important, leave your thumb out"* | **exact** - and the opposite of Rocket Jump Ninja, which the doc already records correctly |
| `6RlGpvcW51s` | 11 653 / 11 653 | **17.5 cm** confirmed on screen - [`frames/6RlGpvcW51s_01m55s.png`](frames/6RlGpvcW51s_01m55s.png); the auto-caption renders it *"under 70.5 cm"* | **verified by frame** - the doc's small/medium boundary was right and the transcript alone could not prove it |
| `6RlGpvcW51s` | 11 653 / 11 653 | *"Medium, somewhere around 115 to 125"* mm mouse length; grip width *"under 8 cm ... 53 to 58 mm"*, *"average ... 57 to 60"*, *"wide, 9 plus ... 62 to 64"* | **exact** - the doc's fit table reproduces all four bands correctly |
| `6RlGpvcW51s` | 11 653 / 11 653 | *"large is like 19 plus"*; spoken over b-roll of a tape measure, no chart - [`frames/6RlGpvcW51s_02m20s.png`](frames/6RlGpvcW51s_02m20s.png) | **exact, and it cuts against the doc's own band** - a 19.0 cm hand is *large* by this source, while the doc applies the *medium* 115-125 mm band. **Noted in the doc.** |
| `6RlGpvcW51s` | 11 653 / 11 653 | *"A perfect sensor in the wrong shape is just like an expensive mistake"* | **exact** - the doc paraphrases this in spec row 1; now quoted |
| `W8ybwi6H8QU` DiamondLobby, 2026-04-27 | **8 739 / 8 739** | *"I'd highly recommend getting a mouse that is at least under 55 g if you play shooters"*; *"I'd still recommend getting something under 65 g"* for Counter-Strike | **exact** - the doc's "under 55-65 g by 2026" |
| `W8ybwi6H8QU` | 8 739 / 8 739 | *"the average person shouldn't over spend $130 on a gaming mouse"* | **exact, but it is the 2026 video** - the doc merged it with the 2024 video's *"$90 and 125 is optimal"* into one DiamondLobby statement. Two videos, two years apart. **Split in the doc.** |
| `W8ybwi6H8QU` | 8 739 / 8 739 | *"ATK VXR 1 Pro, Mad R, MChose L7 or A7V2 ... These are undeniably end game level mice ... can cost anywhere between $45 to $65"*; description names them VXE R1 PRO, VXE MAD R, MCHOSE L7 PRO, MCHOSE A7 ULTRA | **exact** - the doc's model names come from the description, not the audio; both agree |
| `W8ybwi6H8QU` | 8 739 / 8 739 | *"you have to cover the shipping costs to send it back to China"*; and for the brands: *"They often have an extra year of warranty, higher quality control standards and provide more reliable firmware and software"* | **exact, and the second half was missing** - the doc kept the warranty warning but not the positive case for brand mice, which is the argument that closes open question 1 |
| `W8ybwi6H8QU` | 8 739 / 8 739 | *"I think it's best to measure it when it's in a relaxed and natural position ... My 18 by 10 cm hands when flat on a desk are actually 15 by 10 cm in a relaxed position"* | **a third method the doc presents as settled** - the doc's "How to measure" gives only the flat-hand method. **Added to the doc.** |
| `SQcK4N5xCK8` DiamondLobby, 2024-01-31 | **8 459 / 8 459** | *"my maximum weight for a gaming mouse that I would use for first-person shooters is around 8855 G"* (caption artefact; the figure spoken is 85 g) | **the doc's "~85 g in 2024" is the right reading of a broken caption** - recorded here so the reading is visible rather than silent |
| `SQcK4N5xCK8` | 8 459 / 8 459 | *"I would say that spending between $90 and 125 is optimal"* | **exact** - and this, not the $130, is the 2024 figure |
| `SQcK4N5xCK8` | 8 459 / 8 459 | *"anything with a Pixar 3370 or a 3395 sensor will be fine these days"* | **exact** - the source of the 3370 in the doc's sensor row; 3311/3330/3395 come from the 2026 video |
| `SQcK4N5xCK8` | 8 459 / 8 459 | *"I think that rubberized grips ... on a mouse by default are to be avoided if you don't like it you have to apply grip tape"* | **independent corroboration of a known drawback of the mouse that was bought** - the Cobra's rubberised side grip. Accepted by Dmytro already; recorded, not reopened. |
| `SQcK4N5xCK8` | 8 459 / 8 459 | *"avoid plugging the dongle into your PC case directly ... plug the dongle into the adapter and have it sitting on your desk just to avoid any wireless interference"* | **usable and unrecorded** - applies to the wireless alternates. **Added to the doc.** |
| `SQcK4N5xCK8` | 8 459 / 8 459 | description, not spoken: *"the less people using a G502 for long hour gaming the better"* | **quoted accurately, sourced loosely** - the doc reads as though this is in the video. It is in the description. **Marked in the doc.** |
| `ozcZuz5p3ss` Linus Tech Tips, 2025-03-11 | **11 600 / 11 600** | *"the metap panda P1 Pro is impressive at its $40 price ... the latency while quite consistent was a bit of a letdown"*; the Attack Shark R1 *"trailed behind ... with noticeable jitter ... 10.8 milliseconds"* | **exact** - the doc's sweet-spot claim |
| `ozcZuz5p3ss` | 11 600 / 11 600 | *"The Death Adder V3 hyperspeed is in a league of its own with sub-2 millisecond latency it also delivered flawless tracking even at high DPI"* | **half-recorded** - the doc kept the sub-2 ms number as a contrast and dropped the verdict it belongs to. The premium Razer wins this video. |
| `ozcZuz5p3ss` | 11 600 / 11 600 | *"Razer and the panda are rated for 80 million clicks on their top buttons while that goes down to 20 million and just 10 million for the attack shark and the essential"* | **contradicts the doc's own "Ignore" list**, which files click ratings as marketing. Between brands they are; between a brand and a 20-dollar clone they are an 8x gap. **Qualified in the doc.** |
| `ozcZuz5p3ss` | 11 600 / 11 600 | *"it dumped me out of the game to prompt me to install my stupid Razer software ... Razer is the only one that successfully got me killed so far"* | **first-hand, instrumented, and about the brand that was bought** - the doc had only aggregate Reddit complaints about Synapse. Drawback already accepted; recorded. |
| `ozcZuz5p3ss` | 11 600 / 11 600 | *"unlike our beautiful sponsor pulseway"* (0:34), read again at 11:15; description: *"Check out Pulseway today and get up to 40% off"* | **undisclosed sponsorship** - plus an in-video LTT store plug for mouse feet and AliExpress/Amazon affiliate links |
| `UMHmPdVbaIM` Hardware Canucks, 2022-01-21 | **8 703 / 8 703** | *"anything below 80 g for a mouse feels relatively the same"*; *"we're finally starting to have balance adjustments on lightweight mice, which is far more important than the weight itself"* | **exact** - and note he makes **no** fatigue claim, which the doc attributed to him |
| `UMHmPdVbaIM` | 8 703 / 8 703 | *"as BattleNonsense proves here, this input lag reduction is on a log scale and diminishes beyond 3200 DPI"* | **exact** - the doc's "nobody uses above ~3 200" has a measured basis, which the doc did not state |
| `UMHmPdVbaIM` | 8 703 / 8 703 | *"I also remember being really attracted to the MMO-style mouse with the thousand buttons on the side ... I never used the side buttons, and the MMO/RPG bodies are generally much larger"* | **exact** - the doc's fourth-mistake paragraph |
| `UMHmPdVbaIM` | 8 703 / 8 703 | *"driver software is another point of conflict, especially Razer Synapse and Corsair iCUE ... I've encountered plenty of issues with Synapse not playing nice ... or Logitech G Hub just simply failing to start"* | **exact** - supports spec row 9, and lands on **both** finalists, not one |
| `UMHmPdVbaIM` | 8 703 / 8 703 | *"after your Logitech starts to double-click. We all know it's true"* | **the counterweight the doc lacked** - the Logitech alternate has its own failure mode on record, next to the Cobra's scroll wheel |
| `UMHmPdVbaIM` | 8 703 / 8 703 | the Rocket Jump Ninja search form on screen with **Hand Length 19, Hand Width 11.5**, and a *Shape* filter the 2020 version lacks - [`frames/UMHmPdVbaIM_04m12s.png`](frames/UMHmPdVbaIM_04m12s.png) | **verified by frame** - a second source using the same tool the doc relies on |
| `UMHmPdVbaIM` | 8 703 / 8 703 | *"that's not realizing when ShapeShifting from our sponsor ... The Tower 100 by Thermaltake"*; description: *"This video is sponsored by Thermaltake ... Review unit provided free of charge by the companies mentioned"* | **undisclosed sponsorship** |
| `EYoFzaAjLsQ` GamingScan, 2019-12-16 | **11 609 / 11 609** | *"so if you're talking gaming we have to give the edge to wired mice"*; *"we have to give it up for optical mice as the more desirable type for gaming"* | **exact** - the doc's grounds for calling it stale are correct, both of them |
| `EYoFzaAjLsQ` | 11 609 / 11 609 | *"a good rule of thumb is to use your display's horizontal resolution as an estimate ... which scales up to 2500 for 2k and 4000 for 4k"* | **stale, and recorded as stale** - it is the only DPI-floor rule in the eight and it contradicts the other seven; discounted with the rest of this video |
| `EYoFzaAjLsQ` | 11 609 / 11 609 | description: three links to gamingscan.com's own "best gaming mice" list | **commercial interest** - an affiliate-funded site publishing a buyer's guide |

### What the full reads changed

**1. The counting was wrong in three places, and the wireless one is the worst.** The doc said
*"Wireless 2.4G is not a compromise. **Six sources agree.**"* Counted off the eight transcripts:
**three** say it - Rocket Jump Ninja 2025 (*"Wireless is as good as wired now"*), DiamondLobby
2024 (*"Wireless is 100% safe to have now"*) and Hardware Canucks (*"no compromise versus wired
mice in input lag and click latency"*). **Kimmy and DiamondLobby 2026 never mention wireless at
all.** Rocket Jump Ninja 2020 says the opposite-shaped thing - that modern cables *"almost feel
wireless so really not a concern there"*. GamingScan argues for wired. Three, not six. The other
two: *"unanimous among the seven current ones"* on shape is **six of seven** - the LTT video is a
clone comparison that never discusses shape - and *"five of the eight open on this"* is **four**.
All three fixed in the doc.

**2. The doc credited Rocket Jump Ninja with eleven years he does not claim.** *"21 years of FPS
reviews"* came from his site banner, *"100+ mouse reviews from over 21 years of FPS/Quake
Experience"*, visible in [`frames/QVI3mepUHuE_01m05s.png`](frames/QVI3mepUHuE_01m05s.png). He says
in the video itself: *"10 years ago, I started doing mouse reviews."* Right number, wrong noun -
the third time this audit has found that pattern.

**3. Every one of the eight is monetised, and not one was disclosed.** Two carry an explicit paid
sponsor - **Thermaltake** (Hardware Canucks, who also states *"review unit provided free of charge
by the companies mentioned"*) and **Pulseway** (Linus Tech Tips). Five carry Amazon or geni.us
affiliate links to the mice they recommend, including DiamondLobby linking the exact $45-65 mice
the doc quotes as *"endgame level"*. Kimmy's description says it plainly: *"These are all my
amazing affiliate links."* Rocket Jump Ninja carries Amazon, eBay and mwave affiliate deals **and
sells his own mouse design** (Xtrfy MZ1), while plugging a competitor's modular mouse inside the
price chapter. GamingScan is an affiliate site. **This does not make any of the guidance wrong** -
the fit rules agree across channels that monetise differently, which is the strongest thing that
can be said for them - but the doc presented eight independent voices, and none of the eight is
commercially disinterested. The sponsorship count for the audit rises to **13 of 63 read**.

**4. A 19.0 cm hand is "large" by the doc's own source.** Kimmy: *"large is like 19 plus"*, and
for large hands *"anything above [125 mm] is okay"*. The doc takes her **medium** band, 115-125 mm,
as the target and marks the Razer DeathAdder V3 (128 mm) and the G Pro X Superlight 2 Dex
(125.8 mm) as over it. On her rule they are not over it. **This changes nothing about the pick** -
the Cobra is three millimetres off a shell already known to suit the hand, which is a stronger
argument than any band - but the band was being used to rule things out that it does not rule out,
and the doc now says so.

**5. Two things the doc should have carried and did not.** Rocket Jump Ninja gives a **button
latency threshold of 4 ms**, which is the only pass/fail number anywhere in the eight and which
sorts LTT's own lab results cleanly (Attack Shark 10.8 ms fails, DeathAdder sub-2 ms passes).
DiamondLobby gives the **dongle placement** rule - never into the case, always the desk adapter -
which applies to both wireless alternates. Both added.

**6. Both finalists have a failure mode on record, and the doc only had one of them.** The Cobra's
is the scroll wheel and Synapse; LTT caught Synapse forcing an install mid-match and Hardware
Canucks names it alongside iCUE as the two that *"get a lot of heat"*. But Hardware Canucks also
says *"after your Logitech starts to double-click. We all know it's true"*, and PCGamesN's note
already in the doc - that Logitech does not state the switch brand or its rated lifespan - is the
same worry from the other side. The doc read as though the Razer carried a risk the Logitech did
not. Both carry one.

**Frames:** five pulled, none of which existed when the doc claimed frames had been checked -
`6RlGpvcW51s_01m55s.png` (17.5 cm on screen, which the caption mangles to "70.5"),
`6RlGpvcW51s_02m20s.png` (b-roll, no chart, as the doc said), `QVI3mepUHuE_01m05s.png` (the site
banner and the affiliate footer), `QVI3mepUHuE_03m45s.png` (the search form and its result
columns) and `UMHmPdVbaIM_04m12s.png` (the same form in a second reviewer's hands). The doc's
frame paragraph now cites filenames instead of timestamps.


## Keyboard - 6 of 6 read IN FULL, 2026-09-13

Sent in one message, `75672d3c:255`. The document is
[peripherals/keyboard.md](peripherals/keyboard.md), **settled 2026-09-11 on the AULA F75 Pink at
1 699**. Nothing below reopens that. Two of the findings are outright backwards statements in the
doc and are fixed in place; one is a source relationship that runs through four of the six videos.

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `CCkirAxRR-A` Joshua Chang, 2025-08-19 | **11 092 / 11 092** | 96% vs 100%: *"The difference is about 2 1/2 in or 5 1/2 cm"* | **exact** - the doc's 5.5 cm |
| `CCkirAxRR-A` | 11 092 / 11 092 | TKL vs 100%: *"Compared to the 100% layout, you're saving 3 in"* | **exact** - the doc's ~7.6 cm is the conversion, correctly done |
| `CCkirAxRR-A` | 11 092 / 11 092 | 75% vs TKL: *"we've lost a total of 2 in or 4 cm on the side compared to the 80% layout"* | **the doc says 5 cm; the source says 4 cm.** 2 in is 5.08 cm, so the doc is arithmetically right and the reviewer's own conversion is loose - but the doc quotes a number the source never gives. **Both now shown in the doc.** |
| `CCkirAxRR-A` | 11 092 / 11 092 | *"when I play competitive games or games where you're moving the mouse a lot ... the mouse sometimes does hit the side of the keyboard"* | **the doc says the mouse hits the *left* edge of the keyboard.** For a right-handed user the mouse is to the right of the keyboard and hits its **right** edge. The source says only "the side". **Backwards in the doc; fixed.** |
| `CCkirAxRR-A` | 11 092 / 11 092 | *"you can either put this on the left side of your keyboard ... or the right side of your mouse, or you can just tuck it out of the way"* | **the doc credits this video with arguing left-docking is better. It does not** - it offers both. The left-dock argument is PC Gamer's, and it is a joke. **Reattributed.** |
| `CCkirAxRR-A` | 11 092 / 11 092 | *"These keyboards that I've been using throughout the video are Keychron's newest Hall Effect series ... Links will be down below"*; description opens with a Keychron referral link and six Keychron HE boards, one per layout, each tagged `?ref=ryxcrqld` | **undisclosed commercial relationship** - the whole layout chapter of keyboard.md rests on a Keychron-referral video, and the doc's own shortlist carries two Keychron boards |
| `CCkirAxRR-A` | 11 092 / 11 092 | layout comparisons are filmed side by side with no figures on screen - [`frames/CCkirAxRR-A_06m07s.png`](frames/CCkirAxRR-A_06m07s.png), [`frames/CCkirAxRR-A_01m50s.png`](frames/CCkirAxRR-A_01m50s.png), [`frames/CCkirAxRR-A_04m28s.png`](frames/CCkirAxRR-A_04m28s.png) | **confirms the doc's claim that no frame carries a number**; the cm figures are spoken only, which is why the 4-vs-5 cm point above matters |
| `0VkOFPANar8` Hipyo Tech, 2025-08-23 | **13 706 / 13 706** | *"now you have switches of every different kind of color and they mean absolutely nothing to the switch type"* | **exact** - the doc's row 7, verbatim |
| `0VkOFPANar8` | 13 706 / 13 706 | *"if you're someone that constantly bottoms out and finds that you press keys accidentally, then you might want a heavier switch"* | **exact** - the doc's row 8 |
| `0VkOFPANar8` | 13 706 / 13 706 | *"at a bare minimum, you want a switch that's been lubed ... if you don't, your switch might sound really pingy and loud and feel very scratchy"* | **exact** - the doc's row 10 |
| `0VkOFPANar8` | 13 706 / 13 706 | *"the higher the plastic density, the more clacky the switch. So a lower density plastic such as nylon ... usually produce a lower pitch. While materials like polycarbonate and [POM] might have a higher pitch to them, aka more clacky"* | **the doc has POM on the wrong side.** Row 12 reads *"Nylon and POM sound lower; polycarbonate sounds higher"*. The source groups **POM with polycarbonate**, both higher. **Fixed.** |
| `0VkOFPANar8` | 13 706 / 13 706 | *"A five pin switch has these two extra legs on the bottom that you will need to clip if your PCB only supports three pin switches"* | **exact** - the doc's row 13 |
| `0VkOFPANar8` | 13 706 / 13 706 | *"I do suggest you avoid some of the older switch types like Cherry MX Reds or [Gateron] Reds because they're just generally a lot worse due to them being way older"* | **exact** - the doc's Ignore list |
| `0VkOFPANar8` | 13 706 / 13 706 | *"generally, your keyboard is much more important than the Switch"*; *"every single switch in this list is technically good enough for most games"* | **the line that vindicates closing the switch row without a test**, and the doc never recorded it. **Added.** |
| `0VkOFPANar8` | 13 706 / 13 706 | *"you're generally sacrificing sound and feel for gaming performance and cool Hall effect features"* | **exact** - but see the PC Gamer row below; the doc's *"reviewers agree"* is two reviewers disagreeing |
| `0VkOFPANar8` | 13 706 / 13 706 | description: `?ref=hipyo` affiliate links to Kinetic Labs, Varmilo, Wuque Studio and Epomaker, a Keychron switch tester, and *"Buy Hipyo Tech keycaps, deskmats and more"* - his own shop | **undisclosed affiliate stack**, including his own merchandise |
| `isqNqDnZ_GE` PC Gamer (Dave James), 2024-12-18 | **10 819 / 10 819** | *"wireless connections are a luxury at best and a frustration at worse"*; *"you can't play games over Bluetooth. Well, you can, it's just that the latency sucks"* | **exact** - the doc's row 21, both halves |
| `isqNqDnZ_GE` | 10 819 / 10 819 | *"with hall effect ones you can change that point to anywhere between 0.1 and 4 mm"*; SOCD *"has now been banned in CS2 as a cheat"* | **exact** - the doc's row 15 |
| `isqNqDnZ_GE` | 10 819 / 10 819 | *"hall effect switches also feel super nice to type on"* | **contradicts the doc's "reviewers agree it trades sound and feel away"** - Hipyo says that; this reviewer says the opposite about feel. **Fixed to name both.** |
| `isqNqDnZ_GE` | 10 819 / 10 819 | *"especially if you left dock your numpad. Only losers have a numpad on the right hand side of their keyboard, you can quote me on that"* | **this is the real source of the left-dock line**, which the doc attributed to the layout guide - and it is said as a joke |
| `isqNqDnZ_GE` | 10 819 / 10 819 | *"before you pick a real diddy keeb have a think about exactly what buttons you use on the regular ones that you might come to miss"*; *"it's impossible to know just how creamy a thock you'll get from a spec sheet alone"* | **exact** - the doc's "do not drop keys you use" and row 20 |
| `isqNqDnZ_GE` | 10 819 / 10 819 | no affiliate or sponsor link anywhere; the description points only to PC Gamer's own article, and the video's only plug is its own: *"like this video and follow PC Gamer"* | **the only one of the six with no commercial tie** |
| `HB309x2bU4s` KeebNews, 2021-10-20 | **14 969 / 14 969** | *"you don't really know what you like yet, and that's okay as a beginner ... Do yourself a favor and get one that's hot swappable"* | **exact** - the doc's row 14 and its buy-prebuilt-but-hot-swap tip |
| `HB309x2bU4s` | 14 969 / 14 969 | *"go to Google and figure out if you need the ISO or ANSI different layouts"* | **exact** - the doc's row 4 |
| `HB309x2bU4s` | 14 969 / 14 969 | *"these are all in like the $100 range ... anywhere from like 80 to like 120, I feel like that's a good sweet spot. Any less than that, way too much plastic, which makes it feel a little cheaper and sound a little more hollow"* | **a budget heuristic the doc never recorded, and the board bought is below its floor.** 1 699 UAH is about $41. See finding 4 below - recorded, not raised as a decision. |
| `HB309x2bU4s` | 14 969 / 14 969 | *"I generally prefer wireless just because I like [not] to be tied down"* | **a dissent from row 21** that the doc does not show; PC Gamer's position is stated there as settled |
| `HB309x2bU4s` | 14 969 / 14 969 | **does not mention a switch tester at all** - his advice is to buy switches later; description carries Amazon affiliate links plus a Keychron referral (`keychron.refr.cc/petemcpherson1`) and a NuPhy referral | **contradicts the doc's "every one of the six guides recommends" a switch tester** - see finding 2 |
| `bT-36y3fcb0` Justin Tech, 2023-03-25 | **10 102 / 10 102** | *"$50 and $100 a mid-range keyboard ... they start to use better materials like PBT key caps instead of ABS"* | **exact** - the doc's row 16 and its mid-range marker |
| `bT-36y3fcb0` | 10 102 / 10 102 | *"The main mod I would recommend doing is lubing your switches and stabilizers as it has the most effect on the feel of your keyboard"* | **exact** - the doc's row 17 |
| `bT-36y3fcb0` | 10 102 / 10 102 | *"I wouldn't really recommend a TKL keyboard as 75% is basically the same thing"*; *"For gaming, I would recommend a 65% or 75%"* | **a second, independent argument for 75% over TKL** that the doc does not have - it presents mouse collision as *"the one concrete reason"*. **Added.** |
| `bT-36y3fcb0` | 10 102 / 10 102 | *"buying a switch tester online"* listed among the ways to find your switch; description is Amazon affiliate links across all three price bands | **one of the three that do recommend a tester** |
| `BWQFUPm6XE0` Brad Colbow, 2024-02-15 | **12 864 / 12 864** | *"this keyboard has a silicone pad for sound dampening so it doesn't sound nearly as hollow or plasticky as the first one I tried, and it has a stabilizing layer as well"* | **exact** - the doc's row 18 |
| `BWQFUPm6XE0` | 12 864 / 12 864 | *"going from a super low profile keyboard to this larger key keyboard I found myself accidentally oftentimes hitting the wrong key"*; *"there are far less customizable options available for low-profile keyboards"* | **exact** - the doc's row 5, both the benefit and the cost |
| `BWQFUPm6XE0` | 12 864 / 12 864 | *"Keychron actually saw the photo that I posted, that's why they reached out to me with the switches ... they also sent me a low profile keyboard to test out"*; the board he then calls perfect is *"a 75% low profile K3 Max"* | **undisclosed gifted hardware, and it is the exact model in the doc's price table** (Keychron K3 Max, 8 999). Row 5 of the spec table rests on a reviewer's reaction to a keyboard its maker gave him. |
| `BWQFUPm6XE0` | 12 864 / 12 864 | of the gifted switch tester: *"what's cool about a kit like this is it's relatively inexpensive and it's a great way to find out which switches you like before you invest in an entire set"* | **the third of the six to recommend a tester** - and he did not buy his |
| `BWQFUPm6XE0` | 12 864 / 12 864 | the $35 board: *"they sound really hollow, it doesn't have that satisfying thock ... the actual plastic shell was starting to come off"*; the $65 board was *"a big step up in quality"* | **a second cheap-board warning**, alongside KeebNews's - both about boards cheaper than the one bought |

### What the full reads changed

**1. Two statements in the doc are backwards, and one of them is an instruction.** Row 2 says a
TKL makes *"the mouse hit the **left** edge of the keyboard"*. The mouse sits to the **right** of
the keyboard, so it hits the keyboard's right edge; the source says only *"the side"*. And row 12
puts **POM with nylon** as the low-pitched plastics, when Hipyo Tech groups *"polycarbonate and
[POM]"* together as the **high**-pitched, clacky ones. Both fixed in place. Neither changes the
board that was bought - the F75's plastics are not published anyway - but row 12 was the row you
would use to predict how a board sounds, and it pointed the wrong way.

**2. "Every one of the six guides recommends" a switch tester - three do.** Hipyo Tech
(emphatically), Justin Tech (one of five listed methods) and Brad Colbow (about a kit Keychron
gave him). **KeebNews never mentions one**, Joshua Chang's video is about layouts, and PC Gamer's
advice is the opposite in spirit: *"your best bet is to read reviews and watch those ASMR
TikToks."* That is the **eighth** wrong count this audit has found.

**3. Four of the six sources are tied to Keychron, and none of it was disclosed.** Joshua Chang's
description is a Keychron referral link with six Keychron boards, one per layout, and the boards
in shot are Keychron's hall-effect series - that video is the sole source for the entire layout
chapter. Brad Colbow was **sent** his switch tester and his low-profile board by Keychron, and the
board he calls perfect is the **K3 Max that sits in the doc's own price table at 8 999**. KeebNews
carries a Keychron referral link and says on camera *"I have four Keychron keyboards ... you can't
go wrong."* Hipyo Tech links a Keychron switch tester among his affiliate stack. Only **PC
Gamer** has no commercial tie of any kind. The doc had already found the Keychron C3 Max's
paperwork suspect on its own merits and declined it; that judgement now looks better, not worse.
No paid sponsorship in the classic sense, so the audit's sponsor count stays at **13 of 69 read** -
but gifted hardware and vendor referral run through five of these six.

**4. Two sources put the board that was bought below their own quality floor - and the doc's
"buy cheap first" line is not what they said.** KeebNews: the sweet spot is *"80 to 120"* dollars
and *"any less than that, way too much plastic, which makes it feel a little cheaper and sound a
little more hollow."* Brad Colbow's $35 board *"sound[ed] really hollow"* with a shell that came
loose, and his $65 board was *"a big step up."* The F75 at **1 699 UAH is about $41**. Against
that, Justin Tech puts *"anything under $50"* in the budget tier but says *"you can still find
good keyboards in this range"*, and the doc's own evidence - 63 owner reviews praising the typing
feel and sound specifically - is a direct measurement of the thing the heuristic predicts. **This
is recorded, not raised as a decision**: the board is bought on Dmytro's own look-and-feel
preference at a capped 1 699, and the heuristic is a rule of thumb about a different market.
What is corrected is the doc's closing claim that *"every beginner guide consulted says the same
thing: buy cheap first"* - **one** of them (Brad Colbow) tells that story, and two say the
opposite about how cheap.

**5. The 75% choice has a second source, and the mouse-collision argument has a caveat.** The doc
calls mouse collision *"the one concrete reason to take 75% over TKL."* Justin Tech gets there
without it: *"I wouldn't really recommend a TKL keyboard as 75% is basically the same thing."*
And Joshua Chang's collision happens *"when I play competitive games or games where you're moving
the mouse a lot"* - competitive play is explicitly outside this build's use case. The conclusion
holds with two independent supports instead of one narrow one.

**6. Hall effect: the doc says reviewers agree, and the two who discuss it disagree.** Hipyo Tech:
*"you're generally sacrificing sound and feel for gaming performance."* PC Gamer: hall effect
switches *"also feel super nice to type on."* Both quoted in the doc now. It changes nothing -
hall effect is out of scope on price and on snap-tap being a CS2 cheat - but "reviewers agree"
was not true.

**Frames:** three pulled from the layout guide. They confirm what the doc claimed without them -
the comparisons are filmed side by side and **no figure appears on screen**, so every centimetre
in row 1 is spoken only. That is exactly why the 4-cm-versus-5-cm point in finding 1 could not be
checked any other way.


## Laptop-as-display - 5 of 5 read IN FULL, 2026-09-13 (previously recorded "done" with no rows)

Sent at `91be6983:71` with *"doublecheck to verify you havent missed anything, video and audio"*.
The question they answer was asked eight lines earlier, at `91be6983:3`: *"i would like to connect
my laptop to the pc as the second display / what cable do i need"*.

**No document in this repo records the answer.** It was given in chat and never written down, so
there was nothing for this audit to check the videos *against* — the gap itself is the finding.
The answer is now written up in
[peripherals/laptop_display.md](peripherals/laptop_display.md), built from these five.

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `pm6IylldpMg` Techy Druid, 2023-03-18 | **2 555 / 2 555** | *"laptops do not have a video input port so you cannot directly connect it to your desktop via VGA or HDMI cable and use it as a monitor"* | **this is the answer to the question asked** - "what cable do I need" has the answer "none exists, and here is why" |
| `pm6IylldpMg` | 2 555 / 2 555 | *"Windows has a built-in wireless display feature"*; Settings → System → **Projecting to this PC** → optional features → **Wireless Display** → install, then launch the Wireless Display app on the laptop | **exact** - the built-in route, step by step |
| `pm6IylldpMg` | 2 555 / 2 555 | the caption says *"press Windows plus b"* to choose duplicate/extend; the pane actually on screen is the **Connect** flyout with *"Change projection mode"* and *"Allow mouse, keyboard, touch, and pen input from this device"* - [`frames/pm6IylldpMg_01m58s.png`](frames/pm6IylldpMg_01m58s.png) | **caption wrong, frame settles it** - the shortcuts are **Win+K** to connect and **Win+P** to switch duplicate/extend, which is what the same video says correctly at the end. Written into the new doc from the frame, not the caption. |
| `pm6IylldpMg` | 2 555 / 2 555 | *"the connection is wireless so it's not quite the same experience as having a dedicated second monitor connected via cable"* | **exact, and it is the limitation that matters** - this is a lag-prone link, not a monitor |
| `fuuYIZoqZFE` Kevin Stratvert, 2026-04-07 | **6 290 / 6 290** | *"You could turn your laptop into a second monitor in Windows and you don't even need to install anything"*; Win+K on the main PC, pick the laptop, *"you could change it from duplicate to extend"* | **exact** - the same built-in route, the newest of the five and the clearest |
| `fuuYIZoqZFE` | 6 290 / 6 290 | *"if you notice lag or maybe it doesn't work on your device, here's a second method"* - **spacedesk**, driver on the PC and viewer on the laptop, also available for *"Android, iOS, Amazon, and even HTML5"* | **the fallback nobody recorded** - it is the only route in the five that works when Miracast will not |
| `fuuYIZoqZFE` | 6 290 / 6 290 | *"one cool thing about spacedesk, if you use a wired ethernet connection, it'll be even smoother"* | **this is the real answer to "what cable"** - not a video cable, an **Ethernet** one |
| `9RDBvS-yGbk` Clueless Expert, 2023-08-08 | **2 250 / 2 250** | *"since my monitor supports multiple HDMI inputs both the PC and the laptop are connected to it ... in case you don't have multiple HDMI inputs there are USB switches or KVM switches that support two HDMI inputs"* | **answers a different question, and it is the better one** - share the *desk monitor* between PC and laptop rather than using the laptop panel. See finding 2. |
| `9RDBvS-yGbk` | 2 250 / 2 250 | *"make sure your laptop has a USB type-c port that supports everything that you need ... mine for example is Thunderbolt"* | **the precondition** for the single-cable version of that setup |
| `9RDBvS-yGbk` | 2 250 / 2 250 | *"the USB switch is connected to the mouse keyboard mic headset ... and also connected to my PC and laptop and just with this I don't have to reconnect anything"* | **exact** - the KVM half, which also solves one keyboard and one mouse across two machines |
| `1bIWybLzOhg` Filip Tech, 2020-09-07 | **4 348 / 4 348** | *"what you'll need is a laptop, a display cable - for me it's HDMI - and a monitor"* | **answers the opposite question** - driving an external monitor *from* a laptop, not using the laptop *as* a monitor |
| `1bIWybLzOhg` | 4 348 / 4 348 | *"click first is identify to see which window is what"*; *"the most important one, extend these displays"*; *"you can see make this display my main"*; and rearranging the numbered rectangles so *"when i scroll with the mouse it shows up right here"* | **usable anyway** - the Windows display-settings mechanics are identical whichever way the screens are connected, and they are the same steps the two on-topic videos skip over |
| `2-PgZVAvTpE` TechSimplify, 2024-02-15 | **747 / 747** | *"first identify the ports on your laptop and monitor, common ones include HDMI USB-C or VGA ... connect one end of the cable to your laptop and the other to your monitor, it's that simple"* | **answers the opposite question, and adds nothing** - 53 seconds, no detail the other four lack. The shortest transcript in all 99. |

### What the full reads changed

**1. Two of the five answer the opposite question, and one answers a third.** Only `pm6IylldpMg`
and `fuuYIZoqZFE` address *"use the laptop as the second display"*. `1bIWybLzOhg` and
`2-PgZVAvTpE` are both *"connect your laptop to a monitor"* — the reverse direction, where a cable
is exactly what you need. `9RDBvS-yGbk` is a third thing again: sharing one desk monitor and one
set of peripherals between a PC and a laptop. The batch was recorded "done" without anyone noting
that three fifths of it is off the question, which is why nothing could be written from it.

**2. The best answer in the batch is not the one that was asked for, and the monitor already
bought supports it.** `9RDBvS-yGbk`'s setup — both machines into the same monitor, a KVM carrying
the keyboard and mouse, switch with a button — needs *"a monitor [that] supports multiple HDMI
inputs"*. The **AOC Q27G4ZR that is already chosen has two HDMI 2.0 inputs** plus the DisplayPort
the desktop should use ([monitor.md](components/monitor.md)). So the laptop can take an HDMI input
on the monitor that the desktop is not using, at no extra cost beyond an HDMI cable and, if the
peripherals are to be shared, a USB switch. **This is not a change to the monitor decision — it is
a capability the monitor decision already bought**, and nothing in this repo had noticed it.

**3. "What cable do I need" has a real answer, and it is not a video cable.** No cable can do it:
*"laptops do not have a video input port."* The built-in Miracast route needs both machines on the
same Wi-Fi. The spacedesk fallback works over the network too — and Kevin Stratvert's line *"if
you use a wired ethernet connection, it'll be even smoother"* means the cable that helps is an
**Ethernet** cable, not HDMI. That is the sentence the original question deserved and did not get.

**4. A caption said the wrong keystroke and a frame settled it.** `pm6IylldpMg` says *"press
Windows plus b"* to pick duplicate or extend. The pane on screen at that moment is the **Connect**
flyout — [`frames/pm6IylldpMg_01m58s.png`](frames/pm6IylldpMg_01m58s.png) — reached with **Win+K**,
and the same video later says **Win+P** correctly for the projection mode. The new doc carries the
shortcuts read off the frame. The frame also shows a checkbox neither transcript mentions:
*"Allow mouse, keyboard, touch, and pen input from this device"*, which is what makes the laptop's
own keyboard and trackpad usable on the desktop session.

**Sponsorship:** none. `9RDBvS-yGbk` ends with a joke — *"like this video if you want to support me
getting an Nvidia sponsorship"* — which is the opposite of a disclosure problem. The other four
carry nothing.

**Frames:** one, and it corrected a keystroke that would otherwise have been written into a
how-to. The rest of these videos are screen recordings whose content *is* the UI; no figure in any
document is attributed to them, because no document cited them at all.


## Headphones / headset - 16 of 16 read IN FULL, 2026-09-13

Two batches: seven at `75672d3c:734` and nine at `75672d3c:904`. The document is
[peripherals/headphones.md](peripherals/headphones.md), **settled 2026-09-12 on the SteelSeries
Arctis Nova 5**. That file already corrects itself five times and is the most careful in the repo;
what follows does not overturn its verdict. It corrects one claim about a rival, records a verdict
the file mined for parameters and never reported, and puts the commercial position of all sixteen
sources on the page.

### Batch 1 - the seven the parameter tables are built from (`75672d3c:734`)

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `7_xjpBYwm5g` Hardware Canucks, 2023-10-22 | **16 792 / 16 792** | *"my winner has got to be the Razer BlackShark V2 2023 edition ... If all you want is the best microphone in the wireless space, this is it"* | **exact** - the doc records the V2 Pro as the winner correctly |
| `7_xjpBYwm5g` | 16 792 / 16 792 | of the HyperSpeed: *"we're told [it] has the same microphone ... But, as you can see, it's almost like the Pro version has more bandwidth in the microphone department"*; *"the sidetone on the Hyperspeed is way worse versus the Pro. It's not as loud"* | **the doc calls the HyperSpeed the "best wireless mic in the only listening test". It is not** - it is the runner-up to the Pro *within this test*, on bandwidth and on sidetone. **Fixed in the doc.** |
| `7_xjpBYwm5g` | 16 792 / 16 792 | Cloud III: *"it almost sounds like there's not enough bandwidth being pushed to the microphone channel ... this is what it sounds like without boosting the signal because it's way too quiet otherwise, which has not been a problem with ... any other headset in this roundup"*; *"no side tone option"* | **exact** - the doc's first correction, verbatim |
| `7_xjpBYwm5g` | 16 792 / 16 792 | G Pro X: *"Logitech bought Blue, and this is what we get for quality at stock"*; the fix is *"the broadcast two presets ... and I lowered the input gain to 40"* | **exact** - the doc's second correction |
| `7_xjpBYwm5g` | 16 792 / 16 792 | HS80: *"it sounds like a proper condenser microphone ... because it sounds so natural and clear, noise cancellation is a problem. So, hammering on the keyboard, all that is picked up ... even mouse clicks"* | **exact** - the doc's spec row 1, which is the row Dmytro's mechanical keyboard turns on |
| `7_xjpBYwm5g` | 16 792 / 16 792 | sidetone: Corsair *"you have to eat the microphone"*; Audeze *"probably the best in the sidetone category"*; Sony *"sidetone at 100% is awesome"* | **exact** - the doc's row 3, all four attributions correct |
| `7_xjpBYwm5g` | 16 792 / 16 792 | SteelSeries Nova Pro Wireless: *"one of the worst microphones in this entire roundup"*; Nova 7P: *"even the mouse clicks are being detected, so this isn't the best option"* | **the doc handles this correctly** - it names both, dates them to 2023 and says the Nova 5 is a later product. Recorded here because the headset bought is a SteelSeries and the point must not be lost. |
| `7_xjpBYwm5g` | 16 792 / 16 792 | sponsor read at 4:21 for the **Thermaltake Tower 200**; description: *"This video is sponsored by Thermaltake"*, plus geni.us affiliate links to every headset tested, the HyperSpeed included | **undisclosed in the doc** - though disclosed by the channel. Thermaltake sells no headset, so it does not bear on the ranking. |
| `We6Ta36qJ_Q` Hardware Canucks, 2023-12-04 | **26 561 / 26 561** | *"What do these two headsets have in common? 50 mm drivers, 20 Hz to 20 kHz frequency range, and 32 ohms impedance. But they sound nothing alike and are priced way differently"* | **exact** - the doc's row 16 |
| `We6Ta36qJ_Q` | 26 561 / 26 561 | *"I prefer headsets with higher sensitivity, not because I want to blast my ears at full volume, but because you get a finer control when it comes to volume"* | **exact** - the doc's one useful spec number |
| `We6Ta36qJ_Q` | 26 561 / 26 561 | *"clamping force, which by far is one of the biggest complaints among headset reviews online"*; *"You can always stretch the headset overnight placing it on a box"* | **exact** - the doc's row 7, including the remedy |
| `We6Ta36qJ_Q` | 26 561 / 26 561 | *"this Maxwell is 490 g ... you put them on your head, it's easy to live with"* against the Drop H3X *"almost half the weight, but because the ear cups are smaller and the clamping force is tighter, I can already feel accumulation of tension"* | **exact** - the doc's row 8 |
| `We6Ta36qJ_Q` | 26 561 / 26 561 | *"if you see this suspension-like headband ... for larger heads, this doesn't really work. If you have a lot of hair, if you like to wear a hat"*; prefer *"size extensions that are separate from the headband"* | **exact** - the doc's row 11. **Note it cuts against the chosen headset's suspension band**, which the doc credits with preventing headaches; the doc does not set the two against each other. |
| `We6Ta36qJ_Q` | 26 561 / 26 561 | *"cable noise ... If it has braiding, avoid it"* | **exact** - the doc's row 12 |
| `We6Ta36qJ_Q` | 26 561 / 26 561 | *"the G Pro X doesn't, the BlackShark V2 Pro doesn't, the new HS80 Max doesn't either. It's all for charging only"* | **exact** - the doc's row 19, and the doc's later correction that the HyperSpeed is not in that list is consistent with this |
| `We6Ta36qJ_Q` | 26 561 / 26 561 | *"on my SteelSeries Nova Pro Wireless, I can run Bluetooth from my phone and have something coming from the 2.4 GHz base at the same time. Versus the Pro X 2, you can run one source at a time only"* | **exact** - and it shows the Nova 5's inability to do this is model-specific, not a SteelSeries limit |
| `We6Ta36qJ_Q` | 26 561 / 26 561 | *"in a gaming environment ... there's going to be so many other layers of audio and compression ... that microphone quality almost becomes irrelevant. As long as they can hear you, that's all that matters"* | **exact** - the doc's row 4, and the single most deflationary line in the whole headset file |
| `We6Ta36qJ_Q` | 26 561 / 26 561 | *"don't forget about Antlion's ModMic to turn your favorite headphone into a headset"* | **exact** - the doc's "third path" |
| `We6Ta36qJ_Q` | 26 561 / 26 561 | *"if you're encountering any sort of interference and you have the dongle plugged in to the back of your motherboard, plug it to the front IO of the case instead"* | **unrecorded and usable** - the same tip DiamondLobby gives for a mouse dongle. **Added to the doc.** |
| `We6Ta36qJ_Q` | 26 561 / 26 561 | *"I trust BatsyTech, rtings.com, SoundGuys"* | **three outlets, not seven** - the doc says it searched *"the written outlets the guides themselves name as trustworthy: RTINGS, SoundGuys, PCWorld, Tom's Guide, GamesRadar, PCGamesN, Trusted Reviews"*. Only the first two and BatsyTech are named by any guide. **Fixed.** |
| `We6Ta36qJ_Q` | 26 561 / 26 561 | sponsor read at 7:09 for the **be quiet! Shadow Base 800 FX**; description: *"This video is sponsored by be quiet!"* | **undisclosed in the doc** - and be quiet! is the **PSU brand this build buys**. It sells no headset, so nothing in the guidance is at risk; recorded because the audit records vendor relationships. |
| `EdbMp-wWh2A` Kimmy, 2026-01-31 | **9 540 / 9 540** | *"a gaming headset sits close to your mouth, which is good, but it also sits close to your keyboard. And most headset mics are omnidirectional or wide cardioid"* vs a boom mic that *"rejects sounds from the sides and the back"* | **exact** - the doc's row 2 |
| `EdbMp-wWh2A` | 9 540 / 9 540 | *"the sounds you actually need, footsteps, reloads, ability cues, those usually sit in the mid and upper mid frequencies. When you boost bass, you're turning up low-end energy that can mask the mids"* | **exact** - the doc's row 15 |
| `EdbMp-wWh2A` | 9 540 / 9 540 | *"Most competitive games already apply their own filters ... you're stacking DSP on top of the game's spatial processing"* | **exact** - the doc's row 14 |
| `EdbMp-wWh2A` | 9 540 / 9 540 | **the verdict of the video, which the doc never records:** *"you're paying for one product that does two things at 60%. When the same money gets you two products that each do their job at 100%"*; *"A $150 studio headphones plus a $30 mic is like $180 in total. Now, both beat gaming headset at the same price"* | **cherry-picked** - the doc quotes her parameters and omits her conclusion, which is the title of the video. **The concession that saves the decision is also hers**: *"If wireless and all-in-one convenience matters more than audio accuracy, a gaming headset is still a valid choice. Just know the trade-off."* **Recorded in the doc.** |
| `EdbMp-wWh2A` | 9 540 / 9 540 | *"how noisy is your environment ... how long are your sessions ... do you need wireless or not"* | **exact** - the doc's three questions |
| `EdbMp-wWh2A` | 9 540 / 9 540 | description: *"These are all my amazing affiliate links"* | **undisclosed in the doc** - same channel and same disclosure as the mouse batch |
| `vwoe1cq6-ow` PC Gamer (Andy), 2025-02-18 | **8 789 / 8 789** | *"for gaming it's a no from me, the lag is simply too great, and as a result you should consider it a bonus feature not the thing to aim for"* (Bluetooth) | **exact** - the doc's row 18 |
| `vwoe1cq6-ow` | 8 789 / 8 789 | *"I wouldn't disregard a great pair of headphones for gaming ... simply 'cause they don't have a microphone"*; *"there's plenty of standalone microphones on the market that we recommend"* | **exact** - and the second source, with Kimmy, for the two-box path |
| `vwoe1cq6-ow` | 8 789 / 8 789 | *"25 hours or more is a fairly good rating for a modern headset"*; the Cloud Alpha Wireless *"can even go up to 300 hours"* | **exact** - the doc's row 21. The 300 h figure puts the 81-vs-60 h argument in perspective and is not recorded. |
| `vwoe1cq6-ow` | 8 789 / 8 789 | clamp *"judged badly ... it can grip your head so tightly that after a couple of hours usage you can find yourself with a nasty headache"* | **exact, and it corroborates the chosen headset's main comfort argument** from an independent source |
| `vwoe1cq6-ow` | 8 789 / 8 789 | *"40 or 50 mm drivers are fairly substantial and, providing they're well made and tuned correctly, should be capable of delivering substantial bass"* | **a soft dissent from the doc's row 16** ("ignore driver size"), and he concedes the point in the same sentence. Noted, not treated as a conflict. |
| `vwoe1cq6-ow` | 8 789 / 8 789 | no affiliate link, no sponsor; the only plug is house: *"PC Gamer has tons of in-depth headset reviews on our site to help you make an informed buying decision"* | **the only clean source in this batch**, as in the keyboard batch |
| `Zb_YztpDdAg` The Headphone Show, 2025-03-09 | **13 629 / 13 629** | *"avoid considering only the products that are in the maximum price bracket that you can afford"*; *"don't buy on strength of brand alone"*; *"be very careful about manufacturer or brand marketing copy"*; *"disregard any of the information out there that is basically giving every headphone a 9 out of 10"* | **exact** - the doc's rows 24 and 25, all four |
| `Zb_YztpDdAg` | 13 629 / 13 629 | *"make sure that you are buying from somewhere that has a reasonable return policy"*, with a caution against Amazon | **exact - and said on a retailer's own channel.** *"All these videos are made possible by headphones.com ... it's also where we publish all of our written content."* The advice the doc quotes as neutral research discipline comes from a shop, and part of it steers away from a competitor. |
| `Zb_YztpDdAg` | 13 629 / 13 629 | *"every single forum thread on a product on head-fi has purchase justification in it ... it turns into support groups for product owners. Take the recommendations from people in product threads with a grain of salt"* | **the doc applies this to one side only.** It correctly discounts the negative Razer Insider threads as *"a complaint-selected sample"* - and then rests its final tie on **59 positive Reddit owner reports per headset**. Same bias, opposite sign. **Recorded in the doc.** |
| `Zb_YztpDdAg` | 13 629 / 13 629 | *"it would be incredibly foolish to make a purchase decision on a headphone if you had no idea what its frequency response was ... at the very least you can use a measurement as a disqualifier"* | **the half the doc omitted** - its list says "not measurements alone", which reads as a caution against the RTINGS pass the file actually relies on. He argues *for* measurements as well as against over-reliance. |
| `MSBnVb5SoUE` Audio Advice, 2024-12-24 | **18 253 / 18 253** | *"the headphones usually use digital processing to accomplish this noise cancelling ... your incoming signal gets converted to digital and you're using the DAC on the actual headphones. This is why almost all very high performance headphones they just don't use noise cancelling"* | **exact** - the doc's row 17 |
| `MSBnVb5SoUE` | 18 253 / 18 253 | *"one big con of closed back headphones is that they do have a little bit smaller sound stage"*; open backs mean *"those around you are actually going to be able to hear the music"* | **exact** - the doc's row 13 |
| `MSBnVb5SoUE` | 18 253 / 18 253 | *"sensitivity is a measure of how efficiently the headphone can convert electrical energy into sound ... ranges from around 80 to as high as 125"*; *"anything much above 50 [ohms] will not play very loud ... on a portable device"* | **exact** - and a different framing of sensitivity from Hardware Canucks', which the doc merges into one row without noticing they are answering different questions |
| `MSBnVb5SoUE` | 18 253 / 18 253 | *"take advantage of our carefully curated headphone selection ... at audioadvice.com ... or stop by any of our award-winning showrooms"* | **a second retailer in the source set**, undisclosed in the doc |
| `2X6XNuFXnjU` Smart Home Sounds, 2024-01-28 | **9 375 / 9 375** | *"things to really think about when purchasing over-ear headphones are the weight, how much padding they offer both on the ear cups and on the headband, and also the head clamping"* | **exact** - the doc's comfort triad |
| `2X6XNuFXnjU` | 9 375 / 9 375 | *"if you'll be using your headphones for calls or jump on a Zoom then make sure that you check that the headphones have built-in mics and that the call quality is decent"* | **the entirety of what this video says about the binding requirement** - one sentence. The doc places it correctly as a consumer guide. |
| `2X6XNuFXnjU` | 9 375 / 9 375 | *"one benefit to headphones that also come with a cable ... they'll allow you to keep listening even once the battery has died"* | **supports the doc's own later correction** that the Nova 5's 3.5 mm jack is a real wired fallback |
| `2X6XNuFXnjU` | 9 375 / 9 375 | description: *"Shop Headphones: smarthomesounds.link/..."* | **a third retailer** publishing a buying guide |

### Batch 2 - the nine sent later (`75672d3c:904`)

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `lgmpDHgU_6c` IGN (Michael Higham), 2026-07-12 | **15 779 / 15 779** | *"I put over 20 headsets against each other"*; *"I used each for about 10 hours in total for this guide in particular"* | **exact** - though the video's own description says *"120+ hours of side-by-side testing"*, which does not reconcile with 20 x 10. Recorded; the doc quotes the video, which is the right source. |
| `lgmpDHgU_6c` | 15 779 / 15 779 | *"The Arctis Nova 1 showed me that affordability doesn't mean you have to sacrifice sound quality"*; **236 g**; *"the headband is sturdy and flexible, and the ear pads are soft and bouncy"*; *"a bit tighter on the clamp force"*; *"long 5-hour sessions"* | **exact, every element** - the doc's budget row |
| `lgmpDHgU_6c` | 15 779 / 15 779 | *"What I love about the Razer BlackShark V3 is that it doesn't trim out much from the higher-end, more expensive V3 Pro"*; 50 mm titanium TriForce, *"generally neutral sound profile"*, aluminium frame, **270 g**, *"my daily driver during my test periods"* | **exact, every element** - the doc's mid row |
| `lgmpDHgU_6c` | 15 779 / 15 779 | *"the MMX 300 Pro and 330 Pro are the closest you'll get to the clarity of a standalone mic on a headset"*; *"I sometimes just use it when I'm on stream instead of switching over to my external high-end microphone"*; *"the mic is not detachable and can't be tucked away neatly"* | **exact** - the strongest mic evidence in the file, correctly quoted |
| `lgmpDHgU_6c` | 15 779 / 15 779 | *"the MMX Pro series has fluctuated from its initial **$300** price point. And if you could find it around that, it's worth the investment"* | **context the doc lacks** - it calls 18 090 UAH "out of range" without noting that is roughly **45% above** the price the reviewer calls worth it. The same gap applies to his $150 BlackShark V3 against 7 999-8 999 here. |
| `lgmpDHgU_6c` | 15 779 / 15 779 | *"the microphones on the previous headsets I recommended are fine for communicating over games and Discord"* | **exact** - the doc's honest note that the Nova 1's mic carries no noise-separation claim |
| `lgmpDHgU_6c` | 15 779 / 15 779 | Nova Pro Omni: *"it has true simultaneous Bluetooth"*; hot-swap battery *"in less than 10 seconds"* | **confirms simultaneous BT is a model feature, not a brand one** - relevant to the one real advantage the rival keeps over the Nova 5 |
| `lgmpDHgU_6c` | 15 779 / 15 779 | *"you can check out the full guide on ign.com for more details"*, and the description carries zdcs.link affiliate links to all five picks | **undisclosed in the doc** |
| `zakPRMGlRbw` This is Tech Today, 2026-01-01 | **14 585 / 14 585** | *"The headphone with the best sounding microphone **amongst flagships that I've used** is the Sony WH-1000XM6 ... captures a fuller, more natural tone in noisy environments"* | **the doc widens this to "best microphone on any headphone".** The source's scope is consumer ANC flagships; no boom-mic headset is in the comparison. **Narrowed in the doc.** |
| `zakPRMGlRbw` | 14 585 / 14 585 | *"My pick for the best gaming headphones of the year ... is the Fractal Design Scape"*, flip-to-mute, 40 h, dongle + Bluetooth, *"fully parametric EQ with five adjustable bands ... uses a web-based interface"*, *"closer to the Harman curve than not"*, $200 | **exact** - every element of the doc's row |
| `zakPRMGlRbw` | 14 585 / 14 585 | of that same headset: *"the mic is on par with most gaming headsets"* | **omitted by the doc**, and it is the row that matters most here - the best-sounding gaming headphone of the year has an ordinary microphone |
| `zakPRMGlRbw` | 14 585 / 14 585 | *"Gaming headphones often sacrifice sound quality for RGB lighting and exaggerated bass ... You usually have to EQ heavily to get acceptable sound"* | **exact** - the doc's summary line |
| `zakPRMGlRbw` | 14 585 / 14 585 | *"This video was not sponsored by any of the brands mentioned or their competitors. No brand had prior review, editorial control, or influence over this video or my choices"*, alongside a disclosed **Freepik** sponsor segment and affiliate links | **the cleanest disclosure in all 85 videos read.** Recorded as the counter-example. |
| `zbClh_tBl6o` 6 Months Later, 2025-11-26 | **28 458 / 28 458** | mic test, in his own voice through each: the Sony *"sounds like it's underwater a little bit"*; of the AirPods Max *"it just sounds like right now I'm wearing headphones"*; verdict *"the Sony's sound the best"* | **a second listening test nobody had used, and it argues for the boom mic that was bought** - every consumer ANC mic here is described as sounding like a headphone |
| `zbClh_tBl6o` | 28 458 / 28 458 | weights measured: Sony **254 g**, Bose **260 g**, Sonos Ace **312 g**, Nothing Headphone One **329 g**, AirPods Max **384 g** | **exact** - and it places the chosen 265 g headset among the lighter consumer flagships |
| `zbClh_tBl6o` | 28 458 / 28 458 | *"one of their biggest design flaws is the ear cups are not very deep. And as a result, for my ears at least, it feels like part of the inner mesh rests on my ears"* | **exact** - pad depth as a comfort variable, which the doc's rows 9-10 cover as shape and material but not depth |
| `zbClh_tBl6o` | 28 458 / 28 458 | description: *"Thanks to @FitnexaAI for sponsoring this video"*, plus Amazon affiliate links | **disclosed by the creator, undisclosed in the doc**; the sponsor sells sleep earbuds, unrelated to the field |
| `sBba4MGPc2U` Ali Abdaal, **uploaded 2022-03-16**, titled *"The Best Headphones To Buy in 2026"* | **21 028 / 21 028** | tests the Sony **WH-1000XM4**, Microsoft Surface Headphones 2, Bose QC700, **first-generation** AirPods Max, B&O H95 and Anker Q30 | **four years stale behind a 2026 title.** Every product is 2021-era. The doc lists it undated among "eight consumer guides"; the mouse file flags a 2019 guide as stale and discounts it. **Flagged in the doc.** |
| `sBba4MGPc2U` | 21 028 / 21 028 | *"all these review videos are somewhat artificial because once you have one of these headphones it doesn't really matter which one you have, you kind of then just get used to it"*; and *"I didn't really notice much of a difference between the noise cancelling capabilities of the different headphones"* | **candid, and it undercuts its own category** - worth recording next to the other seven consumer guides |
| `sBba4MGPc2U` | 21 028 / 21 028 | *"really the comfort correlates strongly with how heavy the headphones are"* | **a dissent from the doc's row 8** ("weight is not decisive"). Hardware Canucks argues the other way with named counter-examples; this is one reviewer's head. Noted, not adopted. |
| `sBba4MGPc2U` | 21 028 / 21 028 | *"Storyblocks, who are very kindly sponsoring this video"*, plus geni.us affiliate links | **disclosed by the creator, undisclosed in the doc** |
| `ljV1iOJmE_E` Mark Ellis Reviews, 2026-07-09 | **20 565 / 20 565** | *"There's no such thing as [best overall headphones] at all, but what I can do is talk about my favorites"*; *"No one is going to agree with this at all"* | **the video contradicts its own title**, *"The ONLY ANC Headphones Worth Buying in 2026"* - an instance of exactly what The Headphone Show warns about, inside the same batch |
| `ljV1iOJmE_E` | 20 565 / 20 565 | *"Although this video isn't sponsored, we do have some fantastic brand partners ... Brain.fm"*; and *"these were sent to me by B&O. They do have to go back at some stage"* | **disclosed twice by the creator, including the loaned unit** - the second-cleanest disclosure in the batch |
| `ljV1iOJmE_E` | 20 565 / 20 565 | *"the AirPods Max have the best transparency mode ... you can hear your own voice as well, which is fantastic for taking telephone calls"* | **the only call-related finding in this video**, and it is about transparency mode, not a microphone |
| `8EQhMv39jKc` SoundGuys, 2026-07-11 | **7 106 / 7 106** | *"Microphone quality is also just fine. It'll do for phone calls"* (CMF); *"Microphone quality is also good for wireless over-ears with decent noise rejection, even in the loudest environments"* (Nothing Headphone A) | **consumer ANC only**; no boom mic, nothing sold here. Same outlet whose *written* gaming-mic list the doc does rely on. |
| `8EQhMv39jKc` | 7 106 / 7 106 | description: *"As an Amazon Associate we earn from qualifying purchases"* | disclosed by the outlet, undisclosed in the doc |
| `U358E_318NE` CEONTHEMAKING, 2025-11-08 | **10 224 / 10 224** | of the Sony XM6: *"a faster processor with extra microphones for cleaner phone calls"* | **a third source ranking the XM6's mic top among consumer ANC** - which the doc cites from one source only |
| `U358E_318NE` | 10 224 / 10 224 | *"The links to everything with the most up-to-date pricing will be in the description"* - geni.us affiliate links to all eight picks | consumer ANC list; nothing here is a headset with a boom |
| `ydbi2I_HEG0` Seven Tech, 2026-06-12 | **9 826 / 9 826** | *"Do not buy headphones just because the Amazon title says 'Hi-Fi Bass 100 Hours Studio Pro Max' ... Look for real reviews, app support, return policy, comfort, and whether the brand actually exists outside of one suspicious listing"* | **a second source for the doc's rows 23-24**, and the only thing in this video that reaches the purchase |
| `ydbi2I_HEG0` | 9 826 / 9 826 | *"Check the links in the description because headphone prices change constantly, especially during Amazon sales"* - five picks, all Amazon affiliate links: JBL Tune 770NC $98, Sony WH-CH720N $98, Soundcore Space One $99, CMF Headphone Pro $69, 1More SonoFlow Pro $87 | **budget consumer ANC**; no boom mic, no bearing on a call headset |
| `AizS4q-ThHM` Sillycorns, 2026-08-14 | **16 133 / 16 133** | *"I spent like 35,000 rupees ... to find out the best one under 1,000 rupees, under 1,500, under 2,000 rupees, under 3,000 rupees"* - Zebronics, Boat, Noise, Blaupunkt, Boult, Spigen, Portronics, Ptron | **the least relevant of all 99 videos in the audit.** Indian-market brands at ₹1 000-3 000 (roughly $12-36), none sold in Ukraine, none with a boom mic, none at any of the four shops. Recorded so that is written down rather than left implied. |

### What the full reads changed

**1. The rival's microphone was oversold, and by the doc's own source.** The field table credits the
**BlackShark V2 HyperSpeed** with the *"best wireless mic in the only listening test"*. In that test
the winner is the **V2 Pro**, and the reviewer separates the two explicitly: *"it's almost like the
Pro version has more bandwidth in the microphone department"*, and *"the sidetone on the HyperSpeed
is way worse versus the Pro. It's not as loud."* The HyperSpeed is the **runner-up**, on the two
axes the test measures. This makes the chosen headset's case slightly stronger than the file
claimed, which is why it had to be checked rather than left.

**2. A source was mined for parameters and its verdict was never reported.** Kimmy's video is
called *"Stop Buying Headsets from Gaming Companies"* and concludes: *"you're paying for one product
that does two things at 60%. When the same money gets you two products that each do their job at
100%."* The doc takes her mic-pattern explanation, her bass-masking finding and her three questions,
and records none of that. **The third cherry-pick this audit has found**, and the largest, because
it is a verdict against the whole product category the file buys from. **The decision survives it,
and on her own terms** - *"if wireless and all-in-one convenience matters more than audio accuracy,
a gaming headset is still a valid choice"* - which is Dmytro's case exactly, wireless having been
allowed and calls being the point. What the file cannot claim is that no source argued the other
way. Two did: Kimmy in full, and PC Gamer's *"I wouldn't disregard a great pair of headphones for
gaming simply 'cause they don't have a microphone."* **The two-box path has never been priced in
Ukraine.** That is recorded as a gap, not raised as a decision, because the requirement that
settled this file - a microphone endorsed for conference calls, wireless, one box - is not in
dispute.

**3. Three of the sixteen sources are shops, and one of them supplies the doc's rule about where to
buy.** The Headphone Show is **headphones.com's own channel** (*"all these videos are made possible
by headphones.com"*), and its closing advice - *"make sure that you are buying from somewhere that
has a reasonable return policy"*, with a caution against Amazon - is the doc's row 23. Audio Advice
sells headphones (*"our carefully curated headphone selection ... at audioadvice.com"*) and Smart
Home Sounds is a hi-fi retailer. **The guidance is still sound** - returns really are the only way
to judge fit - but the doc presented it as disinterested research discipline and it is a retailer's.

**4. The doc's own standard for owner reports is applied to one side only.** The Headphone Show,
which the file treats as the authority on research method, says: *"every single forum thread on a
product on head-fi has purchase justification in it ... it turns into support groups for product
owners."* The file uses precisely that reasoning to discount the **negative** Razer Insider threads
as complaint-selected - and then settles the final tie on **59 positive Reddit owner reports each**.
Same selection bias, opposite sign, and unremarked. The tie does not move; the confidence in it
should.

**5. Five sponsors, and for once not one of them sells a headset.** Thermaltake (the mic roundup),
**be quiet!** (the buying guide - the PSU vendor of this build), Freepik, Storyblocks and Fit Nexa.
**Four of the five are disclosed in the video itself**, Hardware Canucks discloses both in the
description, and This is Tech Today goes further than any source in the audit: *"This video was not
sponsored by any of the brands mentioned or their competitors. No brand had prior review, editorial
control, or influence."* Mark Ellis discloses both a brand partner and a loaned unit. **The
disclosure failure here is the document's, not the creators'.** Running total: **18 of 85 videos
read carry a paid sponsor.** Separately, **fourteen of the sixteen carry affiliate links** - only
PC Gamer and The Headphone Show do not - and Hardware Canucks' affiliate list includes the
HyperSpeed, the model the file led with for two days.

**6. One video is four years old behind a 2026 title.** Ali Abdaal's *"The Best Headphones To Buy
in 2026"* was uploaded **2022-03-16** and tests the Sony XM4, the first-generation AirPods Max and
the Microsoft Surface Headphones 2. The mouse file marks a 2019 guide *"stale, discounted"*; this
one was listed undated. Its own author concedes the deeper problem: *"all these review videos are
somewhat artificial because once you have one of these headphones it doesn't really matter which one
you have."*

**7. The Sony mic claim has three sources and a narrower scope than the doc gives it.** The doc:
*"Best microphone on any headphone: Sony WH-1000XM6."* The source: *"the best sounding microphone
**amongst flagships that I've used**"* - consumer ANC flagships, with no boom-mic headset in the
comparison. Two more of the nine agree within that scope. **And all three describe consumer ANC
microphones the way 6 Months Later does - *"my voice sounds like it's underwater a little bit"*,
*"it just sounds like right now I'm wearing headphones"*.** That is a positive argument for the boom
mic that was bought, made by three independent listening tests, and the file never makes it.

**8. Eight of the sixteen have no bearing on the purchase at all, and one has none on the country.**
The doc says *"eight are consumer/ANC music-headphone guides"* - that count is **correct**, and it
is the first count in this audit that was. Sillycorns goes further: ₹1 000-3 000 headphones from
Zebronics, Boat, Noise, Blaupunkt, Boult, Spigen and Portronics, none of which any Ukrainian shop
stocks. Written down so the next pass does not have to re-read it to find that out.

**Frames:** none, and correctly so. No document attributes an on-screen figure to any of the
sixteen; the mic roundup's evidence is the recorded audio itself, which a frame cannot carry, and
the rest are talking-head guides. The doc says this about its own sources and it is true.


## Earbuds - 9 of 9 read IN FULL, 2026-09-13 (separate task)

Sent in one message, `91be6983:628`. The document is [../earbuds.md](../../earbuds.md), a separate
matter from this build. It **already states** that all nine were read in full on 2026-09-13; that
pass left no verifiable rows, so the reads are redone here in the quotable format. Most of the
document checks out. **One finding is decisional and goes to Dmytro**: the cheapest model on the
list was withdrawn using another product's verdict.

| Video ID | chars read / total | Verbatim quote | Verdict |
|---|---:|---|---|
| `f7lnPrre2Wk` Andro-news.com, 2026-01-13 (Ukrainian) | **31 598 / 31 598** | of the **CMF Buds Pro 2**, winner of the up-to-$60 class: *"Without it [the gold profile], the CMF headphones sounded the most balanced and high-quality"*; *"we decided to give one extra point to the CMF headphones just because they play well out of the box, without any additional settings"*; *"The only thing that let me down a bit was the ANC"* | **the document has this model's verdict inside out.** It records Andro-news as saying the Pro 2 *"loses on sound to every competitor in its class"* and wins on mic and ANC. The source says the **opposite on both axes**. See finding 1. |
| `f7lnPrre2Wk` | 31 598 / 31 598 | of the **CMF Buds** at **$35**, a different model in the up-to-$40 class: *"In terms of sound, it clearly loses to all competitors. The emphasis here is on the lows, and the mids and highs are clearly suppressed"*; *"they are the best in everything except sound … very good noise cancellation, which almost does not put pressure on the ears … The microphone is also the best among all"* | **this is where the document's description actually comes from.** Two products merged into one claim - the fourth time this audit has found that pattern. |
| `f7lnPrre2Wk` | 31 598 / 31 598 | **Realme Buds Air 7 Pro** wins the up-to-$100 class at **$70** against the Anker Liberty 5 and OnePlus Buds 4: *"now they play at the level of top models in the over $100 category. Almost perfect balance … The sound is truly flagship-level, without any price discounts"* | **exact** - the document's pick, and its strongest single piece of evidence |
| `f7lnPrre2Wk` | 31 598 / 31 598 | *"noise cancellation and microphone quality have been improved. Here, it still falls a little short of the leaders' level, but the difference is not significant"*; battery *"about 6 hours with ANC and the LHDC codec"*, the OnePlus *"about an hour longer"*, the Liberty 5 *"up to 9 hours"* | **exact** - all three battery figures, and the document is right to take 6 h as the Realme's working number |
| `f7lnPrre2Wk` | 31 598 / 31 598 | *"they also added support for on-the-fly translation right in the application. Moreover, **it works on any Android smartphone**, while the OnePlus Buds 4 only works with [its own]"* | **unrecorded, and it favours the pick on this phone** - a Xiaomi owner keeps the feature; a OnePlus buyer would not |
| `f7lnPrre2Wk` | 31 598 / 31 598 | Anker **Liberty 5**: *"they traditionally have high-quality noise cancelling and microphones, slightly better than the models listed above"*; *"the best battery life of any headphone in this top"*, wireless charging; sound *"somewhere on the level of CMF Buds Pro 2"* | **exact** - every clause of the document's Liberty 5 row |
| `f7lnPrre2Wk` | 31 598 / 31 598 | over-$100 trio (OnePlus Buds Pro 3, Anker Liberty 4 Pro, Huawei FreeBuds Pro 4): *"I couldn't choose a clear winner from this trio"*; *"a really cool sound that's already on the threshold of my hearing capabilities"*; *"The only thing you can objectively complain about is the price"* - Anker ~$107, OnePlus ~$125, Huawei from ~$160 | **exact.** Note the local prices: 4 799 and 7 399 UAH against $107 (~4 450) and $125 (~5 200). |
| `f7lnPrre2Wk` | 31 598 / 31 598 | *"a whole bunch of different models on my desk again, **which we bought specifically for the creation of this video**"*; tested *"for about a month"* | **the only source of the nine that buys its own units** - no sponsor, no shop-supplied samples |
| `u0eyHbDMzU8` MyChooz UA, 2026-03-15 (Ukrainian) | **20 432 / 20 432** | OnePlus Buds 4, 6th of 15: *"desirable support for the LHDC 5.0 codec and a source on the **Snapdragon** mobile platform. Yes, friends, this affects the sound, because the sound is **noticeably worse on MediaTek**"* | **exact** - the document's decisive demotion, verbatim, and the Xiaomi 14T Pro is MediaTek |
| `u0eyHbDMzU8` | 20 432 / 20 432 | Realme Buds Air 7 Pro, 5th of 15: *"Budget king. You get $300 worth of sound for $55"*; *"the best sound among TWS in the budget and mid-range segment up to $300"*; *"The microphone here is of a decent level"*; *"Autonomy in our tests is up to 10 hours, taking into account the codec"* | **exact, all four** - and the document correctly flags the 10 h against Andro-news' 6 h |
| `u0eyHbDMzU8` | 20 432 / 20 432 | AirPods Pro 3 on sound: *"Still not the level of Realme Buds Air 7 Pro, Huawei … Technics … or Noble Focus RX5, but already close to this golden league"* | **exact** - the document's "rated above the AirPods Pro 3 on sound" is precisely right, and it is a striking claim to have got right |
| `u0eyHbDMzU8` | 20 432 / 20 432 | Nothing Ear (3), 7th: *"The model has a directional microphone in the case for communication in noisy places. **This really works, not for show**"*; *"the downsides are average noise cancellation and transparency … This is the weakest point of the model"* | **exact, both halves** - the document records the case mic and the ANC weakness correctly |
| `u0eyHbDMzU8` | 20 432 / 20 432 | Nothing Ear (3): *"Up to **9.5 hours** of battery life with headphones and up to 38 hours with the case, taking into account the codec"* | **exact - and it is the ANC-off-style figure.** Gadget Ten gives *"about 5 to 5.5 hours with ANC"* for the same model. The document prints 9.5 h without the qualifier, for its own recommendation. See finding 3. |
| `u0eyHbDMzU8` | 20 432 / 20 432 | Creative Aurvana Ace Mimi, 8th: *"The microphone doesn't cope well in noisy environments, **but in quiet ones everything is fine**"* | **half-quoted in the document**, which drops the second clause and withdraws the whole Creative line on the first. See finding 4. |
| `u0eyHbDMzU8` | 20 432 / 20 432 | *"a special thank you to the **soundmach.ua store** for the provided models"*; Amazon and AliExpress affiliate links | **shop-supplied units**, undisclosed in the document |
| `2hVk-4Timf0` hotline.ua, 2026-08-20 (Ukrainian) | **18 636 / 18 636** | Soundcore Liberty 5 Pro: sound **9/10**, ANC **9/10**, microphone **9/10**; *"in the segment up to 10,000 UAH, this is the best that can be found on the market at all"*; *"the noise cancellation is simply unrealistic"* | **exact** - every number and both quotes |
| `2hVk-4Timf0` | 18 636 / 18 636 | *"I've only been wearing them for a week, scuffs are already appearing, the lid has play"*; overall **8.9**, the highest of the five | **exact - and the 8.9 is stronger than the document says.** It records "in its top five"; the model actually takes the **highest overall score in that five**, above the Sony and Bose flagships. |
| `2hVk-4Timf0` | 18 636 / 18 636 | his own ANC numbers: Bose best of all (*"you won't find a better noise suppressor on the market"*), **Sony 9.8**, Soundcore **9**, AirPods Pro 3 **9**, B&O **8** | **this does not contradict Pete Matheson; it agrees with him.** On this reviewer's own scoring the Soundcore's ANC is **joint third of five**. See finding 2. |
| `2hVk-4Timf0` | 18 636 / 18 636 | on the microphone: *"Not once did the interlocutor complain that the sound quality or microphones were not so good. Therefore, we will also put nine out of 10 here"* | **the 9/10 is anecdote, not a test** - no recording, no comparison. The document counts it as a third source ranking the mic top. |
| `2hVk-4Timf0` | 18 636 / 18 636 | Sony WF-1000XM6 microphone: **7/10** - *"Sony has never been strong in its headphones when it comes to microphones"* - against sound 9.5 and ANC 9.8 from the same reviewer | **a second independent source against RTINGS on the Sony's mic**, which the document presents as Pete Matheson standing alone. It strengthens the document's conclusion. |
| `2hVk-4Timf0` | 18 636 / 18 636 | *"I came across the Liberty 5 Pro for testing. By the way, for which I would like to thank the **Portable store**"*; *"You are on the channel of the **hotline.ua** bargain shopping service"* | **shop channel, shop-loaned unit** - the document records both, correctly and unprompted |
| `44zG1beMWfg` Pete Matheson, 2026-05-22 | **18 247 / 18 247** | *"for transparency, this video is **sponsored by Soundcore**, so you might want to take that into consideration"* | **exact** - disclosed by him at 0:34 and recorded by the document |
| `44zG1beMWfg` | 18 247 / 18 247 | on-screen microphone tiers: **NOT GOOD** (Sony), **FAIR** (AirPods 4, Pixel Buds Pro 2, Bose), **GREAT** (Galaxy Buds 4 Pro, AirPods Pro 3), **PERFECT** (both Soundcore) - [`frames/44zG1beMWfg_11m20s.png`](frames/44zG1beMWfg_11m20s.png) | **verified by frame.** The document quoted those four words with no frame saved; they are on-screen labels, not spoken, and every one is correct. |
| `44zG1beMWfg` | 18 247 / 18 247 | on-screen ANC tiers: **BASIC** (AirPods 4), **OKAY** (Pixel Buds Pro 2), **SOLID** (both Soundcore), **VERY GOOD** (Galaxy Buds 4 Pro, Bose, Sony XM6), **WINNER** (AirPods Pro 3) - [`frames/44zG1beMWfg_12m15s.png`](frames/44zG1beMWfg_12m15s.png) | **verified by frame, with one omission** - the document's table has four rows and drops the **OKAY / Pixel Buds Pro 2** tier |
| `44zG1beMWfg` | 18 247 / 18 247 | *"these guys actually hold the **Guinness World Record for call clarity**"*, said of the sponsor's product | **a vendor marketing claim repeated without checking**, by the sponsored reviewer whose test puts that product first |
| `44zG1beMWfg` | 18 247 / 18 247 | *"I'm **not actually going to rank** the earbuds in terms of their audio quality"*; *"if you aren't sure which one to get, then don't focus on the sound quality, focus on all of the other stuff instead"* | **a limit of this source the document does not state** - it is silent on sound by the author's choice |
| `44zG1beMWfg` | 18 247 / 18 247 | *"I find myself looking for third-party foam ear tips … but there is absolutely no need here when you have this type of design"* (the wing); of the Sony *"they're very heavy … there's nothing locking the Sonys into your ears"* | **exact** - the document's fit note, and it supports its own spec row 8 on weight |
| `4F0289jmqQs` Mike O'Brien, 2025-11-22 | **22 045 / 22 045** | Nothing Ear (3) at $179: *"these are almost the best sounding overall … probably better than all the other ones on this table anywhere near this price point"*; *"very, very deep bass and the very strong treble, sometimes even a tad harsh"* | **exact** - the document's central claim for its recommendation, and its +8/+1 dB reading of it is fair |
| `4F0289jmqQs` | 22 045 / 22 045 | *"the talk button on the side, **which I hope continues to improve**, but I love the idea of that"* | **a reservation the document drops.** It says the case mic is *"confirmed real"* on MyChooz's *"this really works"*; the other source likes the idea and wants it improved. Both are in the file now. |
| `4F0289jmqQs` | 22 045 / 22 045 | best for work and calls, non-Apple: *"my choice in this situation would be the **Galaxy Buds 3 Pro** … great microphones on these, very reliable connection … even though they are a year and a half old now, still a fantastic purchase for this category"* | **a reviewer's explicit best-for-calls pick for a non-Apple user, never priced in the document** - which has the *Buds3 FE* withdrawn and no Buds 3 Pro row at all. See finding 5. |
| `4F0289jmqQs` | 22 045 / 22 045 | *"this video is not sponsored. These are all my own opinions"*, with affiliate links disclosed | **clean** - the second of two in this batch |
| `PB9CVX5pjS8` SoundGuys, 2025-12-03 | **12 628 / 12 628** | **Creative Aurvana Ace 3**, its mid-range champion at **$150**: xMEMS plus dynamic hybrid, *"a 10-band custom EQ … plus 15 EQ presets … including a flat EQ"*, *"both aptX Lossless and LDAC support. That's pretty rare at this price point"*, IPX5, ANC *"reduces the loudness by about 75%"* | **the document says these four videos raised nothing under 9 000. This is a measured lab review of a $150 model** - roughly 6 200 UAH - in the exact line the document withdrew. See finding 4. |
| `PB9CVX5pjS8` | 12 628 / 12 628 | Sony WF-C710N: *"the combination of strong passive isolation and ANC reduce noise by an average of **85%**"*; *"Battery life clocks in at **over 9 hours** per charge"* | **the document credits both numbers to Tom's Guide.** They are SoundGuys' measurements. Tom's Guide's "85%" is a different claim entirely - see the next row. |
| `PB9CVX5pjS8` | 12 628 / 12 628 | AirPods Pro 3: *"these earbuds blocked out an average of **90%** of external noise … literally the best noise cancelling performance we've ever measured on any earbuds or over-ear headphones"* | **a measured flagship ceiling** the document never records; useful as the scale the 85% sits against |
| `tUhLcDnXdwg` Tom's Guide, 2026-03-16 | **10 233 / 10 233** | Sony WF-C710N: *"You're getting about **80 to 85% of the XM6 experience**, but for almost a third of the price"* | **this is the source of the document's "85%", and it means something else** - 85% *of the XM6*, not 85% noise reduction. Right number, wrong thing, twice over. |
| `tUhLcDnXdwg` | 10 233 / 10 233 | Sony WF-1000XM6, its best-overall pick: *"the **call quality isn't the best in its class**"* | **a third source against RTINGS on the Sony's microphone**, inside a video the document filed as adding nothing |
| `tUhLcDnXdwg` | 10 233 / 10 233 | *"The JLab Mini is just **$39**"*; *"The JLab Go Pods ANC … for only $36 and often found for under $25 … These actually outperform all other budget earbuds at this price point"* | **two more sub-budget models the document says this video did not raise.** Both are below the 3 000 UAH floor and neither carries a mic claim, so nothing is lost - but the sentence is false. |
| `tUhLcDnXdwg` | 10 233 / 10 233 | Sennheiser Momentum True Wireless 4: *"aptX Adaptive, so you can access **low-latency streaming for videos**"* | **the one model raised that answers the document's own latency row** (row 5: LDAC is the worst offender, and video is the secondary use). $299, out of budget. |
| `PuFmyHBUmcA` Gadget Ten, 2026-08-01 | **12 210 / 12 210** | EarFun Air Pro 4 Plus at $99: *"the transparency mode and microphone quality aren't up to pace with pricey flagships, [but] the ANC functions admirably considering the price"* | **exact** - the document's addition and its caveat |
| `PuFmyHBUmcA` | 12 210 / 12 210 | Nothing Ear 3: *"The battery life is shorter than some competitors, reaching just about **5 to 5.5 hours with ANC** and about 8.5 hours without"* | **contradicts the 9.5 h in the document's table, for the recommended model.** Both figures are real and measure different states. See finding 3. |
| `PuFmyHBUmcA` | 12 210 / 12 210 | **Marshall Motif 2 ANC at ~$200** - Bluetooth 5.3, LE Audio, multipoint, wireless charging, 30 h with ANC; *"ANC works adequately, but it isn't up to par with Bose or Sony's top offerings, and it doesn't work with LDAC or aptX Adaptive"* | **a third model inside the 3 000-9 000 band that the document says this batch did not raise** |
| `PuFmyHBUmcA` | 12 210 / 12 210 | *"check the links in the description below for today's best deals"*, narration throughout of spec-sheet copy with no testing described | **the weakest source of the nine** - an affiliate listicle, the kind [peripherals/headphones.md](peripherals/headphones.md)'s own research-discipline source warns about |
| `ZpP3-fUWQew` Picky Audio, 2026-04-10 | **19 028 / 19 028** | *"A portion of this video is sponsored by [the headphone brand]"*, disclosed at 0:00; *"I've scored and ranked over 100 earbuds … a spreadsheet on which you can change the weight of important categories like **call quality**, noise cancelling, and … sound quality … my free spreadsheet linked down below"* | **a tool built for exactly this purchase**, and the document does not mention it - the same kind of miss as the mouse file's search tool |
| `ZpP3-fUWQew` | 19 028 / 19 028 | Sony WF-XM6, ranked 3rd at 90/100: *"The transparency mode was also noticeably improved over the XM5. **Same with the call quality in wind**"* | **a fourth view on the Sony's mic, and it is positive - from the one reviewer who runs a windy-city test.** The document's "treat the street test as the more relevant one" rests on a street test that this street test contradicts. |
| `ZpP3-fUWQew` | 19 028 / 19 028 | OnePlus Buds Pro 3, ranked 7th: *"the cheapest bud today … one of the best value buds you can get still today"*; *"you don't get LDAC high-res or aptX adaptive. You only get **LHDC**, so not compatible on most phones"* | **the LHDC limitation does not apply to this phone** - the Xiaomi 14T Pro supports it. An unrecorded point in the model's favour. |
| `ZpP3-fUWQew` | 19 028 / 19 028 | spoken call-quality verdicts for all ten: JBL Tour Pro 3 *"call quality in wind is terrible"*; Status Pro X *"not great in windy conditions"*; Bose, Technics, OnePlus Pro 3, Galaxy Buds 4 Pro, Huawei all *"up there with the best"* | **the document says its mic findings are "unread" because they are audio samples.** The samples are; **the verdicts around them are text**, and they were there to be read. |

### What the full reads changed

**1. DECISIONAL - the cheapest model on the list was withdrawn using a different product's verdict.**
[earbuds.md](../../earbuds.md) withdraws the **CMF Buds Pro 2 at 2 499** with: *"the same review is
explicit that it loses on sound to every competitor in its class - bass-forward with suppressed
mids and highs."* Andro-news says that about the **CMF Buds at $35**, a different model in a
different price class. About the **Buds Pro 2**, which won the up-to-$60 class, the same reviewer
says the opposite: *"Without it [the gold profile], the CMF headphones sounded the **most balanced
and high-quality**"*, and he gave it *"one extra point just because they play well out of the box,
without any additional settings"*. Its weak point in that review is **ANC**, not sound - *"the only
thing that let me down a bit was the ANC"* - and its microphones *"are nice and feel good even on
the street"*. **Two products merged into one claim: the fourth instance of that pattern in this
audit, and the first that changed a purchase recommendation.** Written up for Dmytro in
[pc_build.md](../pc_build.md); not decided here.

**2. hotline does not overturn Pete Matheson on ANC - it agrees with him.** The document says
hotline's 9/10 makes Matheson's mid-pack ANC placement *"the outlier"*. But hotline's own scores
across his five models are Bose best, **Sony 9.8**, Soundcore **9**, AirPods Pro 3 **9**, B&O 8 -
the Soundcore is **joint third of five**, which is exactly where Matheson's on-screen **SOLID** tier
puts it, below Bose, Sony and the AirPods. The 9/10 is a high score inside a top-five list, not a
first place. An accurate quote attached to the wrong conclusion.

**And the two sources that rank its microphone top are both commercially tied.** Matheson's video
is **sponsored by Soundcore** and repeats the vendor's *"Guinness World Record for call clarity"*
claim; hotline is a **shop channel** reviewing a **shop-loaned unit**, and its 9/10 for the
microphone rests on *"not once did the interlocutor complain"* - no recording, no comparison. The
document discloses both relationships honestly. What it does not do is notice that they are the
only two sources making the claim.

**3. The battery figure for the recommended model is the optimistic one of two.** The table gives
the Nothing Ear (3) **9.5 h** - MyChooz's *"up to 9.5 hours … taking into account the codec"*.
Gadget Ten gives *"about 5 to 5.5 hours with ANC and about 8.5 hours without"*. The document's own
spec row 7 warns that **"marketing quotes the ANC-off figure, which runs 20-30% higher"** and sets
a 5 h+ target. With ANC on, the recommendation sits **at the bottom of its own target band**, not
at the top. The same document flagged exactly this discrepancy for the Realme and took the lower
number; it did not do so for its own pick. Neither figure is wrong - they measure different states
- but the table prints one of them without the qualifier.

**4. "Nothing added" was not true of those four videos, and one of the misses matters.** The
document: *"The only sub-budget models they raised were the Sony WF-C710N … and EarFun Air Pro 4."*
In fact **SoundGuys' mid-range champion is the Creative Aurvana Ace 3 at $150** - about 6 200 UAH -
with a measured review: xMEMS hybrid drivers, **10-band EQ plus 15 presets including flat**, **both
aptX Lossless and LDAC**, IPX5, ANC measured at **75% reduction**, and its stated weakness is the
**transparency mode**, not the microphone. That bears directly on the document's withdrawal of the
Creative line, which rests on a **half-quote** about a different Creative model: MyChooz says *"the
microphone doesn't cope well in noisy environments, **but in quiet ones everything is fine**"* and
the document keeps only the first clause. Gadget Ten separately raises the **Marshall Motif 2 ANC
at ~$200**, inside the budget. Tom's Guide raises two JLab models below the budget floor. **This is
the third "nothing usable" dismissal this audit has found to be untrue.**

**5. A misattributed measurement, and a third source on the Sony microphone.** The document credits
Tom's Guide with the Sony WF-C710N's *"85% measured noise reduction, 9 h"*. **Tom's Guide says
neither.** It says the C710N gives *"about 80 to 85% of the XM6 experience"* - a completely
different claim. The **85% noise reduction and the 9 h are SoundGuys' lab measurements**, from the
video the document filed as adding nothing. Right numbers, wrong source, and the "85%" in the
document reads as a measurement of one thing when its cited source meant another. Separately,
Tom's Guide says of the XM6 that *"the call quality isn't the best in its class"* - which, with
hotline's 7/10, makes **three** independent sources against RTINGS on that microphone, where the
document had one. Against that, **Picky Audio - the only reviewer who runs a windy-city test -
says Sony improved "the call quality in wind"** over the XM5. The picture is genuinely mixed and
the document presents it as settled in one direction.

**6. A best-for-calls pick was never priced.** Mike O'Brien's non-Apple answer to *"what is best
for work and for calls"* is the **Galaxy Buds 3 Pro**: *"great microphones on these, very reliable
connection … still a fantastic purchase for this category."* The document has the Galaxy Buds3
**FE** withdrawn and no Buds 3 Pro row at all. For a purchase whose stated point is the
microphone, a reviewer's explicit best-for-calls recommendation going unpriced is a gap worth
closing.

**7. Two things in the pick's favour that were never recorded.** Andro-news: the Realme's live
translation *"works on any Android smartphone, while the OnePlus Buds 4 only works with [its
own]"* - a feature a Xiaomi owner keeps and a OnePlus buyer would lose. And Picky Audio's free
**weighted-scoring spreadsheet**, where call quality can be set as the dominant criterion, is the
one tool in the batch built for this exact question.

**Commercial position of the nine:** **Pete Matheson is sponsored by Soundcore** (disclosed);
**hotline.ua is a shop channel** reviewing a **shop-loaned unit** (disclosed); **MyChooz thanks
soundmach.ua "for the provided models"** (disclosed); **Picky Audio** carries a disclosed headphone
sponsor; SoundGuys, Tom's Guide, Gadget Ten, Mike O'Brien and Seven Tech-style listicles carry
affiliate links. **Mike O'Brien states "this video is not sponsored"**, and **Andro-news bought
every unit itself** - *"which we bought specifically for the creation of this video"* - the only
source in the batch that did. Sponsor total for the audit: **19 of 94 read**.

**Frames:** two, both from Pete Matheson, both settling something the transcript could not. The
document quoted his four microphone tiers - *"perfect"*, *"great"*, *"fair"*, *"not good"* - as if
spoken. **They are on-screen labels and appear nowhere in the transcript**, and
[`frames/44zG1beMWfg_11m20s.png`](frames/44zG1beMWfg_11m20s.png) confirms all four exactly.
[`frames/44zG1beMWfg_12m15s.png`](frames/44zG1beMWfg_12m15s.png) does the same for the ANC tiers and
shows the document dropped one of the five.


## Non-YouTube links - 27 of 27 checked, 2026-09-13

Enumerated by [`audit_tools/derive.py`](audit_tools/derive.py), which prints all 27 with the
session:line they arrived on. **Twenty are real sources Dmytro chose to send. Seven are not** - six
are Google shopping-redirect wrappers pasted inside a quoted AI answer, and one is boilerplate from
a skill's own template. Every page below was fetched over verified TLS on **2026-09-13**; **no
redirect was followed**, and where a page could not be read the verdict is *not read*, not a guess.

`verify_audit.py` checks videos only, so nothing here changes 99/99. These rows are held to the
same rule: **no verdict without a quote.**

### The comparison and ranking sites

| Link | sent at | Verbatim quote | Verdict |
|---|---|---|---|
| `technical.city` RTX 5070 vs **RX 9070** | `03d54ca8:1181` — *"how this site then says the opposite?"* | *"Games benchmarked by notebookcheck.net"*; RTX 5070 **68.78** vs RX 9070 **60.87**, *"RTX 5070 has 13% better value for money than RX 9070"*, and *"The GeForce RTX 5070 is our recommended choice as it beats the Radeon RX 9070 in performance tests"* | **exact** — [tools.md](tools.md)'s charge that it *"does no testing - its own page says the FPS come from notebookcheck"* is verbatim correct |
| `technical.city` RTX 5070 vs **RX 9070 XT** | `79b886d7:1130` — *"somehow i see that they are more balanced than you say"* | RTX 5070 **68.78** vs RX 9070 XT **64.58**, *"6.5% performance advantage"*, cost-effectiveness 74.30 vs 63.71, *"17% better value for money"* | **exact** — tools.md's *"ranks the RTX 5070 above the RX 9070 XT, contradicting every real review"* holds |
| `technical.city`, the game list | both pages | the FPS table runs **Atomic Heart, Counter-Strike 2, Cyberpunk 2077, Battlefield 5, Far Cry 5, Fortnite, Forza Horizon 4, Forza Horizon 5, PUBG, Valorant, GTA V, Metro Exodus, The Witcher 3** | **tools.md overstates this one line.** It says *"Games are 2015-2018 titles (Battlefield 5, Far Cry 5, Witcher 3)"*. **Eight of the thirteen are 2015-2019; five are 2020 or later** — Valorant, Cyberpunk 2077, Forza Horizon 5, CS2 and Atomic Heart. The point stands — the suite is majority-legacy and esports-heavy — but not as stated. **Fixed.** |
| Tom's Hardware **GPU hierarchy** | `79b886d7:1149` — *"another useful page"* | page reachable; title *"GPU Benchmarks Hierarchy 2026 - Graphics Card Rankings | Tom's Hardware"*. **Body returned truncated by the fetcher; no ranking row or methodology sentence could be read.** | **NOT READ.** [tools.md](tools.md) describes it as *"one ranked table per part type, updated continuously"* — consistent with the title and nothing more. Recorded as unverified rather than assumed. |
| Tom's Hardware **CPU hierarchy** | `bd8d79b0:431` — *"why so few intel ones, are they worse? or expensive? … here are much more intels"* | page reachable; title *"CPU Benchmarks and Hierarchy 2026: CPU Rankings | Tom's Hardware"*. **Body truncated; no methodology or ranking read.** | **NOT READ** — and Dmytro's question, whether the Intel side was thin because Intel is worse or because it is expensive, has no answer sourced from this page anywhere in the repo |
| `gamingpc.com.ua` RX 9070 XT catalogue | `79b886d7:1170` — *"their build with RX 9070 XT 16GB perform much worse, than 5070 ones / please check why"* | the site's own disclaimer: *"Показники FPS є усередненими і служать для демонстрації"* — the FPS figures are averaged and serve for demonstration. **48 builds listed; every card today reads "0fps".** Cheapest: Core i5 13400 / RX 9070 XT at **99 884** | **the site concedes the point tools.md argues at length, and the doc never quoted it.** Also: the per-card FPS widget is **empty today**, so tools.md's *"a card widget said 22 FPS for Cyberpunk 1440p"* **cannot be re-observed** — recorded as no longer checkable, not as wrong. |
| `gamingpc.com.ua` Vision 5 Pro | `4d4f7b00:1302` — *"what do you think about this pc, price and components"* | **119 073 ₴**, in stock. Ryzen 7 7700 / RTX 5070 12GB / **32GB DDR5-5600** / Gigabyte B650M Gaming Plus WiFi / 1TB Kingston NV3 / DeepCool LE360 V2 / **be quiet! System Power 11 750W** / GameMax Infinity Plus. FPS table, "High": Cyberpunk **190** at 1440p, **218** at 1080p, 122 at 4K; **Valorant 510 / 510 / 340**; **Rust 89 / 89 / 67** | **the CPU-bound signature is visible and the numbers are not native rendering.** 190 FPS at 1440p High on an RTX 5070 is DLSS-with-frame-generation territory, as tools.md says. **But its specific example — *"Valorant 327/327/327 … identical at 1080p, 1440p and 4K"* — does not match this page**: here 1080p and 1440p are identical and 4K differs. **Narrowed in the doc.** |

### The shop listings — prices as at 2026-09-13

| Link | sent at | Verbatim quote | Verdict |
|---|---|---|---|
| `click.ua` **ASGARD AS275QC monitor** | `4d4f7b00:1486` — *"did you do proper research? … there are measurements on the same bloody site, did you bother to open them?"* | *"Монітор ASGARD Gaming 27" AS275QC VA Black Curved 200Hz"*, **8 599 ₴ → 6 999 ₴**, *"В наявності"*. VA, WQHD 2560×1440, **200 Гц**, 1 мс, **300 кд/м2**, **5000:1**, curved; *"Регулювання по висоті: відсутнє"*; 2× HDMI, 2× DisplayPort, 2×2 W speakers, FreeSync + G-Sync. One review, Антон, 2026-07-28: *"Хорошее четкое изображение, плавная картинка без рывков в динамичных играх"* | **price unchanged, still in stock.** Every figure in [monitor.md](components/monitor.md) verified, including *"no height adjustment"* and the thin single review. **The monitor decision is closed and nothing here reopens it.** Three specs on the page are not in the doc: **300 nits, 5000:1, and four inputs** — Dmytro was right that measurements were on the page. |
| `click.ua` **AM5 processor list** | `91be6983:250` — *"Ryzen 7 9700X Tray - is it bad? the tray? dont see BOX on click, can you check yourself?"* | **Ryzen 7 9700X (Tray), 12 892 ₴, "В наявності"** — and of 24 AM5 SKUs listed, BOX exists for the 7700X, 9900X, 7900X, 9800X3D, 7600X, 7400, 7800X3D, 9950X3D and 7600, **but not for the 9700X** | **Dmytro was right, and the doc's price is stale here.** [cpu.md](components/cpu.md) lists the 9700X at *"11 190 / 12 599"* tray/box. click.ua's tray today is **12 892 — above the doc's box price.** Those figures came from other shops; the doc does not say which, and a price without a shop and a date is not a price. |
| `click.ua` **AeroCool P500C-G-WT-v1** | `91be6983:346` — *"i also chose this case. is it ok? please check per our reqs"* | **3 045 ₴** (from 3 199), in stock. ATX/mATX/ITX, 398×285×476 mm, **GPU 450 mm**, **cooler 162 mm**, radiators 120-360 top / 120-360 bottom / 120-280 side / 120 rear, **4× 120 mm ARGB included**, magnetic top and bottom filters, curved tempered glass front and side, 7 slots, no PSU | **no document in this repo ever answered this question.** Specs recorded; **the case decision is closed and this does not reopen it.** |
| `click.ua` **AeroCool D502A-G-WT-v1** | `91be6983:369` — *"this one?"* | **3 056 ₴** (from 3 599), in stock. 477×213×461 mm, **GPU 400 mm** (without front radiator), **cooler 171 mm**, 4× ARGB (3 front + 1 rear), front panel *"2 USB 3.x, **1 USB Type-C**, 1 audio"*, magnetic filters top and side, 0.5 mm steel, PSU to 220 mm | **the front USB-C claim is verified.** [pc_build.md](../pc_build.md) item 7 and this file both assert *"the AeroCool D502A has front USB-C"* — the listing says so. Also unanswered at the time it was asked. |
| `click.ua` **ASGARD Hel prebuilt** | `4d4f7b00:1351` — *"what about this one"* | *"Персональний комп`ютер ASGARD Hel (A84F.32.S10.97XT.16.5979)"*, **96 099 ₴** (from 106 979), in stock. **Ryzen 5 8400F** (6c, 4.2-4.7 GHz) / B650 / **32GB DDR5-5600** / **RX 9070 XT 16GB** / 1TB NVMe / 650W / 1stPlayer T3 case / air cooling / Wi-Fi 6 / **36-month warranty** | **no document in this repo answered this question either.** Recorded as a fact, **not proposed**: it is a different purchase shape with a far weaker CPU. See finding 4. |
| `rozetka` **AULA F75 Pink Black** | `75672d3c:601` — *"see a lot of bad reviews on this aula, if thats the right one"* | *"Клавіатура дротова AULA F75 Pink Switch USB Black (6978080504890)"*, **Є в наявності**, **3.5/5, 63** reviews, **1 999 ₴ → 1 699 ₴**, and **1 614 ₴** *"Ціна при оплаті Карткою Rozetka"*. Warranty *"12 місяців. Обмін/повернення товару впродовж 14 днів"* | **the 3.5/63 figure is exact — and one paragraph of [keyboard.md](peripherals/keyboard.md) is now wrong.** It says *"Rozetka is not a source for the Aula. Its F75 listings are marketplace sellers at 2 100-3 800"* and that the black SKU was out of stock there. **Today Rozetka sells it first-party at 1 699, in stock — the same as the four component shops, and 1 614 with their own card, which would be the cheapest price anywhere.** **Fixed.** |
| `rozetka` AULA F75, the listing copy | same | Rozetka's own product text: *"**Бездротова** механічна клавіатура з підключенням **Wired**"* — "wireless mechanical keyboard with Wired connection" | **the cause of the 1-star reviews, on the page itself.** [keyboard.md](peripherals/keyboard.md) diagnosed the 13 one-star reviews as buyers of the wired F75 expecting a wireless one; here is the contradiction that produces them, in the seller's own copy. **Added.** |
| `rozetka` AULA F75, the specs | same | *"Монтажна плита з **полікарбонату**"*; *"PORON-шумопоглинальний матеріал, 8-кратно спінену IXPE-підкладку … PET-акустичну мембрану, силіконову нижню прокладку та PORON-нижній демпфер"*; *"стабілізатори та балансувальна штанга точно відрегульовані"* | **three rows the doc marks "not published" for this board are published here** — polycarbonate plate, five-layer damping, factory-tuned stabilisers. Keycap material is still not stated, so *"PBT per shop listings, unconfirmed"* stands. **Added.** |
| `rozetka` **SteelSeries Arctis Nova 5** | `75672d3c:1175` — *"these are nova right?"* | *"Навушники SteelSeries Arctis Nova 5 Wireless Black (5707119053228)"*, **5 895 ₴**, in stock, **265 г**, 5/5 from 1 review; delivery *"Кур'єр Meest International (з ЄС) — Відправимо **18 вересня** — **169₴**"*; *"Гарантія. 12 місяців. Повернення товару впродовж **30 днів**"* | **every figure in [headphones.md](peripherals/headphones.md) verified exactly** — 5 895, EU dispatch ~18 Sep, +169 delivery, 265 g, the single-review card. **One thing unrecorded: a 30-day return window**, double the usual 14, which matters for a headset that has to be worn to be judged. |
| `rozetka` **Стіл Оптима L** | `4d4f7b00:943` — *"nah, very weak options / this one is better than all options you presented"* | *"Геймерський комп'ютерний стіл Оптима чорний (розмір L: 138х82 см)"*, **4 100 ₴ → 2 994 ₴**, in stock, **4.7/5 from 169** reviews, seller **CyberStaff 4.5/5, 129 оцінок**; seller's blurb *"◉ На відділення 〰 400 грн ◉ На адресу додому 〰 435 грн"*; Rozetka's own delivery block: *"Тариф перевізника"*; widths *"124 / 138 / 156"*, custom sizes in 7 days | **[desk.md](peripherals/desk.md) is exactly right, including the part it was careful about.** Its distinction between the seller's own delivery blurb and Rozetka's "carrier's rate" is verified word for word. Only drift: the seller's rating count reads **129** today against the doc's 132. |

### The RAM guide Dmytro pasted, and its own citations

The guide at `a43557ac:489` was sent as a link **and pasted in full as text** at `a43557ac:1215`,
so it is quotable from the transcript itself. **The four links inside it are the guide's citations,
not links Dmytro chose** — they are listed among the 27 because they were pasted with it.

| Link | Verbatim quote | Verdict |
|---|---|---|
| r/buildapc *"A layman's guide to RAM terminology"* | *"I thought I would **stick to DDR4 for now** because that's the most affordable option and what I see the most questions on around here"*; *"First word latency = [CAS Latency]/[0.5*Speed]"*; *"every RAM manufacturer makes both single and dual [rank]"* | **exact** — [tools.md](tools.md)'s *"Useful for mechanism, DDR4-scoped"* is right, and the formula and the rank point are both in the text |
| the same guide, on what it does **not** cover | *"I may be convinced to add a section about the pitfalls of **DDR5 RAM wrt XMP problems with four slot boards**, but I thought I would stick to DDR4 for now"* | **it names this build's exact configuration as the thing it declines to cover** — DDR5 on a four-slot board. Nothing in the repo records that the guide flagged it. **Added to tools.md.** |
| `benzhaomin.github.io/bdiefinder` | *"Find Samsung B-Die **DDR 4** memory kits on Amazon, Newegg and many more"*; database *"updated early July 2026"*; *"manufacturers can change ICs … Purchase at your own risk"* | **DDR4 only** — no bearing on a DDR5 build |
| `gamersnexus.net` memory timings | published **2 July 2018**; tRCD is *"The minimum number of clock cycles required between opening a row of memory and accessing columns within it"* | **DDR4-era, accurate, and the definitions are still correct** — the mechanism does not change with the generation |
| `tomshardware.com` Micron discontinues Ballistix | page reachable; **body returned truncated, nothing quotable read** | **NOT READ.** Nothing in this repo cites it. |
| `github.com/integralfx/MemTestHelper` DDR4 OC Guide | titled *"DDR4 OC Guide"*, covering DDR4 on Intel and AMD platforms | **DDR4 only** |

### The seven that are not sources Dmytro chose

| Link | sent at | What it actually is | Verdict |
|---|---|---|---|
| `google.de/goto?url=…` **×6** | `75672d3c:1109` | the footnote citations of an **AI answer Dmytro pasted**, whose text reads *"the Razer BlackShark V2 HyperSpeed is generally considered excellent and highly comfortable for glasses wearers … Weighing in at only 280 grams"* | **unresolvable, and deliberately not followed.** They are Google redirect wrappers with opaque payloads; the rule for this audit is no redirect-following. **The claim they were cited for was later settled the other way and then withdrawn entirely** — [headphones.md](peripherals/headphones.md) records that RTINGS warned about glasses, that a second source claimed to confirm it *"does not"*, and that the glasses objection was dropped on 2026-09-12. **A pasted answer whose every citation is unopenable is exactly the kind of evidence this audit exists to catch.** |
| `warp.dev/factories/request-access` | `836b850a:1070` | the default `cta_url` inside the **skill-doctor skill's own JSON template**, loaded into the session as SKILL.md text — it appears in `.claude/skills/skill-doctor/scripts/render_report.py` as a hard-coded fallback | **not a link Dmytro sent.** Confirmed against the skill file on disk. |

### One link belongs to a different matter

| Link | sent at | Verbatim quote | Verdict |
|---|---|---|---|
| `uristy.ua/ua` | `7b40f5b8:693` — *"check both legal docx and forums like … and other forums like that"* | *"Юристи.UA – це швидка юридична допомога та підбір юристів онлайн або по телефону. Консультація надається безкоштовно і платно"*; **147 296** consultations, **32 611** lawyers, *"15 хвилин середня швидкість відповіді юриста"* | **a lawyer-matching and consultation marketplace, not a source of law.** Its answers are individual practitioners' free-text replies, not case law or statute — useful for how a question is usually handled in practice, and **not** citable as authority. **Belongs to the legal matter, not to this build**, and is recorded here only because it is one of the 27. |

### What the checks changed

**1. The criticism of the two aggregator sites is sound, and one sentence of it was too broad.**
technical.city really does publish no testing of its own — *"Games benchmarked by notebookcheck.net"*
— really does rank the RTX 5070 above both the RX 9070 and the 9070 XT, and really does compute a
value score. What [tools.md](tools.md) got slightly wrong is the vintage: it says the suite is
*"2015-2018 titles"* and names three, but **five of the thirteen are 2020 or later**. Corrected.
Likewise its gamingpc.com.ua example — *"Valorant 327/327/327 … identical at 1080p, 1440p and 4K"*
— does not describe the page checked today, where **1080p and 1440p are identical and 4K differs**.
The CPU-bound signature is real; the illustration was imprecise.

**2. And gamingpc.com.ua concedes the point itself.** *"Показники FPS є усередненими і служать для
демонстрації"* — averaged, for demonstration. The strongest line available against those numbers
was on the site all along and nobody quoted it. Its per-build FPS widget now reads **0fps**, so the
contradiction the doc recorded can no longer be reproduced; that is written down rather than
quietly dropped.

**3. Two shop facts in the docs have moved, and both move in Dmytro's favour.** **Rozetka now sells
the AULA F75 Black first-party at 1 699 — 1 614 with a Rozetka card — in stock**, against
[keyboard.md](peripherals/keyboard.md)'s *"Rozetka is not a source for the Aula … marketplace
sellers at 2 100-3 800"* and its note that the black SKU was out of stock there. And the **Ryzen 7
9700X is tray-only at click.ua at 12 892**, which is **above the 12 599 box price**
[cpu.md](components/cpu.md) quotes from an unnamed shop. A price with no shop and no date attached
is the same failure as the hotline floors in [price_check.md](price_check.md).

**4. Two direct questions from Dmytro were never answered in any document.** *"What do you think
about this pc, price and components"* (gamingpc Vision 5 Pro, **119 073**) and *"what about this
one"* (ASGARD Hel, **96 099**). Both are priced and itemised above. **Neither is proposed here** —
they are prebuilts with fixed CPUs, and the Hel's **Ryzen 5 8400F** is far below anything in
[cpu.md](components/cpu.md)'s table. What they *do* supply is evidence the repo was missing:
[ram.md](components/ram.md) argues 32GB from the prebuilt market and cites **only US builders**;
**both Ukrainian machines Dmytro sent ship 32GB DDR5-5600**, one beside an RX 9070 XT and one
beside an RTX 5070. That is the local corroboration the argument lacked.

**5. Three pages could not be read, and are recorded as unread.** Both Tom's Hardware hierarchy
pages and the Micron/Ballistix article returned truncated bodies through the fetcher; Reddit and
Rozetka refuse automated fetches outright, so the AULA, Nova 5 and desk listings were read in a
browser instead and the Reddit guide was quoted from the full text Dmytro had pasted. **No page was
summarised from a search result or a title.**

**6. The keyboard listing explains its own bad reviews.** Rozetka's copy for the wired F75 opens
*"Бездротова механічна клавіатура з підключенням Wired"* — wireless, connection wired. The doc
worked out from the reviews that the 1-star ratings were buyers expecting wireless; the sentence
that misleads them is in the listing.

**7. Everything in [desk.md](peripherals/desk.md) checks out, including the part it hedged.** The
2 994 price, the 169 reviews, the 124/138/156 widths, the custom-size offer, and — most usefully —
its refusal to treat the seller's *"400 / 435"* delivery blurb as equivalent to Rozetka's own
quote, because Rozetka's block still says only *"Тариф перевізника"*. It is the most careful
sourcing in the repo and it survived re-checking word for word.

### What the partial reads had missed — added 2026-09-13 after re-reading the four in full

Three findings, none of which overturns anything already written, and one qualification that is
owed to a decision put to Dmytro.

**1. The Soundcore Liberty 4 Pro has a second, independent source — and it beats the Liberty 5.**
Mike O'Brien's **$150 mid-range category**, in the part of his video that had only been grepped:

> *"my choice here are the **Soundcore Liberty 4 Pros**. These are **$129** and they do a lot
> right. These have solid ANC. These have great sound quality"*
> *"although technically the Soundcore Liberty 5s in some ways are better, better dust resistance,
> better battery life … the Liberty 5s … feel like they're just boring to me and they're not quite
> as good as these. So **sound and ANC better on the Liberty 4 Pros in my opinion**"*

[earbuds.md](../earbuds.md) carries the Liberty 4 Pro at **4 799** with one line — *"joint winner
of Andro-news' over-$100 bracket"*. It now has a **second source that prefers it to the Liberty 5
on sound and on ANC**, and a useful feature nobody recorded: a **touch slider and display on the
case**, which controls the buds from devices that cannot run the app. He also names the field he
was choosing from — *"the Soundcore Liberty 4 Pro, the Liberty 5, the EarFuns, Galaxy Buds 3 FE if
they're on sale, OnePlus Buds 4"* — which is very nearly this file's own shortlist.

**2. A "reference microphone" in the budget band, never priced.** MyChooz's **fourth place**, also
inside the grepped region:

> **Huawei FreeBuds Pro 4**, $200: *"They have **the best microphone in their class**. This is the
> same as the Apple AirPods Pro 3, one level"*; *"the main reason to buy, friends, is the balance
> of sound, features, and design. **Plus a reference microphone**."*

For a purchase whose stated point is the microphone, that is the strongest mic claim made about any
model anywhere near the budget — ~8 300 UAH at $200 — and **it has no row and no price in
[earbuds.md](../earbuds.md)**, which lists it only as one of Andro-news' three joint winners and
says "not priced". Against it, and the reason it is recorded rather than recommended: *"some of the
functions only work on branded devices with Harmony OS … the L2HC codec, as well as spatial sound,
translator, voice assistant"*, and battery is *"up to 6.5 hours"*. **That is now the second
unpriced best-for-calls candidate**, with the Galaxy Buds 3 Pro.

**3. The hotline ANC finding is directly quotable, not inferred.** The single line missed in that
transcript is the one that states the conclusion outright:

> *"Third place is shared between two models. These are the **Sound Core Liberty Pro 5 and the
> third-generation AirPods Pro** … First place Soundcore. This is **8.9**."*

So the Liberty 5 Pro's ANC is **joint third of five in that reviewer's own ranking** — which is
what this audit concluded from his individual scores, now said by him in as many words — while its
**overall** score of 8.9 is first. Both halves of the finding confirmed.

**4. A qualification owed to the CMF decision.** The re-read confirms the misattribution exactly:
the *"loses on sound"* verdict belongs to the **$35 CMF Buds** and the **Buds Pro 2** is the one
that *"sounded the most balanced and high-quality"*. **But the full passage carries a caveat that
the decision item should have had**, and it is fair to the alternative:

> *"After using the gold profile settings, Realme and OnePlus, which have identical hardware,
> started to play almost the same and **no worse than CMF**. In the end, we decided to give **one
> extra point** to the CMF headphones just because they play well **out of the box**, without any
> additional settings."*

So the CMF's sound win over the Realme is **worth one point and it is an out-of-the-box win**:
after a gold-profile setup, which the reviewer says *"literally everyone can follow"*, the Realme
matches it. That narrows the gap the retraction opens without closing it — the withdrawal was still
made on the wrong product's verdict. **Added to the decision in [pc_build.md](../pc_build.md).**

**5. And one source's own limit, from the head+tail gap.** Ali Abdaal, on the video already flagged
as four years stale behind a 2026 title: *"I'm not an audiophile, no one in our team is really an
audiophile, and so **we don't objectively know what these headphones sound like**. All we can say
is what our subjective experience [is]."* It strengthens the case for discounting that video rather
than changing it.
