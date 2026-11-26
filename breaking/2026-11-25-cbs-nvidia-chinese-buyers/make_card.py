#!/usr/bin/env python3
"""UPDATE card (TALL v4, 2440x3092): CBS News investigation (Nov. 25, 2026, Josh Boswell) finds two
California companies buying Nvidia's most advanced chips are Chinese-owned: RiCloud AI (parent Yuxing
InfoTech, Shenzhen) and Aivres (formerly Inspur; Inspur group blacklisted March 2023). Follows
breaking/2026-11-23-megaspeed-listed and 2026-11-25-lutnick-bis-agents.
Uses /home/box/whip/templates/make_card_tall_v4.py unchanged, adding a local "chains" graphic:
ownership flow rows (Nvidia -> California buyer -> Chinese owner) with a note and status line each.
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
FOLDER = "breaking/2026-11-25-cbs-nvidia-chinese-buyers"
FILES = ("card.png", "card.json", "make_card.py", "alt.txt", "tweet.txt")

spec = importlib.util.spec_from_file_location("tall_v4", TEMPLATE)
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)
E = html.escape

CSS = f"""
.h1{{font-size:98px}}
.chains{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.chain{{flex:1;background:#14141a;border-left:4px solid {T.GRN};padding:16px 18px 14px;display:flex;flex-direction:column;gap:12px}}
.flow{{display:grid;grid-template-columns:1fr 54px 1fr 54px 1fr;align-items:stretch}}
.step{{background:#1c1c24;border-top:6px solid {T.BLU};padding:12px 14px;display:flex;flex-direction:column;gap:6px}}
.step.owner{{border-top-color:{T.RED};background:rgba(255,45,42,.10)}}
.sn{{font-family:'Anton',sans-serif;font-size:46px;line-height:1;color:{T.PAPER}}}
.step.owner .sn{{color:{T.YEL}}}
.ss{{font-family:'Inter',sans-serif;font-size:21px;font-weight:600;line-height:1.24;color:#c8c4ba}}
.arr{{display:flex;align-items:center;justify-content:center}}
.note{{font-family:'Inter',sans-serif;font-size:27px;font-weight:600;line-height:1.26;color:#d8d4ca;flex:1}}
.status{{font-family:'Inter',sans-serif;font-size:23px;font-weight:800;line-height:1.2;color:{T.GRN};border-top:2px solid #2c2c34;padding-top:9px}}
.lbl{{font-family:'Archivo Black',sans-serif;font-size:15px;letter-spacing:.14em;color:{T.MUTE}}}
.b{{font-size:21px;line-height:1.22}}
.strip{{padding:16px 20px}}
"""

ARROW = f'''<svg width="48" height="34" viewBox="0 0 48 34" aria-hidden="true"><path d="M4 17h34" stroke="{T.YEL}" stroke-width="5" stroke-linecap="round"/><path d="M28 6l13 11-13 11" fill="none" stroke="{T.YEL}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'''


def render(g: dict) -> str:
    out = []
    for c in g["chains"]:
        parts = []
        for i, s in enumerate(c["steps"]):
            if i:
                parts.append(f'<div class="arr">{ARROW}</div>')
            cls = "step owner" if s.get("owner") else "step"
            lbl = '<div class="lbl">OWNER</div>' if s.get("owner") else ('<div class="lbl">BUYER</div>' if i == 1 else '<div class="lbl">SELLER</div>')
            parts.append(f'<div class="{cls}">{lbl}<div class="sn">{E(s["name"])}</div><div class="ss">{E(s["sub"])}</div></div>')
        out.append(
            f'<div class="chain"><div class="flow">{"".join(parts)}</div>'
            f'<div class="note">{E(c["note"])}</div><div class="status">{E(c["status"])}</div></div>'
        )
    return f'<div class="panel"><div class="ph">{E(g.get("title", ""))}</div><div class="chains">{"".join(out)}</div></div>'


_orig = T.render_graphic
T.render_graphic = lambda g: render(g) if (g or {}).get("type") == "chains" else _orig(g)


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
