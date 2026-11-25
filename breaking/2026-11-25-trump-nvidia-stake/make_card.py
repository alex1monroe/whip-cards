#!/usr/bin/env python3
"""UPDATE card (TALL v4, 2440x3092): Trump's Nvidia stake, per OGE disclosures reported by CBS News
(Isabel Vincent, updated Nov. 25, 2026). Running story with breaking/2026-11-25-nvidia-huang-pardon.
Uses /home/box/whip/templates/make_card_tall_v4.py unchanged, adding a local "ranges" graphic type
(low-high range bars on a shared $0-$100M scale plus a small two-date strip). No Whip scores. Whip illustration.
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
FOLDER = "breaking/2026-11-25-trump-nvidia-stake"
FILES = ("card.png", "card.json", "make_card.py", "alt.txt")

spec = importlib.util.spec_from_file_location("tall_v4", TEMPLATE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)

COLORS = {"red": T.RED, "yellow": T.YEL, "green": T.GRN, "blue": T.BLU}

RANGES_CSS = f"""
.rows{{flex:1;display:flex;flex-direction:column;justify-content:space-evenly;min-height:0}}
.rr-top{{display:flex;justify-content:space-between;align-items:flex-end;gap:20px}}
.rl{{font-family:'Anton',sans-serif;font-size:58px;line-height:1;color:{T.PAPER}}}
.rs{{font-family:'Inter',sans-serif;font-size:21px;font-weight:600;color:#a8a49a;margin-top:6px}}
.rv{{font-family:'Anton',sans-serif;font-size:84px;line-height:1;white-space:nowrap}}
.rtrack{{position:relative;height:58px;margin-top:12px;background:#1a1a20}}
.rtick{{position:absolute;top:0;bottom:0;width:2px;background:#2c2c34}}
.rseg{{position:absolute;top:0;bottom:0}}
.rcap{{position:absolute;top:-6px;bottom:-6px;width:6px;background:{T.PAPER}}}
.axis{{position:relative;height:26px;margin-top:4px}}
.axis span{{position:absolute;transform:translateX(-50%);font-family:'Inter',sans-serif;font-size:17px;font-weight:700;color:{T.MUTE}}}
.axis span:first-child{{transform:none}} .axis span:last-child{{transform:translateX(-100%)}}
.pnote{{font-family:'Inter',sans-serif;font-size:17px;font-weight:600;color:{T.MUTE};margin-top:4px}}
.tstrip{{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:12px;border-top:2px solid #2c2c34;padding-top:12px}}
.ts{{display:flex;gap:14px;align-items:flex-start}}
.ts .d{{font-family:'Anton',sans-serif;font-size:34px;line-height:1;color:{T.YEL};white-space:nowrap}}
.ts .t{{font-family:'Inter',sans-serif;font-size:20px;font-weight:600;color:{T.PAPER};line-height:1.25}}
.strip .means{{gap:9px}}
.strip .b{{font-size:19px}}
.strip .n{{font-size:28px;flex:0 0 36px}}
"""


def render_ranges(g: dict) -> str:
    amax = float(g.get("axis_max", 100))
    ticks = g.get("ticks") or []
    tick_html = "".join(
        f'<div class="rtick" style="left:{100*t/amax:.2f}%"></div>' for t in ticks
    )
    axis = "".join(
        f'<span style="left:{100*t/amax:.2f}%">${t}M</span>' for t in ticks
    )
    rows = []
    for r in g.get("rows") or []:
        col = COLORS.get(r.get("color", "yellow"), T.YEL)
        lo, hi = 100 * float(r["low"]) / amax, 100 * float(r["high"]) / amax
        rows.append(
            f'<div class="rr"><div class="rr-top"><div><div class="rl">{html.escape(r["label"])}</div>'
            f'<div class="rs">{html.escape(r["sub"])}</div></div>'
            f'<div class="rv" style="color:{col}">{html.escape(r["value"])}</div></div>'
            f'<div class="rtrack">{tick_html}'
            f'<div class="rseg" style="left:{lo:.2f}%;width:{hi-lo:.2f}%;background:{col}"></div>'
            f'<div class="rcap" style="left:calc({lo:.2f}% - 3px)"></div>'
            f'<div class="rcap" style="left:calc({hi:.2f}% - 3px)"></div></div>'
            f'<div class="axis">{axis}</div></div>'
        )
    note = f'<div class="pnote">{html.escape(g["note"])}</div>' if g.get("note") else ""
    strip = ""
    if g.get("strip"):
        strip = '<div class="tstrip">' + "".join(
            f'<div class="ts"><div class="d">{html.escape(s["date"])}</div><div class="t">{html.escape(s["text"])}</div></div>'
            for s in g["strip"]
        ) + "</div>"
    return (
        f'<div class="panel"><div class="ph">{html.escape(g.get("title", ""))}</div>'
        f'<div class="rows">{"".join(rows)}</div>{note}{strip}</div>'
    )


_orig = T.render_graphic


def render_graphic(g):
    if (g or {}).get("type") == "ranges":
        return render_ranges(g)
    return _orig(g)


T.render_graphic = render_graphic


def main() -> None:
    data = json.loads((OUT / (sys.argv[1] if len(sys.argv) > 1 else "card.json")).read_text())
    h = T.build_html(data).replace("</style>", RANGES_CSS + "</style>", 1)
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
