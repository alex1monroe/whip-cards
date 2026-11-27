#!/usr/bin/env python3
"""Lean v5 BREAKING card: Air Force Cloud One breach (Reuters, Nov 27, 2026).
Tall portrait (card.png) + 16:9 (card-16x9.png). Reuses /home/box/whip/templates/make_card_lean_v5.py
(chrome, CSS, brand, footer). Red BREAKING tag + two-tone chip (label yellow, category white, no dot).
Hero = hub-and-spoke diagram: Cloud One -> systems it runs. Short "What this means" strip, other side,
Source: Reuters, Whip illustration. Does not post or schedule anything."""
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

ICONS = {
    "pay": '<rect x="6" y="16" width="52" height="34" rx="4" fill="none" stroke="{c}" stroke-width="5"/><circle cx="32" cy="33" r="8" fill="none" stroke="{c}" stroke-width="5"/>',
    "truck": '<rect x="4" y="16" width="34" height="26" fill="none" stroke="{c}" stroke-width="5"/><path d="M38 24h12l8 10v8H38z" fill="none" stroke="{c}" stroke-width="5" stroke-linejoin="round"/><circle cx="16" cy="48" r="6" fill="{c}"/><circle cx="48" cy="48" r="6" fill="{c}"/>',
    "radar": '<path d="M8 52 A28 28 0 0 1 56 52" fill="none" stroke="{c}" stroke-width="5"/><path d="M18 52 A16 16 0 0 1 46 52" fill="none" stroke="{c}" stroke-width="5"/><path d="M32 52 L50 18" stroke="{c}" stroke-width="5" stroke-linecap="round"/><circle cx="32" cy="52" r="5" fill="{c}"/>',
    "missile": '<path d="M32 4 C40 12 42 22 42 30 V48 H22 V30 C22 22 24 12 32 4Z" fill="none" stroke="{c}" stroke-width="5" stroke-linejoin="round"/><path d="M22 40 L12 54 H22 M42 40 L52 54 H42" fill="none" stroke="{c}" stroke-width="5" stroke-linejoin="round"/><path d="M27 54 h10" stroke="{c}" stroke-width="5"/>',
}

def icon(name, color, size):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 60" aria-hidden="true">{ICONS[name].replace("{c}", color)}</svg>'

CLOUD = ('<svg class="cloud" viewBox="0 0 120 80" aria-hidden="true"><path d="M30 70 H92 A22 22 0 0 0 92 26 '
         'A30 30 0 0 0 36 22 A24 24 0 0 0 30 70Z" fill="none" stroke="%s" stroke-width="7" stroke-linejoin="round"/>'
         '<path d="M58 30 L50 48 H64 L56 66" fill="none" stroke="%s" stroke-width="6" stroke-linejoin="round" stroke-linecap="round"/></svg>') % (PAPER, RED)

def diagram(d, fmt):
    tall = fmt == "tall"
    W, Hh = (1076, 720) if tall else (1744, 470)
    nw, nh = (440, 196) if tall else (560, 160)
    hub_r = 185 if tall else 165
    cx, cy = W / 2, Hh / 2
    pos = ([(0, 0), (W - nw, 0), (0, Hh - nh), (W - nw, Hh - nh)] if tall else
           [(0, 20), (0, Hh - nh - 20), (W - nw, 20), (W - nw, Hh - nh - 20)])
    lines, nodes = "", ""
    for (x, y), n in zip(pos, d["nodes"]):
        hot = n.get("hot")
        ex = x + nw if x == 0 else x
        ey = y + nh / 2
        col = YEL if hot else "#59605b"
        lines += f'<path d="M{cx:.0f} {cy:.0f} L{ex:.0f} {ey:.0f}" stroke="{col}" stroke-width="{8 if hot else 6}" stroke-dasharray="{"none" if hot else "2 16"}" stroke-linecap="round"/>'
        lines += f'<circle cx="{ex:.0f}" cy="{ey:.0f}" r="10" fill="{col}"/>'
        note = f'<div class="nnote">{L.esc(n["note"])}</div>' if n.get("note") else ""
        nodes += (f'<div class="node{" hot" if hot else ""}" style="left:{x}px;top:{y}px;width:{nw}px;height:{nh}px">'
                  f'{icon(n["icon"], YEL if hot else PAPER, 64 if tall else 58)}<div class="ntxt"><div class="nlab">{L.esc(n["label"])}</div>{note}</div></div>')
    hub = (f'<div class="hub" style="left:{cx-hub_r:.0f}px;top:{cy-hub_r:.0f}px;width:{hub_r*2}px;height:{hub_r*2}px">'
           f'{CLOUD}<div class="hubt">{L.esc(d["hub"])}</div><div class="hubs">{L.esc(d["hub_sub"])}</div></div>')
    svg = f'<svg class="lines" width="{W}" height="{Hh}" viewBox="0 0 {W} {Hh}">{lines}</svg>'
    return f'<div class="diagram" style="width:{W}px;height:{Hh}px">{svg}{nodes}{hub}</div>'

