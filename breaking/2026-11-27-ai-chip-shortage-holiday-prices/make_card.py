#!/usr/bin/env python3
"""Lean v5 tall STAT HERO + typographic holiday price-hike rows, plus a 16:9 wide sibling.
Reuses /home/box/whip/templates/make_card_lean_v5.py (chrome, CSS, brand, footer);
chip with no dot (label yellow, category white). Facts per NOTES.md. Does not post."""
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

def hero_stat(d, fmt):
    return f'''<div class="hero stat"><div class="stat">{L.mark(d["stat"])}</div>
  <div class="statsub"><span class="bar"></span>{L.esc(d["stat_sub"])}</div></div>'''
L.hero_quote = hero_stat

def rows_html(d):
    rows = ""
    for i, b in enumerate(d["bars"]):
        cls = " y" if i == 0 else ""
        note = f'<span>{L.esc(b["note"])}</span>' if b.get("note") else ""
        rows += (
            f'<div class="brow{cls}"><div class="blab">{L.esc(b["label"])}{note}</div>'
            f'<div class="bval">{L.esc(b["text"])}</div></div>'
        )
    title = f'<div class="btitle">{L.esc(d["bars_title"])}</div>' if d.get("bars_title") else ""
    return f'<div class="bars">{title}{rows}</div>'

def extra(d, fmt):
    tall = fmt == "tall"
    d_head = d.get("headline_px", 56) if tall else d.get("headline_px_wide", 46)
    d_stat = d.get("stat_px", 400) if tall else d.get("stat_px_wide", 228)
    return f"""
.headline{{font-size:{d_head}px;max-width:none;margin-top:{34 if tall else 20}px}}
.hero.stat{{margin-top:{36 if tall else 8}px}}
.stat{{font-family:'Anton',sans-serif;font-size:{d_stat}px;line-height:.9;color:{L.YEL};letter-spacing:-.005em;margin-left:-6px}}
.statsub{{display:flex;align-items:center;gap:20px;margin-top:{18 if tall else 10}px;font-family:'Inter',sans-serif;font-weight:800;font-size:{46 if tall else 32}px;line-height:1.1;color:{L.PAPER}}}
.bar{{width:64px;height:8px;background:{L.YEL};flex:0 0 64px}}
.bars{{margin-top:{44 if tall else 0}px;max-width:{1076 if tall else 980}px;border-top:2px solid #2a2d2b;padding-top:{8 if tall else 4}px}}
.btitle{{font-family:'Archivo Black',sans-serif;font-size:24px;letter-spacing:.14em;text-transform:uppercase;color:{L.MUTE};margin-bottom:16px}}
.brow{{display:flex;align-items:baseline;justify-content:space-between;gap:28px;padding:{26 if tall else 16}px 0;border-bottom:2px solid #2a2d2b}}
.brow:last-child{{border-bottom:none;padding-bottom:{10 if tall else 4}px}}
.blab{{font-family:'Inter',sans-serif;font-weight:800;font-size:{44 if tall else 34}px;line-height:1;color:#cfcbc1}}
.blab span{{display:block;font-weight:600;font-size:{26 if tall else 24}px;color:{L.MUTE};margin-top:6px;text-transform:none}}
.brow.y .blab{{color:{L.PAPER}}}
.bval{{font-family:'Anton',sans-serif;font-size:{80 if tall else 58}px;line-height:.9;color:{L.PAPER};white-space:nowrap}}
.brow.y .bval{{color:{L.YEL}}}
""" + ("" if tall else """
.page{bottom:118px}
.spacer{display:none;flex:none}
.mid{display:flex;align-items:center;gap:80px;flex:1;min-height:0;margin-top:8px;margin-bottom:12px}
.mid .hero.stat{margin-top:0;flex:0 0 640px;max-width:640px}
.mid .statsub{margin-top:16px}
.mid .bars{flex:1;margin-top:0;border-top:none;padding-top:0}
.other{margin-top:0}
""")

def build(d, fmt):
    h = L.build({**d, "layout": "quote", "quote": "", "attribution": ""}, fmt)
    rows = rows_html(d)
    if fmt == "tall":
        h = h.replace('<div class="spacer"></div>', rows + '<div class="spacer"></div>', 1)
    else:
        h = h.replace(
            '<div class="hero stat">',
            '<div class="mid"><div class="hero stat">',
            1,
        )
        # Close the hero, then place rows INSIDE mid before the spacer.
        h = h.replace(
            '</div>\n  <div class="spacer"></div>',
            '</div>' + rows + '</div><div class="spacer"></div>',
            1,
        )
        # Fallback if whitespace differs
        if 'class="mid"' in h and 'class="bars"' not in h:
            h = h.replace('<div class="spacer"></div>', '</div>' + rows + '<div class="spacer"></div>', 1)
    return h.replace("</style>", extra(d, fmt) + "</style>", 1)

def words(d):
    parts = [d["kicker"], d["headline"], d["stat"], d["stat_sub"], d.get("bars_title"), d.get("other_side")]
    parts += [x for b in d["bars"] for x in (b["label"], b.get("note"), b["text"])]
    return sum(L.words(p) for p in parts if p)

if __name__ == "__main__":
    d = json.loads((OUT / "card.json").read_text())
    wc = words(d)
    # debug HTML for wide if --debug
    if "--debug" in sys.argv:
        Path("/tmp/card-wide.html").write_text(build(d, "wide"))
        Path("/tmp/card-tall.html").write_text(build(d, "tall"))
        print("wrote /tmp/card-wide.html /tmp/card-tall.html")
    print(L.chrome(build(d, "tall"), OUT / "card.png", *L.SIZES["tall"]))
    print(L.chrome(build(d, "wide"), OUT / "card-16x9.png", *L.SIZES["wide"]))
    print("words (excl. brand/date/source/footer):", wc)
    if wc > 40:
        sys.exit(f"word count {wc} exceeds 40")
