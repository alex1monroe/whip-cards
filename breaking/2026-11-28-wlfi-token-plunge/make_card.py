#!/usr/bin/env python3
"""Lean v5 BREAKING card: Trump family-backed WLFI token falls ~50% overnight (Reuters, Nov 28, 2026).
Adapted from ../2026-11-28-america-save-act/make_card.py (no-dot chip, lean v5 chrome) and
../2026-11-27-puerto-rico-power-bill-protest/make_card.py (BREAKING tag, two-bar hero, What-this-means strip).
Hero = two bars: WLFI price ~$0.039 (Nov 27) -> ~$0.018 (Nov 28 morning), per Reuters. Two-line other side
(World Liberty; Binance). Renders card.png (2440x3092) + card-16x9.png (3840x2160). Does not post or schedule."""
import importlib.util, json, sys
from pathlib import Path

OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else Path(__file__).resolve().parent
spec_ = importlib.util.spec_from_file_location("lean", "/home/box/whip/templates/make_card_lean_v5.py")
L = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(L)
YEL, RED, PAPER, MUTE, INK = L.YEL, L.RED, L.PAPER, L.MUTE, L.INK

def lockup_breaking(d):
    # BREAKING tag + two-tone chip (label yellow, category white), no dot
    k = L.esc(d["kicker"]); first, _, rest = k.partition(" · ")
    return (f'<div class="tagrow"><span class="brk">{L.esc(d["breaking"])}</span>'
            f'<div class="lockup"><span class="lk-main">{first}</span><span class="lk-rest">{rest}</span></div></div>')

def chart(d, fmt):
    mx = max(b["value"] for b in d["bars"])
    rows = ""
    for b in d["bars"]:
        pct = b["value"] / mx * 100
        cls = "bar hot" if b.get("hot") else "bar"
        rows += (f'<div class="brow"><div class="blab">{L.esc(b["label"])}</div>'
                 f'<div class="btrack"><div class="{cls}" style="width:{pct:.1f}%"><span class="bval">{L.esc(b["text"])}</span></div></div></div>')
    return f'<div class="chart {fmt}"><div class="ctitle">{L.esc(d["chart_title"])}</div>{rows}</div>'

def means(d, fmt):
    # "|" = forced line break on the 4:5 card only (avoids an orphaned "2025.")
    txt = L.esc(d["means"]).replace("|", "<br>" if fmt == "tall" else " ")
    return f'<div class="means"><div class="mlab">What this<br>means</div><div class="mtxt">{txt}</div></div>'

def other_lines(d):
    out = ""
    for s in d["other_side"]:
        lab, _, rest = s.partition(":")
        out += f'<div class="oline"><b>{L.esc(lab)}:</b> {L.esc(rest.strip())}</div>'
    return f'<div class="other">{out}</div>'

def extra(fmt):
    tall = fmt == "tall"
    return f"""
.tagrow{{display:flex;align-items:stretch;gap:16px}}
.brk{{display:inline-flex;align-items:center;background:{RED};color:#fff;font-family:'Archivo Black',sans-serif;font-size:{26 if tall else 30}px;letter-spacing:.14em;line-height:1;padding:12px 20px 11px;white-space:nowrap}}
.lockup{{white-space:nowrap;{'font-size:26px;' if tall else ''}}}
.headline{{font-size:{66 if tall else 60}px;white-space:normal;margin-top:{30 if tall else 22}px;max-width:{1100 if tall else 1800}px}}
.chart{{margin-top:{56 if tall else 30}px;background:#141917;border:3px solid #3a403c;padding:{'48px 44px 52px' if tall else '28px 36px 30px'}}}
.ctitle{{font-family:'Archivo Black',sans-serif;font-size:{28 if tall else 26}px;letter-spacing:.12em;color:#bdb9af;text-transform:uppercase;line-height:1}}
.brow{{display:flex;flex-direction:{'column' if tall else 'row'};align-items:{'stretch' if tall else 'center'};gap:{14 if tall else 26}px;margin-top:{48 if tall else 24}px}}
.blab{{font-family:'Inter',sans-serif;font-weight:800;font-size:{54 if tall else 40}px;color:{PAPER};line-height:1;{'' if tall else 'flex:0 0 280px;'}}}
.btrack{{flex:1;height:{170 if tall else 100}px;background:#0d100f}}
.bar{{height:100%;background:#6a706c;display:flex;align-items:center;justify-content:flex-end;box-sizing:border-box;padding-right:28px}}
.bar.hot{{background:{YEL}}}
.bval{{font-family:'Anton',sans-serif;font-size:{110 if tall else 74}px;line-height:1;color:{INK};white-space:nowrap}}
.means{{display:flex;align-items:center;gap:28px;margin-top:{56 if tall else 34}px;border-top:4px solid {YEL};padding-top:{22 if tall else 16}px}}
.mlab{{font-family:'Anton',sans-serif;font-size:{40 if tall else 36}px;line-height:.95;color:{YEL};text-transform:uppercase;flex:0 0 auto}}
.mtxt{{font-family:'Inter',sans-serif;font-weight:700;font-size:{42 if tall else 40}px;line-height:1.15;color:{PAPER}}}
.other{{margin-top:{0 if tall else 26}px}}
.oline + .oline{{margin-top:6px}}
"""

def build(d, fmt):
    h = L.build({**d, "layout": "quote", "quote": "", "attribution": "", "art": "none", "other_side": "X"}, fmt)
    start = h.index('<div class="hero quote">'); end = h.index('<div class="spacer"></div>')
    body = chart(d, fmt) + ("" if fmt == "tall" else means(d, fmt))
    h = h[:start] + body + "\n  " + h[end:]
    if fmt == "tall":
        h = h.replace('<div class="spacer"></div>', means(d, fmt) + '<div class="spacer"></div>', 1)
    h = h.replace(L.lockup(d["kicker"]), lockup_breaking(d), 1)
    h = h.replace('<div class="other other">X</div>', other_lines(d), 1)
    assert 'class="oline"' in h and 'class="tagrow"' in h
    return h.replace("</style>", extra(fmt) + "</style>", 1)

def words(d):
    parts = [d["breaking"], d["kicker"], d["headline"], d["chart_title"], d["means"].replace("|", " ")] + d["other_side"]
    parts += [b["label"] + " " + b["text"] for b in d["bars"]]
    return sum(L.words(p) for p in parts if p)

if __name__ == "__main__":
    d = json.loads((OUT / "card.json").read_text())
    if "--debug" in sys.argv:
        Path("/tmp/wlfi-tall.html").write_text(build(d, "tall")); Path("/tmp/wlfi-wide.html").write_text(build(d, "wide"))
    print(L.chrome(build(d, "tall"), OUT / "card.png", *L.SIZES["tall"]))
    print(L.chrome(build(d, "wide"), OUT / "card-16x9.png", *L.SIZES["wide"]))
    wc = words(d)
    print("words (excl. brand/date/source/footer):", wc)
    if wc > 40:
        sys.exit(f"word count {wc} exceeds 40")