def means(d):
    return f'<div class="means"><div class="mlab">What this<br>means</div><div class="mtxt">{L.esc(d["means"])}</div></div>'

def extra(fmt):
    tall = fmt == "tall"
    return f"""
.tagrow{{display:flex;align-items:stretch;gap:16px}}
.brk{{display:inline-flex;align-items:center;background:{RED};color:#fff;font-family:'Archivo Black',sans-serif;font-size:30px;letter-spacing:.14em;line-height:1;padding:12px 20px 11px}}
.headline{{font-size:{62 if tall else 60}px;white-space:nowrap;margin-top:{30 if tall else 22}px;max-width:none}}
.diagram{{position:relative;margin-top:{50 if tall else 30}px}}
.lines{{position:absolute;left:0;top:0}}
.node{{position:absolute;display:flex;align-items:center;gap:22px;background:#141917;border:3px solid #3a403c;padding:0 26px}}
.node svg{{flex:0 0 auto}}
.node.hot{{border:4px solid {YEL};background:#1c1a0c}}
.nlab{{font-family:'Inter',sans-serif;font-weight:800;font-size:{40 if tall else 40}px;line-height:1.05;color:{PAPER}}}
.nnote{{font-family:'Anton',sans-serif;font-size:{48 if tall else 44}px;line-height:1;color:{YEL};margin-top:8px}}
.hub{{position:absolute;border-radius:50%;background:radial-gradient(circle at 50% 40%,#3a0d0c 0%,#1a0807 70%);border:6px solid {RED};box-shadow:0 0 0 14px rgba(255,45,42,.16),0 0 60px rgba(255,45,42,.35);display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}}
.cloud{{width:{120 if tall else 112}px;height:auto}}
.hubt{{font-family:'Anton',sans-serif;font-size:{64 if tall else 60}px;line-height:1;color:{PAPER};margin-top:6px}}
.hubs{{font-family:'Archivo Black',sans-serif;font-size:24px;letter-spacing:.16em;color:{RED};margin-top:8px}}
.means{{display:flex;align-items:center;gap:28px;margin-top:{48 if tall else 0}px;border-top:4px solid {YEL};padding-top:{22 if tall else 16}px}}
.mlab{{font-family:'Anton',sans-serif;font-size:{40 if tall else 36}px;line-height:.95;color:{YEL};text-transform:uppercase;flex:0 0 auto}}
.mtxt{{font-family:'Inter',sans-serif;font-weight:700;font-size:{42 if tall else 40}px;line-height:1.15;color:{PAPER}}}
.other{{margin-top:{0 if tall else 18}px}}
"""

def build(d, fmt):
    h = L.build({**d, "layout": "quote", "quote": "", "attribution": "", "art": "none"}, fmt)
    start = h.index('<div class="hero quote">'); end = h.index('<div class="spacer"></div>')
    body = diagram(d, fmt) + ("" if fmt == "tall" else means(d))
    h = h[:start] + body + "\n  " + h[end:]
    if fmt == "tall":
        h = h.replace('<div class="spacer"></div>', means(d) + '<div class="spacer"></div>', 1)
    h = h.replace(L.lockup(d["kicker"]), lockup_breaking(d), 1)
    return h.replace("</style>", extra(fmt) + "</style>", 1)

def words(d):
    parts = [d["breaking"], d["kicker"], d["headline"], d["hub"], d["hub_sub"], d["means"], d["other_side"]]
    parts += [x for n in d["nodes"] for x in (n["label"], n.get("note"))]
    return sum(L.words(p) for p in parts if p)

if __name__ == "__main__":
    d = json.loads((OUT / "card.json").read_text())
    if "--debug" in sys.argv:
        Path("/tmp/cloudone-tall.html").write_text(build(d, "tall")); Path("/tmp/cloudone-wide.html").write_text(build(d, "wide"))
    print(L.chrome(build(d, "tall"), OUT / "card.png", *L.SIZES["tall"]))
    print(L.chrome(build(d, "wide"), OUT / "card-16x9.png", *L.SIZES["wide"]))
    wc = words(d)
    print("words (excl. brand/date/source/footer):", wc)
    if wc > 40:
        sys.exit(f"word count {wc} exceeds 40")
