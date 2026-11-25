#!/usr/bin/env python3
"""ISSUE MOMENTUM card (TALL v4), Nov 25, 2026: Nov 23 vs Nov 24 Whip heat, percent movement only. No Whip scores. Draft only."""
import importlib.util, json, shutil, sys
from pathlib import Path
OUT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("tv4", "/home/box/whip/templates/make_card_tall_v4.py")
tv4 = importlib.util.module_from_spec(spec); spec.loader.exec_module(tv4)
COL = {"up": "#ff6a3a", "hot": "#ffcc00", "down": "#5aaeff"}
def render_momentum(g):
    out = []
    for sec in g["sections"]:
        c = COL[sec["kind"]]
        rows = "".join(
            f'<div style="display:flex;align-items:baseline;gap:22px;border-top:1px solid #26262c;padding:12px 0">'
            f'<div style="font-family:Anton,sans-serif;font-size:46px;line-height:1;color:{c};width:250px;flex:none;text-align:right">{tv4.esc(r[0])}</div>'
            f'<div style="font-family:Inter,sans-serif;font-weight:700;font-size:30px;line-height:1.15;color:#ece8de">{tv4.esc(r[1])}</div></div>'
            for r in sec["rows"])
        out.append(f'<div style="margin-bottom:22px"><div style="font-family:\'Archivo Black\',sans-serif;font-size:24px;letter-spacing:.14em;color:{c};border-left:8px solid {c};padding-left:14px;margin-bottom:6px">{tv4.esc(sec["title"])}</div>{rows}</div>')
    return '<div class="panel" style="padding:26px 34px 6px">' + "".join(out) + '</div>'
tv4.render_graphic = render_momentum
r = tv4.main([str(OUT / "card.json")])
dest = Path("/workspace/whip-cards/2026-11-25-momentum"); dest.mkdir(parents=True, exist_ok=True)
for f in ("card.png", "card.json", "post.txt", "alt.txt", "make_card.py"):
    if (OUT / f).exists(): shutil.copy(OUT / f, dest / f); print("copied", dest / f)
