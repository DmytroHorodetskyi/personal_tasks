# Build specifications: what each part must be, per build

The purpose of this sheet is one thing: **when a store proposes a substitute, decide in thirty
seconds whether it is acceptable.** One table per component, a column per build, and a last
column saying why the row decides the purchase. Under each table, the grounds for rejection.

The three builds and their totals are in [../pc_build.md](../pc_build.md). The full arguments are
in [components/](components/) - this file carries acceptance criteria only. Prices are mostly
Telemart, 2026-09-10; they are the reference point, not a quote.

**Every row is a measurable quantity with its unit.** Where the industry uses a label -
"DDR5-6000", "CL36", "PCIe 4.0" - the number behind it is given too, because a label cannot be
compared against a substitute and a number can.

---

## CPU

| | **Lean** | **Working** | **Max** | Why it decides the purchase |
|---|---|---|---|---|
| **Part** | Ryzen 5 **7500F** | Ryzen 7 **9700X** | Ryzen 7 **9700X** | - |
| **Price** | 6 589 | 15 099 | 15 099 | - |
| **SKU** | MPK (retail, incl. cooler) | BOX | BOX | Tray carries the shop's warranty, often 12 months, against AMD's 36. The retail premium is 360-1 409 depending on the chip. |
| Socket | AM5 | AM5 | AM5 | Platform life to 2029, Zen 6 lands on it. LGA1851 has no runway. |
| Cores / threads | 6 / 12 | **8 / 16** | **8 / 16** | Eight is the work requirement: IDE, language servers, git on heavy repos. Six is the Lean compromise. |
| Boost clock | 5.0 GHz | **5.5 GHz** | **5.5 GHz** | What the chip runs at when one or two cores are busy, which is most of this workload. Base clock is only the floor under all-core load. |
| TDP | 65W | 65W | 65W | **A cooler decision, not just a CPU one.** 105W+ forces the 2 845 Phantom Spirit instead of the 1 515 AK400, and a louder machine. |
| L3 cache | 32MB | 32MB | 32MB | X3D's 96MB is a gaming purchase at 1440p, not a work one. Flips only if a local Postgres or ClickHouse turns out to be real. |
| iGPU | **none** | 2-CU RDNA 2 | 2-CU RDNA 2 | Without one: no display output and no way to diagnose the machine with the graphics card pulled. The known cost of Lean. |

**Reject:** any tray SKU; any 105W+ part unless the cooler is re-costed; Intel LGA1851; a 9600X.

---

## GPU

| | **Lean** | **Working** | **Max** | Why it decides the purchase |
|---|---|---|---|---|
| **Part** | RX **9070 GRE** Hellhound | RX **9070 GRE** Hellhound | **RX 9070 Sapphire PURE** (was: 9070 XT) | - |
| **Price** | 32 179 | 32 179 | **39 999** (Telemart, in stock) | - |
| Chip | 9070 GRE | 9070 GRE | **9070 XT** | At 1440p the card sets the frame rate. The XT is ~25-30% above the GRE - the whole difference between Working and Max. |
| VRAM | 12GB | 12GB | **16GB** | 12GB is adequate at 1440p today; **16GB is now the reason Max exists at all**, since the XT tier priced itself out. Measured evidence that 12GB is the live limit: a 1440p RT frame shows an RTX 5070 at 11 230 of 12 288 MB. |
| Memory bus | 192-bit | 192-bit | **256-bit** | Bus width x data rate = bandwidth. It is why a cut-down card stays cut down whatever its clocks. |
| **Memory bandwidth** | **~480 GB/s** | **~480 GB/s** | **~640 GB/s** | GDDR6 at 20 Gbps: 192-bit gives ~480 GB/s, 256-bit ~640 GB/s (AMD quotes "up to 640", some sources 644.6). A third more bandwidth is part of why the XT is ~25-30% faster, not just its clocks. |
| Board power | ~220W | ~220W | **247W measured** (220W TBP) | Sets PSU sizing and the connector count. **Use the measured figure, not the TBP** - ComputerBase measured the Sapphire PURE at 247W, the highest of the non-XT group, because it carries a large factory overclock. Max peak is ~400W, 53% of the 750W PSU. |
| Cooler family | Hellhound | Hellhound | **Sapphire PURE - 29.0 dB(A) measured** (ComputerBase) | **The model, not the chip, decides noise and failure rate:** 0.47% RMA across 4 340+ units, 29.0 dB(A) on the silent BIOS, PTM7950, dual ball-bearing fans. |
| Power connector | 2x 8-pin | 2x 8-pin | **2x 8-pin** | Avoids the 12V-2x6 connector and its failure history entirely. **Note for any XT substitute:** the Hellhound XT takes two but the Red Devil XT takes **three** - an earlier version of this row said 2x for every candidate and was wrong. The 750W PSU carries four connectors, so all of them fit. |
| Slots / length | ≤2.5 slots, ~300-330mm | same | same | Physical fit against the case's 392mm limit. Read the length from the card's review in mm, not the shop listing. |
| Dual BIOS | silent BIOS required | same | same | **29.0 dB(A)** on the Hellhound's silent BIOS. The OC BIOS costs **+3.5 dB(A)** for ~4% more power - not a trade worth making. |

