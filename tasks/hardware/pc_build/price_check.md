# Price check across shops, 2026-09-11

> **Shop settled 2026-09-13: Dmytro buys at click.ua.** Every table below was
> built around Telemart because `code/ua_prices.py` contacted four shops and
> click.ua was not one of them - a tooling gap, never a preference. click.ua is
> now in the script and priced first. **See [click_basket.md](click_basket.md)**;
> the shops below are a fairness cross-check, not where the basket is ordered.

Every part in all three builds, priced at **named retailers and checked for
stock** - not at a hotline floor. Run with
[`code/ua_prices.py`](../../../code/ua_prices.py) against [parts.json](parts.json);
Rozetka and Comfy read by hand in a browser because they refuse scripted requests.

## Why this exists

The build sheet carried hotline's cheapest offer for most parts. That number is
set by whichever of ~40 sellers is momentarily cheapest - on the 9700X that is
`PulsePad`, `iDrop`, `LuckyLink.kiev.ua`, shops with no service department. **A
floor nobody will honour is not a price.** Worse, a cheap listing at a real shop
is often a product they no longer stock; three of this document's first-pass
"best prices" turned out to be out of stock.

## The shops, and which are actually independent

| Source | Read how | Independent? |
|---|---|---|
| **Telemart** | script, their search page | yes - component specialist, assembles |
| **Brain** | script, their own quick-search API | yes - component specialist |
| **ITbox** | script, same API shape as Brain | **no - identical catalogue and prices to Brain on all 19 parts.** Kept only because its stock flag is honest where Brain's is not |
| **Rozetka** | browser, by hand | yes - largest retailer, easiest RMA, states stock clearly |
| **Comfy** | browser, by hand | yes - but stocks almost nothing here |
| **Foxtrot** | script | yes - carries the monitors and one CPU, at list price |
| **КТС** | browser | stocks none of these parts - only prebuilt PCs |
| **MOYO** | browser | catalogue is prebuilts and laptops; no components matched |
| hotline | script | **directory only** - who stocks it and what they advertise. Never the price we act on |

**ITbox and Brain are one catalogue.** Every one of the 19 parts came back at the
identical price from both. Treating them as two confirmations would have been
double-counting; what ITbox adds is `InStock`, which matches Brain's own product
page exactly, where Brain's own API field reads `false` for everything.

## The stock problem

Brain's quick-search reports `IsPresent: false` on every product, in stock or
not, so it cannot be used. Checked against Brain's product pages directly:

| Part | Brain price | Brain page says |
|---|---:|---|
| Crucial Pro 32GB CP2K16G60C36U5B | 21 094 | **Немає в наявності** |
| Lian Li Lancool 216 | 4 699 | **Немає в наявності - товар не доступний** |
| be quiet! Pure Power 13 M 750W | 5 419 | **Немає в наявності** |
| Windows 11 Home ESD KW9-00664 | 7 098 | **Є в наявності** |

And at Rozetka, **the Ryzen 5 7500F MPK is "Немає в наявності"** - as it is at
Brain/ITbox. The multipack SKU is not currently buyable at any of the four.

So the three cheapest numbers in the first pass - the 21 094 RAM, the 4 699
case, and the MPK CPU - are all listings, not offers. They are struck out below.

## The parts

UAH, 2026-09-11. **Best** = cheapest at a named shop that will actually sell it.

