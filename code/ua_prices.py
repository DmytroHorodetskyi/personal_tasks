"""Ukrainian retail price check for a list of parts, across named shops.

The rules this obeys, after an antivirus alert on 2026-09-11 stopped an earlier
version that broke all four:

1. **TLS certificates are verified.** `CLAUDE.md` records that this network
   intercepts TLS, which tempts you into `ssl.CERT_NONE`. Do not. Strict
   verification was tested against every host below and works; a host that fails
   it is reported as unverifiable rather than silently trusted.
2. **Redirects are never followed.** Nothing here clicks an aggregator's
   outbound link. Following `hotline.ua/go/price/<id>/` walks an affiliate
   tracker into a long tail of unknown resellers, and that traffic pattern is
   what the antivirus flagged - correctly.
3. **Only the shops in `SHOPS` are contacted**, each on its own domain through
   its own search. No host outside that table is ever requested.
4. **hotline is a directory, not a price source.** It answers "who stocks this
   and what do they advertise", read off hotline's own page. Every price we act
   on is read from a named shop instead.

So a part gets two kinds of evidence: the advertised spread across ~40 sellers
(hotline, one request) and the real price at shops we would actually buy from
(direct, one request each). Rozetka serves search over JavaScript and cannot be
read this way - check it by hand in a browser.

Usage:

    PYTHONUTF8=1 venv/Scripts/python.exe code/ua_prices.py parts.json -o out.md
    PYTHONUTF8=1 venv/Scripts/python.exe code/ua_prices.py "Lancool 216" --find

`parts.json` is a list of objects:

    [{"name": "Cooler - Deepcool AK400",
      "query": "Deepcool AK400",          # or "url": a pinned hotline page
      "match": ["AK400"],                  # all must appear in the title
      "exclude": ["ZERO", "Digital"],      # none may appear
      "shop_query": "AK400"}]              # what to type into each shop's search

`match`/`exclude` are case-insensitive substrings, applied to both the hotline
title and every shop result, so the right SKU is picked without hand-copying
URLs - and so a shop's own naming has to agree before its price is counted.
"""

import argparse
import html
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HEADERS = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                   "(KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "uk-UA,uk;q=0.9,en;q=0.8",
    "Accept-Encoding": "identity",
}

