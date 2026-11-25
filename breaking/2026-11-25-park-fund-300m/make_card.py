#!/usr/bin/env python3
"""NEW card (TALL v4, bars): Park Service donation account took in $347M in Sept. 2026; source undisclosed.
Uses /home/box/whip/templates/make_card_tall_v4.py unchanged, adding a "bars" graphic type
locally (template untouched). Source: The New York Times, Nov. 24, via Mediaite and Quartz. No Whip scores.

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
FOLDER = "breaking/2026-11-25-park-fund-300m"
FILES = (
    "card.png", "card.json", "make_card.py", "alt.txt",
    "card-v2.png", "card-v2.json", "alt-v2.txt", "tweet-v2.txt",
)

spec = importlib.util.spec_from_file_location("tall_v4", TEMPLATE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)

COLORS = {"red": T.RED, "yellow": T.YEL, "green": T.GRN, "blue": T.BLU, "mute": "#5a5862"}

BARS_CSS = f"""
.groups{{flex:1;display:flex;flex-direction:column;justify-content:space-evenly;min-height:0;gap:8px}}
.groups.single{{justify-content:stretch;gap:0;padding:4px 0 8px}}
.gblock{{display:flex;flex-direction:column}}
.groups.single .gblock{{flex:1;min-height:0;justify-content:space-evenly}}
.gt{{font-family:'Archivo Black',sans-serif;font-size:17px;letter-spacing:.16em;color:#c8c4ba;margin:4px 0 8px}}
.groups.single .gt{{font-size:22px;letter-spacing:.18em;margin:0}}
.bar{{display:grid;grid-template-columns:270px 1fr 230px;gap:18px;align-items:center;padding:6px 0}}
.groups.single .bar{{grid-template-columns:290px 1fr 310px;gap:16px;padding:10px 8px 10px 0}}
.bl{{font-family:'Anton',sans-serif;font-size:50px;line-height:1;color:{T.PAPER}}}
.groups.single .bl{{font-size:66px}}
.bs{{font-family:'Inter',sans-serif;font-size:20px;font-weight:600;color:#a8a49a;margin-top:4px;line-height:1.2}}
.groups.single .bs{{font-size:22px;margin-top:6px}}
.track{{height:84px;background:#1a1a20;position:relative}}
.groups.single .track{{height:120px}}
.fill{{position:absolute;left:0;top:0;bottom:0}}
.bv{{font-family:'Anton',sans-serif;font-size:74px;line-height:1;text-align:right}}
.groups.single .bv{{font-size:92px}}
.bar.small .bl{{font-size:42px}} .bar.small .track{{height:60px}} .bar.small .bv{{font-size:60px}}
.pnote{{font-family:'Inter',sans-serif;font-size:17px;font-weight:600;color:{T.MUTE};margin-top:6px}}
.strip .means{{gap:10px}}
.strip .b{{font-size:20px}}
.strip .n{{font-size:30px;flex:0 0 38px}}
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
            label = html.escape(it["label"])
            value = html.escape(it["value"])
            rows.append(
                f'<div class="{cls}"><div><div class="bl">{label}</div>{sub}</div>'
                f'<div class="track"><div class="fill" style="width:{w:.1f}%;background:{col}"></div></div>'
                f'<div class="bv" style="color:{col}">{value}</div></div>'
            )
        gt = f'<div class="gt">{html.escape(gr["title"])}</div>' if gr.get("title") else ""
        parts.append(f'<div class="gblock">{gt}{"".join(rows)}</div>')
    note = f'<div class="pnote">{html.escape(g["note"])}</div>' if g.get("note") else ""
    gcls = "groups single" if len(groups) == 1 else "groups"
    title = html.escape(g.get("title", ""))
    return (
        f'<div class="panel"><div class="ph">{title}</div>'
        f'<div class="{gcls}">{"".join(parts)}</div>{note}</div>'
    )


_orig_graphic = T.render_graphic


def render_graphic(g):
    if (g or {}).get("type") == "bars":
        return render_bars(g)
    return _orig_graphic(g)


T.render_graphic = render_graphic


def main() -> None:
    json_name = sys.argv[1] if len(sys.argv) > 1 else "card.json"
    src_json = OUT / json_name
    data = json.loads(src_json.read_text())
    h = T.build_html(data).replace("</style>", BARS_CSS + "</style>", 1)
    out_name = data.get("output", "card.png")
    png = T.render_png(h, OUT / out_name)
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