| Part | Carried | Telemart | Brain / ITbox | Rozetka | Foxtrot | hotline floor (n) | **Best, in stock** |
|---|---:|---:|---:|---:|---:|---:|---:|
| **CPU** Ryzen 5 7500F **MPK** | 6 589 | not stocked | ~~7 721~~ no stock | ~~6 860~~ no stock | - | 7 459 (9) | **unavailable - see below** |
| **CPU** Ryzen 5 7500F tray *(fallback)* | - | 6 559 | 6 519 | 5 999 | - | 5 825 | **6 519** + cooler |
| **CPU** Ryzen 7 9700X BOX/WOF | 15 099 | 14 499 | 18 080 | **13 936** | 18 080 | 12 699 (37) | **13 936** |
| **GPU** RX 9070 GRE Hellhound 12GB | 32 179 | **32 179** | not stocked | 33 120 | - | 30 253 (6) | **32 179** |
| **GPU** Sapphire RX 9070 PURE 16GB | 39 999 | **39 999** | not stocked | 42 334 | 44 805 | 39 867 (24) | **39 999** |
| **MB** ASRock B850M Pro RS WiFi | 6 965 | **6 965** | not stocked | 7 247 | - | 6 588 (42) | **6 965** |
| **MB** ASRock B850 Pro RS WiFi | 8 829 | 8 829 | not stocked | **8 642** | - | 8 005 (28) | **8 642** |
| **MB** ASUS TUF B850-PLUS WIFI *(Max alt)* | 9 399 | **9 399** | 9 976 | 9 689 | - | 9 421 (39) | **9 399** |
| **RAM** Kingston FURY 16GB 2x8 CL30 | 15 599 | 16 599 | 16 562 | **16 035** | - | 15 628 (42) | **16 035** |
| **RAM** Crucial Pro 32GB 2x16 CL36 | 24 099 | 24 099 | ~~21 094~~ no stock | **23 789** | - | 21 469 (22) | **23 789** |
| **SSD** WD Green SN3000 1TB | 6 999 | **6 999** | 7 245 | 8 404 | - | 6 936 (37) | **6 999** |
| **SSD** Samsung 990 EVO Plus 1TB | 10 399 | **10 679** | 11 596 | 12 192 | - | 9 899 (50) | **10 679** |
| **SSD** Kingston FURY Renegade G5 1TB | 11 999 | **11 999** | 2TB only | 13 126 | - | 12 065 (39) | **11 999** |
| **Cooler** Deepcool AK400 | 1 699 | **1 699** | **1 699** | **1 699** | 1 699 *(Comfy)* | 1 509 (26) | **1 699** |
| **PSU** be quiet! Pure Power 13 M 750W | 5 419 | **5 419** | ~~5 419~~ no stock | **5 419** | - | 5 292 (13) | **5 419** |
| **Case** Deepcool CC560 **Limited V2** | 2 280 | 2 399 | 2 399 | **2 280** | - | 2 075 (23) | **2 280** |
| **Case** Lian Li Lancool 216 Black | 4 949 | **4 949** | ~~4 699~~ no stock | not stocked | - | 4 927 (**1**) | **4 949** |
| **Monitor** AOC Q27G4XF | 6 757 | not stocked | 7 820 | **6 899** | 7 899 | 7 343 (5) | **6 899** |
| **Monitor** AOC Q27G4ZR | 9 233 | not stocked | 9 998 | **8 669** | 10 099 | 10 099 (9) | **8 669** |
| **OS** Windows 11 Home ESD KW9-00664 | **2 500** | 8 304 | **7 098** | 8 299 | - | 4 628 (7) | **7 098** |

The AK400 at **1 699** is the only part that comes back identical from five
independent shops. The PSU at **5 419** agrees at Telemart and Rozetka.

## The four things this changes

1. **The Windows licence is wrong by 4 598 in every build.** The sheet carries
   **2 500**; the cheapest ESD in stock at a named shop is **Brain 7 098**, with
   Rozetka 8 299 and Telemart 8 304. hotline shows 4 628 at one small seller,
   unconfirmed. **+13 794 across the three builds** - the largest error in the
   sheet by a wide margin.

2. **The Lean build's CPU cannot be bought as planned.** The Lean tier uses the
   **7500F MPK** precisely because that SKU ships a Wraith Stealth, which is what
   lets the cooler row read 0. It is out of stock at Rozetka and at Brain/ITbox
   and absent from Telemart. The fallback is the **tray 7500F at 6 519 (Brain)
   plus an AK400 at 1 699 = 8 218**, so the MPK's real saving was **1 629**, and
   Lean loses its "no cooler" line. If the MPK reappears, take it.

3. **The 9700X BOX is over-carried by 1 163** - Rozetka 13 936, Telemart 14 499
   against our 15 099. Brain and Foxtrot both quote 18 080, which is list price,
   not an offer.

4. **The Q27G4ZR fell to 8 669 at Rozetka, in stock** - below hotline's entire
   listed range (10 099 - 10 981) and below the 9 233 we carry. **-564.**

Two corrections that do not move money but prevent a wrong purchase:

- **There is no SKU called "CC560 V2" in the Lean row.** Deepcool ships a *CC560
  V2* (R-CC560-BKGAA4-G-2, Rozetka 2 689), a *CC560 ARGB V2*, and a *CC560
  Limited V2* (R-CC560-BKNAA0-G-2). Our 2 280 is the **Limited V2**, the plain
  non-ARGB one [case.md](components/case.md) argues for. Pinned by part number so
  a shop cannot substitute the ARGB.
