#!/usr/bin/env python3
"""BREAKING card (TALL v4, 2440x3092): Judge upholds NYC two-year rent freeze (Nov. 25, 2026).
Sources: Gothamist (1:49 p.m. ET); The New York Times; New York Post (2:34 p.m. ET).
Uses /home/box/whip/templates/make_card_tall_v4.py unchanged, adding a local "stat_timeline"
graphic: a big single-stat row, a short 3-beat timeline with a NEW badge, and two attributed
quotes. No Whip scores, % moves or heat meters. Whip illustration. Does not post or schedule.
"""
import html
import importlib.util
import json
import shutil
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
TEMPLATE = Path("/home/box/whip/templates/make_card_tall_v4.py")
FOLDER = "breaking/2026-11-25-nyc-rent-freeze"
FILES = ("card.png", "card.json", "make_card.py", "alt.txt")

spec = importlib.util.spec_from_file_location("tall_v4", TEMPLATE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
E = html.escape

CSS = f"""
.stats{{display:grid;grid-template-columns:1.35fr 1fr;gap:14px;margin-bottom:12px}}
.stat{{background:#14141a;border-left:6px solid {T.YEL};padding:12px 18px 14px}}
.stat.b2{{border-left-color:{T.GRN}}}
.sv{{font-family:'Anton',sans-serif;font-size:118px;line-height:.95;color:{T.YEL}}}
.stat.b2 .sv{{color:{T.PAPER}}}
.sl{{font-family:'Inter',sans-serif;font-size:24px;font-weight:700;line-height:1.2;color:#d8d4ca;margin-top:6px}}
.node{{grid-template-columns:200px 32px 1fr;gap:2px 14px}}
.date{{font-size:40px}}
.line{{font-size:26px;line-height:1.22}}
.ev{{grid-template-columns:0 1fr;gap:0}}
.iconwrap{{width:0}}
.node.new .date{{color:{T.YEL}}}
.node.new .dot{{background:{T.YEL};width:24px;height:24px;box-shadow:0 0 0 3px {T.INK},0 0 0 6px rgba(255,204,0,.35)}}
.node.new .ev{{background:rgba(255,204,0,.08);border-left:4px solid {T.YEL};padding:8px 12px}}
.newb{{display:inline-block;background:{T.RED};color:{T.PAPER};font-family:'Archivo Black',sans-serif;font-size:14px;letter-spacing:.16em;padding:3px 7px 2px;line-height:1;margin-top:4px}}
.dcol{{display:flex;flex-direction:column;align-items:flex-end}}
.nodes .node:last-child .rail::before{{bottom:50%}}
.quotes{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:10px}}
.qbox{{background:#14141a;border-left:4px solid {T.YEL};padding:10px 14px 11px}}
.qbox.g{{border-left-color:{T.GRN}}}
.qh{{font-family:'Archivo Black',sans-serif;font-size:14px;letter-spacing:.16em;color:#a8a49a;margin-bottom:5px}}
.qt{{font-family:'Inter',sans-serif;font-size:20px;font-weight:600;font-style:italic;line-height:1.28;color:{T.PAPER}}}
.qa{{font-family:'Inter',sans-serif;font-size:15px;font-weight:700;color:#a8a49a;margin-top:6px}}
.panel{{padding:12px 18px 12px}}
.strip{{padding:14px 20px 14px;margin-top:12px}}
.means{{gap:9px}}
.b{{font-size:21px;line-height:1.22}}
"""


def render(g: dict) -> str:
    stats = "".join(
        f'<div class="stat{" b2" if i else ""}"><div class="sv">{E(s["value"])}</div><div class="sl">{E(s["label"])}</div></div>'
        for i, s in enumerate(g.get("stats") or [])
    )
    rows = []
    for n in g.get("nodes") or []:
        kl = "node " + (n.get("dot") or "blue") + (" new" if n.get("new") else "")
        badge = '<span class="newb">NEW</span>' if n.get("new") else ""
        rows.append(
            f'<div class="{kl}"><div class="dcol"><div class="date">{E(n["date"])}</div>{badge}</div>'
            f'<div class="rail"><div class="dot"></div></div>'
            f'<div class="ev"><span class="iconwrap"></span><div class="line">{E(n["text"])}</div></div></div>'
        )
    quotes = "".join(
        f'<div class="qbox{" g" if i else ""}"><div class="qh">{E(q["head"])}</div><div class="qt">“{E(q["text"])}”</div>'
        f'<div class="qa">{E(q["attr"])}</div></div>'
        for i, q in enumerate(g.get("quotes") or [])
    )
    return (
        f'<div class="panel"><div class="stats">{stats}</div>'
        f'<div class="ph">{E(g.get("title", "HOW WE GOT HERE"))}</div>'
        f'<div class="nodes">{"".join(rows)}</div><div class="quotes">{quotes}</div></div>'
    )


_orig = T.render_graphic
T.render_graphic = lambda g: render(g) if (g or {}).get("type") == "stat_timeline" else _orig(g)


def main() -> None:
    data = json.loads((OUT / (sys.argv[1] if len(sys.argv) > 1 else "card.json")).read_text())
    h = T.build_html(data).replace("</style>", CSS + "</style>", 1)
    png = T.render_png(h, OUT / data.get("output", "card.png"))
    print(png, png.stat().st_size)
    dest = Path(f"/workspace/whip-cards/{FOLDER}")
    dest.mkdir(parents=True, exist_ok=True)
    for name in FILES:
        f = OUT / name
        if f.exists():
            shutil.copy(f, dest / name)
            print("copied", dest / name)


if __name__ == "__main__":
    main()
