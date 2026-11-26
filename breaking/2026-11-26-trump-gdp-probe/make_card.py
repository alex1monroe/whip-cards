#!/usr/bin/env python3
"""BREAKING card (lean v5, tall, QUOTE HERO): Trump on Truth Social (Thanksgiving, Nov 26, 2026) calls for an
immediate investigation after BEA's second estimate (Nov 25) revised Q3 2026 real GDP growth to 4.3% from the
3.4% advance estimate (Oct 29). Verbatim quote per Truth Social post / Reuters / Washington Times / Axios.
BEA other side per its Nov 25 release technical notes (software investment, consumer spending, updated source data).
Reuses /home/box/whip/templates/make_card_lean_v5.py (chrome, CSS, brand, footer, quote hero); adds a small
two-bar revision visual under the quote; lockup chip with no dot (label yellow, category white). No Whip data.
Does not post."""
import importlib.util, json
from pathlib import Path

OUT = Path(__file__).resolve().parent
spec_ = importlib.util.spec_from_file_location("lean", "/home/box/whip/templates/make_card_lean_v5.py")
L = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(L)

def lockup_nodot(kicker):
    k = L.esc(kicker); first, _, rest = k.partition(" · ")
    rest_h = f'<span class="lk-rest">{rest}</span>' if rest else ""
    return f'<div class="lockup"><span class="lk-main">{first}</span>{rest_h}</div>'
L.lockup = lockup_nodot

def bars_html(d):
    vmax = max(b["value"] for b in d["bars"])
    rows = ""
    for b in d["bars"]:
        pct = b["value"] / vmax * 100
        cls = " y" if b["color"] == "yellow" else ""
        rows += f'''<div class="brow{cls}"><div class="blab">{L.esc(b["label"])}<span>{L.esc(b["date"])}</span></div>
  <div class="btrack"><div class="bfill" style="width:{pct*0.70:.1f}%"></div><div class="bval">{b["value"]:.1f}%</div></div></div>'''
    return f'<div class="bars"><div class="btitle">{L.esc(d["bars_title"])}</div>{rows}</div>'

EXTRA = f"""
.headline{{font-size:52px}}
.hero.quote{{margin-top:44px}}
.qtext{{font-size:116px;line-height:1.0}}
.qmark{{font-size:300px;height:84px}}
.attr{{margin-top:30px}}
.bars{{margin-top:48px;max-width:1076px;border-top:2px solid #2a2d2b;padding-top:30px}}
.btitle{{font-family:'Archivo Black',sans-serif;font-size:24px;letter-spacing:.14em;text-transform:uppercase;color:{L.MUTE};margin-bottom:24px}}
.brow{{display:flex;align-items:center;gap:28px;margin-bottom:20px}}
.brow:last-child{{margin-bottom:0}}
.blab{{flex:0 0 270px;font-family:'Inter',sans-serif;font-weight:800;font-size:32px;line-height:1.1;color:#cfcbc1}}
.blab span{{display:block;font-weight:600;font-size:28px;color:{L.MUTE};margin-top:4px}}
.brow.y .blab{{color:{L.PAPER}}}
.btrack{{flex:1;padding-right:20px;display:flex;align-items:center;gap:22px}}
.bfill{{height:76px;background:{L.PAPER};opacity:.5}}
.brow.y .bfill{{background:{L.YEL};opacity:1}}
.bval{{font-family:'Anton',sans-serif;font-size:84px;line-height:1;color:{L.PAPER};white-space:nowrap}}
.brow.y .bval{{color:{L.YEL}}}
"""

def build(d, fmt):
    h = L.build({**d, "layout": "quote"}, fmt)
    h = h.replace('<div class="spacer"></div>', bars_html(d) + '<div class="spacer"></div>', 1)
    return h.replace("</style>", EXTRA + "</style>", 1)

def words(d):
    parts = [d["kicker"], d["headline"], d["quote"], d["attribution"], d["bars_title"], d.get("other_side")]
    parts += [x for b in d["bars"] for x in (b["label"], b["date"], f'{b["value"]}%')]
    return sum(L.words(p) for p in parts if p)

if __name__ == "__main__":
    d = json.loads((OUT / "card.json").read_text())
    print(L.chrome(build(d, "tall"), OUT / "card.png", *L.SIZES["tall"]))
    print("words (excl. brand/date/source/footer):", words(d))