- **The Lancool 216 Black has one seller on hotline and is out of stock at
  Brain.** Telemart at 4 949 is the only source - confirmed `InStock` on their
  product page. It is the one part here with real supply risk, so if the build
  is not ordered soon, expect to re-check this row first.

## Totals, recomputed from in-stock prices

| | **Lean** | **Working** | **Max** |
|---|---:|---:|---:|
| CPU | 7500F **tray** 6 519 | 9700X BOX **13 936** | 9700X BOX **13 936** |
| Cooler | **AK400 1 699** - the MPK is unavailable | AK400 **1 699** | AK400 **1 699** |
| GPU | 9070 GRE **32 179** | 9070 GRE **32 179** | RX 9070 PURE **39 999** |
| Board | B850M Pro RS WiFi **6 965** | B850 Pro RS WiFi **8 642** | B850 Pro RS WiFi **8 642** |
| RAM | 16GB **16 035** | 32GB **23 789** | 32GB **23 789** |
| SSD | SN3000 **6 999** | 990 EVO Plus **10 679** | Renegade G5 **11 999** |
| PSU | **5 419** | **5 419** | **5 419** |
| Case | CC560 Limited V2 **2 280** | Lancool 216 **4 949** | Lancool 216 **4 949** |
| Monitor | Q27G4XF **6 899** | Q27G4ZR **8 669** | Q27G4ZR **8 669** |
| Windows 11 Home | **7 098** | **7 098** | **7 098** |
| **Total** | **92 092** | **117 059** | **126 199** |
| Was carried | 85 287 | 114 859 | 124 279 |
| Change | **+6 805** | **+2 200** | **+1 920** |

> **Superseded in one row, 2026-09-12.** The monitor is now the **ASGARD AS275QC at 6 999** in
> all three builds - see [components/monitor.md](components/monitor.md). Totals become
> **92 192 / 115 389 / 124 529**. The table above is left as the record of the 2026-09-11 pass
> and is not rewritten.

**All three still fit the 130 000 range**, Max with **3 801** to spare - down from
the 5 388 the old numbers claimed, so the headroom is thinner than it looked but
the shape of the ladder is unchanged. Lean's rise is the Windows licence plus the
MPK falling through; the other two are almost all the licence.

## Buying this basket

No single shop carries it, and cheapest-per-part means three orders:

- **Telemart** - GPU (both), B850M board, SN3000, Renegade G5, PSU, Lancool 216,
  AK400. They assemble, and they are the only source for the Lancool.
- **Rozetka** - 9700X, B850 Pro RS WiFi, 32GB RAM, 16GB RAM, both monitors,
  CC560 Limited V2.
- **Brain** - the Windows licence, and the tray 7500F for Lean.

Consolidating Working onto Telemart alone costs about **+1 400** (RAM +310,
monitor unavailable there at all) and buys one warranty counterpart instead of
three. Dmytro's call, not this document's.

## Method notes, and what is still not covered

- **Hosts contacted by the script: hotline.ua, telemart.ua, brain.com.ua,
  itbox.ua, foxtrot.com.ua only.** Any other host raises `Blocked`. Certificates
  verified, redirects never followed - the header of `code/ua_prices.py` says why
  both matter.
- **Rozetka and Comfy refuse scripted requests** (Rozetka renders client-side,
  Comfy returns 403) and were read in a browser. **КТС and MOYO were checked and
  stock none of these parts** - both are prebuilt-and-appliance catalogues.
  Citycom was not reachable on any search URL tried.
- **Stock is confirmed for every price in the totals.** Rozetka states it in
  search. ITbox's `InStock` was checked against Brain's own product pages and
  matches, so it speaks for the Brain/ITbox catalogue. Telemart states nothing
  in search, but its **product pages carry a schema.org `availability`**, and a
  card priced 0 in search is always `OutOfStock` on the page - `ua_prices.py`
  now reads that automatically, one request per kept item. **All 25 Telemart
  lines came back `InStock` on 2026-09-11**, including the two parts Telemart
  alone carries, the Lancool 216 and the Renegade G5.
- **hotline throttles** after a few dozen requests and then serves an empty
  page. The directory column was captured earlier the same day; use `--cache` on
  a repeat run.
- Prices move weekly in this market - see the memory-crisis section in
  [../../pc_build.md](../pc_build.md). Good for days, not weeks.
