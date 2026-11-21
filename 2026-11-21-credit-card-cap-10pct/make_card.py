#!/usr/bin/env python3
"""BREAKING card: Trump says he would work with Democrats on a one-year 10% credit card rate cap (Nov 21, 2026; Fox News/Saturday in America).
Context number: Federal Reserve G.19 (released Nov 6, 2026), commercial bank credit card plans, accounts assessed interest, Q3 2026 = 22.36%.
Draft only. Illustration, not a screenshot. Adapted from 2026-11-20-fbi-ncic-breach/make_card.py."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "breaking-credit-card-cap-10pct"
FOLDER = "2026-11-21-credit-card-cap-10pct"
W = 568
RED, YEL, GRY = "#ff2d2a", "#ffcc00", "#4a4a54"
# APR bars: Fed G.19 Q3 2026 average (accounts assessed interest) vs proposed 10% cap; axis 0-25%
X0, X1, MAX = 0, W, 25.0
sx = lambda v: X0 + (X1-X0)*v/MAX
parts = []
for t in (0, 5, 10, 15, 20, 25):
    x = sx(t); anchor = "start" if t == 0 else ("end" if t == 25 else "middle")
    parts.append(f'<line x1="{x}" y1="20" x2="{x}" y2="186" stroke="#26262c" stroke-width="1"/>'
                 f'<text x="{x}" y="204" text-anchor="{anchor}" font-family="Inter" font-size="11.5" font-weight="600" fill="#6c6a64">{t}%</text>')
bars = [(28, 22.36, RED, "AVG. APR, CARDS CHARGED INTEREST", "22.36%", "Fed G.19, Q3 2026"),
        (110, 10.0, YEL, "PROPOSED ONE-YEAR CAP", "10%", "Trump on Fox, Nov. 21")]
for y, v, col, lab, val, src in bars:
    parts.append(f'<text x="0" y="{y}" font-family="Archivo Black" font-size="12" letter-spacing="1.6" fill="#c8c4ba">{lab}</text>'
                 f'<rect x="0" y="{y+8}" width="{sx(v):.1f}" height="44" fill="{col}"/>'
                 f'<text x="{sx(v)-10:.1f}" y="{y+42}" text-anchor="end" font-family="Anton" font-size="32" fill="#09090b">{val}</text>'
                 f'<text x="{W}" y="{y}" text-anchor="end" font-family="Inter" font-size="12" font-weight="600" fill="#8a867c">{src}</text>')
# gap bracket
parts.append(f'<line x1="{sx(10)}" y1="170" x2="{sx(22.36)}" y2="170" stroke="#f4f0e6" stroke-width="2" stroke-dasharray="5 4"/>'
             f'<text x="{(sx(10)+sx(22.36))/2}" y="164" text-anchor="middle" font-family="Archivo Black" font-size="11" letter-spacing="1.4" fill="#f4f0e6">GAP: 12.36 PTS</text>')
legend = (f'<line x1="0" y1="226" x2="{W}" y2="226" stroke="#3a3a44" stroke-width="1.2" stroke-dasharray="3 5"/>'
          f'<text x="0" y="252" font-family="Archivo Black" font-size="13" letter-spacing="2" fill="{YEL}">Q3 2026 = JUL–SEP · COMMERCIAL BANK CARD PLANS</text>'
          f'<text x="0" y="276" font-family="Archivo Black" font-size="13" letter-spacing="2" fill="{RED}">JAN. 3: DEMOCRATS TAKE BOTH CHAMBERS</text>'
          f'<text x="{W}" y="276" text-anchor="end" font-family="Inter" font-size="12.5" font-weight="600" fill="#8a867c">per AP, NBC News</text>')
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="288" viewBox="0 0 {W} 288">{"".join(parts)}{legend}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: Fox News / Saturday in America (Nov. 21, 2026); Federal Reserve G.19 (Nov. 6, 2026), Q3 2026; AP, NBC News. Illustration.</span><span>Whip illustration &middot; not a Fed or Fox graphic</span></div>
<div class="tag"><span class="dot"></span>BREAKING &middot; CREDIT CARDS</div>
<div class="left">
  <div class="h1">A 10% CAP<br><span class="r">ON CARD RATES?</span></div>
  <div class="h2">TRUMP SAYS HE&rsquo;D WORK WITH<br>DEMOCRATS ON A ONE-YEAR CAP</div>
  <div class="att">Asked on Fox News&rsquo; &ldquo;Saturday in America&rdquo; if a one-year 10% cap is a place to work with Democrats: &ldquo;It is&hellip; I would do it.&rdquo;</div>
</div>
<div class="panel">
  <div class="ph">CURRENT AVERAGE VS. PROPOSED CAP &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>The idea:</b> card interest capped at 10% for one year, per the Fox interview.</div></div>
  <div class="b"><div class="n">02</div><div><b>Today:</b> cards charged interest averaged 22.36% in Q3, per the Fed.</div></div>
  <div class="b"><div class="n">03</div><div><b>Next step:</b> a cap needs Congress; Democrats hold 56 Senate seats from Jan. 3.</div></div>
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