**Reject:** reference or blower designs; any model with no measured noise or RMA data - which
includes the **Red Devil** currently standing in for Max, on availability alone; the **RX 9070
non-XT**, 2 806 under the XT for a slower card; a "9070 XT" at a suspiciously low price that
turns out to be out of stock.

---

## Motherboard

| | **Lean** | **Working** | **Max** | Why it decides the purchase |
|---|---|---|---|---|
| **Part** | MSI **B850M GAMING PRO WIFI6E** | ASRock **B850 Pro RS WiFi** | ASRock **B850 Pro RS WiFi** | - |
| **Price** | 7 599 | ~9 400 | ~9 400 | - |
| Socket / chipset | AM5 / B850 | AM5 / B850 | AM5 / B850 | B850 gives PCIe 5.0 to the GPU slot. X870 mainly adds USB4 and costs ~4 700 more for a port that will not be used. |
| Wi-Fi | required | required | required | A stated requirement - it rules out the non-WiFi SKUs of otherwise identical boards. |
| Ethernet | 2.5GbE | 2.5GbE | 2.5GbE | A board was dropped for being stuck on gigabit and nothing else. |
| M.2 slots | 2 minimum | **4** (1x Gen5x4, 2x Gen4x4, 1x Gen3x4) | **4** | The second slot is the storage upgrade path that makes 1TB a deferral rather than a commitment. The ASRock has four, so that path is wide open. |
| M.2 heat cover | on primary slot | present, plus a bottom-side heatsink | present, plus a bottom-side heatsink | It is why the SSD is bought bare - the drive's own heatsink conflicts with it and removing one voids warranties. |
| **BIOS Flashback** | wanted | **present** (button) | **present** (button) | Lets the board's firmware be updated **with no CPU installed**. On a board bought for a CPU newer than its shipping BIOS, this is the difference between a build that posts and one that needs a loaner chip. |
| USB-C | wanted | 1 front + 2 rear | 1 front + 2 rear | A front-panel USB-C header is the one port on this list you would notice missing daily. |
| VRM temp under load | under 80 C | under 80 C | under 80 C | Measured after an hour of sustained load: the one electrical characteristic that separates boards in this price band. |
| DIMM slots populated | 2 of 4, **the A2/B2 pair** | 2 of 4, **the A2/B2 pair** | 2 of 4, **the A2/B2 pair** | AM5 is 2-DIMM-optimised; filling all four forces a lower speed. **Which two matters:** populate the second slot of each channel (usually the 2nd and 4th from the CPU), because open A1/B1 slots cause fewer signal reflections than open A2/B2 ones. Confirm the labelling in the board manual - it is not always silk-screened. |
| Exact SKU | read the suffix | read the suffix | read the suffix | TUF vs PRIME, TOMAHAWK vs TOMAHAWK MAX, WIFI vs non-WIFI are different boards with near-identical names. |

