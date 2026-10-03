# Brief: in-depth check of the Green Cell UPSLP700 before buying

Written 2026-09-30 for a fresh conversation. Load the `component-research` and
`repo-tooling-first` skills first. Background is in [ups.md](ups.md), in the sections
"The minimum wattage to shop by", "Cross-check of the pure-sine requirement" and "All shops,
sweep". Don't re-research what's settled there.

## Settled — do not reopen

- **Need:** a clean shutdown only, no runtime. The UPS carries the PC + monitor at **~475 W at the
  wall** (Working build: 9700X, RX 9070 PURE, Cougar GEX X2 850 PSU, which has active PFC).
- **Requirements:** pure sine on battery, **≥700 W real**, battery built in, Schuko sockets,
  transfer time under ~10 ms (the PSU rides through ~19–21 ms).
- **Shops:** any reputable Ukrainian shop, not only click.ua.
- **Candidate:** Dmytro likes the **Green Cell UPSLP700 (PowerProof 1000VA / 700W)**.

## What is known, and how weakly

| Fact | Value | Source quality |
|---|---|---|
| Price / seller | **7 743 ₴**, RozetkaEU, ships from the EU | [Rozetka listing p569712112](https://hard.rozetka.com.ua/ua/green-cell-upslp700/p569712112/), read 2026-09-30 |
| Power | 700 W / 1000 VA → **68% load** | Rozetka field + search summary |
| Waveform | pure sine | Rozetka field + search summary |
| Battery | 2 × 12 V 7 Ah, built in | same |
| Sockets | 4 × Schuko | same (one search result said 2 — **check**) |
| Transfer | 2–6 ms | same |
| Warranty | 24 mo (battery 12 mo) | search summary only |
| Reviews | Rozetka 4★ / **1 review** | Rozetka |

**The maker's own page and datasheet were never opened.** Everything above comes from Rozetka's
seller-entered fields or web-search summaries.

## Questions to answer, most decisive first

1. **Maker spec, read in full** (greencell.global product page + datasheet/manual PDF):
   - Pure sine **on battery**, and the distortion (THD) figure.
   - Real W, transfer time, socket count and type, battery model and whether it's user-replaceable.
   - Runtime at ~475 W, or the runtime curve.
   - The model code: are UPSLP700 and "UPS08 1000VA 700W" the same unit?
2. **Does the maker or anyone say anything about active-PFC PSUs?** Quote it if they do.
3. **Independent reviews or tests** (reviews, forums, YouTube). Look especially for fan noise,
   beeping, battery life, failures, and behaviour on real power cuts with gaming PCs. Transcripts
   go in `pc_build/sources/`; every number needs a video ID and timestamp.
4. **USB shutdown:** is it HID-compliant, so Windows handles shutdown natively? Does it have its
   own software?
5. **Warranty for a unit shipped by RozetkaEU:** who services it in Ukraine, and how is a
   warranty claim or a 14-day return handled?
6. **Price and stock at other reputable shops.** It wasn't found outside Rozetka in the sweep,
   but check. Quote shop + price + stock; hotline is a directory, not a price.
7. **Close alternatives, one line each, only if something above fails:** SVC SL-1KS-LCD
   (6 704 Brain), Green Cell UPS09 (9 880 Rozetka), PowerWalker VI 1500 CSW (13 339 Rozetka).

## Rules

- Every source read in full, with a verbatim quote per row, in a coverage table written to
  `ups.md` under a new dated section. Targeted edits only; the file is shared with other sessions.
- State plainly what could not be read (Cloudflare, 403, PDF not found). Never imply coverage.
- The answer to Dmytro goes brief: buy or don't buy, the deciding facts, open risks. Detail goes
  in the doc. Don't commit.

## Done when

Buy / don't-buy on the UPSLP700, with the maker-confirmed specs, at least one independent review
or an explicit "none found", the warranty path, and the best price at a named shop.
