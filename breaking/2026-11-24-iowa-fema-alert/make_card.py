#!/usr/bin/env python3
"""UPDATE card: FEMA emergency alert for Iowa lead azide detonation, 9 a.m. Wed Nov 25 (sent Tue Nov 24, 2026).
Sources: WQAD (8:44 AM CST Nov 24) and Quad-City Times/QC Online (Nov 24) on the FEMA alert. Rings are schematic, not a real map. No Whip scores."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-iowa-fema-alert"
FOLDER = "breaking/2026-11-24-iowa-fema-alert"
W, H = 568, 300
RED, YEL, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#f4f0e6", "#8a867c"
cx, cy = 170, 168
p = []
p.append(f'<text x="0" y="22" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">FEMA ALERT ZONES &#183; SCHEMATIC</text>')
p.append(f'<text x="0" y="44" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">Not to scale; not a map. Per the FEMA alert (WQAD)</text>')
p.append(f'<circle cx="{cx}" cy="{cy}" r="118" fill="rgba(255,204,0,.16)" stroke="{YEL}" stroke-width="2.5"/>')
p.append(f'<path d="M {cx} {cy} L {cx-58} {cy+28} A 64 64 0 0 0 {cx-10} {cy+63} Z" fill="rgba(255,45,42,.55)" stroke="{RED}" stroke-width="2"/>')
p.append(f'<circle cx="{cx}" cy="{cy}" r="64" fill="none" stroke="{RED}" stroke-width="2.5" stroke-dasharray="6 5"/>')
p.append(f'<circle cx="{cx}" cy="{cy}" r="9" fill="{PAPER}"/>')
p.append(f'<text x="{cx}" y="{cy-16}" text-anchor="middle" font-family="Archivo Black" font-size="11" letter-spacing="1" fill="{PAPER}">PLANT</text>')
p.append(f'<text x="{cx-66}" y="{cy+92}" text-anchor="middle" font-family="Archivo Black" font-size="10" fill="{RED}">SW</text>')
lx = 330
p.append(f'<rect x="{lx}" y="76" width="18" height="18" fill="rgba(255,45,42,.55)" stroke="{RED}"/>')
p.append(f'<text x="{lx+28}" y="90" font-family="Archivo Black" font-size="14" fill="{PAPER}">0&#8211;5 MI SOUTHWEST</text>')
p.append(f'<text x="{lx+28}" y="110" font-family="Inter" font-size="13" font-weight="600" fill="#c8c4ba">Some residents may</text>')
p.append(f'<text x="{lx+28}" y="127" font-family="Inter" font-size="13" font-weight="600" fill="#c8c4ba">be evacuated</text>')
p.append(f'<rect x="{lx}" y="160" width="18" height="18" fill="rgba(255,204,0,.3)" stroke="{YEL}"/>')
p.append(f'<text x="{lx+28}" y="174" font-family="Archivo Black" font-size="14" fill="{PAPER}">5&#8211;20 MILES</text>')
p.append(f'<text x="{lx+28}" y="194" font-family="Inter" font-size="13" font-weight="600" fill="#c8c4ba">Stay indoors with</text>')
p.append(f'<text x="{lx+28}" y="211" font-family="Inter" font-size="13" font-weight="600" fill="#c8c4ba">windows closed</text>')
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(p)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: FEMA alert as reported by WQAD and the Quad-City Times (Nov. 24). Schematic illustration.</span><span>Whip illustration &middot; not a FEMA or news graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; IOWA BLAST</div>
<div class="left">
  <div class="h1">FEMA ALERT:<br><span class="y">9 A.M. WEDNESDAY</span></div>
  <div class="h2">POSSIBLE EVACUATIONS NEAR<br>IOWA ARMY AMMUNITION PLANT</div>
  <div class="att">An emergency alert sent Tuesday morning set the controlled detonation of degraded lead azide in Middletown, Iowa, for 9 a.m. Wednesday, Nov. 25 (WQAD).</div>
</div>
<div class="panel">
  <div class="ph">WHO THE ALERT COVERS &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>When:</b> Detonation set for 9 a.m. Wednesday, Nov. 25, per the alert.</div></div>
  <div class="b"><div class="n">02</div><div><b>Near the plant:</b> Some within 5 miles southwest may be evacuated; watch local media for routes and shelters.</div></div>
  <div class="b"><div class="n">03</div><div><b>5&#8211;20 miles:</b> Stay inside, windows closed. FEMA info line: 800-621-3362.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#4a1f08 0%,#2a1206 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ff2d2a;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:58px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:26px;line-height:1.02;color:#f4f0e6;margin-top:8px}
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