**Reject:** no Wi-Fi; 1GbE only; a single M.2 slot; any board with no VRM measurement - which
currently includes **all four of Telemart's B850 alternatives**. The largest open item in the
build; see [components/motherboard.md](components/motherboard.md).

---

## RAM

| | **Lean** | **Working** | **Max** | Why it decides the purchase |
|---|---|---|---|---|
| **Part** | Kingston FURY **16GB (2x8)** | Crucial Pro **32GB (2x16)** | Crucial Pro **32GB (2x16)** | - |
| **Price** | 15 599 | 24 099 | 24 099 | - |
| Capacity | 16GB | **32GB** | **32GB** | Measured demand on the current machine is ~8-11.5GB, so 16GB works but leaves no headroom for an IDE plus a game. |
| Data rate | **6000 MT/s** | **6000 MT/s** | **6000 MT/s** | Mega-transfers per second - the label "DDR5-6000". The actual clock is **3000 MHz**, doubled because DDR transfers twice per cycle; CPU-Z showing 3000 MHz is correct, not a fault. The AM5 controller runs **1:1 with the memory to ~6000**, then halves the ratio: a 6000 kit beats a 7200 kit here, and 8000 measures flat or worse. |
| CAS latency | **30 cycles** | **36 cycles** | **36 cycles** | Clock cycles the memory takes to respond. Cycles alone are not comparable across data rates - convert to time. |
| **Absolute latency** | **10.0 ns** | **12.0 ns** | **12.0 ns** | **This is the comparable number: ns = CL x 2000 / MT/s.** So 36 at 6000 = 12.0 ns, 30 at 6000 = 10.0 ns, and 32 at 6400 = 10.0 ns - identical to CL30/6000 despite the bigger numbers on the box. **Do not pay for CL30:** measured CL30 vs CL40 (13.3 ns) at 6000 was 8.5% at 1080p on an RTX 4090, and less at 1440p. |
| Secondary timings | 30-36-36-76 | **36-38-38-80** | **36-38-38-80** | The full string is tCAS-tRCD-tRP-tRAS, and **tighter is better**. This is where the Crucial Pro earns its place: **36-38-38-80** against the Corsair Vengeance's **36-44-44-96** at the same CL36 and the same data rate. Two kits with identical headline specs are not the same kit. |
| Profile | EXPO | EXPO or AM5-proven XMP | EXPO or AM5-proven XMP | Without it the kit runs at the JEDEC 4800 default and the purchase is wasted. One BIOS setting. |
| Modules | exactly 2 (2x8GB) | exactly 2 (2x16GB) | exactly 2 (2x16GB) | DDR5 controllers do badly with four - which is also why 16GB cannot be upgraded by adding a pair. Going to 32GB later replaces the kit. |
| Rank | single-rank | single-rank | single-rank | **All of these are single-rank.** Every DDR5 IC is currently 16Gb, so a 16GB DDR5 module can only be single-rank; dual-rank begins at 32GB *modules*. Dual-rank carries roughly a 9% advantage, but reaching it here would mean 2x32GB - i.e. 64GB, at 2.7x the price. **Not a lever in this build.** (An earlier version of this row claimed the 2x16GB kit was dual-rank. It is not - that is DDR4 behaviour.) |
| Voltage | 1.4 V | 1.35 V | 1.35 V | The EXPO profile's voltage, above the 1.1 V JEDEC default. Nothing to act on - just do not expect JEDEC voltage at rated speed. |
| Board QVL | present | present | present | On memory that should boot once and never be thought about again, QVL presence beats a timing number. |
| Module height | any | any | any | Normally a real fit risk with air coolers - **not here**: the AK400 in its single-fan form leaves ~59mm of DIMM clearance (43mm with a second fan), so even tall RGB kits clear it. |