# Every host this program is allowed to contact. Adding one means checking that
# it serves search results to a plain GET, and that we would buy from it.
ALLOWED_HOSTS = {"hotline.ua", "telemart.ua", "brain.com.ua", "www.itbox.ua",
                 "www.foxtrot.com.ua"}


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    """Refuse every redirect: a 3xx means our URL was wrong, not that we should
    go wherever we are sent."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


OPENER = urllib.request.build_opener(
    urllib.request.HTTPSHandler(context=ssl.create_default_context()), _NoRedirect)

# hotline's Nuxt payload escapes every slash as this literal six-character run.
SLASH = "\\" + "u002F"


class Blocked(Exception):
    """A request to a host outside the allowlist."""


CACHE_DIR = None          # set by --cache; None disables caching
CACHE_MAX_AGE = 6 * 3600  # a price older than this is not worth reusing


def _cache_path(url):
    import hashlib
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:16]
    return os.path.join(CACHE_DIR, digest + ".html")


def fetch(url, tries=3, pause=2.0):
    host = urllib.parse.urlsplit(url).hostname or ""
    if host not in ALLOWED_HOSTS:
        raise Blocked(host)

    # hotline starts serving an empty shell after a few dozen requests, so a run
    # that has to be repeated must not pay for the same page twice.
    path = _cache_path(url) if CACHE_DIR else None
    if path and os.path.exists(path) and time.time() - os.path.getmtime(path) < CACHE_MAX_AGE:
        with open(path, encoding="utf-8") as fh:
            return fh.read()

    last = None
    for attempt in range(tries):
        try:
            with OPENER.open(urllib.request.Request(url, headers=HEADERS), timeout=60) as resp:
                body = resp.read().decode("utf-8", "replace")
            if path and len(body) > 2000:
                with open(path, "w", encoding="utf-8") as fh:
                    fh.write(body)
            return body
        except urllib.error.HTTPError as exc:
            # 429/5xx is the shop asking us to slow down; anything else is a
            # wrong URL, where retrying is just noise.
            if exc.code not in (429, 500, 502, 503) or attempt == tries - 1:
                raise
            last = exc
            time.sleep(pause * 8 * (attempt + 1))
        except ssl.SSLError as exc:
            raise RuntimeError("certificate did not verify for %s" % host)
        except Exception as exc:
            last = exc
            time.sleep(pause)
    raise last


def unescape(text):
    text = text.replace(SLASH, "/")
    if "\\u" not in text:
        return text
    try:
        return (text.encode("utf-8").decode("unicode_escape")
                .encode("latin-1", "ignore").decode("utf-8", "ignore"))
    except Exception:
        return text


def wanted(title, match, exclude):
    low = title.lower()
    return (all(t.lower() in low for t in match)
            and not any(t.lower() in low for t in exclude))


# ------------------------------------------- hotline, used only as a directory

OFFER_RE = (r'firmTitle:"([^"]+)",firmExtraInfo:\{(.{0,1500}?)\},guaranteeTerm'
            r'(.{0,2500}?)price:(\d+)')


def hotline_search(query):
    """Candidate products for a query. The payload is one long minified object;
    each product starts at its own url:"...", so slice on those boundaries -
    image lists push minPrice an unknown distance from the title."""
    body = fetch("https://hotline.ua/ua/sr/?q=" + urllib.parse.quote(query))
    starts = [m.start() for m in re.finditer(r'url:"' + re.escape(SLASH), body)]
    found, seen = [], set()
    for i, start in enumerate(starts):
        chunk = body[start:starts[i + 1] if i + 1 < len(starts) else start + 20000]
        head = re.match(r'url:"(' + re.escape(SLASH) + r'[^"]+)",title:"([^"]+)"', chunk)
        if not head:
            continue
        url = "https://hotline.ua/ua" + unescape(head.group(1))
        if url in seen:
            continue
        seen.add(url)
        price = re.search(r'minPrice:(\d+),maxPrice:(\d+)', chunk)
        found.append({"url": url, "title": unescape(head.group(2)),
                      "min": int(price.group(1)) if price else 0,
                      "max": int(price.group(2)) if price else 0})
    return found


def hotline_offers(url):
    """What each seller advertises, read off hotline's own page. No link from
    this list is ever followed - the shop names are the point, not the links."""
    body = fetch(url)
    offers = []
    for m in re.finditer(OFFER_RE, body, re.S):
        site = re.search(r'website:"([^"]*)"', m.group(2))
        offers.append({"shop": unescape(m.group(1)),
                       "site": (site.group(1) if site else "").lower(),
                       "price": int(m.group(4))})
    best = {}
    for offer in offers:
        key = offer["site"] or offer["shop"]
        if key not in best or offer["price"] < best[key]["price"]:
            best[key] = offer
    return sorted(best.values(), key=lambda o: o["price"])


# --------------------------------------------------- the shops, read direct

def telemart(query):
    """Telemart's search cards, plus the product URL so stock can be settled.

    Their search states no availability, but a price of 0 on a card means the
    item is not orderable, and the product page carries a schema.org
    `availability` that agrees with it. `telemart_stock` reads that.
    """
    body = fetch("https://telemart.ua/ua/search/" + urllib.parse.quote(query) + "/")
    items, seen = [], set()
    for m in re.finditer(r'data-prod-name="([^"]*)"[^>]*?data-prod-price="(\d+)"', body):
        name = html.unescape(m.group(1))
        if name in seen:
            continue
        seen.add(name)
        price = int(m.group(2))
        link = re.search(r'href="(https://telemart\.ua/ua/products/[^"]+)"',
                         body[m.start():m.start() + 4000])
        items.append({"name": name, "price": price,
                      "url": link.group(1) if link else None,
                      "stock": False if price == 0 else None})
    return items


def telemart_stock(url):
    """True/False from the product page's schema.org availability, None if absent."""
    try:
        body = fetch(url, tries=2)
    except Exception:
        return None
    found = re.search(r'"availability"\s*:\s*"[^"]*?(InStock|OutOfStock|PreOrder)"', body)
    return found.group(1) == "InStock" if found else None


