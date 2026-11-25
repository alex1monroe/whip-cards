#!/usr/bin/env python3
"""NEW card (TALL v4, 2440x3092): Rep. Robert Garcia (top Democrat on House Oversight) lists Eric Trump's
business ties on X and asks him to testify under oath voluntarily (Nov. 23, 2026); Eric Trump calls the
claims "untrue and libelous" (Nov. 23-24). Related to, but separate from, breaking/2026-11-25-hadrian-pentagon-loan
and 2026-11-25-hadrian-raskin-letters (Don Jr. / 1789 Capital).
Uses /home/box/whip/templates/make_card_tall_v4.py unchanged, adding a local "ties" graphic: a company tie
table (company | tie | what the record shows) above a two-column "Garcia says / Eric Trump says" panel.
No Whip scores, % moves or heat meters. Whip illustration, not a screenshot. Does not post or schedule.
"""
import html
import importlib.util
import json
import shutil
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
TEMPLATE = Path("/home/box/whip/templates/make_card_tall_v4.py")
FOLDER = "breaking/2026-11-25-eric-trump-garcia"
FILES = ("card.png", "card.json", "make_card.py", "alt.txt", "tweet.txt", "card-v2.png", "card-v2.json", "alt-v2.txt", "tweet-v2.txt")

spec = importlib.util.spec_from_file_location("tall_v4", TEMPLATE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
E = html.escape

CSS = f"""
.h1{{font-size:96px}}
.panel{{padding:12px 18px 14px;gap:0}}
.rows{{flex:1;display:flex;flex-direction:column;min-height:0}}
.row{{flex:1;display:grid;grid-template-columns:262px 1fr;gap:16px;align-items:center;border-top:2px solid #2c2c34;padding:6px 0}}
.row:first-child{{border-top:none}}
.co{{font-family:'Anton',sans-serif;font-size:36px;line-height:1;color:{T.PAPER}}}
.tie{{display:inline-block;margin-top:6px;font-family:'Archivo Black',sans-serif;font-size:14px;letter-spacing:.12em;color:{T.INK};background:{T.BLU};padding:4px 8px 3px}}
.tie.stake,.tie.inv{{background:{T.GRN}}}
.rt{{font-family:'Inter',sans-serif;font-size:21px;font-weight:600;line-height:1.24;color:#d8d4ca}}
.row.flag{{background:rgba(255,45,42,.08);border:2px dashed {T.RED};padding:6px 10px;margin-top:4px}}
.row.flag .rt b{{color:{T.YEL}}}
.vs{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:12px;flex:0 0 auto}}
.side{{background:#14141a;border-top:6px solid {T.BLU};padding:12px 16px 12px;display:flex;flex-direction:column;gap:8px}}
.side.r{{border-top-color:{T.RED}}}
.st{{font-family:'Anton',sans-serif;font-size:38px;line-height:1;color:{T.YEL}}}
.sq{{font-family:'Inter',sans-serif;font-size:21px;font-weight:600;line-height:1.26;color:{T.PAPER};flex:1}}
.sm{{font-family:'Inter',sans-serif;font-size:15px;font-weight:700;color:{T.MUTE};letter-spacing:.04em}}
.strip{{padding:14px 20px 14px;margin-top:12px}}
.means{{gap:9px}}
.b{{font-size:21px;line-height:1.22}}
"""


def tie_class(t: str) -> str:
    t = t.upper()
    if "STAKE" in t:
        return "stake"
    if "INVESTOR" in t:
        return "inv"
    return ""


def render(g: dict) -> str:
    rows = "".join(
        f'<div class="row{" flag" if r.get("flag") else ""}"><div><div class="co">{E(r["co"])}</div>'
        f'<span class="tie {tie_class(r["tie"])}">{E(r["tie"])}</span></div>'
        f'<div class="rt">{E(r["text"])}</div></div>'
        for r in g["rows"]
    )
    vs = (
        f'<div class="vs"><div class="side"><div class="st">{E(g["left_title"])}</div>'
        f'<div class="sq">{E(g["left"])}</div><div class="sm">{E(g["left_meta"])}</div></div>'
        f'<div class="side r"><div class="st">{E(g["right_title"])}</div>'
        f'<div class="sq">{E(g["right"])}</div><div class="sm">{E(g["right_meta"])}</div></div></div>'
    )
    return (
        f'<div class="panel"><div class="ph">{E(g.get("title", ""))}</div>'
        f'<div class="rows">{rows}</div>{vs}</div>'
    )


_orig = T.render_graphic
T.render_graphic = lambda g: render(g) if (g or {}).get("type") == "ties" else _orig(g)


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
