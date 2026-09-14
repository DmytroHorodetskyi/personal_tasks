"""The three settled builds, costed from named-shop prices.

Rewritten 2026-09-12. The previous version priced six exploratory builds (A-F) against
hotline.ua's lowest anonymous offer, 2026-09-09, and appended a "+7% realistic retail"
fudge. Both are obsolete: the build is settled on three tiers, and this project prices at
shops read directly - see ../price_check.md for why hotline is a directory of who stocks
what, not a price.

Repriced 2026-09-13 at click.ua, the shop Dmytro buys from; every line stock-checked
there. The per-part working, and the parts click.ua does not stock, are in
../click_basket.md.

Run:  PYTHONUTF8=1 venv/Scripts/python.exe tasks/hardware/pc_build/builds.py > tasks/hardware/pc_build/builds.md
"""

# key: (category, model, price_uah, shop)
#
# Repriced 2026-09-13 at **click.ua**, the shop Dmytro buys from. Every line is read from
# click.ua's own search and stock-checked; see ../click_basket.md for the per-part working,
# the parts click.ua does not stock at all, and the substitutions chosen for them.
PARTS = {
    # --- CPU ---------------------------------------------------------------
    # click.ua carries no BOX AM5 SKU. Lean takes the Multipack (bundles a Wraith
    # Stealth, so it needs no separate cooler); the 9700X is tray-only there.
    "cpu_7500f":   ("CPU", "Ryzen 5 7500F (Multipack, bundled cooler)",  7085,  "click.ua"),
    "cpu_9700x_b": ("CPU", "Ryzen 7 9700X (tray)",                      12892,  "click.ua"),

    # --- GPU ---------------------------------------------------------------
    # The RX 9070 GRE is not sold at click.ua in any brand, so the ladder moves up a rung.
    "gpu_9060xt":  ("GPU", "PowerColor RX 9060 XT 16GB Hellhound",      29659,  "click.ua"),
    "gpu_9070pu":  ("GPU", "Sapphire RX 9070 16GB PURE",                43908,  "click.ua"),
    "gpu_9070xt":  ("GPU", "Gigabyte RX 9070 XT 16GB Gaming",           52034,  "click.ua"),

    # --- Motherboard -------------------------------------------------------
    "mb_b850m":    ("Motherboard", "ASRock B850M Pro RS WiFi (mATX)",    7632,  "click.ua"),
    "mb_b850":     ("Motherboard", "ASRock B850 Pro RS WiFi (ATX)",      9168,  "click.ua"),
    "mb_tuf":      ("Motherboard", "ASUS TUF B850-PLUS WIFI (ATX)",      9976,  "click.ua"),

    # --- RAM ---------------------------------------------------------------
    # The Crucial Pro CL36 kit is not stocked; the Kingston CL36 kit replaces it.
    "ram_16":      ("RAM", "Kingston Fury Beast 16GB (2x8) DDR5-6000 CL30",  17974, "click.ua"),
    "ram_32":      ("RAM", "Kingston Fury Beast 32GB (2x16) DDR5-6000 CL36", 25099, "click.ua"),

    # --- SSD ---------------------------------------------------------------
    # At click.ua the 990 PRO is cheaper than the EVO Plus, so Working takes the PRO.
    "ssd_sn3000":  ("SSD", "WD Green SN3000 1TB",                        7483,  "click.ua"),
    "ssd_990pro":  ("SSD", "Samsung 990 PRO 1TB",                       12162,  "click.ua"),
    "ssd_g5":      ("SSD", "Kingston FURY Renegade G5 1TB",             16700,  "click.ua"),

    # --- Cooler / PSU / Case ----------------------------------------------
    "cool_ak400":  ("Cooler", "Deepcool AK400",                          1699,  "click.ua"),
    # be quiet! Pure Power 13 M 750W is not sold at click.ua; the whole 750W-class
    # shelf was checked against psu.md's criteria - see ../click_basket.md.
    "psu_cougar":  ("PSU", "Cougar GEX X2 850 850W",                     5799,  "click.ua"),
    # Neither the CC560 Limited V2 nor the Lancool 216 is stocked; these are the two
    # AeroCool cases Dmytro picked at click.ua on 2026-09-12, specced in components/case.md.
    "case_p500c":  ("Case", "AeroCool P500C-G-WT-v1",                    3045,  "click.ua"),
    "case_d502a":  ("Case", "AeroCool D502A-G-WT-v1",                    3056,  "click.ua"),

    # --- Monitor / OS ------------------------------------------------------
    "mon_asgard":  ("Monitor", "ASGARD AS275QC 27in 1440p 200Hz VA",     6999,  "click.ua"),
    "os_home":     ("OS", "Windows 11 Home",                             8799,  "click.ua"),
}

