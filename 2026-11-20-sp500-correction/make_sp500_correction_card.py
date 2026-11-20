#!/usr/bin/env python3
"""BREAKING card: S&P 500 falls 3.7% and closes in correction territory as the AI-stock sell-off deepens (Nov 20, 2026).
Sources: AP (S&P -3.7%, Nasdaq negative for 2026), Yahoo Finance (Nasdaq -5.3%, Dow -1.9%, correction close, Nvidia -14%).
Illustration, not a screenshot. Uses the shared Whip v4 base."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "breaking-sp500-correction"
FOLDER = "2026-11-20-sp500-correction"

bars = [("DOW", 1.9, "Yahoo Finance"), ("S&amp;P 500", 3.7, "AP"), ("NASDAQ", 5.3, "Yahoo Finance")]
scale = 31  # px per percent
parts = []
for i, (lab, v, src) in enumerate(bars):
    x = 70 + i * 165
    h = v * scale
    col = "#ffcc00" if lab.startswith("S&amp;P") else "#ff2d2a"
    parts.append(f'<rect x="{x}" y="40" width="110" height="{h:.0f}" fill="{col}"/>'
                 f'<text x="{x+55}" y="{40+h+40:.0f}" text-anchor="middle" font-family="Anton" font-size="38" fill="#f4f0e6">-{v}%</text>'
                 f'<text x="{x+55}" y="28" text-anchor="middle" font-family="Archivo Black" font-size="15" letter-spacing="2" fill="#f4f0e6">{lab}</text>'
                 f'<text x="{x+55}" y="{40+h+60:.0f}" text-anchor="middle" font-family="Inter" font-size="12" fill="#8a867c">{src}</text>')
graphic = f'''<svg xmlns="http://www.w3.org/2000/svg" width="568" height="296" viewBox="0 0 568 296">
<line x1="40" y1="40" x2="548" y2="40" stroke="#f4f0e6" stroke-width="2"/>
<text x="40" y="58" font-family="Inter" font-size="11" fill="#8a867c" transform="rotate(-90 34 58)"></text>
{''.join(parts)}
</svg>'''

html = wrap(f"""
<div class="footer"><span>Sources: AP; Yahoo Finance, Nov. 20, 2026 closing figures</span><span>Whip illustration &middot; not an official graphic</span></div>
<div class="tag"><span class="dot"></span>BREAKING &middot; MARKETS</div>
<div class="left">
  <div class="h1">S&amp;P 500 FALLS<br><span class="y">INTO A<br>CORRECTION</span><br>AS AI STOCKS SLIDE</div>
  <div class="att">The S&amp;P 500 fell 3.7% Friday, per AP, and closed more than 10% below its Oct. 6 record, per Yahoo Finance.</div>
</div>
<div class="panel">
  <div class="ph">FRIDAY&rsquo;S DROP BY INDEX &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>Correction:</b> Wall Street&rsquo;s term for a close 10%+ below a record high, per AP.</div></div>
  <div class="b"><div class="n">02</div><div><b>Nasdaq:</b> the tech-heavy index is now negative for 2026, per AP.</div></div>
  <div class="b"><div class="n">03</div><div><b>Chips led:</b> Nvidia, AMD, Broadcom and Micron fell double digits, per Yahoo Finance.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#3a0a08 0%,#1c0604 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:126px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:56px;line-height:.98;color:#f4f0e6}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:12px;width:470px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:112px;width:600px;z-index:5;background:rgba(18,12,14,.88);border-top:4px solid #ff2d2a;padding:12px 16px 10px}
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
for f in (src, Path(__file__).resolve()):
    shutil.copy(f, dest / f.name); print("copied", dest / f.name)
