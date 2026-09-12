"""The three settled builds, costed from named-shop prices.

Rewritten 2026-09-12. The previous version priced six exploratory builds (A-F) against
hotline.ua's lowest anonymous offer, 2026-09-09, and appended a "+7% realistic retail"
fudge. Both are obsolete: the build is settled on three tiers, and this project prices at
shops read directly - see ../price_check.md for why hotline is a directory of who stocks
what, not a price.

Every figure below is the same one in the build table of ../pc_build.md, each with the shop
that quoted it, stock-checked 2026-09-11.

Run:  PYTHONUTF8=1 venv/Scripts/python.exe tasks/hardware/pc_build/builds.py > tasks/hardware/pc_build/builds.md
"""

# key: (category, model, price_uah, shop)
PARTS = {
    # --- CPU ---------------------------------------------------------------
    "cpu_7500f":   ("CPU", "Ryzen 5 7500F (tray)",                    6519,  "Brain"),
    "cpu_9700x_b": ("CPU", "Ryzen 7 9700X (BOX)",                    13936,  "Rozetka"),

    # --- GPU ---------------------------------------------------------------
    "gpu_9070gre": ("GPU", "Radeon RX 9070 GRE 12GB",                32179,  "Telemart"),
    "gpu_9070pu":  ("GPU", "Sapphire RX 9070 16GB PURE",             39999,  "Telemart"),

    # --- Motherboard -------------------------------------------------------
    "mb_b850m":    ("Motherboard", "ASRock B850M Pro RS WiFi (mATX)",  6965,  "Telemart"),
    "mb_b850":     ("Motherboard", "ASRock B850 Pro RS WiFi (ATX)",    8642,  "Rozetka"),
    "mb_tuf":      ("Motherboard", "ASUS TUF B850-PLUS WIFI (ATX)",    9399,  "Telemart"),

    # --- RAM ---------------------------------------------------------------
    "ram_16":      ("RAM", "16GB (2x8) DDR5-6000",                   16035,  "Rozetka"),
    "ram_32":      ("RAM", "32GB (2x16) DDR5-6000 CL36",             23789,  "Rozetka"),

    # --- SSD ---------------------------------------------------------------
    "ssd_sn3000":  ("SSD", "WD Green SN3000 1TB",                     6999,  "Telemart"),
    "ssd_990evo":  ("SSD", "Samsung 990 EVO Plus 1TB",               10679,  "Telemart"),
    "ssd_g5":      ("SSD", "Kingston Renegade G5 1TB",               11999,  "Telemart"),

    # --- Cooler / PSU / Case ----------------------------------------------
    "cool_ak400":  ("Cooler", "Deepcool AK400",                       1699,  "Telemart"),
    "psu_bq750":   ("PSU", "be quiet! Pure Power 13 M 750W",          5419,  "Telemart"),
    "case_cc560":  ("Case", "Deepcool CC560 Limited V2",              2280,  "Rozetka"),
    "case_lc216":  ("Case", "Lian Li Lancool 216",                    4949,  "Telemart"),

    # --- Monitor / OS ------------------------------------------------------
    "mon_xf":      ("Monitor", "AOC Q27G4XF 27in 1440p 180Hz",        6899,  "Rozetka"),
    "mon_zr":      ("Monitor", "AOC Q27G4ZR 27in 1440p 240Hz",        8669,  "Rozetka"),
    "os_home":     ("OS", "Windows 11 Home",                          7098,  "Brain"),
}

# Peripherals are budgeted separately from the machine - see ../pc_build.md.
PERIPHERALS = [
    ("Keyboard",   "AULA F75 Pink Switch, wired",              1699, "Brain / ITbox / Foxtrot / Telemart"),
    ("Mouse",      "Razer Cobra, wired, 58 g",                 2499, "Telemart / ITbox / Foxtrot"),
    ("Mouse mat",  "A4Tech X7-300MP, 437x350",                  299, "Telemart / Brain / ITbox"),
    ("Headphones", "SteelSeries Arctis Nova 5 Wireless",       5990, "Rozetka"),
    ("Desk",       "Стіл Оптима L, 138x82x75",                 2994, "Rozetka (+ delivery)"),
]

BUILDS = {
    "Lean - 6 cores, 12GB card, 16GB RAM, 180Hz": [
        "cpu_7500f", "mb_b850m", "ram_16", "gpu_9070gre", "ssd_sn3000",
        "psu_bq750", "cool_ak400", "case_cc560", "mon_xf", "os_home",
    ],
    "Working - the recommendation": [
        "cpu_9700x_b", "mb_b850", "ram_32", "gpu_9070gre", "ssd_990evo",
        "psu_bq750", "cool_ak400", "case_lc216", "mon_zr", "os_home",
    ],
    "Max - RX 9070 16GB, faster SSD": [
        "cpu_9700x_b", "mb_b850", "ram_32", "gpu_9070pu", "ssd_g5",
        "psu_bq750", "cool_ak400", "case_lc216", "mon_zr", "os_home",
    ],
}

# Substitutions priced in ../pc_build.md, shown under the tables rather than as extra tiers.
VARIANTS = [("Max", "mb_tuf", "mb_b850", "if Brain quotes rather than Telemart")]

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
    print("Shop prices, stock-checked 2026-09-11, from [price_check.md](price_check.md).")
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
