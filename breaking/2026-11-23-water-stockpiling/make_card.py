#!/usr/bin/env python3
"""Follow-up card: household water stockpiling after the outages (Mon Nov 23, 2026).
Sources: Yahoo Finance (Rainey); Bloomberg via NY Post/TT (Millerchip); Guardian/Worldpanel; White House; Ready.gov; BBC.
Illustration. No Whip scores."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "followup-water-stockpiling"
FOLDER = "breaking/2026-11-23-water-stockpiling"
W = 568
RED, YEL, BLU, INK, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#09090b", "#f4f0e6", "#8a867c"
parts = []
rows = [
    ("OCT 22", "U.K. Be Ready", "3-day supply, 9 litres of water per person (BBC)", BLU),
    ("LATE OCT", "Costco buying", "CFO: more water and cans, citing social media (Bloomberg)", MUTE),
    ("NOV 12-17", "U.S. outages", "Microsoft, FAA, banks, United, NSA", RED),
    ("NOV 18", "Clayton", '"This is not a cyberattack" (White House)', YEL),
    ("NOV 19", "Walmart", "CFO: higher comps on jug water and propane (Yahoo)", BLU),
]
y = 4
for d, lab, note, col in rows:
    parts.append(f'<rect x="0" y="{y}" width="{W}" height="48" rx="4" fill="#15151b" stroke="{col}" stroke-width="{3 if col==YEL else 1.5}"/>')
    parts.append(f'<text x="16" y="{y+32}" font-family="Anton" font-size="20" fill="{col}">{d}</text>')
    parts.append(f'<text x="128" y="{y+20}" font-family="Archivo Black" font-size="14" letter-spacing="1.1" fill="{PAPER}">{lab.upper()}</text>')
    parts.append(f'<text x="128" y="{y+38}" font-family="Inter" font-size="12.5" font-weight="600" fill="#c8c4ba">{note}</text>')
    y += 54
H = y
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: Yahoo Finance (Nov. 19); Bloomberg via NY Post and Transport Topics; the Guardian / Worldpanel; White House (Nov. 18); Ready.gov; BBC. Illustration.</span><span>Whip illustration &middot; not a government or news graphic</span></div>
<div class="tag"><span class="dot"></span>FOLLOW-UP &middot; THE OUTAGES</div>
<div class="left">
  <div class="h1">SHOPPERS<br>STOCKED <span class="y">WATER</span></div>
  <div class="h2">RETAILERS REPORT HIGHER<br>SALES, A SMALL U.S. LIFT</div>
  <div class="att">Walmart CFO John David Rainey told Yahoo Finance jug bottled water and propane are selling at higher comps, a relatively small lift. U.K. bottled-water sales rose 67% after Be Ready, Worldpanel data show.</div>
</div>
<div class="panel">
  <div class="ph">THE TIMELINE &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">SHOWS</span></div>
  <div class="b"><div class="n">01</div><div><b>The U.S. lift:</b> Rainey called it relatively small and often a pull-forward of demand.</div></div>
  <div class="b"><div class="n">02</div><div><b>The official line:</b> DNI Clayton said the outages were "not a cyberattack." Rubio said they were not related.</div></div>
  <div class="b"><div class="n">03</div><div><b>U.S. guidance:</b> Ready.gov advises at least 1 gallon of water per person per day for several days.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0d2a3a 0%,#081820 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#3d8bff;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:64px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:26px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:100px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #ffcc00;padding:12px 16px 10px}
.ph{font-family:'Archivo Black',sans-serif;font-size:13px;letter-spacing:.16em;color:#8a867c;margin-bottom:8px}
.panel svg{display:block}
.strip{position:absolute;left:48px;right:48px;top:470px;height:150px;z-index:5;background:rgba(14,14,18,.94);border-top:4px solid #ffcc00;display:grid;grid-template-columns:150px 1fr 1fr 1fr;gap:20px;padding:16px 22px}
.wt{font-family:'Anton',sans-serif;font-size:40px;line-height:.92;color:#f4f0e6}
.b{display:flex;gap:10px;font-weight:600;font-size:16.5px;line-height:1.16;color:#c8c4ba}
.b b{color:#ffcc00;font-weight:800}
.n{font-family:'Anton',sans-serif;font-size:30px;line-height:.9;color:#3d8bff}
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
