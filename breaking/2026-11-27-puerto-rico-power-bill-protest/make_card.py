#!/usr/bin/env python3
"""Lean v5 BREAKING card: thousands protest Puerto Rico power bills / cost of living (AP, EFE, Nov 27, 2026).
Adapted from ../2026-11-27-air-force-cloud-one-update/make_card.py. Hero = two bars: Puerto Rico vs U.S. average
residential electricity price, cents/kWh, September 2026 (EIA Form 861M, preliminary). Tall card.png (1220x1546 @2x)
+ card-16x9.png (1920x1080). Does not post or schedule anything."""
import importlib.util, json, sys
from pathlib import Path

OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else Path(__file__).resolve().parent
spec_ = importlib.util.spec_from_file_location("lean", "/home/box/whip/templates/make_card_lean_v5.py")
L = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(L)
YEL, RED, PAPER, MUTE, INK = L.YEL, L.RED, L.PAPER, L.MUTE, L.INK

def lockup_breaking(d):
    k = L.esc(d["kicker"]); first, _, rest = k.partition(" · ")
    return (f'<div class="tagrow"><span class="brk">{L.esc(d["breaking"])}</span>'
            f'<div class="lockup"><span class="lk-main">{first}</span><span class="lk-rest">{rest}</span></div></div>')

def chart(d, fmt):
    tall = fmt == "tall"
    mx = max(b["value"] for b in d["bars"])
    rows = ""
    for b in d["bars"]:
        pct = b["value"] / mx * 100
        cls = "bar hot" if b.get("hot") else "bar"
        rows += (f'<div class="brow"><div class="blab">{L.esc(b["label"])}</div>'
                 f'<div class="btrack"><div class="{cls}" style="width:{pct:.1f}%"><span class="bval">{b["value"]:.2f}¢</span></div></div></div>')
    return (f'<div class="chart {fmt}"><div class="ctitle">{L.esc(d["chart_title"])}</div>{rows}'
            f'<div class="cnote">{L.esc(d["chart_note"])}</div></div>')

def means(d):
    return f'<div class="means"><div class="mlab">What this<br>means</div><div class="mtxt">{L.esc(d["means"])}</div></div>'

def extra(fmt):
    tall = fmt == "tall"
    return f"""
.tagrow{{display:flex;align-items:stretch;gap:16px}}
.brk{{display:inline-flex;align-items:center;background:{RED};color:#fff;font-family:'Archivo Black',sans-serif;font-size:30px;letter-spacing:.14em;line-height:1;padding:12px 20px 11px}}
.headline{{font-size:{66 if tall else 66}px;white-space:nowrap;margin-top:{30 if tall else 22}px;max-width:none}}
.lockup{{white-space:nowrap;{'font-size:26px;' if tall else ''}}}
.tagrow .brk{{{'font-size:26px;' if tall else ''}white-space:nowrap}}
.headline{{white-space:normal;max-width:{1100 if tall else 1800}px}}
.chart{{margin-top:{64 if tall else 34}px;background:#141917;border:3px solid #3a403c;padding:{'56px 44px 44px' if tall else '30px 36px 24px'}}}
.ctitle{{font-family:'Archivo Black',sans-serif;font-size:{28 if tall else 26}px;letter-spacing:.12em;color:#bdb9af;text-transform:uppercase;line-height:1}}
.brow{{display:flex;flex-direction:{'column' if tall else 'row'};align-items:{'stretch' if tall else 'center'};gap:{14 if tall else 26}px;margin-top:{56 if tall else 24}px}}
.blab{{font-family:'Inter',sans-serif;font-weight:800;font-size:{54 if tall else 40}px;color:{PAPER};line-height:1;{'' if tall else 'flex:0 0 260px;'}}}
.btrack{{flex:1;height:{170 if tall else 96}px;background:#0d100f}}
.bar{{height:100%;background:#6a706c;display:flex;align-items:center;justify-content:flex-end;box-sizing:border-box;padding-right:28px}}
.bar.hot{{background:{YEL}}}
.bval{{font-family:'Anton',sans-serif;font-size:{110 if tall else 64}px;line-height:1;color:{INK}}}
.cnote{{font-family:'Inter',sans-serif;font-weight:600;font-size:{26 if tall else 22}px;color:#8f948f;margin-top:{26 if tall else 16}px}}
.means{{display:flex;align-items:center;gap:28px;margin-top:{64 if tall else 40}px;border-top:4px solid {YEL};padding-top:{22 if tall else 16}px}}
.mlab{{font-family:'Anton',sans-serif;font-size:{40 if tall else 36}px;line-height:.95;color:{YEL};text-transform:uppercase;flex:0 0 auto}}
.mtxt{{font-family:'Inter',sans-serif;font-weight:700;font-size:{42 if tall else 40}px;line-height:1.15;color:{PAPER}}}
.other{{margin-top:{0 if tall else 18}px}}
"""

def build(d, fmt):
    h = L.build({**d, "layout": "quote", "quote": "", "attribution": "", "art": "none"}, fmt)
    start = h.index('<div class="hero quote">'); end = h.index('<div class="spacer"></div>')
    body = chart(d, fmt) + ("" if fmt == "tall" else means(d))
    h = h[:start] + body + "\n  " + h[end:]
    if fmt == "tall":
        h = h.replace('<div class="spacer"></div>', means(d) + '<div class="spacer"></div>', 1)
    h = h.replace(L.lockup(d["kicker"]), lockup_breaking(d), 1)
    return h.replace("</style>", extra(fmt) + "</style>", 1)

def words(d):
    parts = [d["breaking"], d["kicker"], d["headline"], d["means"], d["other_side"]]
    parts += [d["chart_title"], d["chart_note"]] + [b["label"] + " " + f'{b["value"]:.2f}' for b in d["bars"]]
    return sum(L.words(p) for p in parts if p)

if __name__ == "__main__":
    from PIL import Image
    d = json.loads((OUT / "card.json").read_text())
    if "--debug" in sys.argv:
        Path("/tmp/prpower-tall.html").write_text(build(d, "tall")); Path("/tmp/prpower-wide.html").write_text(build(d, "wide"))
    print(L.chrome(build(d, "tall"), OUT / "card.png", *L.SIZES["tall"]))
    wide = L.chrome(build(d, "wide"), OUT / "card-16x9.png", *L.SIZES["wide"])
    im = Image.open(wide)
    if im.size != (1920, 1080):
        im.convert("RGB").resize((1920, 1080), Image.LANCZOS).save(wide, optimize=True)
    print(wide)
    wc = words(d)
    print("words (excl. brand/date/source/footer):", wc)
    if wc > 40:
        sys.exit(f"word count {wc} exceeds 40")
