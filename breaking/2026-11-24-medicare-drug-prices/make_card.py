#!/usr/bin/env python3
"""@America card: Medicare sets lower prices on 13 of its costliest drugs (Tue Nov 24, 2026).
Sources: CMS; Reuters (Beasley, Nov 23). Illustration of generic Rx bottles — not product packaging,
no drugmaker logos or branding. No Whip scores. No predictions."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "america-medicare-drug-prices"
FOLDER = "breaking/2026-11-24-medicare-drug-prices"
W, H = 568, 300
RED, YEL, BLU, PAPER, MUTE, INK = "#ff2d2a", "#ffcc00", "#3d8bff", "#f4f0e6", "#8a867c", "#09090b"
AMBER, AMBER_DK, AMBER_LT = "#c97820", "#8a5210", "#e09a3a"
CAP, LABEL, COUNTER = "#f4f0e6", "#efebe0", "#1a1c20"

def bottle(cx, y_top, scale, accent=False):
    """Schematic amber Rx bottle. Label is only a generic Rx — no brand marks."""
    s = scale
    bw, bh = 62 * s, 126 * s
    cap_w, cap_h = 70 * s, 15 * s
    neck_w, neck_h = 30 * s, 9 * s
    x = cx - bw / 2
    cap_x = cx - cap_w / 2
    neck_x = cx - neck_w / 2
    body_y = y_top + cap_h + neck_h - 2 * s
    gid = f"amber{int(cx)}{int(y_top)}"
    parts = [
        f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0">'
        f'<stop offset="0%" stop-color="{AMBER_LT}"/>'
        f'<stop offset="35%" stop-color="{AMBER}"/>'
        f'<stop offset="100%" stop-color="{AMBER_DK}"/>'
        f'</linearGradient></defs>'
    ]
    parts.append(f'<ellipse cx="{cx+2*s}" cy="{body_y+bh+3*s}" rx="{bw*0.46}" ry="{7*s}" fill="#000" opacity=".35"/>')
    parts.append(f'<rect x="{cap_x}" y="{y_top}" width="{cap_w}" height="{cap_h}" rx="{3*s}" fill="{CAP}"/>')
    parts.append(f'<rect x="{cap_x}" y="{y_top+cap_h*0.48}" width="{cap_w}" height="{1.6*s}" fill="#d8d4ca"/>')
    parts.append(f'<rect x="{neck_x}" y="{y_top+cap_h-1}" width="{neck_w}" height="{neck_h+2}" fill="{AMBER_DK}"/>')
    parts.append(f'<rect x="{x}" y="{body_y}" width="{bw}" height="{bh}" rx="{9*s}" fill="url(#{gid})"/>')
    lw, lh = 44 * s, 34 * s
    lx, ly = cx - lw / 2, body_y + 30 * s
    stroke = YEL if accent else "#c8c4ba"
    parts.append(f'<rect x="{lx}" y="{ly}" width="{lw}" height="{lh}" rx="{2*s}" fill="{LABEL}" stroke="{stroke}" stroke-width="{1.2*s}"/>')
    rx_size = 15 * s
    parts.append(
        f'<text x="{cx}" y="{ly+lh*0.68}" text-anchor="middle" font-family="Anton" font-size="{rx_size}" fill="{RED}">Rx</text>'
    )
    return "".join(parts), body_y + bh

parts = []
parts.append(f'<text x="0" y="20" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">13 DRUGS WITH NEW MEDICARE PRICES</text>')
parts.append(f'<text x="0" y="40" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">Schematic bottles, not product packaging. Source: CMS, Reuters</text>')

# row of 11 small generic silhouettes, kept over the two featured bottles
# so the "+11" label is not covered by the 45% box
mini_y = 56
mini_gap = 18
mini_start = 16
for i in range(11):
    mx = mini_start + i * mini_gap
    parts.append(f'<rect x="{mx-5.5}" y="{mini_y}" width="11" height="3.5" rx="1" fill="{CAP}" opacity=".9"/>')
    parts.append(f'<rect x="{mx-4.5}" y="{mini_y+3.5}" width="9" height="18" rx="2" fill="{AMBER}" opacity=".75"/>')
parts.append(f'<text x="{mini_start + 10*mini_gap + 16}" y="{mini_y+16}" font-family="Archivo Black" font-size="11" letter-spacing="0.8" fill="{MUTE}">+11</text>')

# two featured bottles
b1, b1_bot = bottle(78, 92, 1.0, accent=False)
b2, b2_bot = bottle(188, 92, 1.0, accent=False)
parts.append(b1)
parts.append(b2)
# typographic captions — names as Whip type, not logos
parts.append(f'<text x="78" y="{b1_bot+22}" text-anchor="middle" font-family="Archivo Black" font-size="13" letter-spacing="0.6" fill="{PAPER}">Trulicity</text>')
parts.append(f'<text x="78" y="{b1_bot+38}" text-anchor="middle" font-family="Inter" font-size="11" font-weight="600" fill="{MUTE}">diabetes</text>')
parts.append(f'<text x="188" y="{b2_bot+22}" text-anchor="middle" font-family="Archivo Black" font-size="13" letter-spacing="0.6" fill="{PAPER}">Biktarvy</text>')
parts.append(f'<text x="188" y="{b2_bot+38}" text-anchor="middle" font-family="Inter" font-size="11" font-weight="600" fill="{MUTE}">HIV</text>')

# counter line under bottles
parts.append(f'<rect x="16" y="{b1_bot+4}" width="226" height="3" fill="#2a2c32"/>')

# stat box: 45% always paired with "vs. recent yearly spending"
bx, by, bw, bh = 290, 70, 270, 210
parts.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="4" fill="#15151b" stroke="{YEL}" stroke-width="2.5"/>')
parts.append(f'<text x="{bx+20}" y="{by+28}" font-family="Archivo Black" font-size="12" letter-spacing="1.4" fill="{MUTE}">MEDICARE ESTIMATE</text>')
parts.append(f'<text x="{bx+20}" y="{by+108}" font-family="Anton" font-size="86" fill="{YEL}">45%</text>')
parts.append(f'<text x="{bx+20}" y="{by+138}" font-family="Archivo Black" font-size="16" letter-spacing="0.8" fill="{PAPER}">LOWER SPENDING</text>')
parts.append(f'<text x="{bx+20}" y="{by+162}" font-family="Inter" font-size="14" font-weight="600" fill="#c8c4ba">vs. recent yearly spending</text>')
parts.append(f'<rect x="{bx+20}" y="{by+178}" width="{bw-40}" height="1" fill="#2a2c32"/>')
parts.append(f'<text x="{bx+20}" y="{by+198}" font-family="Archivo Black" font-size="13" letter-spacing="1.2" fill="{YEL}">STARTS 2028</text>')

graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: CMS, Reuters. Illustration.</span><span>Whip illustration &middot; not a government or news graphic</span></div>
<div class="tag"><span class="dot"></span>@AMERICA &middot; MEDICARE</div>
<div class="left">
  <div class="h1">MEDICARE:<br><span class="y">LOWER PRICES</span></div>
  <div class="h2">ON ITS COSTLIEST DRUGS</div>
  <div class="att">Includes Trulicity and Biktarvy<br>Starts 2028 &middot; Source: CMS, Reuters</div>
</div>
<div class="panel">
  <div class="ph">PRESCRIPTION PRICES &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b one"><div class="n">01</div><div>New negotiated prices for 13 drugs; Medicare estimates 45% lower spending on them vs. recent yearly spending.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0e3a32 0%,#0a221c 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ff2d2a;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:64px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:28px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:12px;width:470px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:100px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #ffcc00;padding:12px 16px 10px}
.ph{font-family:'Archivo Black',sans-serif;font-size:13px;letter-spacing:.16em;color:#8a867c;margin-bottom:8px}
.panel svg{display:block}
.strip{position:absolute;left:48px;right:48px;top:470px;height:150px;z-index:5;background:rgba(14,14,18,.94);border-top:4px solid #ffcc00;display:grid;grid-template-columns:150px 1fr;gap:20px;padding:16px 22px}
.wt{font-family:'Anton',sans-serif;font-size:40px;line-height:.92;color:#f4f0e6}
.b{display:flex;gap:14px;font-weight:600;font-size:22px;line-height:1.25;color:#c8c4ba;align-items:flex-start;padding-top:8px}
.b b{color:#ffcc00;font-weight:800}
.n{font-family:'Anton',sans-serif;font-size:30px;line-height:.9;color:#ff2d2a}
""")
def render(html):
    out_html = OUT / f"{NAME}.html"; out_html.write_text(html)
    png = OUT / "card.png"
    r = subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                        "--force-device-scale-factor=2", "--window-size=1200,675", f"--screenshot={png}",
                        "file://" + str(out_html)], capture_output=True, text=True)
    if r.returncode != 0: sys.exit("render failed: " + r.stderr[-800:])
    out_html.unlink()
    return png
src = render(html)
print(src, src.stat().st_size)
dest = Path(f"/workspace/whip-cards/{FOLDER}")
dest.mkdir(parents=True, exist_ok=True)
for f in (src, Path(__file__).resolve()):
    if f.exists(): shutil.copy(f, dest / f.name); print("copied", dest / f.name)