# Peripherals are budgeted separately from the machine - see ../pc_build.md.
# NOT YET REPRICED AT CLICK.UA: these are the 2026-09-11 shop prices.
PERIPHERALS = [
    ("Keyboard",   "AULA F75 Pink Switch, wired",              1699, "Brain / ITbox / Foxtrot"),
    ("Mouse",      "Razer Cobra, wired, 58 g",                 2499, "ITbox / Foxtrot"),
    ("Mouse mat",  "A4Tech X7-300MP, 437x350",                  299, "Brain / ITbox"),
    ("Headphones", "SteelSeries Arctis Nova 5 Wireless",       5990, "Rozetka"),
    ("Desk",       "\u0421\u0442\u0456\u043b \u041e\u043f\u0442\u0438\u043c\u0430 L, 138x82x75", 2994, "Rozetka (+ delivery)"),
]

BUILDS = {
    "Lean - 6 cores, 16GB card, 16GB RAM": [
        # No cooler line: the 7500F Multipack bundles one, per components/cooling.md.
        "cpu_7500f", "mb_b850m", "ram_16", "gpu_9060xt", "ssd_sn3000",
        "psu_cougar", "case_p500c", "mon_asgard", "os_home",
    ],
    "Working - the recommendation": [
        "cpu_9700x_b", "mb_b850", "ram_32", "gpu_9070pu", "ssd_990pro",
        "psu_cougar", "cool_ak400", "case_d502a", "mon_asgard", "os_home",
    ],
    "Max - RX 9070 XT, Gen 5 SSD": [
        "cpu_9700x_b", "mb_b850", "ram_32", "gpu_9070xt", "ssd_g5",
        "psu_cougar", "cool_ak400", "case_d502a", "mon_asgard", "os_home",
    ],
}

# Substitutions priced in ../pc_build.md, shown under the tables rather than as extra tiers.
VARIANTS = [("Max", "mb_tuf", "mb_b850", "the alternative board priced in ../pc_build.md")]

ORDER = ["CPU", "Motherboard", "RAM", "GPU", "SSD", "PSU", "Cooler", "Case", "Monitor", "OS"]


def uah(value):
    return f"{value:,}".replace(",", " ")


def render(name, keys):
    rows = sorted((PARTS[k] for k in keys), key=lambda r: ORDER.index(r[0]))
    total = sum(r[2] for r in rows)
    out = ["", f"### {name} - {uah(total)} UAH", "",
           "| Part | Model | UAH | Shop |", "|---|---|---:|---|"]
    for cat, model, price, shop in rows:
        out.append(f"| {cat} | {model} | {uah(price)} | {shop} |")
    out.append(f"| | **Total** | **{uah(total)}** | |")
    for build, new_key, old_key, why in VARIANTS:
        if name.startswith(build):
            delta = PARTS[new_key][2] - PARTS[old_key][2]
            out.append("")
            out.append(f"Variant: **{PARTS[new_key][1]}** instead of {PARTS[old_key][1]}, "
                       f"{why} - {uah(total + delta)} total ({delta:+d}).")
    return "\n".join(out), total


if __name__ == "__main__":
    chunks, totals = [], {}
    for name, keys in BUILDS.items():
        text, total = render(name, keys)
        chunks.append(text)
        totals[name] = total

    print("<!-- generated by tasks/hardware/pc_build/builds.py - do not edit by hand -->")
    print("\n# The three builds, costed\n")
    print("Prices read at **click.ua** and stock-checked 2026-09-13 - the shop Dmytro buys from.")
    print("Working from [click_basket.md](click_basket.md); other shops in [price_check.md](price_check.md).")
    print("Peripherals are budgeted separately and listed at the end.\n")
    print("## Totals\n")
    print("| Build | UAH |")
    print("|---|---:|")
    for name, total in totals.items():
        print(f"| {name} | {uah(total)} |")
    print("\n".join(chunks))

    ptotal = sum(p[2] for p in PERIPHERALS)
    print("")
    print(f"### Peripherals (separate budget) - {uah(ptotal)} UAH")
    print("")
    print("| Part | Model | UAH | Shop |")
    print("|---|---|---:|---|")
    for cat, model, price, shop in PERIPHERALS:
        print(f"| {cat} | {model} | {uah(price)} | {shop} |")
    print(f"| | **Total** | **{uah(ptotal)}** | |")
    print("")
    print("Desk delivery is charged at the carrier's rate and is not included.")
