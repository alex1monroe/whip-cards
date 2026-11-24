#!/usr/bin/env python3
"""UPDATE card: AP calls Tennessee's 4th District for Democrat Victoria Broderick over Rep. Scott DesJarlais (R)
(Tue Nov 24, 2026, 11:12 a.m. CT). Sources: AP via WZTV/Fox17 and NewsChannel 9; NYT on X (2125285034433056884).
Draft only. Whip illustration; schematic Tennessee outline, not to scale, not a real map or AP graphic.
No Whip scores. No hook. No total House seat count."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-tn04-broderick"
FOLDER = "breaking/2026-11-24-tn04-broderick"
W, H = 568, 300
RED, YEL, BLU, PAPER, MUTE, INK = "#ff2d2a", "#ffcc00", "#3d8bff", "#f4f0e6", "#8a867c", "#09090b"

parts = []
parts.append(f'<text x="0" y="20" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">TENNESSEE&rsquo;S 4TH DISTRICT</text>')
parts.append(f'<text x="0" y="40" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">Schematic, not to scale. Highlight shows the district&rsquo;s general area</text>')
# schematic Tennessee outline (simplified parallelogram-like shape)
tn = "26,66 470,56 560,52 548,68 522,86 498,106 476,128 458,160 16,164 22,144 12,124 26,104 16,84"
parts.append(f'<polygon points="{tn}" fill="#1a1f2a" stroke="#4a4a54" stroke-width="2"/>')
dist = "236,82 282,84 302,98 344,102 378,110 372,138 358,160 268,160 262,132 244,108"
parts.append(f'<polygon points="{dist}" fill="{BLU}" opacity=".9" stroke="{PAPER}" stroke-width="2"/>')
parts.append(f'<text x="312" y="138" text-anchor="middle" font-family="Anton" font-size="26" fill="{PAPER}">TN-04</text>')
# R -> D flip marker
fy = 190
parts.append(f'<text x="0" y="{fy}" font-family="Archivo Black" font-size="12.5" letter-spacing="1.6" fill="{MUTE}">AP CALL &middot; 11:12 A.M. CT &middot; TUE., NOV. 24</text>')
parts.append(f'<rect x="0" y="{fy+12}" width="46" height="40" rx="3" fill="{RED}"/><text x="23" y="{fy+43}" text-anchor="middle" font-family="Anton" font-size="30" fill="{PAPER}">R</text>')
parts.append(f'<text x="62" y="{fy+44}" font-family="Anton" font-size="32" fill="{YEL}">&rarr;</text>')
parts.append(f'<rect x="100" y="{fy+12}" width="46" height="40" rx="3" fill="{BLU}"/><text x="123" y="{fy+43}" text-anchor="middle" font-family="Anton" font-size="30" fill="{PAPER}">D</text>')
parts.append(f'<text x="164" y="{fy+30}" font-family="Archivo Black" font-size="14" letter-spacing=".6" fill="{PAPER}">FLIP: Victoria Broderick (D)</text>')
parts.append(f'<text x="164" y="{fy+50}" font-family="Inter" font-size="13" font-weight="600" fill="#c8c4ba">defeated Rep. Scott DesJarlais (R), the incumbent</text>')
# counties
parts.append(f'<text x="0" y="{fy+80}" font-family="Inter" font-size="11.5" font-weight="600" fill="{MUTE}">Counties: Bledsoe, Cannon, Coffee, Davidson, Franklin, Grundy, Marion,</text>')
parts.append(f'<text x="0" y="{fy+96}" font-family="Inter" font-size="11.5" font-weight="600" fill="{MUTE}">Rutherford, Sequatchie, Van Buren, Warren</text>')
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: AP via WZTV, NYT (Nov. 24, 2026). Illustration.</span><span>Whip illustration &middot; not an AP graphic or official map</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; ELECTIONS</div>
<div class="left">
  <div class="h1">TN-04<br><span class="y">FLIPS BLUE</span></div>
  <div class="h2">BRODERICK UNSEATS<br>REP. DESJARLAIS</div>
  <div class="att">AP called Tennessee&rsquo;s 4th Congressional District for Democrat Victoria Broderick at 11:12 a.m. CT Tuesday. The New York Times called it one of the biggest upsets of the midterms.</div>
  <div class="chips"><span>Affordability</span><span>Health care</span><span>Rural hospitals</span></div>
</div>
<div class="panel">
  <div class="ph">THE FLIP &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>The flip:</b> Democrat Victoria Broderick defeated Republican incumbent Rep. Scott DesJarlais, per AP.</div></div>
  <div class="b"><div class="n">02</div><div><b>Her issues:</b> affordability, health care access, rural hospitals, housing and voluntary pre-K.</div></div>
  <div class="b"><div class="n">03</div><div><b>The upset:</b> the New York Times called it one of the biggest upsets of the midterms.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0b1f4a 0%,#0a1430 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:74px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:28px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.chips{display:flex;gap:8px;margin-top:12px}
.chips span{font-family:'Archivo Black',sans-serif;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#09090b;background:#3d8bff;padding:5px 9px 4px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:100px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #3d8bff;padding:12px 16px 10px}
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
for f in (src, Path(__file__).resolve()):
    if f.exists(): shutil.copy(f, dest / f.name); print("copied", dest / f.name)
