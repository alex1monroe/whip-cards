#!/usr/bin/env python3
"""UPDATE card: FBI investigating apparent breach of NCIC (Nov 20, 2026; CNN, Reuters relay).
Draft only. Illustration, not a screenshot. Adapted from 2026-11-20-nsa-update-restored/make_card.py."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-fbi-ncic-breach"
FOLDER = "2026-11-20-fbi-ncic-breach"
W = 568
RED, YEL, GRY = "#ff2d2a", "#ffcc00", "#4a4a54"
# hub-and-spoke: NCIC links federal, state, local agencies; used for warrants + background checks
cx, cy = W/2, 112
nodes = [(90, 40, "FEDERAL"), (W-90, 40, "STATE"), (90, 186, "LOCAL"), (W-90, 186, "POLICE NATIONWIDE")]
parts = []
for x, y, lab in nodes:
    parts.append(f'<line x1="{cx}" y1="{cy}" x2="{x}" y2="{y}" stroke="{RED}" stroke-width="2.4" stroke-dasharray="6 5"/>')
for x, y, lab in nodes:
    parts.append(f'<rect x="{x-82}" y="{y-20}" width="164" height="40" fill="#16161b" stroke="#c8c4ba" stroke-width="1.6"/>'
                 f'<text x="{x}" y="{y+6}" text-anchor="middle" font-family="Archivo Black" font-size="{13 if len(lab)<10 else 11.5}" letter-spacing="1.6" fill="#f4f0e6">{lab}</text>')
parts.append(f'<circle cx="{cx}" cy="{cy}" r="54" fill="#3a1014" stroke="{RED}" stroke-width="3"/>'
             f'<text x="{cx}" y="{cy+2}" text-anchor="middle" font-family="Anton" font-size="34" fill="#f4f0e6">NCIC</text>'
             f'<text x="{cx}" y="{cy+24}" text-anchor="middle" font-family="Archivo Black" font-size="11" letter-spacing="1.6" fill="{RED}">BREACHED?</text>')
legend = (f'<line x1="0" y1="226" x2="{W}" y2="226" stroke="#3a3a44" stroke-width="1.2" stroke-dasharray="3 5"/>'
          f'<text x="0" y="252" font-family="Archivo Black" font-size="13" letter-spacing="2" fill="{YEL}">USED FOR: WARRANTS &amp; BACKGROUND CHECKS</text>'
          f'<text x="0" y="276" font-family="Archivo Black" font-size="13" letter-spacing="2" fill="{RED}">SEPT: FBI JOBS-SITE BREACH</text>'
          f'<text x="{W}" y="276" text-anchor="end" font-family="Inter" font-size="12.5" font-weight="600" fill="#8a867c">per CNN</text>')
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="288" viewBox="0 0 {W} 288">{"".join(parts)}{legend}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: CNN (two people briefed), Reuters, Nov. 20, 2026. Illustration.</span><span>Whip illustration &middot; not an FBI graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; FBI DATABASE</div>
<div class="left">
  <div class="h1">FBI CRIME<br><span class="r">DATABASE HIT.</span></div>
  <div class="h2">APPARENT HACKER BREACH<br>OF NCIC UNDER INVESTIGATION</div>
  <div class="att">Per CNN, citing two people briefed. Federal, state and local agencies use NCIC to share warrant and background-check information.</div>
</div>
<div class="panel">
  <div class="ph">HOW NCIC CONNECTS &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>Under review:</b> the FBI is investigating; what was accessed has not been reported.</div></div>
  <div class="b"><div class="n">02</div><div><b>Second one:</b> it follows a September breach tied to an FBI jobs website, per CNN.</div></div>
  <div class="b"><div class="n">03</div><div><b>No comment yet:</b> the FBI did not immediately respond to CNN.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#3a0b10 0%,#22080c 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:80px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:30px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.y{color:#ffcc00}
.r{color:#ff2d2a}
.panel{position:absolute;right:48px;top:112px;width:600px;z-index:5;background:rgba(14,10,12,.88);border-top:4px solid #ff2d2a;padding:12px 16px 10px}
.ph{font-family:'Archivo Black',sans-serif;font-size:13px;letter-spacing:.16em;color:#8a867c;margin-bottom:4px}
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
