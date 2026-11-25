#!/usr/bin/env python3
"""NEW card (TALL v4, 2440x3092): House stock-trading ban (Stop Insider Trading Act, H.R. 11142)
teed up for a floor vote (Nov. 25, 2026). Sources: Bloomberg Government; House Rules Committee;
Punchbowl News. Uses /home/box/whip/templates/make_card_tall_v4.py unchanged, adding a local
"does_doesnt" graphic: a two-column WHAT IT DOES / WHAT IT DOESN'T comparison plus a compact
horizontal timeline row. No Whip scores, % moves or heat meters. Whip illustration.
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
FOLDER = "breaking/2026-11-25-stock-trading-ban-vote"
FILES = ("card.png", "card.json", "make_card.py", "alt.txt")

spec = importlib.util.spec_from_file_location("tall_v4", TEMPLATE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
E = html.escape

CHECK = f'<svg width="54" height="54" viewBox="0 0 36 36"><circle cx="18" cy="18" r="16" fill="{T.GRN}"/><path d="M10 18.5l5 5 11-11" fill="none" stroke="{T.INK}" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CROSS = f'<svg width="54" height="54" viewBox="0 0 36 36"><circle cx="18" cy="18" r="16" fill="{T.RED}"/><path d="M12 12l12 12M24 12L12 24" fill="none" stroke="{T.PAPER}" stroke-width="3.6" stroke-linecap="round"/></svg>'

CSS = f"""
.cols{{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px;min-height:0}}
.col{{background:#14141a;border-top:6px solid {T.GRN};padding:14px 18px;display:flex;flex-direction:column;gap:14px}}
.col.no{{border-top-color:{T.RED}}}
.ch{{display:flex;align-items:center;gap:12px;font-family:'Anton',sans-serif;font-size:50px;line-height:1;color:{T.PAPER}}}
.it{{flex:1;display:flex;flex-direction:column;justify-content:center;border-top:2px solid #2c2c34;padding-top:12px}}
.itt{{font-family:'Anton',sans-serif;font-size:56px;line-height:1.02;color:{T.YEL}}}
.col.no .itt{{color:{T.PAPER}}}
.itb{{font-family:'Inter',sans-serif;font-size:28px;font-weight:600;line-height:1.25;color:#d8d4ca;margin-top:8px}}
.hph{{margin-top:14px}}
.hrow{{display:grid;grid-template-columns:repeat(4,1fr);gap:0;position:relative;margin-top:4px}}
.hrow::before{{content:"";position:absolute;left:12.5%;right:12.5%;top:13px;height:3px;background:#4a4a54}}
.hs{{display:flex;flex-direction:column;align-items:center;text-align:center;padding:0 8px;position:relative}}
.hd{{width:20px;height:20px;border-radius:50%;background:{T.BLU};border:3px solid {T.PAPER};margin:3px 0 8px;z-index:1}}
.hs.red .hd{{background:{T.RED}}}
.hs.acc .hd{{background:{T.YEL};width:26px;height:26px;margin:0 0 5px;box-shadow:0 0 0 3px {T.INK}}}
.hs.up .hd{{background:{T.INK};border:3px dashed {T.PAPER}}}
.hdate{{font-family:'Anton',sans-serif;font-size:34px;line-height:1;color:{T.PAPER}}}
.hs.acc .hdate{{color:{T.YEL}}}
.ht{{font-family:'Inter',sans-serif;font-size:20px;font-weight:600;line-height:1.25;color:#d8d4ca;margin-top:6px}}
.panel{{padding:12px 18px 14px}}
.strip{{padding:14px 20px 14px;margin-top:12px}}
.means{{gap:9px}}
.b{{font-size:21px;line-height:1.22}}
"""


def render(g: dict) -> str:
    def col(c, icon, kl):
        items = "".join(
            f'<div class="it"><div class="itt">{E(i["title"])}</div><div class="itb">{E(i["text"])}</div></div>'
            for i in c["items"]
        )
        return f'<div class="col {kl}"><div class="ch">{icon}{E(c["head"])}</div>{items}</div>'

    steps = "".join(
        f'<div class="hs {s.get("kind", "")}"><div class="hd"></div><div class="hdate">{E(s["date"])}</div>'
        f'<div class="ht">{E(s["text"])}</div></div>'
        for s in g.get("steps") or []
    )
    return (
        f'<div class="panel"><div class="ph">{E(g.get("title", ""))}</div>'
        f'<div class="cols">{col(g["does"], CHECK, "yes")}{col(g["doesnt"], CROSS, "no")}</div>'
        f'<div class="ph hph">{E(g.get("steps_title", "THE ROAD SO FAR"))}</div>'
        f'<div class="hrow">{steps}</div></div>'
    )


_orig = T.render_graphic
T.render_graphic = lambda g: render(g) if (g or {}).get("type") == "does_doesnt" else _orig(g)


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
