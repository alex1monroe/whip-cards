#!/usr/bin/env python3
"""UPDATE card (TALL v4, 2440x3092): S&P Global Ratings places Nvidia's 'AA' ratings on CreditWatch Negative
over management and governance risks (Nov. 25, 2026). Running story with breaking/2026-11-24-huang-assurances,
2026-11-25-nvidia-huang-pardon, 2026-11-25-trump-nvidia-stake, 2026-11-25-schumer-huang-export and
2026-11-25-vance-huang-pardon. Sources: S&P Global Ratings research update; Reuters; CNBC; Nvidia press release.
Uses /home/box/whip/templates/make_card_tall_v4.py unchanged, adding a local "watch" graphic: a rating-scale
ladder (current grade vs. possible one-notch cut) beside S&P's four stated concerns, plus a compact
"what happens next" row (pattern from 2026-11-25-schumer-huang-export). No Whip scores, % moves, heat meters
or stock charts. Whip illustration. Does not post or schedule.
"""
import html
import importlib.util
import json
import shutil
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
TEMPLATE = Path("/home/box/whip/templates/make_card_tall_v4.py")
FOLDER = "breaking/2026-11-25-sp-nvidia-creditwatch"
FILES = ("card.png", "card.json", "make_card.py", "alt.txt", "tweet.txt")

spec = importlib.util.spec_from_file_location("tall_v4", TEMPLATE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
E = html.escape

CSS = f"""
.cols{{flex:1;display:grid;grid-template-columns:.78fr 1.22fr;gap:14px;min-height:0}}
.col{{background:#14141a;border-top:6px solid {T.YEL};padding:12px 16px;display:flex;flex-direction:column;gap:8px;min-height:0;overflow:hidden}}
.col.fl{{border-top-color:{T.RED}}}
.cht{{font-family:'Archivo Black',sans-serif;font-size:16px;letter-spacing:.14em;color:#c8c4ba}}
.rung{{flex:1;display:flex;flex-direction:column;justify-content:center;border:2px solid #2c2c34;padding:8px 14px;background:#101015}}
.grade{{font-family:'Anton',sans-serif;font-size:64px;line-height:1;color:#6c6a64}}
.rn{{font-family:'Inter',sans-serif;font-size:18px;font-weight:700;line-height:1.2;color:#8a867c;margin-top:2px}}
.rung.now{{border:3px solid {T.YEL};background:rgba(255,204,0,.10)}}
.rung.now .grade{{color:{T.YEL};font-size:84px}}
.rung.now .rn{{color:{T.PAPER}}}
.rung.maybe{{border:3px dashed {T.RED}}}
.rung.maybe .grade{{color:{T.PAPER}}}
.rung.maybe .rn{{color:#d8d4ca}}
.arrow{{font-family:'Anton',sans-serif;color:{T.RED};font-size:22px;letter-spacing:.1em;text-align:center;line-height:1}}
.lnote{{font-family:'Inter',sans-serif;font-size:17px;font-weight:600;line-height:1.25;color:#a8a49a}}
.it{{flex:1;display:flex;flex-direction:column;justify-content:center;border-top:2px solid #2c2c34;padding-top:6px}}
.itt{{font-family:'Anton',sans-serif;font-size:36px;line-height:1.02;color:{T.YEL}}}
.itb{{font-family:'Inter',sans-serif;font-size:22px;font-weight:600;line-height:1.24;color:#d8d4ca;margin-top:5px}}
.hph{{margin-top:12px}}
.hrow{{display:grid;grid-template-columns:repeat(4,1fr);position:relative;margin-top:4px}}
.hrow::before{{content:"";position:absolute;left:12.5%;right:12.5%;top:13px;height:3px;background:#4a4a54}}
.hs{{display:flex;flex-direction:column;align-items:center;text-align:center;padding:0 8px}}
.hd{{width:20px;height:20px;border-radius:50%;background:{T.BLU};border:3px solid {T.PAPER};margin:3px 0 8px;z-index:1}}
.hs.acc .hd{{background:{T.YEL};width:26px;height:26px;margin:0 0 5px;box-shadow:0 0 0 3px {T.INK}}}
.hs.up .hd{{background:{T.INK};border:3px dashed {T.PAPER}}}
.hdate{{font-family:'Anton',sans-serif;font-size:32px;line-height:1;color:{T.PAPER}}}
.hs.acc .hdate{{color:{T.YEL}}}
.ht{{font-family:'Inter',sans-serif;font-size:19px;font-weight:600;line-height:1.25;color:#d8d4ca;margin-top:6px}}
.h1{{font-size:96px}}
.panel{{padding:12px 18px 14px}}
.strip{{padding:14px 20px 14px;margin-top:12px}}
.means{{gap:9px}}
.b{{font-size:21px;line-height:1.22}}
"""


def render(g: dict) -> str:
    rungs = []
    for r in g["ladder"]:
        kind = r.get("kind", "")
        if kind == "maybe":
            rungs.append('<div class="arrow">▼ ONE NOTCH?</div>')
        note = f'<div class="rn">{E(r["note"])}</div>' if r.get("note") else ""
        rungs.append(f'<div class="rung {kind}"><div class="grade">{E(r["grade"])}</div>{note}</div>')
    ladder = (
        f'<div class="col"><div class="cht">{E(g["ladder_title"])}</div>{"".join(rungs)}'
        f'<div class="lnote">{E(g.get("ladder_note", ""))}</div></div>'
    )
    flags = "".join(
        f'<div class="it"><div class="itt">{E(f["title"])}</div><div class="itb">{E(f["text"])}</div></div>'
        for f in g["flags"]
    )
    flags = f'<div class="col fl"><div class="cht">{E(g["flags_title"])}</div>{flags}</div>'
    steps = "".join(
        f'<div class="hs {s.get("kind", "")}"><div class="hd"></div><div class="hdate">{E(s["date"])}</div>'
        f'<div class="ht">{E(s["text"])}</div></div>'
        for s in g.get("steps") or []
    )
    return (
        f'<div class="panel"><div class="cols">{ladder}{flags}</div>'
        f'<div class="ph hph">{E(g.get("steps_title", "WHAT HAPPENS NEXT"))}</div>'
        f'<div class="hrow">{steps}</div></div>'
    )


_orig = T.render_graphic
T.render_graphic = lambda g: render(g) if (g or {}).get("type") == "watch" else _orig(g)


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
