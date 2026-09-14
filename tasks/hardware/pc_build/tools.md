# Tools: benchmarks, comparisons, prices

## Ukrainian prices

| Site | What it is good for |
|---|---|
| [hotline.ua](https://hotline.ua/ua/computer/) | **The main tool.** Every SKU with the full list of shops and the price spread. Used for every number in this task. Has price history per product - use it to see whether a part is drifting up. |
| [ek.ua](https://ek.ua/ua/) | Second aggregator (ex e-katalog). Better spec filters than hotline for some categories; cross-check prices. |
| [rozetka.com.ua](https://rozetka.com.ua) | Largest retailer. Rarely cheapest, easiest returns/warranty. |
| [telemart.ua](https://telemart.ua/ua/) | Component specialist, has a PC configurator with compatibility checks and assembly service. |
| [brain.com.ua](https://brain.com.ua/ukr/) | Component specialist, usually well stocked, competitive on GPUs. |
| [citycom.ua](https://citycom.ua), [fparts.com.ua](https://fparts.com.ua), [itbox.ua](https://itbox.ua) | The other three worth checking; often the cheapest hotline offer sits in one of them. |

Practice: shortlist on hotline, then buy the SKU from a shop with a physical presence and a
service department. On a 40k GPU the 5% you save at an unknown shop is not worth the RMA risk.

**Never quote hotline's floor as the price** (settled 2026-09-11). It is whichever of ~40
sellers is momentarily cheapest, usually a shop with no service department, and on this task it
was wrong in both directions - 4 598 too low on the Windows licence, 3 005 too high on the RAM.
**Dmytro buys at click.ua (2026-09-13); quote its price as the price and use the rest as a
fairness cross-check.**
Use [`code/ua_prices.py`](../../../code/ua_prices.py) instead: it reads click.ua, Telemart, Brain, ITbox
and Foxtrot direct on their own domains and uses hotline only as a directory of who stocks what.
Rozetka and Comfy refuse scripted requests and are read by hand in a browser; **КТС and MOYO
stock no PC components** (prebuilts and appliances only) and Citycom exposes no reachable search
URL. The result for this build is [price_check.md](price_check.md).

**A price without a stock check is not a price either.** On 2026-09-11 three of the cheapest
listings - a 32GB kit, the Lancool 216 and the 7500F MPK - were all out of stock at the shop
advertising them. **ITbox and Brain are one catalogue** (identical prices on all 19 parts), so
they count as one source; use ITbox's `InStock`, which matches Brain's product pages, because
Brain's own API reports `IsPresent: false` for everything. **Telemart states stock nowhere in
search, but every product page carries a schema.org `availability`** - and a search card priced
0 is always `OutOfStock`. `ua_prices.py` reads that page automatically, so no Telemart price
needs a phone call to confirm.

Two rules that script enforces, after an antivirus alert here: **verify TLS certificates** (the
intercepting proxy tempts you into disabling it - don't), and **never follow hotline's outbound
`go/price/` links**, which walk an affiliate tracker into a long tail of unknown resellers.

## Reviews and benchmark data that can be trusted

| Source | Use |
|---|---|
| [TechPowerUp](https://www.techpowerup.com/review/) | The most complete per-card reviews: 25-game suites at 1080p/1440p/4K, plus measured power, noise in dB, temperatures, and a **relative performance** chart per resolution. Their [GPU database](https://www.techpowerup.com/gpu-specs/) is the reference for specs. |
| [Tom's Hardware GPU hierarchy](https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html) and [CPU hierarchy](https://www.tomshardware.com/reviews/cpu-hierarchy,4312.html) | One ranked table per part type, updated continuously. Best single answer to "is X faster than Y". |
| [TechSpot](https://www.techspot.com/) / Hardware Unboxed (YouTube) | The best large-sample game testing, and the most honest about value per currency. Their "GPU pricing update" and "50 game benchmark" pieces are the ones to read. |
| Gamers Nexus (YouTube + [gamersnexus.net](https://gamersnexus.net)) | Methodology-obsessed: thermals, acoustics normalised to noise level, case airflow, PSU teardowns. The place to check a *case* or *cooler* before buying. |
| Digital Foundry | Image quality: DLSS4 vs FSR4, frame generation, whether an upscaler is usable. |
| [Cybenetics database](https://www.cybenetics.com/index.php?option=power-supplies) | Independently measured PSU efficiency **and noise**. Check any PSU here before buying; the 80+ sticker says little. |
| **Benchmark videos with no commentary** | Channels like Testing Games, Benchmarks for Gamers and Jegs TV publish FPS only as on-screen overlays and a closing average chart. `code/yt_transcript.py` returns nothing for these - the data is in the pixels. Use **`code/yt_frames.py`** to pull stills at the chapter timestamps (the "Average result" chapter first), then read the images. Verify which card a percentage chart favours from a raw overlay frame before trusting its direction. |
| [SPL PSU tier list](https://psutierlist.org/) ([mirror](https://tuerie.github.io/psu-tier-list/)) | Teardown-based letter grade for nearly every PSU on the market, with the **OEM named** and a one-line note on what is wrong with it. A/A+ best, C the floor for a gaming build. Pairs with Cybenetics: Cybenetics measures the unit, this grades the platform. The fastest way to vet a shop's proposed substitute. |
| **Motherboard VRM analysis** | There is **no usable tier list for AM5** (checked 2026-09-13). Tech Guided names a Reddit motherboard VRM spreadsheet, but says in the same breath that it *"hasn't been updated for over a year now, so it only lists am4 chipset motherboards and 12th generation Intel chipsets"* - **nothing on B850**. Use the reviewers instead: **Buildzoid** (Actually Hardcore Overclocking), **Gamers Nexus** and **Hardware Unboxed**, named independently by Tech Guided and Paul's Hardware. This is the one component where a tier list does *not* substitute for a review. |
| [RTINGS](https://www.rtings.com/monitor) | Monitor measurements: response time, overshoot, HDR brightness, text clarity. Filter by 1440p/240Hz and read the "Text Clarity" section before choosing OLED. |
| Monitors Unboxed (YouTube) / [TFTCentral](https://tftcentral.co.uk/) | Panel-level monitor analysis. |
| [Blender Open Data](https://opendata.blender.org/) | Real render benchmark spread per CPU/GPU - the honest answer for productivity claims. |
| [3DMark / Time Spy result search](https://www.3dmark.com/search) | Compare your finished build against thousands of identical ones; use it to confirm the machine performs as expected after assembly. |
| [Cinebench 2024](https://www.maxon.net/en/cinebench) / [Geekbench browser](https://browser.geekbench.com/) | CPU verification after assembly. |
| [PassMark CPU](https://www.cpubenchmark.net/) / [GPU](https://www.videocardbenchmark.net/) | Very rough, huge sample. Fine as a sanity check, not for buying decisions. |

## Quick comparison / estimation tools

| Tool | Note |
|---|---|
| [nanoreview.net](https://nanoreview.net/en/gpu-compare) | Fast side-by-side of two CPUs or GPUs with aggregated game FPS at each resolution. Good first pass. |
| [cpu-monkey.com](https://www.cpu-monkey.com/) | Same idea for CPUs, with a large spec/benchmark database. |
| [PCPartPicker](https://pcpartpicker.com/list/) | **Compatibility checking**: socket, RAM support, cooler height, GPU length, PSU wattage, case clearance. It has no Ukrainian shops, so use it for the compatibility warnings and ignore its prices. |
| [be quiet! PSU calculator](https://www.bequiet.com/en/psucalculator) / [OuterVision](https://outervision.com/power-supply-calculator) | PSU sizing sanity check. |
| [GPU length / clearance in TechPowerUp reviews](https://www.techpowerup.com/review/) | Physical fit numbers per card model. |

## Things to distrust

- **UserBenchmark** - openly biased scoring and a weighting formula that has been repeatedly
  called out; ignore it entirely.
- **"Bottleneck calculators"** and the flood of 2026 SEO "FPS calculators"
  (thepcbottleneckcalculator, mypcbottleneck, techbenchpro, teamzlab and similar). They
  interpolate from scraped numbers and invent precision they do not have. If you want an FPS
  estimate, read TechPowerUp's chart for the actual game.
- Any single YouTube "benchmark" channel with no methodology page - a lot of them replay
  canned footage.
- **technical.city** and the spec-aggregator class generally (also nanoreview, gpucheck,
  pcbench.net, howmanyfps). Worked example, added 2026-09-11 after it appeared to contradict
  this project's GPU conclusion: it ranks the **RTX 5070 12.9% above the RX 9070**, where every
  controlled test puts the 9070 ahead in modern raster. **Its own six synthetic scores
  contradict each other** - 3DMark 11 gives the 9070 **+23.7%**, Cloud Gate gives the 5070
  **+24.2%**, Ice Storm the 5070 +16.7%, Fire Strike the 9070 +4.5%. A 48-point spread between
  tests of the same two cards is noise being averaged into a number. Worse, **Cloud Gate,
  Ice Storm and Vantage are DX9/DX10 tests from 2008-2013** - they say nothing about RDNA4 or
  Blackwell. And its "1440p gaming" sample is **six games: CS2, CS:GO, Valorant, GTA V,
  Metro Exodus and Battlefield 5** - three esports titles that run CPU-bound at hundreds of FPS
  (where NVIDIA's lower driver overhead genuinely wins), and **nothing newer than 2023**. It is
  not measuring modern AAA at 1440p, which is what this build is for. Reviewers also note a
  general skew toward NVIDIA in its GPU rankings.

## How to verify a claim about a build (the method, 2026-09-09)

**"Build FPS" is not a thing you can look up.** No site measures whole builds - they measure
GPUs and CPUs separately, and every "build FPS" number is a model on top of that. This is why
retailer configurators disagree wildly with each other.

The method that works:

1. **Decompose the build.** At 1440p your frame rate is the GPU's, unless the CPU is too weak
   to keep up. So do two lookups - GPU performance, then a check that the CPU is not a
   bottleneck - never one composite number.
2. **GPU: use per-game charts from outlets that publish their test rig.** The filter is
   simple: does the page state the **CPU, the settings and the driver version**? If not, close
   it. TechPowerUp GPU reviews, TechSpot/Hardware Unboxed head-to-heads, Gamers Nexus,
   ComputerBase.
3. **CPU: Tom's CPU hierarchy, read at 1440p.** 1080p charts exaggerate CPU differences, 4K
   hides them. At 1440p anything from a Ryzen 7 7700 upward will not meaningfully limit an
   RX 9070 XT-class card.
4. **Two-source rule.** Never act on one chart. If two of three outlets agree, that is the
   number. (This task's own 17% GPU figure was single-sourced until Tom's and TechSpot
   confirmed it.)
5. **For one specific game**, search YouTube for the exact card plus game plus resolution and
   watch a video with a frametime overlay and visible settings. Real gameplay you can judge
   with your own eyes.
6. **After the build exists - the only number that is truly yours.** Run 3DMark Time Spy and
   Cinebench, then search the [3DMark result database](https://www.3dmark.com/search) for the
   same CPU+GPU pair. Matching scores mean the machine is assembled correctly; 15% low means
   something is wrong - a mis-seated cooler, RAM running at 4800 instead of 6000, or a
   throttling case.

### Reject any source that

- gives FPS without stating the CPU, settings and driver
- shows the **same FPS at 1080p and 4K** (that is a CPU cap in a model, not a measurement)
- calls itself an "FPS calculator" or "bottleneck calculator"
- computes value or "cost-effectiveness" from **MSRP** rather than local retail price

### Sites checked in this task and rejected

| Site | What it looked like | What it actually was |
|---|---|---|
| **technical.city** | A clean spec-and-FPS comparison page | Does no testing - **its own page says so: *"Games benchmarked by notebookcheck.net"***. The suite is **13 titles, eight of them 2015-2019** (GTA V, Witcher 3, PUBG, Fortnite, Far Cry 5, Forza Horizon 4, Battlefield 5, Metro Exodus) and five from 2020 on (Valorant, Cyberpunk 2077, Forza Horizon 5, CS2, Atomic Heart) - majority-legacy and esports-heavy, CPU-limited at 1440p on modern cards. *(Corrected 2026-09-13: this said "Games are 2015-2018 titles", naming three; the full list was never read.)* Ranks the RTX 5070 **above** the RX 9070 XT - **68.78 vs 64.58, "6.5% performance advantage"** - and above the plain RX 9070 by 13%, contradicting every real review. Its "cost-effectiveness" score (74.30 vs 63.71) is computed from MSRP. |
| **gamingpc.com.ua** FPS widget | Per-build FPS for real purchasable configs | **The site says it itself: *"Показники FPS є усередненими і служать для демонстрації"*** - averaged, for demonstration *(quoted 2026-09-13; this was never recorded)*. Values track the **CPU**, not the GPU model. On the Vision 5 Pro page checked 2026-09-13: **Valorant 510 / 510 / 340** and **Rust 89 / 89 / 67** - identical at 1080p and 1440p, different at 4K. *(Corrected: this row said "Valorant 327/327/327 … identical at 1080p, 1440p and 4K"; the 4K column does differ. The CPU-bound signature is real, the illustration was not.)* Cyberpunk reads **190 FPS at 1440p "High" on an RTX 5070**, which is DLSS-with-frame-generation territory, not native. The per-card FPS widget now reads **0fps** across the catalogue, so the earlier "22 FPS vs 190 on the same page" contradiction **can no longer be reproduced** - recorded, not withdrawn. |
| A second Ukrainian configurator | Same idea, opposite bias | Showed the RX 9070 XT ahead of the RTX 5070 by **+61% in Cyberpunk, +96% in CS2, +66% Fortnite** - against a real raster gap of 7-17%. Also priced both GPUs ~10 000 above the cheapest Ukrainian offer and defaulted to the worst-reviewed 9070 XT model, DDR5-5600 RAM and a PCIe 3.0 SSD. |

**Use retailer configurators for prices and for what a shop will actually assemble. Never for
performance.**

## How to compare the builds in this task

1. Pick the game/workload you actually care about.
2. Look up the GPU in the TechPowerUp relative-performance chart **at 1440p** (not 1080p -
   CPU differences vanish at 1440p, GPU differences grow).
3. Look up the CPU in the Tom's Hardware gaming hierarchy, then check its multicore score in
   Cinebench/Blender if the work load matters.
4. Price both in hotline.ua on the day, then compare total build cost, not part cost.
5. After assembly, run 3DMark Time Spy and Cinebench and compare against the result search
   for the same parts - that catches a mis-seated cooler, a thermally throttling case or RAM
   running at 4800 instead of 6000.

## Reading a YouTube review without watching it (added 2026-09-10)

Hardware Unboxed, Gamers Nexus and Monitors Unboxed publish their conclusions in video
only, so the reasoning above is otherwise unreachable in text. `code/yt_transcript.py`
pulls the caption track plus the title, channel, date, chapter list and description:

```bash
PYTHONUTF8=1 venv/Scripts/python.exe code/yt_transcript.py <url> -o notes.md
```

No API key and no account - it reads the same auto-caption track the player uses. A 22-minute
review comes out at ~20 KB of clean text with a `[mm:ss]` marker every 30 s, so a claim can be
cited back to its timestamp. `--stamp 0` drops the markers, `--no-body` keeps only the
metadata and chapters, `--lang uk` tries a Ukrainian track.

**The chapter list is the most useful part of a benchmark video.** It names every game tested
and the timestamp of the averages and the cost-per-frame section, which is where the verdict
lives.

**What the transcript cannot give you: the numbers on screen.** The FPS tables are graphics;
the narration carries the percentages the reviewer chooses to say out loud and the conclusion,
not the full table. So use a transcript for the reasoning and the verdict, and take figures
from the written outlets in the table above. The two-source rule still applies.

Videos read this way, with what they were worth, are recorded beside this file:
[scattervolt_2026.md](scattervolt_2026.md).


### Videos read so far

| Video | Worth |
|---|---|
| ScatterVolt, "Best CPU GPU Combo for Every Budget" (2026-08) | Full record in [scattervolt_2026.md](scattervolt_2026.md). Opinion tier; useful on price direction and on what a builder pairs. |
| Linus Tech Tips, "Stop WASTING Money on Fancy RAM" (2026-02) | **Genuinely useful, and read carefully** (corrected 2026-09-13). Four CPUs x eight DDR5 speeds. It does **not** settle CL30-vs-CL36 in favour of CL36: *"anything with a tuned expo profile"* is said of the **9950X**, while of the **9800X3D** he says *"6,000 mega transfer CL30 is still the sweet spot"*. His advice for a machine used for work is the low-latency kit. The CL36 pick rests on Hardware Unboxed's 8.5% figure and on Gamers Nexus below - see [components/ram.md](components/ram.md). |
| PC Builder, "Best RAM for Gaming 2026" (2026-04) | **Genuinely useful.** Carries the TechSpot/Hardware Unboxed 16GB stutter data and the DDR5 four-stick rule. Same doc. |
| Gamers Nexus, "i5-10600K Cache Ratio & RAM Overclock" (2020) | **Upgraded 2026-09-13: it is the production counterweight to LTT above.** DDR4 and Intel, so the numbers do not transfer - but it is the only source in this project that benchmarked memory tuning against **production** applications: **3.5% in Blender, 1.6% in 7-zip**, against 10-17% in games. His own conclusion matches this project's: once faster memory costs ~$100 more, *"you're kind of approaching just the better class of CPU."* It is also the video the Reddit RAM guide leans on, and it does **not** support that guide's headline claim. |
| Linus Tech Tips, "Please Stop Buying the Wrong SSD" (2026-04) | **Useful.** DRAM matters most on an OS drive; which drives hide whether they have it. |
| PC Builder, "Best SSD for Gaming 2026" (2026-05) | **Useful.** Heatsink rule, cache affects writes not reads, Gen 5 not worth it, HDDs only for cold bulk. |
| Tech Notice, "Ultimate SSD Guide" (2024-12) | **One useful chart.** Sequential speeds are noise; the full-system-drive test is the one that separates drives. |
| Tech Guided, "How to Choose an SSD" (2024-01) | **Nothing usable.** Beginner-level, pre-crisis pricing. |
| Socket-X, "Every 2026 RAM Brand Explained" (2026-05) | **Useful.** Who makes the silicon, per-brand sourcing behaviour, and the Crucial wind-down. |
| GamingScan, "How To Choose RAM" (2019) | **Nothing usable.** DDR4-era; its four-stick advice is wrong for AM5. |
| r/buildapc "Layman's guide to RAM terminology" (supplied as text) | **Useful for mechanism**, DDR4-scoped. Slot population, secondary timings, the first-word-latency formula (*"First word latency = [CAS Latency]/[0.5*Speed]"*), and why rank is not printed on the box (*"every RAM manufacturer makes both single and dual"*). **It says its own scope outright** — *"I thought I would **stick to DDR4 for now**"* — and names the thing it declines to cover: *"the pitfalls of **DDR5 RAM wrt XMP problems with four slot boards**."* **That is this build's exact configuration**, and it is the one place the guide points at a risk it then does not address. *(Checked 2026-09-13.)* **Its four embedded citations are all DDR4-only too** — B-Die Finder (*"Find Samsung B-Die DDR 4 memory kits"*), the GamersNexus timings guide (2 July 2018), the MemTestHelper *"DDR4 OC Guide"*, and a Tom's Hardware Ballistix news item whose body could not be read. |

**reddit.com is blocked** to both the fetcher and the browser here, so a Reddit thread has to be
pasted in as text to be read.
