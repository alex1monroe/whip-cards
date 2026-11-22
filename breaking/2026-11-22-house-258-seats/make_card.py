#!/usr/bin/env python3
"""BREAKING card: Democrats reach at least 258 House seats, most since 1992 (Sun Nov 22, 2026).
Source: AP (apnews.com/article/democrats-house-majority-election-2026-congress-721096a4d9ba2cd68683692361798cdb),
AP on X 1:11 PM ET (x.com/AP/status/2124566573813760317). Draft only. Illustration. No Whip scores."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "breaking-house-258"
FOLDER = "breaking/2026-11-22-house-258-seats"
W = 568
RED, YEL, BLU, INK, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#09090b", "#f4f0e6", "#8a867c"
parts = []
parts.append(f'<text x="0" y="22" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">U.S. HOUSE · 435 SEATS</text>')
parts.append(f'<text x="0" y="44" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">Each square = 1 seat. Per AP, as of Sunday, Nov. 22</text>')
# icon grid 435 seats: 29 cols x 15 rows
cols, size, gap, y0 = 35, 12, 3.5, 58
for i in range(435):
    r, c = divmod(i, cols)
    if i < 258: col = BLU
    elif i < 262: col = "#5a5a64"
    else: col = RED
    parts.append(f'<rect x="{c*(size+gap):.1f}" y="{y0 + r*(size+gap):.1f}" width="{size}" height="{size}" rx="2" fill="{col}"/>')
leg_y = y0 + 13*(size+gap) + 20
for x, col, lab in ((0, BLU, "DEMOCRATS: 258+"), (190, "#5a5a64", "4 OUTSTANDING"), (350, RED, "REPUBLICANS")):
    parts.append(f'<rect x="{x}" y="{leg_y-12}" width="14" height="14" rx="2" fill="{col}"/><text x="{x+20}" y="{leg_y}" font-family="Archivo Black" font-size="12.5" letter-spacing="1" fill="{PAPER}">{lab}</text>')
H = leg_y + 10
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Source: AP (Nov. 22, 2026). Illustration.</span><span>Whip illustration &middot; not an AP graphic</span></div>
<div class="tag"><span class="dot"></span>BREAKING &middot; ELECTIONS</div>
<div class="left">
  <div class="h1">258 HOUSE<br><span class="y">SEATS FOR DEMS</span></div>
  <div class="h2">LARGEST HOUSE MAJORITY<br>SINCE THE 1992 ELECTION</div>
  <div class="att">AP: the total was reached Sunday when Democrat Chuck Hubbard defeated Rep. Virginia Foxx (R) in North Carolina. Four House races remain outstanding.</div>
</div>
<div class="panel">
  <div class="ph">THE NEW HOUSE &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>The count:</b> Democrats hold at least 258 of 435 seats; 218 is a majority.</div></div>
  <div class="b"><div class="n">02</div><div><b>The gain:</b> Democrats picked up 44 seats so far, per AP.</div></div>
  <div class="b"><div class="n">03</div><div><b>Still open:</b> four House races, including one each in Minnesota and Tennessee.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0b1f4a 0%,#0a1430 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ff2d2a;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:74px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:28px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:112px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #ffcc00;padding:12px 16px 10px}
.ph{font-family:'Archivo Black',sans-serif;font-size:13px;letter-spacing:.16em;color:#8a867c;margin-bottom:8px}
.panel svg{display:block}
.strip{position:absolute;left:48px;right:48px;top:470px;height:150px;z-index:5;background:rgba(14,14,18,.94);border-top:4px solid #ffcc00;display:grid;grid-template-columns:150px 1fr 1fr 1fr;gap:20px;padding:16px 22px}
.wt{font-family:'Anton',sans-serif;font-size:40px;line-height:.92;color:#f4f0e6}
.b{display:flex;gap:10px;font-weight:600;font-size:18px;line-height:1.16;color:#c8c4ba}
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
for f in (src, Path(__file__).resolve(), OUT / "tweet.md"):
    if f.exists(): shutil.copy(f, dest / f.name); print("copied", dest / f.name)
