#!/usr/bin/env python3
"""BREAKING card (lean v5, tall): SpaceX pledges 1 newly issued Class A share to every currently
active Trump Account; Musk personally matches (Nov 25, 2026). Timing per Musk's X post (via CNBC,
Business Insider): SpaceX share next month (Dec 2026), Musk's share when his lockup expires June 2027.
Sell rule per Treasury guidance via CNBC. Sources: SpaceX IR, CNBC, Reuters. No Whip data. Does not post.
Reuses /home/box/whip/templates/make_card_lean_v5.py (chrome, CSS, brand, footer); custom share-tiles hero;
lockup chip with no dot (label yellow, category white)."""
import importlib.util, json, sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
spec_ = importlib.util.spec_from_file_location("lean", "/home/box/whip/templates/make_card_lean_v5.py")
L = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(L)

def lockup_nodot(kicker):
    k = L.esc(kicker); first, _, rest = k.partition(" · ")
    rest_h = f'<span class="lk-rest">{rest}</span>' if rest else ""
    return f'<div class="lockup"><span class="lk-main">{first}</span>{rest_h}</div>'
L.lockup = lockup_nodot

def share_icon():
    # stylized stock certificate: not a logo, not a screenshot
    return f'''<svg viewBox="0 0 120 150" class="cert" aria-hidden="true">
<rect x="6" y="6" width="108" height="138" rx="10" fill="none" stroke="{L.PAPER}" stroke-width="8"/>
<rect x="24" y="30" width="72" height="10" rx="5" fill="{L.PAPER}" opacity=".55"/>
<rect x="24" y="52" width="52" height="10" rx="5" fill="{L.PAPER}" opacity=".35"/>
<circle cx="60" cy="104" r="22" fill="{L.YEL}"/></svg>'''

def hero_tiles(d, fmt):
    tiles = "".join(
        f'''<div class="tile{' t2' if i else ''}">{share_icon()}
  <div class="tt"><div class="n">1 SHARE</div><div class="who">{L.esc(t["who"])}</div>
  <div class="when">{L.mark(t["when"])}</div></div></div>''' + ('<div class="plus">+</div>' if i == 0 else '')
        for i, t in enumerate(d["tiles"]))
    return f'<div class="hero tiles">{tiles}</div>' + (f'<div class="eq">{L.mark(d["eq"])}</div>' if d.get("eq") else "") + ''

EXTRA = f"""
.hero.tiles{{display:flex;flex-direction:column;gap:0;margin-top:56px}}
.tile{{display:flex;align-items:center;gap:40px;background:rgba(244,240,230,.06);border-left:12px solid {L.PAPER};padding:40px 40px}}
.tile.t2{{border-left-color:{L.YEL}}}
.cert{{width:124px;flex:0 0 124px}}
.n{{font-family:'Anton',sans-serif;font-size:120px;line-height:.92;color:{L.PAPER}}}
.who{{font-family:'Inter',sans-serif;font-weight:800;font-size:44px;color:{L.PAPER};margin-top:6px}}
.when{{font-family:'Inter',sans-serif;font-weight:700;font-size:38px;color:#cfcbc1;margin-top:4px}}
.plus{{font-family:'Anton',sans-serif;font-size:80px;line-height:1;color:{L.YEL};padding:6px 0 6px 40px}}
.eq{{font-family:'Inter',sans-serif;font-weight:800;font-size:44px;color:{L.PAPER};margin-top:34px}}
.means{{font-family:'Archivo Black',sans-serif;font-size:26px;letter-spacing:.14em;color:{L.YEL};margin-bottom:14px}}
"""

def build(d, fmt):
    h = L.build({**d, "layout": "quote", "quote": "X", "attribution": "X"}, fmt)
    start = h.index('<div class="hero quote">'); end = h.index('<div class="spacer"></div>')
    h = h[:start] + hero_tiles(d, fmt) + "\n  " + h[end:]
    h = h.replace('<div class="spacer"></div>', '<div class="spacer"></div><div class="means">WHAT THIS MEANS</div>', 1)
    return h.replace("</style>", EXTRA + "</style>", 1)

def words(d):
    parts = [d["kicker"], d["headline"], d["eq"], d.get("finding"), d.get("other_side")]
    parts += [x for t in d["tiles"] for x in ("1 share", t["who"], t["when"])]
    return sum(L.words(p) for p in parts if p) + 3  # + "WHAT THIS MEANS"

if __name__ == "__main__":
    d = json.loads((OUT / "card.json").read_text())
    print(L.chrome(build(d, "tall"), OUT / "card.png", *L.SIZES["tall"]))
    print("words (excl. brand/date/source/footer):", words(d))
