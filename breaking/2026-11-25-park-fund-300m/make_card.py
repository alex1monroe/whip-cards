#!/usr/bin/env python3
"""NEW card (TALL v4, bars): Park Service donation account took in $347M in Sept. 2026; source undisclosed.
Uses /home/box/whip/templates/make_card_tall_v4.py unchanged, adding a "bars" graphic type
locally (template untouched). Source: The New York Times, Nov. 24 (via Quartz, Mediaite). No Whip scores."""
import html
import importlib.util
import shutil
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
TEMPLATE = Path("/home/box/whip/templates/make_card_tall_v4.py")
FOLDER = "breaking/2026-11-25-park-fund-300m"
FILES = ("card.png", "card.json", "make_card.py", "alt.txt")

spec = importlib.util.spec_from_file_location("tall_v4", TEMPLATE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)

COLORS = {"red": T.RED, "yellow": T.YEL, "green": T.GRN, "blue": T.BLU, "mute": "#5a5862"}

BARS_CSS = f"""
.groups{{flex:1;display:flex;flex-direction:column;justify-content:space-evenly;min-height:0;gap:8px}}
.gt{{font-family:'Archivo Black',sans-serif;font-size:17px;letter-spacing:.16em;color:#c8c4ba;margin:4px 0 4px}}
.bar{{display:grid;grid-template-columns:270px 1fr 230px;gap:18px;align-items:center;padding:6px 0}}
.bl{{font-family:'Anton',sans-serif;font-size:50px;line-height:1;color:{T.PAPER}}}
.bs{{font-family:'Inter',sans-serif;font-size:20px;font-weight:600;color:#a8a49a;margin-top:4px;line-height:1.2}}
.track{{height:84px;background:#1a1a20;position:relative}}
.fill{{position:absolute;left:0;top:0;bottom:0}}
.bv{{font-family:'Anton',sans-serif;font-size:74px;line-height:1;text-align:right}}
.bar.small .bl{{font-size:42px}} .bar.small .track{{height:60px}} .bar.small .bv{{font-size:60px}}
.pnote{{font-family:'Inter',sans-serif;font-size:17px;font-weight:600;color:{T.MUTE};margin-top:6px}}
"""

def render_bars(g: dict) -> str:
    groups = g.get("groups") or []
    vmax = max(float(it["amount"]) for gr in groups for it in gr["items"]) or 1
    parts = []
    for gr in groups:
        rows = []
        for it in gr["items"]:
            col = COLORS.get(it.get("color", "red"), T.RED)
            w = max(2.0, 100.0 * float(it["amount"]) / vmax)
            sub = f'<div class="bs">{html.escape(it["sub"])}</div>' if it.get("sub") else ""
            cls = "bar small" if gr.get("small") else "bar"
            rows.append(f'''<div class="{cls}"><div><div class="bl">{html.escape(it["label"])}</div>{sub}</div>
<div class="track"><div class="fill" style="width:{w:.1f}%;background:{col}"></div></div>
<div class="bv" style="color:{col}">{html.escape(it["value"])}</div></div>''')
        gt = f'<div class="gt">{html.escape(gr["title"])}</div>' if gr.get("title") else ""
        parts.append(f'<div>{gt}{"".join(rows)}</div>')
    note = f'<div class="pnote">{html.escape(g["note"])}</div>' if g.get("note") else ""
    return f'''<div class="panel"><div class="ph">{html.escape(g.get("title",""))}</div>
<div class="groups">{"".join(parts)}</div>{note}</div>'''

_orig_graphic = T.render_graphic
def render_graphic(g):
    if (g or {}).get("type") == "bars":
        return render_bars(g)
    return _orig_graphic(g)
T.render_graphic = render_graphic

def main() -> None:
    import json
    data = json.loads((OUT / "card.json").read_text())
    h = T.build_html(data).replace("</style>", BARS_CSS + "</style>", 1)
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
