#!/usr/bin/env python3
"""UPDATE card: national survey David Shor shared on Nvidia bringing back Jensen Huang (Mon Nov 23, 2026).
Source: two survey charts in https://x.com/davidshor/status/2125018153885597829 (fielded Nov 23, 2026;
2,207 responses for the agree-more question, 2,223 for awareness; weighted to 2024 voters).
Pollster not printed on the charts, so not named. Illustration, not a copy. No Whip scores. No summed figures."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-nvidia-huang-poll"
FOLDER = "breaking/2026-11-23-nvidia-huang-poll"
W = 568
RED, YEL, BLU, INK, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#09090b", "#f4f0e6", "#8a867c"
# segment colors: supporters (blue), opponents (orange), not sure (grey)
SEG = [("Supporters, a lot", "#3d8bff", PAPER), ("Supporters, a little", "#8fbaff", INK),
       ("Opponents, a little", "#e8935a", INK), ("Opponents, a lot", "#d9541e", PAPER), ("Not sure", "#5a5850", PAPER)]
ROWS = [("EVERYONE", [10, 15, 15, 33, 28]), ("HARRIS", [4, 8, 12, 55, 21]), ("SWING", [9, 16, 16, 32, 26]), ("TRUMP VOTERS", [16, 21, 18, 11, 35])]
parts = []
parts.append(f'<text x="0" y="22" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">WHO DO YOU AGREE WITH MORE?</text>')
parts.append(f'<text x="0" y="44" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">Per survey charts David Shor shared Nov. 23 &#183; % of respondents</text>')
# legend (two lines)
lx, ly = 0, 70
for i, (lab, col, _) in enumerate(SEG):
    if i == 3: lx, ly = 0, 92
    parts.append(f'<rect x="{lx}" y="{ly-11}" width="12" height="12" rx="2" fill="{col}"/>')
    parts.append(f'<text x="{lx+18}" y="{ly}" font-family="Inter" font-size="13" font-weight="700" fill="#c8c4ba">{lab}</text>')
    lx += 18 + len(lab) * 7.6 + 22
LBL = 138
BW = W - LBL
y = 108
for name, vals in ROWS:
    parts.append(f'<text x="0" y="{y+26}" font-family="Archivo Black" font-size="13" letter-spacing="0.6" fill="{PAPER}">{name}</text>')
    x = LBL
    tot = sum(vals)
    for v, (lab, col, tc) in zip(vals, SEG):
        w = BW * v / tot
        parts.append(f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="40" fill="{col}" stroke="#09090b" stroke-width="1.5"/>')
        parts.append(f'<text x="{x+w/2:.1f}" y="{y+28}" text-anchor="middle" font-family="Anton" font-size="{19 if w>24 else 15}" fill="{tc}">{v}</text>')
        x += w
    y += 48
H = y - 4
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Source: survey charts David Shor posted on X, Nov. 23 &middot; 2,207 responses, weighted to 2024 voters</span><span>Whip illustration &middot; not the survey&rsquo;s chart</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; AI CHIPS</div>
<div class="left">
  <div class="h1">MORE SIDE WITH<br><span class="y">THE OPPONENTS</span></div>
  <div class="h2">NEW SURVEY ON NVIDIA<br>BRINGING BACK HUANG</div>
  <div class="att">The question&rsquo;s premise: Trump pushed Nvidia&rsquo;s board to bring back Huang and said he gave it assurances about Huang&rsquo;s legal standing. Supporters say Huang hasn&rsquo;t been charged and Nvidia must run at full strength to stay ahead of China. Opponents say a president shouldn&rsquo;t pick who runs a private company.</div>
</div>
<div class="panel">
  <div class="ph">THE SURVEY &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">SHOWS</span></div>
  <div class="b"><div class="n">01</div><div><b>Largest group:</b> 33% of everyone agree &ldquo;a lot more&rdquo; with the opponents.</div></div>
  <div class="b"><div class="n">02</div><div><b>Unsure:</b> 28% of everyone and 35% of Trump voters say &ldquo;not sure.&rdquo;</div></div>
  <div class="b"><div class="n">03</div><div><b>Awareness:</b> 26% say they heard &ldquo;a lot&rdquo; about Huang&rsquo;s return (2,223 responses).</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#14401a 0%,#0b2410 45%,#09090b 82%)}
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
