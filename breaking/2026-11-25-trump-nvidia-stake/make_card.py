#!/usr/bin/env python3
"""UPDATE card (TALL v4, 2440x3092): Trump's Nvidia stake, per OGE disclosures reported by CBS News
(Isabel Vincent, updated Nov. 25, 2026). Running story with breaking/2026-11-25-nvidia-huang-pardon
and the Nov. 23 CNBC clip. Uses /home/box/whip/templates/make_card_tall_v4.py unchanged, adding a
local "ranges" graphic type (low-high range bars on a shared $0-$100M scale, an attributed quote,
and a compact timeline strip). No Whip scores. No stock % moves. Whip illustration.

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
FOLDER = "breaking/2026-11-25-trump-nvidia-stake"
FILES = (
    "card.png", "card.json", "make_card.py", "alt.txt",
    "card-v2.png", "card-v2.json", "alt-v2.txt", "tweet-v2.txt",
)

spec = importlib.util.spec_from_file_location("tall_v4", TEMPLATE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)

COLORS = {"red": T.RED, "yellow": T.YEL, "green": T.GRN, "blue": T.BLU}

RANGES_CSS = f"""
.rows{{flex:0 0 auto;display:flex;flex-direction:column;gap:8px;min-height:0}}
.rr-top{{display:flex;justify-content:space-between;align-items:flex-end;gap:20px}}
.rl{{font-family:'Anton',sans-serif;font-size:52px;line-height:1;color:{T.PAPER}}}
.rs{{font-family:'Inter',sans-serif;font-size:20px;font-weight:600;color:#a8a49a;margin-top:4px}}
.rv{{font-family:'Anton',sans-serif;font-size:76px;line-height:1;white-space:nowrap}}
.rtrack{{position:relative;height:48px;margin-top:10px;background:#1a1a20}}
.rtick{{position:absolute;top:0;bottom:0;width:2px;background:#2c2c34}}
.rseg{{position:absolute;top:0;bottom:0}}
.rcap{{position:absolute;top:-6px;bottom:-6px;width:6px;background:{T.PAPER}}}
.axis{{position:relative;height:22px;margin-top:3px}}
.axis span{{position:absolute;transform:translateX(-50%);font-family:'Inter',sans-serif;font-size:16px;font-weight:700;color:{T.MUTE}}}
.axis span:first-child{{transform:none}} .axis span:last-child{{transform:translateX(-100%)}}
.pnote{{font-family:'Inter',sans-serif;font-size:16px;font-weight:600;color:{T.MUTE};margin-top:6px}}
.qbox{{margin-top:10px;background:#14141a;border-left:4px solid {T.YEL};padding:10px 14px 11px}}
.qt{{font-family:'Inter',sans-serif;font-size:21px;font-weight:600;font-style:italic;line-height:1.28;color:{T.PAPER}}}
.qa{{font-family:'Inter',sans-serif;font-size:16px;font-weight:700;color:#a8a49a;margin-top:6px}}
.tstrip{{display:flex;flex-direction:column;justify-content:space-evenly;flex:1;min-height:0;gap:8px;margin-top:10px;border-top:2px solid #2c2c34;padding-top:10px;padding-bottom:4px}}
.ts{{display:grid;grid-template-columns:118px 1fr;gap:12px;align-items:start}}
.ts .d{{font-family:'Anton',sans-serif;font-size:30px;line-height:1;color:{T.PAPER};white-space:nowrap;text-align:right;padding-top:1px}}
.ts.accent .d{{color:{T.YEL}}}
.ts .t{{font-family:'Inter',sans-serif;font-size:19px;font-weight:600;color:{T.PAPER};line-height:1.25}}
.strip .means{{gap:8px}}
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
    quote = ""
    if g.get("quote"):
        q = g["quote"]
        quote = (
            f'<div class="qbox"><div class="qt">“{html.escape(q.get("text", ""))}”</div>'
            f'<div class="qa">{html.escape(q.get("attr", ""))}</div></div>'
        )
    strip = ""
    if g.get("strip"):
        items = []
        for s in g["strip"]:
            kl = "ts accent" if s.get("accent") else "ts"
            items.append(
                f'<div class="{kl}"><div class="d">{html.escape(s["date"])}</div>'
                f'<div class="t">{html.escape(s["text"])}</div></div>'
            )
        strip = '<div class="tstrip">' + "".join(items) + "</div>"
    return (
        f'<div class="panel"><div class="ph">{html.escape(g.get("title", ""))}</div>'
        f'<div class="rows">{"".join(rows)}</div>{note}{quote}{strip}</div>'
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
