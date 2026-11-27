#!/usr/bin/env python3
"""NEW card (lean v5, tall, KEY-STAT HERO, two stacked roles): a consortium that includes the U.S. DFC agreed
Nov 25, 2026 to buy Lukoil International; Treasury's OFAC must approve. BIDDER (DFC) + REGULATOR (Treasury).
Other side: DFC official to Reuters. Reuses /home/box/whip/templates/make_card_lean_v5.py (chrome, CSS, brand,
footer); chip with no dot (label yellow, category white). Facts per sources.md. No Whip data. Does not post."""
import importlib.util, json, sys
from pathlib import Path

OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent
spec_ = importlib.util.spec_from_file_location("lean", "/home/box/whip/templates/make_card_lean_v5.py")
L = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(L)

def lockup_nodot(kicker):
    k = L.esc(kicker); first, _, rest = k.partition(" · ")
    rest_h = f'<span class="lk-rest">{rest}</span>' if rest else ""
    return f'<div class="lockup"><span class="lk-main">{first}</span>{rest_h}</div>'
L.lockup = lockup_nodot

def hero_roles(d, fmt):
    rows = ""
    for i, r in enumerate(d["roles"]):
        cls = " y" if r["color"] == "yellow" else ""
        plus = '<div class="plus">+</div>' if i else ""
        rows += f'''{plus}<div class="role{cls}"><div class="rbig">{L.esc(r["big"])}</div>
  <div class="rsub"><span class="bar"></span>{L.mark(r["sub"])}</div></div>'''
    return f'<div class="hero roles">{rows}</div>'
L.hero_quote = hero_roles

def extra(d):
    return f"""
.headline{{font-size:{d.get('headline_px',56)}px;max-width:1040px}}
.hero.roles{{margin-top:48px}}
.role{{}}
.rbig{{font-family:'Anton',sans-serif;font-size:{d.get('big_px',250)}px;line-height:.9;color:{L.PAPER};letter-spacing:-.005em;margin-left:-6px}}
.role.y .rbig{{color:{L.YEL}}}
.rsub{{display:flex;align-items:center;gap:20px;margin-top:20px;font-family:'Inter',sans-serif;font-weight:800;font-size:42px;line-height:1.12;color:{L.PAPER};max-width:1076px}}
.plus{{font-family:'Anton',sans-serif;font-size:120px;line-height:1;color:{L.MUTE};margin:22px 0 8px -2px}}
"""

def build(d, fmt):
    h = L.build({**d, "layout": "quote", "quote": "", "attribution": ""}, fmt)
    return h.replace("</style>", extra(d) + "</style>", 1)

def words(d):
    parts = [d["kicker"], d["headline"], d.get("other_side")] + [x for r in d["roles"] for x in (r["big"], r["sub"])]
    return sum(L.words(p) for p in parts if p)

if __name__ == "__main__":
    d = json.loads((OUT / "card.json").read_text())
    print(L.chrome(build(d, "tall"), OUT / "card.png", *L.SIZES["tall"]))
    print("words (excl. brand/date/source/footer):", words(d))
