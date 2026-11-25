#!/usr/bin/env python3
"""UPDATE card (TALL v4, tiles): FinCEN discloses cybersecurity incident (Nov. 24, 2026).
Running story with the Nov. 24 CIA/ODNI breach card (same maroon background, shield tiles, red NEW tile).
Uses /home/box/whip/templates/make_card_tall_v4.py unchanged, adding a "tiles" graphic type locally.
Sources: FinCEN notice; ABC News, Nov. 25; Nextgov/FCW; The Verge. No Whip scores. No commentators.

Usage:
    python3 make_card.py              # renders card.json -> card.png
    python3 make_card.py card-v2.json # renders card-v2.json -> card-v2.png
Does not post or schedule. v1 files are left in place when rendering v2.
"""
import html
import importlib.util
import json
import shutil
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
TEMPLATE = Path("/home/box/whip/templates/make_card_tall_v4.py")
FOLDER = "breaking/2026-11-25-fincen-breach"
FILES = (
    "card.png", "card.json", "make_card.py", "alt.txt",
    "card-v2.png", "card-v2.json", "alt-v2.txt", "tweet-v2.txt",
)

spec = importlib.util.spec_from_file_location("tall_v4", TEMPLATE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)

TILES_CSS = f"""
body{{background:radial-gradient(ellipse at 70% 38%,#4a0b14 0%,#300a12 45%,#09090b 82%)}}
.panel{{border-top-color:{T.RED}}}
.grid{{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:16px;min-height:0;margin-top:4px}}
.tile{{position:relative;background:#2a2a32;border:2px solid #4a4a54;border-radius:8px;padding:16px 20px 14px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;min-height:0}}
.tile.hot{{background:{T.RED};border:4px solid {T.YEL}}}
.tile svg{{display:block;margin-bottom:4px}}
.tn{{font-family:'Anton',sans-serif;font-size:58px;line-height:1;color:{T.PAPER}}}
.tl{{font-family:'Archivo Black',sans-serif;font-size:16px;letter-spacing:.08em;text-transform:uppercase;color:{T.PAPER};margin-top:6px;line-height:1.2}}
.tile.hot .tl{{color:{T.YEL}}}
.tt{{font-family:'Inter',sans-serif;font-size:22px;font-weight:600;line-height:1.25;color:#c8c4ba;margin-top:8px}}
.tile.hot .tt{{color:{T.PAPER}}}
.td{{font-family:'Archivo Black',sans-serif;font-size:15px;letter-spacing:.12em;color:{T.INK};background:{T.YEL};padding:4px 10px 3px;margin-top:10px}}
.badge{{position:absolute;top:12px;right:12px;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.14em;background:{T.YEL};color:{T.INK};padding:5px 10px 4px}}
.callout{{margin-top:14px;font-family:'Anton',sans-serif;font-size:40px;line-height:1;color:{T.YEL};text-align:center}}
.pnote{{font-family:'Inter',sans-serif;font-size:16px;font-weight:600;color:{T.MUTE};margin-top:6px;text-align:center}}
"""

def shield(hot: bool) -> str:
    x = ('<path d="M33 32 l18 18 M51 32 l-18 18" stroke="#ffcc00" stroke-width="5" stroke-linecap="round"/>'
         if hot else "")
    return (f'<svg width="84" height="76" viewBox="0 0 84 76" aria-hidden="true">'
            f'<path d="M42 6 l30 12 v20 c0 20 -14 31 -30 36 c-16 -5 -30 -16 -30 -36 v-20 z" fill="none" '
            f'stroke="{T.PAPER}" stroke-width="4"/>{x}</svg>')

def render_tiles(g: dict) -> str:
    tiles = []
    for it in g.get("items") or []:
        hot = bool(it.get("new"))
        badge = '<div class="badge">NEW</div>' if hot else ""
        date = f'<div class="td">{html.escape(it["date"])}</div>' if it.get("date") else ""
        tiles.append(f'''<div class="tile{' hot' if hot else ''}">{badge}{shield(hot)}
<div class="tn">{html.escape(it["name"])}</div><div class="tl">{html.escape(it.get("label",""))}</div>
<div class="tt">{html.escape(it.get("text",""))}</div>{date}</div>''')
    callout = f'<div class="callout">{html.escape(g["callout"])}</div>' if g.get("callout") else ""
    note = f'<div class="pnote">{html.escape(g["note"])}</div>' if g.get("note") else ""
    return f'''<div class="panel"><div class="ph">{html.escape(g.get("title",""))}</div>
<div class="grid">{"".join(tiles)}</div>{callout}{note}</div>'''

_orig = T.render_graphic
def render_graphic(g):
    if (g or {}).get("type") == "tiles":
        return render_tiles(g)
    return _orig(g)
T.render_graphic = render_graphic

def main() -> None:
    json_name = sys.argv[1] if len(sys.argv) > 1 else "card.json"
    data = json.loads((OUT / json_name).read_text())
    h = T.build_html(data).replace("</style>", TILES_CSS + "</style>", 1)
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
