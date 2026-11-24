#!/usr/bin/env python3
"""BREAKING card: U.S. preparing to raise tariffs on China, EU and 14 other economies (Tue Nov 24, 2026).
Sources: WSJ Nov 24 (via WSJ on X 2125219121826549968 and Il Sole 24 Ore summary); Federal Register 2026-05214 (Mar 17, 2026: 16 economies). Illustration. No Whip scores. No rates (not public)."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "breaking-tariffs-16"
FOLDER = "breaking/2026-11-24-tariffs-16-economies"
W = 568
RED, YEL, BLU, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#f4f0e6", "#8a867c"
econ = ["China","European Union","Japan","South Korea","India","Mexico","Vietnam","Taiwan","Thailand","Malaysia","Indonesia","Singapore","Cambodia","Bangladesh","Switzerland","Norway"]
parts = [f'<text x="0" y="22" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">16 ECONOMIES IN THE SECTION 301 PROBE</text>',
         f'<text x="0" y="44" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">As listed by USTR in the Federal Register, March 17, 2026</text>']
cw, ch, gap = 134, 56, 8
for i, n in enumerate(econ):
    c, r = i % 4, i // 4
    x, y = c*(cw+gap), 62 + r*(ch+gap)
    col = RED if n == "China" else (YEL if n == "European Union" else BLU)
    parts.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="4" fill="#15151b" stroke="{col}" stroke-width="{3 if col!=BLU else 1.5}"/>')
    parts.append(f'<text x="{x+cw/2}" y="{y+34}" text-anchor="middle" font-family="Archivo Black" font-size="{11.5 if len(n)>11 else 15}" letter-spacing="0.8" fill="{PAPER}">{n.upper()}</text>')
H = 62 + 4*(ch+gap)
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: Wall Street Journal (Nov. 24); Federal Register, USTR (Mar. 17, 2026). Illustration.</span><span>Whip illustration &middot; not a government or news graphic</span></div>
<div class="tag"><span class="dot"></span>BREAKING &middot; TARIFFS</div>
<div class="left">
  <div class="h1">NEW TARIFFS<br><span class="y">BEING PREPARED</span></div>
  <div class="h2">CHINA, THE EU AND<br>14 OTHER ECONOMIES</div>
  <div class="att">The U.S. is preparing to raise tariffs after a months-long probe into government support that the administration says created &ldquo;excess capacity&rdquo; in manufacturing, per the WSJ.</div>
</div>
<div class="panel">
  <div class="ph">WHO'S IN THE PROBE &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>Who:</b> 16 economies have been under the Section 301 probe since March (Federal Register).</div></div>
  <div class="b"><div class="n">02</div><div><b>When:</b> Trade Rep. Jamieson Greer could release findings as soon as this week (WSJ).</div></div>
  <div class="b"><div class="n">03</div><div><b>Rates:</b> Final tariff rates and start dates have not been made public yet.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0b2a52 0%,#071a33 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ff2d2a;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:60px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
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
