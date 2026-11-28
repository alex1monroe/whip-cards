#!/usr/bin/env python3
"""Lean v5 tall STAT HERO card + small bars, plus a 16:9 wide sibling.
Shared by Nov 26 storm-outages and Iowa EPA cards.
Reuses /home/box/whip/templates/make_card_lean_v5.py (chrome, CSS, brand, footer); chip with no dot
(label yellow, category white). Facts per NOTES.md. Does not post."""
import importlib.util, json, sys
from pathlib import Path

OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else Path(__file__).resolve().parent
spec_ = importlib.util.spec_from_file_location("lean", "/home/box/whip/templates/make_card_lean_v5.py")
L = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(L)

def lockup_nodot(kicker):
    k = L.esc(kicker); first, _, rest = k.partition(" · ")
    rest_h = f'<span class="lk-rest">{rest}</span>' if rest else ""
    return f'<div class="lockup"><span class="lk-main">{first}</span>{rest_h}</div>'
L.lockup = lockup_nodot

def hero_stat(d, fmt):
    return (
        f'<div class="hero stat"><div class="stat">{L.mark(d["stat"])}</div>'
        f'<div class="statsub"><span class="bar"></span>{L.esc(d["stat_sub"])}</div></div>'
    )
L.hero_quote = hero_stat

def bars_html(d):
    vmax = max(b["value"] for b in d["bars"])
    rows = ""
    for i, b in enumerate(d["bars"]):
        pct = b["value"] / vmax * 100
        cls = " y" if i == 0 else ""
        note = f'<span>{L.esc(b["note"])}</span>' if b.get("note") else ""
        rows += (
            f'<div class="brow{cls}"><div class="blab">{L.esc(b["label"])}{note}</div>'
            f'<div class="btrack"><div class="bfill" style="width:{pct*0.66:.1f}%"></div>'
            f'<div class="bval">{L.esc(b["text"])}</div></div></div>'
        )
    return f'<div class="bars"><div class="btitle">{L.esc(d["bars_title"])}</div>{rows}</div>'

def extra(d, fmt):
    tall = fmt == "tall"
    d_head = d.get("headline_px", 56) if tall else d.get("headline_px_wide", 50)
    d_stat = d.get("stat_px", 300) if tall else d.get("stat_px_wide", 300)
    bars_max = "1076px" if tall else "none"
    css = f"""
.headline{{font-size:{d_head}px;max-width:none;margin-top:{34 if tall else 20}px}}
.hero.stat{{margin-top:{40 if tall else 0}px}}
.stat{{font-family:'Anton',sans-serif;font-size:{d_stat}px;line-height:.92;color:{L.YEL};letter-spacing:-.005em;margin-left:-6px}}
.statsub{{display:flex;align-items:center;gap:20px;margin-top:{22 if tall else 16}px;font-family:'Inter',sans-serif;font-weight:800;font-size:{46 if tall else 32}px;line-height:1.1;color:{L.PAPER}}}
.bar{{width:64px;height:8px;background:{L.YEL};flex:0 0 64px}}
.bars{{margin-top:{56 if tall else 0}px;max-width:{bars_max};border-top:{'2px solid #2a2d2b' if tall else 'none'};padding-top:{30 if tall else 0}px}}
.btitle{{font-family:'Archivo Black',sans-serif;font-size:{24 if tall else 22}px;letter-spacing:.14em;text-transform:uppercase;color:{L.MUTE};margin-bottom:{24 if tall else 18}px}}
.brow{{display:flex;align-items:center;gap:28px;margin-bottom:{18 if tall else 14}px}}
.brow:last-child{{margin-bottom:0}}
.blab{{flex:0 0 {300 if tall else 240}px;font-family:'Inter',sans-serif;font-weight:800;font-size:{36 if tall else 32}px;line-height:1.1;color:#cfcbc1}}
.blab span{{display:block;font-weight:600;font-size:{26 if tall else 24}px;color:{L.MUTE};margin-top:4px;text-transform:lowercase}}
.brow.y .blab{{color:{L.PAPER}}}
.btrack{{flex:1;padding-right:20px;display:flex;align-items:center;gap:22px}}
.bfill{{height:{68 if tall else 56}px;background:{L.PAPER};opacity:.5}}
.brow.y .bfill{{background:{L.YEL};opacity:1}}
.bval{{font-family:'Anton',sans-serif;font-size:{72 if tall else 60}px;line-height:1;color:{L.PAPER};white-space:nowrap}}
.brow.y .bval{{color:{L.YEL}}}
"""
    if not tall:
        css += """
.page{bottom:118px}
.spacer{display:none;flex:none}
.mid{display:flex;align-items:center;gap:72px;flex:1;min-height:0;margin-top:8px;margin-bottom:16px}
.mid .hero.stat{margin-top:0;flex:0 0 620px;max-width:620px}
.mid .statsub{margin-top:16px}
.mid .bars{flex:1;margin-top:0;max-width:none;border-top:none;padding-top:0}
.other{margin-top:0}
"""
    return css

def build(d, fmt):
    h = L.build({**d, "layout": "quote", "quote": "", "attribution": ""}, fmt)
    rows = bars_html(d)
    if fmt == "tall":
        h = h.replace('<div class="spacer"></div>', rows + '<div class="spacer"></div>', 1)
    else:
        h = h.replace('<div class="hero stat">', '<div class="mid"><div class="hero stat">', 1)
        h = h.replace(
            '</div>\n  <div class="spacer"></div>',
            '</div>' + rows + '</div><div class="spacer"></div>',
            1,
        )
        if 'class="mid"' in h and 'class="bars"' not in h:
            h = h.replace('<div class="spacer"></div>', '</div>' + rows + '<div class="spacer"></div>', 1)
    return h.replace("</style>", extra(d, fmt) + "</style>", 1)

def words(d):
    parts = [d["kicker"], d["headline"], d["stat"], d["stat_sub"], d["bars_title"], d.get("other_side")]
    parts += [x for b in d["bars"] for x in (b["label"], b.get("note"), b["text"])]
    return sum(L.words(p) for p in parts if p)

if __name__ == "__main__":
    d = json.loads((OUT / "card.json").read_text())
    wc = words(d)
    if "--debug" in sys.argv:
        Path("/tmp/card-wide.html").write_text(build(d, "wide"))
        Path("/tmp/card-tall.html").write_text(build(d, "tall"))
        print("wrote /tmp/card-wide.html /tmp/card-tall.html")
    print(L.chrome(build(d, "tall"), OUT / "card.png", *L.SIZES["tall"]))
    print(L.chrome(build(d, "wide"), OUT / "card-16x9.png", *L.SIZES["wide"]))
    print("words (excl. brand/date/source/footer):", wc)
