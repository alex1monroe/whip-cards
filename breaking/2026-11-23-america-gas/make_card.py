#!/usr/bin/env python3
"""@America card: National gas average falls to $3.64 ahead of Thanksgiving (Mon Nov 23, 2026).
Sources: AAA Gas Prices (as of Nov 23, 2026); AAA Nov 19 release. No Whip scores."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap

OUT = Path(__file__).resolve().parent
NAME = "america-gas-prices"
FOLDER = "breaking/2026-11-23-america-gas"

W = 568
RED, YEL, BLU, GRN, INK, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#2ecc71", "#09090b", "#f4f0e6", "#8a867c"

parts = []
parts.append(f'<text x="0" y="22" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">U.S. REGULAR GAS AVERAGE &middot; PER GALLON</text>')
parts.append(f'<text x="0" y="44" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">AAA national average, as of Nov. 23, 2026</text>')

rows = [
    ("1 MONTH AGO", "$4.29", "429", 360, MUTE),
    ("1 WEEK AGO",  "$3.81", "381", 315, BLU),
    ("TODAY",       "$3.64", "364", 295, YEL),
    ("1 YEAR AGO",  "$3.07", "307", 240, RED),
]
y = 64
for lab, price, _, bw, col in rows:
    is_today = (lab == "TODAY")
    parts.append(f'<rect x="0" y="{y}" width="{W}" height="54" rx="4" fill="#15151b" stroke="{col}" stroke-width="{3 if is_today else 1.5}"/>')
    parts.append(f'<text x="16" y="{y+34}" font-family="Archivo Black" font-size="14" letter-spacing="1.1" fill="{YEL if is_today else PAPER}">{lab}</text>')
    parts.append(f'<rect x="168" y="{y+18}" width="{bw - 40}" height="18" rx="3" fill="{col}" opacity="0.9"/>')
    parts.append(f'<text x="{W - 18}" y="{y+38}" text-anchor="end" font-family="Anton" font-size="28" fill="{col}">{price}</text>')
    y += 62
H = y
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'

html = wrap(f"""
<div class="footer"><span>Source: AAA Gas Prices (as of Nov. 23, 2026) &amp; AAA Nov. 19 release.</span><span>Whip illustration &middot; not an AAA graphic</span></div>
<div class="tag"><span class="dot"></span>@AMERICA &middot; GAS PRICES</div>
<div class="left">
  <div class="h1">GAS FALLS TO<br><span class="y">$3.64</span> A GALLON</div>
  <div class="h2">SLIDING FOR WEEKS AHEAD<br>OF THANKSGIVING TRAVEL</div>
  <div class="att">Down from $4.29 a month ago as crude oil cooled, though still above $3.07 a year ago.</div>
</div>
<div class="panel">
  <div class="ph">AAA NATIONAL AVERAGE &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT TO<br><span class="y">WATCH</span></div>
  <div class="b"><div class="n">01</div><div><b>The drop:</b> cheaper crude oil pushed pump prices down for weeks before the holiday.</div></div>
  <div class="b"><div class="n">02</div><div><b>The catch:</b> drivers are still paying well above last year&rsquo;s $3.07 national average.</div></div>
  <div class="b"><div class="n">03</div><div><b>Next up:</b> AAA says the slide could keep Thanksgiving below the 2022 record.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#102a45 0%,#0b1a2c 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ff2d2a;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:64px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:28px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:112px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #ffcc00;padding:12px 16px 10px}
.ph{font-family:'Archivo Black',sans-serif;font-size:13px;letter-spacing:.16em;color:#8a867c;margin-bottom:8px}
.panel svg{display:block}
.strip{position:absolute;left:48px;right:48px;top:470px;height:150px;z-index:5;background:rgba(14,14,18,.94);border-top:4px solid #ffcc00;display:grid;grid-template-columns:150px 1fr 1fr 1fr;gap:20px;padding:16px 22px}
.wt{font-family:'Anton',sans-serif;font-size:40px;line-height:.92;color:#f4f0e6}
.b{display:flex;gap:10px;font-weight:600;font-size:17px;line-height:1.16;color:#c8c4ba}
.b b{color:#ffcc00;font-weight:800}
.n{font-family:'Anton',sans-serif;font-size:30px;line-height:.9;color:#ff2d2a}
""")

out_html = OUT / f"{NAME}.html"
out_html.write_text(html)
png = OUT / "card.png"
r = subprocess.run([
    "google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
    "--force-device-scale-factor=2", "--window-size=1200,675", f"--screenshot={png}",
    "file://" + str(out_html)
], capture_output=True, text=True)
if r.returncode != 0:
    sys.exit("render failed: " + r.stderr[-800:])
out_html.unlink()
print("rendered:", png, png.stat().st_size)

dest = Path(f"/workspace/whip-cards/{FOLDER}")
dest.mkdir(parents=True, exist_ok=True)
for f in (png, Path(__file__).resolve()):
    if f.exists():
        shutil.copy(f, dest / f.name)
        print("copied:", dest / f.name)
