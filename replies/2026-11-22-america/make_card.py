#!/usr/bin/env python3
"""Daily @America card, Nov 22, 2026. Draft only. Electricity bills & data centers.
No Whip scores. Illustration."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap

OUT = Path(__file__).resolve().parent
NAME = "america-electricity-data-centers"
FOLDER = "replies/2026-11-22-america"
YEL, RED, BLU, PAPER, MUTE, INK = "#ffcc00", "#ff2d2a", "#4aa8ff", "#f4f0e6", "#8a867c", "#09090b"

# Right-hand comparison graphic (1200 CSS px card; panel is 600 wide)
graphic = f'''<svg xmlns="http://www.w3.org/2000/svg" width="568" height="292" viewBox="0 0 568 292">
  <rect x="0" y="0" width="272" height="200" rx="4" fill="rgba(255,45,42,.12)" stroke="{RED}" stroke-width="2"/>
  <text x="16" y="28" font-family="Archivo Black" font-size="12" letter-spacing="1.6" fill="{RED}">DATA-CENTER DEMAND</text>
  <text x="16" y="112" font-family="Anton" font-size="86" fill="{PAPER}">+19%</text>
  <text x="16" y="148" font-family="Barlow Condensed" font-weight="800" font-size="22" letter-spacing=".04em" fill="{PAPER}">A YEAR, SINCE 2000</text>
  <text x="16" y="178" font-family="Inter" font-size="13" fill="{MUTE}">Howden, from EIA and S&amp;P Global</text>

  <rect x="296" y="0" width="272" height="200" rx="4" fill="rgba(74,168,255,.10)" stroke="{BLU}" stroke-width="2"/>
  <text x="312" y="28" font-family="Archivo Black" font-size="12" letter-spacing="1.6" fill="{BLU}">GRID CAPACITY</text>
  <text x="312" y="112" font-family="Anton" font-size="86" fill="{PAPER}">+2%</text>
  <text x="312" y="148" font-family="Barlow Condensed" font-weight="800" font-size="22" letter-spacing=".04em" fill="{PAPER}">A YEAR, SINCE 2000</text>
  <text x="312" y="178" font-family="Inter" font-size="13" fill="{MUTE}">Same Howden analysis</text>

  <rect x="0" y="216" width="568" height="76" rx="4" fill="rgba(255,204,0,.08)" stroke="{YEL}" stroke-width="2"/>
  <text x="16" y="244" font-family="Archivo Black" font-size="12" letter-spacing="1.6" fill="{YEL}">SHARE OF U.S. GRID CAPACITY</text>
  <text x="16" y="276" font-family="Anton" font-size="28" fill="{PAPER}">0.1% <tspan fill="{MUTE}" font-size="20">IN 2000</tspan>   <tspan fill="{YEL}">→</tspan>   5% <tspan fill="{MUTE}" font-size="20">IN 2025</tspan></text>
</svg>'''

html = wrap(f"""
<div class="footer"><span>Sources: Howden, Nov. 11, 2026 (EIA and 451 Research by S&amp;P Global) &middot; Ballotpedia, Nov. 6 &middot; Cornell Chronicle / Nature Energy, Nov. 9 &middot; Fortune, Nov. 22</span><span>Whip illustration</span></div>
<div class="tag"><span class="dot"></span>ELECTRICITY BILLS &amp; DATA CENTERS</div>
<div class="left">
  <div class="h1">+19% A YEAR<br><span class="vs">VS. +2%</span></div>
  <div class="h2">DATA-CENTER POWER DEMAND<br>VS. U.S. GRID CAPACITY</div>
  <div class="att">Howden, Nov. 11, from EIA and 451 Research by S&amp;P Global. Also reported today by Fortune.</div>
</div>
<div class="panel">
  <div class="ph">HOW FAST EACH HAS GROWN &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THE<br><span class="y">RECORD SHOWS</span></div>
  <div class="b"><div class="n">01</div><div><b>Ballots:</b> On Nov. 3, voters favored limiting data-center development in 40 of 41 local measures, per Ballotpedia.</div></div>
  <div class="b"><div class="n">02</div><div><b>Costs:</b> A Cornell study found data centers paid 38% of 2025 infrastructure costs tied to their growth, $3.12B of $8.25B.</div></div>
  <div class="b"><div class="n">03</div><div><b>Jobs:</b> The same study found each gigawatt of data-center capacity can create 15,000 jobs across the economy.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0b1f4a 0%,#0a1430 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:16px;letter-spacing:.14em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:126px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:72px;line-height:.92;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:24px;line-height:1.05;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:12px;width:470px}
.vs,.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:108px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #ffcc00;padding:12px 16px 10px}
.ph{font-family:'Archivo Black',sans-serif;font-size:13px;letter-spacing:.16em;color:#8a867c;margin-bottom:8px}
.panel svg{display:block}
.strip{position:absolute;left:48px;right:48px;top:470px;height:150px;z-index:5;background:rgba(14,14,18,.94);border-top:4px solid #ffcc00;display:grid;grid-template-columns:150px 1fr 1fr 1fr;gap:18px;padding:16px 22px}
.wt{font-family:'Anton',sans-serif;font-size:36px;line-height:.92;color:#f4f0e6}
.b{display:flex;gap:10px;font-weight:600;font-size:16.5px;line-height:1.18;color:#c8c4ba}
.b b{color:#ffcc00;font-weight:800}
.n{font-family:'Anton',sans-serif;font-size:28px;line-height:.9;color:#ff2d2a}
.footer span{line-height:1.3}
.footer{font-size:11px}
""")

def render(html):
    out_html = OUT / f"{NAME}.html"
    out_html.write_text(html)
    png = OUT / "card.png"
    r = subprocess.run([
        "google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu",
        "--hide-scrollbars", "--force-device-scale-factor=2",
        "--window-size=1200,675", f"--screenshot={png}",
        "file://" + str(out_html),
    ], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("render failed: " + r.stderr[-800:])
    out_html.unlink()
    return png

src = render(html)
print(src, src.stat().st_size)
