#!/usr/bin/env python3
"""Lean v5 UPDATE card: Nvidia Blackwell gear at Shanghai site tied to Alice Huang (Bloomberg, Nov 27, 2026).
Tall portrait (card.png) + 16:9 (card-16x9.png). Reuses /home/box/whip/templates/make_card_lean_v5.py
(chrome, CSS, brand, footer). Red UPDATE tag + two-tone chip (label yellow, category white, no dot).
Hero = flow diagram: Nvidia Blackwell -> ? (route unknown) -> Shanghai data center linked to Alice Huang.
Short "What this means" strip, other side, source line, Whip illustration. Does not post or schedule anything."""
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

CHIP = ('<svg width="{s}" height="{s}" viewBox="0 0 64 64" aria-hidden="true"><rect x="14" y="14" width="36" height="36" rx="3" fill="none" stroke="{c}" stroke-width="5"/>'
        '<rect x="24" y="24" width="16" height="16" fill="{c}"/>'
        + "".join(f'<path d="M{x} 4v8M{x} 52v8M4 {x}h8M52 {x}h8" stroke="{{c}}" stroke-width="4"/>' for x in (22, 32, 42)) + '</svg>')
BLDG = ('<svg width="{s}" height="{s}" viewBox="0 0 64 64" aria-hidden="true"><rect x="8" y="10" width="48" height="46" rx="3" fill="none" stroke="{c}" stroke-width="5"/>'
        '<path d="M8 25h48M8 40h48" stroke="{c}" stroke-width="5"/><circle cx="18" cy="18" r="3" fill="{c}"/><circle cx="18" cy="33" r="3" fill="{c}"/><circle cx="18" cy="48" r="3" fill="{c}"/>'
        '<path d="M30 18h18M30 33h18M30 48h18" stroke="{c}" stroke-width="4"/></svg>')

def node(icon, label, note, x, y, w, h, hot, isz):
    col = YEL if hot else PAPER
    return (f'<div class="node{" hot" if hot else ""}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px">'
            f'{icon.replace("{c}", col).replace("{s}", str(isz))}<div class="ntxt"><div class="nlab">{L.esc(label)}</div>'
            f'<div class="nnote">{L.esc(note)}</div></div></div>')

def diagram(d, fmt):
    tall = fmt == "tall"
    if tall:
        W, Hh = 1076, 760; nw, nh = 1076, 190; r = 120
        a = (0, 0); b = (0, Hh - nh); cx, cy = W / 2, Hh / 2
        lines = (f'<path d="M{cx} {nh} L{cx} {Hh-nh}" stroke="{RED}" stroke-width="8" stroke-dasharray="4 20" stroke-linecap="round"/>'
                 f'<path d="M{cx-22} {Hh-nh-30} L{cx} {Hh-nh-4} L{cx+22} {Hh-nh-30}" fill="none" stroke="{RED}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>')
        hubx, huby = cx - r, cy - r
        sub = f'<div class="hubs side" style="left:{cx + r + 36}px;top:{cy - 44}px">{L.esc(d["hub_sub"]).replace(": ", ":<br><span>")}</span></div>'
    else:
        W, Hh = 1744, 400; nw, nh = 600, 230; r = 120
        a = (0, (Hh - nh) / 2); b = (W - nw, (Hh - nh) / 2); cx, cy = W / 2, (Hh - 20) / 2 + 10
        y = Hh / 2
        lines = (f'<path d="M{nw} {y} L{W-nw} {y}" stroke="{RED}" stroke-width="8" stroke-dasharray="4 20" stroke-linecap="round"/>'
                 f'<path d="M{W-nw-30} {y-22} L{W-nw-4} {y} L{W-nw-30} {y+22}" fill="none" stroke="{RED}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>')
        cy = y; hubx, huby = cx - r, cy - r - 24
        sub = f'<div class="hubs below" style="left:{cx-200}px;top:{huby + 2*r + 18}px;width:400px">{L.esc(d["hub_sub"]).replace(": ", ": <span>")}</span></div>'
    nodes = node(CHIP, d["from_label"], d["from_note"], a[0], a[1], nw, nh, False, 92 if tall else 84)
    nodes += node(BLDG, d["to_label"], d["to_note"], b[0], b[1], nw, nh, True, 92 if tall else 84)
    hub = f'<div class="hub" style="left:{hubx:.0f}px;top:{huby:.0f}px;width:{2*r}px;height:{2*r}px"><div class="hubt">{L.esc(d["hub"])}</div></div>'
    svg = f'<svg class="lines" width="{W}" height="{Hh}" viewBox="0 0 {W} {Hh}">{lines}</svg>'
    return f'<div class="diagram" style="width:{W}px;height:{Hh}px">{svg}{nodes}{hub}{sub}</div>'