**Reject:** single-module kits (single-channel); 4-stick configurations; anything above 6400 on
AM5; no EXPO/XMP; 64GB at 59 486, which is 2.7x the price of 32GB.

---

## Storage

| | **Lean** | **Working** | **Max** | Why it decides the purchase |
|---|---|---|---|---|
| **Part** | WD **Green SN3000 1TB** | Samsung **990 PRO 1TB** | Samsung **990 PRO 1TB** | - |
| **Price** | 6 999 | 12 399 | 12 399 | - |
| Live alternative | - | 990 EVO Plus 1TB, 10 679 | 990 EVO Plus 1TB, 10 679 | Named best-value on the chart that matters despite having no DRAM. |
| Capacity | 1TB | 1TB | 1TB | 270GB migrates from the current machine, and 1440p titles run 100-150GB each. 512GB starts life over half full; 2TB is money this build cannot spare. |
| Interface | PCIe 4.0 x4, M.2 2280 | PCIe 4.0 x4, M.2 2280 | PCIe 4.0 x4, M.2 2280 | **x4 is the lane count that matters** - a x2 or x1 slot or adapter halves or quarters the ceiling. 2280 = 22mm wide, 80mm long. Gen 5 is ~20% faster on the test that matters but runs much hotter and needs the board's M.2 cooling confirmed first. |
| Cache | HMB accepted | **DRAM preferred** | **DRAM preferred** | This is the only drive, so it is the OS drive - where DRAM matters most, and more as it fills. A proven HMB controller is fine; a cheap DRAM-less drive is not. |
| Heatsink | bare SKU | bare SKU | bare SKU | The board's M.2 cover usually conflicts with the drive's own, and removing the drive's can void the warranty. |
| The metric | random, not sequential | random, not sequential | random, not sequential | Every Gen 4 drive is within a hair on sequential. Random small I/O is what git, node_modules and container layers actually do. |
| Sustained write | check it | check it | check it | **The number that separates a good HMB drive from a bad one:** write speed *after* the SLC cache is exhausted. A cheap DRAM-less drive can fall to low hundreds of MB/s; this is what a big game install or a container pull actually hits. |
| Endurance / warranty | ~600 TBW, 5 yr | ~600 TBW, 5 yr | ~600 TBW, 5 yr | The industry standard - compare on this rather than on speed claims. |
| Free space to keep | 15% | 15% | 15% | Drives slow measurably as they fill. |

**Reject:** QLC; any drive whose DRAM presence cannot be confirmed on TechPowerUp (vendor pages
hide it, and colour tiers mean nothing - WD Black SN7100 and SN770 are DRAM-less, the SN850X is
not); the Kingston NV3 and its variable bill of materials; heatsink SKUs; a 512GB SSD plus an
HDD, which now costs the same as one good 1TB drive.

---

## CPU cooler

| | **Lean** | **Working** | **Max** | Why it decides the purchase |
|---|---|---|---|---|
| **Part** | Deepcool **AK400** | Deepcool **AK400** | Deepcool **AK400** | - |
| **Price** | 1 515 | 1 515 | 1 515 | - |
| Class | single-tower 120mm air, 4 heatpipes | same | same | Every build uses a 65W CPU. A dual-tower or an AIO buys nothing. |
| Rated for | 220W claimed, 65W needed | same | same | Tie it to the CPU row above: change the CPU's TDP and this line changes with it. The rating is a marketing class, not a promise. |
| Height | **155mm** | 155mm | 155mm | The number to check against the case - the Lancool 216 allows 180.5mm, so it clears with 25mm spare. |
| Measured noise | 29 dBA | 29 dBA | 29 dBA | Fan runs 500-1 850 RPM. Comparable to the GPU's silent BIOS, so neither dominates. |
| Case clearance | must clear side panel | same | same | Confirm height against the case before buying, not after. |
| Extra fans | none initially | none initially | none initially | Build with the case's own fans, then add an Arctic P12 Pro 5-pack (882) only if noise actually bothers you. |