def foxtrot(query):
    body = fetch("https://www.foxtrot.com.ua/uk/search?query=" + urllib.parse.quote(query))
    items, seen = [], set()
    pat = (r'data-title="([^"]*)"[^>]*?data-variant="([^"]*)"[^>]*?data-price="(\d+)"')
    for m in re.finditer(pat, body):
        name = html.unescape(m.group(1))
        if name in seen:
            continue
        seen.add(name)
        items.append({"name": name, "price": int(m.group(3)),
                      "stock": m.group(2) == "InStock"})
    return items


def brain(query):
    """Brain's own quick-search API - the endpoint its search box calls.

    Their HTML search page 404s to a plain request; this is the same host, a
    plain GET, and it returns JSON with a stock flag.
    """
    body = fetch("https://brain.com.ua/api/v1/quick_search/?Search=" + urllib.parse.quote(query))
    data = json.loads(body)
    items = []
    for product in data.get("Response", {}).get("Hits", {}).get("Products", []):
        items.append({"name": product.get("NameUa") or product.get("Name", ""),
                      "price": int(product.get("Price") or 0),
                      # IsPresent comes back false even for items their own page
                      # shows in stock, so it is not reported as a stock answer.
                      "stock": None})
    return items


def itbox(query):
    """ITbox runs the same search engine as Brain, with a flatter payload and a
    stock flag that can actually be believed."""
    body = fetch("https://www.itbox.ua/api/v1/elastic_quick_search/?Search="
                 + urllib.parse.quote(query))
    items = []
    for product in json.loads(body).get("Products", []):
        items.append({"name": product.get("Name", ""),
                      "price": int(product.get("Price") or 0),
                      "stock": bool(product.get("InStock") or product.get("IsAvailable"))})
    return items


SHOPS = [("Telemart", telemart), ("Brain", brain), ("ITbox", itbox), ("Foxtrot", foxtrot)]

# Serve search over JavaScript - a plain GET returns an empty shell. Check by hand.
BY_HAND = ["Rozetka", "Comfy", "КТС", "MOYO", "Citycom"]


# ------------------------------------------------------------------ driver

def check(part):
    match, exclude = part.get("match", []), part.get("exclude", [])
    # The directory is a nice-to-have. hotline throttles after a few dozen
    # requests and then serves an empty shell, and that must not cost us the
    # shop prices, which are the part we actually act on.
    note, product, offers = None, None, []
    try:
        if part.get("url"):
            product = {"url": part["url"], "title": part.get("name", ""), "min": 0, "max": 0}
        else:
            candidates = hotline_search(part["query"])
            product = next((c for c in candidates if wanted(c["title"], match, exclude)), None)
            if product is None:
                note = ("hotline returned nothing - throttled" if not candidates
                        else "no hotline product matched: " + "; ".join(
                            c["title"] for c in candidates[:6]))
        if product:
            offers = hotline_offers(product["url"])
    except Exception as exc:
        note = "directory unavailable (%s)" % type(exc).__name__

    result = {"part": part, "product": product, "offers": offers, "note": note, "shops": {}}
    query = part.get("shop_query") or part.get("query") or ""
    # Shops name the same SKU differently from hotline, so a part may narrow the
    # filter separately for them; default to the hotline one.
    s_match = part.get("shop_match", match)
    s_exclude = part.get("shop_exclude", exclude)
    for label, search in SHOPS:
        time.sleep(1.5)  # one part at a time; shops rate-limit a fast loop
        try:
            hits = [i for i in search(query) if wanted(i["name"], s_match, s_exclude)]
        except urllib.error.HTTPError as exc:
            hits = [{"name": "no results (HTTP %s)" % exc.code, "price": 0, "stock": None}]
        except Blocked as exc:
            hits = [{"name": "refused: host %s is not on the allowlist" % exc, "price": 0,
                     "stock": None}]
        except Exception as exc:
            hits = [{"name": "search failed: %s" % type(exc).__name__, "price": 0,
                     "stock": None}]
        hits = hits[:4]
        if label == "Telemart":
            # One extra request per kept item, to turn "not stated" into an answer.
            for hit in hits:
                if hit.get("url") and hit["stock"] is None:
                    hit["stock"] = telemart_stock(hit["url"])
        result["shops"][label] = hits
    return result