def means(d):
    return f'<div class="means"><div class="mlab">What this<br>means</div><div class="mtxt">{L.esc(d["means"])}</div></div>'

def extra(fmt):
    tall = fmt == "tall"
    return f"""
.tagrow{{display:flex;align-items:stretch;gap:16px}}
.brk{{display:inline-flex;align-items:center;background:{RED};color:#fff;font-family:'Archivo Black',sans-serif;font-size:30px;letter-spacing:.14em;line-height:1;padding:12px 20px 11px}}
.headline{{font-size:{62 if tall else 66}px;white-space:nowrap;margin-top:{30 if tall else 22}px;max-width:none}}
.diagram{{position:relative;margin-top:{44 if tall else 34}px}}
.lines{{position:absolute;left:0;top:0}}
.node{{position:absolute;display:flex;align-items:center;gap:28px;background:#141917;border:3px solid #3a403c;padding:0 34px;box-sizing:border-box}}
.node svg{{flex:0 0 auto}}
.node.hot{{border:4px solid {YEL};background:#1c1a0c}}
.nlab{{font-family:'Inter',sans-serif;font-weight:800;font-size:{48 if tall else 44}px;line-height:1.05;color:{PAPER}}}
.nnote{{font-family:'Anton',sans-serif;font-size:{44 if tall else 40}px;line-height:1.05;color:{YEL};margin-top:10px}}
.node:not(.hot) .nnote{{color:#bdb9af}}
.hub{{position:absolute;border-radius:50%;background:radial-gradient(circle at 50% 40%,#3a0d0c 0%,#1a0807 70%);border:6px solid {RED};box-shadow:0 0 0 14px rgba(255,45,42,.16),0 0 60px rgba(255,45,42,.35);display:flex;align-items:center;justify-content:center;box-sizing:border-box}}
.hubt{{font-family:'Anton',sans-serif;font-size:150px;line-height:1;color:{PAPER}}}
.hubs{{position:absolute;font-family:'Archivo Black',sans-serif;font-size:{28 if tall else 26}px;letter-spacing:.12em;color:#bdb9af;line-height:1.25}}
.hubs span{{color:{RED}}}
.hubs.below{{text-align:center}}
.means{{display:flex;align-items:center;gap:28px;margin-top:{44 if tall else 26}px;border-top:4px solid {YEL};padding-top:{22 if tall else 16}px}}
.mlab{{font-family:'Anton',sans-serif;font-size:{40 if tall else 36}px;line-height:.95;color:{YEL};text-transform:uppercase;flex:0 0 auto}}
.mtxt{{font-family:'Inter',sans-serif;font-weight:700;font-size:{42 if tall else 40}px;line-height:1.15;color:{PAPER}}}
.other{{margin-top:{0 if tall else 14}px}}
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
    parts = [d["breaking"], d["kicker"], d["headline"], d["from_label"], d["from_note"], d["hub_sub"],
             d["to_label"], d["to_note"], d["means"], d["other_side"]]
    return sum(L.words(p) for p in parts if p)

if __name__ == "__main__":
    d = json.loads((OUT / "card.json").read_text())
    if "--debug" in sys.argv:
        Path("/tmp/nv-tall.html").write_text(build(d, "tall")); Path("/tmp/nv-wide.html").write_text(build(d, "wide"))
    print(L.chrome(build(d, "tall"), OUT / "card.png", *L.SIZES["tall"]))
    print(L.chrome(build(d, "wide"), OUT / "card-16x9.png", *L.SIZES["wide"]))
    wc = words(d)
    print("words (excl. brand/date/source/footer):", wc)
    if wc > 40:
        sys.exit(f"word count {wc} exceeds 40")
