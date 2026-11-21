#!/usr/bin/env python3
"""UPDATE card: Trump reacts on Fox News to reported FBI NCIC breach (Nov 21, 2026; Fox News/Saturday in America, NBC News, CNN).
Draft only. Illustration, not a screenshot. Adapted from 2026-11-20-fbi-ncic-breach/make_card.py."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-ncic-trump-reacts"
FOLDER = "2026-11-21-ncic-update-trump-reacts"
W = 568
RED, YEL, GRY = "#ff2d2a", "#ffcc00", "#4a4a54"
# timeline diagram: how the story has moved (all times ET)
steps = [("NOV 20 · 9:26 PM", "CNN REPORTS", "FBI probing", "apparent breach"),
         ("NOV 20 · 11:19 PM", "NBC NEWS", "People briefed", "confirm probe"),
         ("NOV 21 · ~10:10 AM", "TRUMP ON FOX", "\u201cIt\u2019s not good.", "I don\u2019t like that.\u201d"),
         ("AS OF NOW", "FBI", "No public", "comment")]
parts = [f'<line x1="{W/8}" y1="70" x2="{W*7/8}" y2="70" stroke="{GRY}" stroke-width="3"/>']
step = W/4
for i, (t, who, l1, l2) in enumerate(steps):
    x = W/8 + i*step
    hot = i == 2
    col = RED if hot else ("#c8c4ba" if i < 2 else YEL)
    parts.append(f'<circle cx="{x}" cy="70" r="{15 if hot else 10}" fill="{"#3a1014" if hot else "#16161b"}" stroke="{col}" stroke-width="3"/>')
    anchor = "middle"
    parts.append(f'<text x="{x}" y="34" text-anchor="{anchor}" font-family="Archivo Black" font-size="10" letter-spacing="0.8" fill="#8a867c">{t}</text>')
    parts.append(f'<text x="{x}" y="112" text-anchor="{anchor}" font-family="Anton" font-size="{24 if hot else 20}" fill="{col}">{who}</text>')
    parts.append(f'<text x="{x}" y="136" text-anchor="{anchor}" font-family="Inter" font-size="13" font-weight="600" fill="#c8c4ba">{l1}</text>')
    parts.append(f'<text x="{x}" y="154" text-anchor="{anchor}" font-family="Inter" font-size="13" font-weight="600" fill="#c8c4ba">{l2}</text>')
legend = (f'<line x1="0" y1="196" x2="{W}" y2="196" stroke="#3a3a44" stroke-width="1.2" stroke-dasharray="3 5"/>'
          f'<text x="0" y="224" font-family="Archivo Black" font-size="13" letter-spacing="2" fill="{YEL}">NCIC: WARRANTS &amp; BACKGROUND CHECKS</text>'
          f'<text x="0" y="250" font-family="Archivo Black" font-size="13" letter-spacing="2" fill="{RED}">STILL UNREPORTED: WHO, AND WHAT WAS ACCESSED</text>'
          f'<text x="0" y="276" font-family="Inter" font-size="12.5" font-weight="600" fill="#8a867c">Times ET. Trump call-in time approximate.</text>')
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="288" viewBox="0 0 {W} 288">{"".join(parts)}{legend}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: Fox News / Saturday in America (Nov. 21), NBC News, CNN (Nov. 20, 2026). Illustration.</span><span>Whip illustration &middot; not an FBI or Fox graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; FBI DATABASE</div>
<div class="left">
  <div class="h1">&ldquo;IT&rsquo;S<br><span class="r">NOT GOOD.&rdquo;</span></div>
  <div class="h2">TRUMP REACTS TO REPORTED<br>HACK OF FBI CRIME DATABASE</div>
  <div class="att">President Trump on Fox News&rsquo; &ldquo;Saturday in America,&rdquo; Nov. 21: &ldquo;It&rsquo;s not good. I don&rsquo;t like that.&rdquo; NBC News and CNN report the FBI is investigating an apparent NCIC breach.</div>
</div>
<div class="panel">
  <div class="ph">HOW THE STORY MOVED &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>On record:</b> the president called the reported breach &ldquo;not good&rdquo; on Fox News.</div></div>
  <div class="b"><div class="n">02</div><div><b>Under review:</b> the FBI is investigating, per NBC News and CNN, citing people briefed.</div></div>
  <div class="b"><div class="n">03</div><div><b>Open questions:</b> who did it and what was accessed have not been reported.</div></div>
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