def render(results):
    out = ["<!-- generated by code/ua_prices.py - do not edit by hand -->", ""]
    for res in results:
        part = res["part"]
        out.append("### %s\n" % part.get("name", part.get("query")))
        if "error" in res:
            out.append("**%s.** Saw: %s\n" % (res["error"], "; ".join(res.get("seen", []))))
            continue

        offers = res["offers"]
        if offers:
            cheapest = ", ".join("%s %d" % (o["shop"], o["price"]) for o in offers[:3])
            out.append("**Advertised across %d sellers: %d - %d.** Cheapest three: %s."
                       % (len(offers), offers[0]["price"], offers[-1]["price"], cheapest))
            out.append("Directory: [%s](%s)\n" % (res["product"]["title"], res["product"]["url"]))
        elif res.get("note"):
            out.append("_Directory: %s._\n" % res["note"])
        else:
            out.append("No seller listed on the directory.\n")

        out.append("| Read direct at | UAH | Their SKU name | Stock |")
        out.append("|---|---:|---|---|")
        for label, hits in res["shops"].items():
            if not hits:
                out.append("| %s | - | not found in their search | - |" % label)
            for hit in hits:
                stock = {True: "in stock", False: "no", None: "not stated"}[hit["stock"]]
                out.append("| %s | %s | %s | %s |"
                           % (label, hit["price"] or "-", hit["name"][:80], stock))
        out.append("")
    out.append("Rozetka, Comfy, КТС, MOYO and Citycom block or hide search from a plain")
    out.append("request. Check those in a browser by hand.")
    return "\n".join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("parts", help="JSON file of parts, or a query with --find")
    ap.add_argument("--find", action="store_true", help="list matching hotline products and stop")
    ap.add_argument("-o", "--out", help="write markdown here (default: stdout)")
    ap.add_argument("--json", help="also dump the raw result as JSON here")
    ap.add_argument("--cache", help="directory to cache fetched pages in, so a repeated "
                                    "run does not re-request what the shops already answered")
    args = ap.parse_args(argv)

    if args.cache:
        global CACHE_DIR
        CACHE_DIR = args.cache
        os.makedirs(CACHE_DIR, exist_ok=True)

    if args.find:
        for cand in hotline_search(args.parts):
            print("%7d - %-7d %-62s %s" % (cand["min"], cand["max"], cand["title"][:60], cand["url"]))
        return 0

    with open(args.parts, encoding="utf-8") as fh:
        parts = json.load(fh)

    results = []
    for part in parts:
        sys.stderr.write("... %s\n" % part.get("name", part.get("query")))
        sys.stderr.flush()
        try:
            results.append(check(part))
        except Exception as exc:
            results.append({"part": part, "error": "failed: %s: %s" % (type(exc).__name__, exc)})

    text = render(results)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text)
    else:
        print(text)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(results, fh, ensure_ascii=False, indent=1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
