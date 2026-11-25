#!/usr/bin/env python3
"""BREAKING card (TALL v4, 2440x3092): second federal judge (Christopher Cooper, D.D.C.) blocks
Executive Order 14418, Trump's August 2026 birthright-citizenship order (Nathan v. Trump, Nov. 25, 2026).
Sources: Nathan v. Trump mem. op. (D.D.C. No. 26-cv-3377); ACLU; MS NOW; The Hill; ABC News; Bloomberg Law;
CBS News; Reuters. Adapted from breaking/2026-11-25-stock-trading-ban-vote/make_card.py: same
"does_doesnt" two-column comparison (here: exceptions the Supreme Court recognized vs. the order's new
categories) plus a compact horizontal timeline row. No Whip scores, % moves or heat meters.
Whip illustration. Does not post or schedule.
"""
import html
import importlib.util
import json
import shutil
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
TEMPLATE = Path("/home/box/whip/templates/make_card_tall_v4.py")
FOLDER = "breaking/2026-11-25-birthright-second-judge"
FILES = ("card.png", "card.json", "make_card.py", "alt.txt", "tweet.txt", "card-v2.png", "card-v2.json", "alt-v2.txt", "tweet-v2.txt", "card-v3.png", "card-v3.json", "alt-v3.txt", "tweet-v3.txt")

spec = importlib.util.spec_from_file_location("tall_v4", TEMPLATE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
E = html.escape

CHECK = f'<svg width="54" height="54" viewBox="0 0 36 36"><circle cx="18" cy="18" r="16" fill="{T.GRN}"/><path d="M10 18.5l5 5 11-11" fill="none" stroke="{T.INK}" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
CROSS = f'<svg width="54" height="54" viewBox="0 0 36 36"><circle cx="18" cy="18" r="16" fill="{T.RED}"/><path d="M12 12l12 12M24 12L12 24" fill="none" stroke="{T.PAPER}" stroke-width="3.6" stroke-linecap="round"/></svg>'

CSS = f"""
.cols{{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px;min-height:0}}
.col{{background:#14141a;border-top:6px solid {T.GRN};padding:12px 18px;display:flex;flex-direction:column;gap:8px;min-height:0;overflow:hidden}}
.col.no{{border-top-color:{T.RED}}}
.ch{{display:flex;align-items:center;gap:12px;font-family:'Anton',sans-serif;font-size:40px;line-height:1;color:{T.PAPER}}}
.csub{{font-family:'Inter',sans-serif;font-size:16px;font-weight:600;line-height:1.2;color:#8e8a82;margin:2px 0 0 66px}}
.col.has-sub{{gap:6px;padding:10px 18px}}
.col.has-sub .it{{padding-top:6px}}
.col.has-sub .itb{{margin-top:6px}}
.it{{flex:1;display:flex;flex-direction:column;justify-content:center;border-top:2px solid #2c2c34;padding-top:8px}}
.itt{{font-family:'Anton',sans-serif;font-size:44px;line-height:1.02;color:{T.YEL}}}
.col.no .itt{{color:{T.PAPER}}}
.itb{{font-family:'Inter',sans-serif;font-size:25px;font-weight:600;line-height:1.25;color:#d8d4ca;margin-top:8px}}
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
        sub = c.get("subhead")
        sub_html = f'<div class="csub">{E(sub)}</div>' if sub else ""
        kl2 = f"{kl} has-sub" if sub else kl
        return f'<div class="col {kl2}"><div class="ch">{icon}{E(c["head"])}</div>{sub_html}{items}</div>'

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
