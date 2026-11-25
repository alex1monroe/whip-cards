#!/usr/bin/env python3
"""UPDATE card (TALL v4, 2440x3092): Vance says Jensen Huang wouldn't need a pardon (Nov. 25, 2026).
Running story with breaking/2026-11-25-nvidia-huang-pardon and 2026-11-25-trump-nvidia-stake.
Sources: New York Post; Fox News video; Reuters; CNBC. Uses /home/box/whip/templates/make_card_tall_v4.py
unchanged, adding a local "timeline_new" graphic: the standard v4 timeline plus a NEW badge on one
beat and a hollow dot for an upcoming beat, without cutting the rail. No Whip scores. Whip illustration.
Does not post or schedule.
"""
import html
import importlib.util
import json
import shutil
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
TEMPLATE = Path("/home/box/whip/templates/make_card_tall_v4.py")
FOLDER = "breaking/2026-11-25-vance-huang-pardon"
FILES = ("card.png", "card.json", "make_card.py", "alt.txt")

spec = importlib.util.spec_from_file_location("tall_v4", TEMPLATE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)

EXTRA_CSS = f"""
.node{{grid-template-columns:214px 32px 1fr}}
.node.new .date{{color:{T.YEL}}}
.node.new .dot{{background:{T.YEL};width:24px;height:24px;box-shadow:0 0 0 3px {T.INK},0 0 0 6px rgba(255,204,0,.35)}}
.node.new .ev{{background:rgba(255,204,0,.08);border-left:4px solid {T.YEL};padding:8px 12px 8px 8px}}
.node.up .dot{{background:{T.INK};border:3px dashed {T.PAPER}}}
.node.up .date{{color:#c8c4ba}}
.node.up .line{{color:#d8d4ca}}
.newb{{display:inline-block;background:{T.RED};color:{T.PAPER};font-family:'Archivo Black',sans-serif;font-size:15px;letter-spacing:.16em;padding:4px 8px 3px;line-height:1;margin-top:6px}}
.dcol{{display:flex;flex-direction:column;align-items:flex-end}}
.nodes .node:last-child .rail::before{{bottom:50%}}
"""


def render_timeline_new(g: dict) -> str:
    rows = []
    nodes = g.get("nodes") or []
    for i, n in enumerate(nodes):
        kl = ["node", (n.get("dot") or "blue")]
        if n.get("new"):
            kl.append("new")
        if n.get("upcoming"):
            kl.append("up")
        badge = '<span class="newb">NEW</span>' if n.get("new") else ""
        rows.append(
            f'<div class="{" ".join(kl)}"><div class="dcol"><div class="date">{html.escape(n["date"])}</div>{badge}</div>'
            f'<div class="rail"><div class="dot"></div></div>'
            f'<div class="ev"><span class="iconwrap"></span><div class="line">{html.escape(n["text"])}</div></div></div>'
        )
    return (
        f'<div class="panel"><div class="ph">{html.escape(g.get("title", "HOW WE GOT HERE"))}</div>'
        f'<div class="nodes">{"".join(rows)}</div></div>'
    )


_orig = T.render_graphic


def render_graphic(g):
    if (g or {}).get("type") == "timeline_new":
        return render_timeline_new(g)
    return _orig(g)


T.render_graphic = render_graphic


def main() -> None:
    data = json.loads((OUT / (sys.argv[1] if len(sys.argv) > 1 else "card.json")).read_text())
    h = T.build_html(data).replace("</style>", EXTRA_CSS + "</style>", 1)
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