**Reject:** any AIO; anything sized for 120W+ unless the CPU changes; substituting the MPK's
bundled Wraith cooler outside the Lean build - it is louder, and quiet is a stated goal.

---

## Power supply

| | **Lean** | **Working** | **Max** | Why it decides the purchase |
|---|---|---|---|---|
| **Part** | be quiet! **Pure Power 13 M 750W** | same | same | - |
| **Price** | 5 419 | 5 419 | 5 419 | Telemart, 2026-09-11. Was the 850W at 5 796; the 850W was sized against a 9800X3D build that no longer exists. |
| Output | **750W** | 750W | 750W | Sizing is not about peak; it is about sitting near 50-60% load where efficiency peaks and the fan stays off. 650W is rejected on connectors, not on watts. Above 1000W is wasted money. |
| System peak draw | ~373W | ~373W | ~483W | 9700X / 7500F both at **88W PPT** (not the 65W TDP) + GPU limit (GRE 220W, Red Devil XT 330W) + ~65W. **Load: 50% / 50% / 64%** of 750W - the band where the fan stays stopped. Worst case with the CPU in its optional 105W mode (142W PPT): 537W, **72%**. Transients are covered by ATX 3.1's certified 2x-rating excursion, not by continuous headroom. |
| Measured noise | LAMBDA A or better | same | same | The pick measures **6.51 dBA** - quieter than the 850W's 10.65 on the same platform. The 80+ sticker says nothing about noise. |
| Measured efficiency | ETA Gold or better | same | same | The pick is ETA Platinum - independently measured, not a sticker. |
| Fan-stop | required | required | required | The fan stops below a load threshold, so the machine is silent at idle, which is most of a work day. |
| Rails / standard | single +12V **62.5A (full 750W)**, ATX 3.1 | same | same | One rail means no per-rail limits to plan around. ATX 3.1 certifies **2x rated power for 100 microseconds** - 1 500W - which is what actually covers GPU transient spikes. Measured RDNA4 excursions are ~13% over nominal. |
| GPU connectors | **4x PCIe 6+2**, plus 1 native 12V-2x6 (600W) | same | same | The **GRE needs 2x 8-pin; the Red Devil XT needs 3x** - an earlier version of this row said 2x for every build and was wrong. Four covers the worst case with one spare, no adapter. The 12V-2x6 goes unused, which is the intent. |
| **SPL tier list grade** | **A** | A | A | Independent teardown-based grading ([psutierlist.org](https://psutierlist.org/)). **Reject anything below B**; the 650W of this same family is only B+ (85C bulk caps) and the 1000W is A- for poor 200% excursion response - in this family, bigger is graded *worse*. |
| Warranty | 10 years | 10 years | 10 years | The longest on the shortlist, and the PSU is the part whose failure can take others with it. |

**Build rules:** use the unit's **own** cables - modular pinouts are not standardised between
PSUs, and a cable from another unit can destroy a drive. On the Red Devil's three 8-pin sockets,
use the dual-head PCIe cable for two and a single-head cable for the third; do not daisy-chain
all three off one cable.

**Reject:** any unit with no Cybenetics or independent lab data - a previous pick was withdrawn
for exactly that; anything without fan-stop; a supervisor IC listed without short-circuit
protection.

---

## Case

| | **Lean** | **Working** | **Max** | Why it decides the purchase |
|---|---|---|---|---|
| **Part** | Deepcool **CC560 V2** | Lian Li **Lancool 216** | Lian Li **Lancool 216** | - |
| **Price** | 2 280 | 4 949 | 4 949 | - |
| Front | mesh | mesh | mesh | A glass or solid front at this budget costs temperature, therefore fan speed, therefore noise. |
| Fans included | 4 | 3 (2x160mm + 1x140mm) | 3 (2x160mm + 1x140mm) | Enough that no extra fan purchase is needed. Spending 3 000 on fans before hearing the machine is the classic first-build mistake. |
| GPU clearance | longer than the card | **up to 392mm** | **up to 392mm** | Any 9070-class card (~300-330mm) fits with room. Read the card's length from its review; the shop listing will not tell you. |
| Cooler clearance | taller than 155mm | **up to 180.5mm** | **up to 180.5mm** | The AK400's 155mm clears it. Check this row again if the cooler ever changes. |
| Dust filter | required | present | present | A model was rejected for lacking a front filter. |
| Measured noise data | **none** | present | present | **This is what Lean's 2 669 saving buys.** If measured quiet matters more, the NZXT H5 Flow (2024) at 3 479 has been measured. |

**Reject:** glass-front or zero-fan designer cases at this budget; the Montech AIR 903 MAX
(48.5 dBA with PWM hunting in the operating band).

---

## Monitor

| | **Lean** | **Working** | **Max** | Why it decides the purchase |
|---|---|---|---|---|
| **Part** | AOC **Q27G4XF** | AOC **Q27G4ZR** | AOC **Q27G4ZR** | - |
| **Price** | 6 757 | from 9 233 | from 9 233 | - |
| Size / resolution | 27" / 2560x1440 | 27" / 2560x1440 | 27" / 2560x1440 | ~109 pixels per inch at 27", which is the density where 1440p text is sharp without scaling. The stated target. |
| Panel | IPS | Fast IPS | Fast IPS | Text clarity over eight-hour days; OLED's subpixel layout is why RTINGS' text-clarity section must be read before considering one. |
| Refresh | 180Hz | **240Hz** (260Hz OC) | **240Hz** (260Hz OC) | The Lean panel gives up 60Hz for 2 794. The "260Hz" seen in some listings is the overclock, not the native rate - which also explains the Philips 260Hz figure. |
| Adaptive Sync | required | **48-240Hz**, G-Sync compatible | **48-240Hz**, G-Sync compatible | Without VRR you choose between tearing and v-sync latency at every frame rate below the panel's maximum. The 48Hz floor is where low-framerate compensation has to take over. |
| HDR | not a factor | HDR400 badge only | HDR400 badge only | HDR400 is not real HDR - do not pay anything for it, and do not expect it to look like HDR. |
| Port for full refresh | DisplayPort | **DisplayPort 1.4 + DSC** | **DisplayPort 1.4 + DSC** | **The port trap.** This panel's HDMI is 2.0 and caps at **144Hz** - use DisplayPort or silently lose 40% of what you paid for. |
| Measured response | **4.6 ms**, 0.1% overshoot | measured, low overshoot | measured, low overshoot | Grey-to-grey transition time as measured, not the "1 ms" on the box. **Overshoot %** is the artefact a spec sheet never mentions - 0.1% is excellent. Set overdrive to "Faster"; drop to "Fast" for anything locked at 60. |
| Measured brightness | 365 nits | 545 nits, 1410:1 | 545 nits, 1410:1 | Under ~400 nits is noticeably dim in a bright room - the Lean panel's real cost. |
| Stand | height adjust + VESA 100x100 | 130mm travel, tilt/swivel/pivot | 130mm travel, tilt/swivel/pivot | **Two monitors were rejected on this row alone** for being tilt-only. Height adjustment is not a luxury at eight hours a day. |

**Open:** the **Philips 27M2N3501PA at 9 139** is listed as an identical-panel 260Hz option and
has never been assessed.

**Reject:** any panel with no independent measurements; tilt-only stands; assuming the headline
refresh rate works on every input.

---

## Windows

| | **Lean** | **Working** | **Max** | Why it decides the purchase |
|---|---|---|---|---|
| **Part** | Windows 11 **Home** | Windows 11 **Home** | Windows 11 **Home** | Home is the default. Pro buys BitLocker, Hyper-V and Remote Desktop hosting - worth revisiting if containers turn out to be real. |
| **Price** | 2 500 | 2 500 | 2 500 | - |
