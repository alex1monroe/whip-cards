#!/usr/bin/env python3
"""Daily three-circle card, Nov 25, 2026. Thread: your Thanksgiving bill."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap, render, HERE
R = 158
A = (700, 262); B = (880, 262); C = (790, 418)
svg = f"""
<svg class="venn" width="1200" height="675" viewBox="0 0 1200 675">
 <circle cx="{A[0]}" cy="{A[1]}" r="{R}" fill="#ff2d2a" fill-opacity=".20" stroke="#ff2d2a" stroke-width="4"/>
 <circle cx="{B[0]}" cy="{B[1]}" r="{R}" fill="#ffcc00" fill-opacity=".16" stroke="#ffcc00" stroke-width="4"/>
 <circle cx="{C[0]}" cy="{C[1]}" r="{R}" fill="#4aa8ff" fill-opacity=".18" stroke="#4aa8ff" stroke-width="4"/>
</svg>"""
html = wrap(svg + """
<div class="tag"><span class="dot"></span>TODAY IN THREE STORIES</div>
<div class="left">
  <div class="h1">YOUR<br><span class="y">THANKSGIVING BILL.</span></div>
  <div class="it"><div class="n r">01</div><div><b>Inflation still high</b><br>A key inflation gauge rose 3.8% in October from a year earlier, the Commerce Department said, even as gas prices eased.</div></div>
  <div class="it"><div class="n y">02</div><div><b>Gas at a March low</b><br>AAA&rsquo;s national average is about $3.59 a gallon, the lowest since March, but still above this time last year.</div></div>
  <div class="it"><div class="n bl">03</div><div><b>Thanksgiving dinner up 6%</b><br>A classic dinner for 10 costs about $58.63, the Farm Bureau&rsquo;s survey found. Turkey is up 10%.</div></div>
</div>
<div class="lab la" style="left:640px;top:200px"><span class="r">INFLATION<br>STILL HIGH</span></div>
<div class="lab la" style="left:940px;top:200px"><span class="y">GAS AT A<br>MARCH LOW</span></div>
<div class="lab la" style="left:790px;top:505px"><span class="bl">THANKSGIVING<br>DINNER UP 6%</span></div>
<div class="lab ov" style="left:790px;top:222px">GAS PRICES<br>EASED IN<br>OCTOBER</div>
<div class="lab ov" style="left:712px;top:372px">FOOD PRICES<br>ABOVE<br>LAST YEAR</div>
<div class="lab ov" style="left:868px;top:372px">HIGH DIESEL<br>RAISES<br>FOOD COSTS</div>
<div class="lab ctr" style="left:790px;top:312px">YOUR<br>THANKSGIVING<br>BILL</div>
<div class="footer"><span>Nov 25, 2026. Sources: Inflation: Commerce Dept. (BEA), AP, Reuters &middot; Gas: AAA, Yahoo Finance, GasBuddy &middot; Dinner: American Farm Bureau Federation, AP &middot; Overlaps: gas eased in October: AP; food prices above last year: USDA Economic Research Service, AP; diesel raises food costs: Farm Bureau, AP (AAA diesel data)</span></div>
""", """
body{background:radial-gradient(ellipse at 66% 50%,#1c1220 0%,#100c12 45%,#09090b 80%)}
.venn{position:absolute;left:0;top:0;z-index:2}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ff2d2a;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:17px;letter-spacing:.16em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00;display:inline-block}
.left{position:absolute;left:48px;top:128px;width:450px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:50px;line-height:.98;color:#f4f0e6;margin-bottom:22px}
.y{color:#ffcc00}.r{color:#ff4a47}.bl{color:#6cb8ff}
.it{display:flex;gap:12px;margin-bottom:14px;font-family:'Inter',sans-serif;font-size:14.5px;line-height:1.3;color:#c8c4ba;width:420px}
.it b{font-family:'Barlow Condensed',sans-serif;font-weight:800;font-size:22px;color:#f4f0e6;letter-spacing:.01em}
.n{font-family:'Anton',sans-serif;font-size:30px;line-height:1}
.lab{position:absolute;transform:translate(-50%,-50%);text-align:center;z-index:6}
.la{font-family:'Barlow Condensed',sans-serif;font-weight:900;font-size:24px;line-height:1.0;letter-spacing:.02em}
.ov{font-family:'Barlow Condensed',sans-serif;font-size:14px;font-weight:800;letter-spacing:.04em;color:#ffffff;line-height:1.05}
.ctr{font-family:'Anton',sans-serif;font-size:15px;line-height:1.05;color:#f4f0e6;background:rgba(9,9,11,.8);padding:6px 9px;border:1px solid #3a3a40}
.footer span{line-height:1.35}.footer{font-size:12px}
""")
out_html = HERE/"cards"/"html"/"daily-venn-2026-11-25.html"; out_html.parent.mkdir(parents=True, exist_ok=True)
out_html.write_text(html)
png = HERE/"cards"/"daily-venn-2026-11-25.png"
r = subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=2","--window-size=1200,675",f"--screenshot={png}","file://"+str(out_html)],capture_output=True,text=True)
print("chrome rc", r.returncode)
if r.stderr:
    print("stderr", r.stderr[-500:])
for dest in [Path("/home/box/whip/daily-venn/2026-11-25/card.png"), Path("/workspace/whip-cards/2026-11-25-daily-venn/card.png")]:
    dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy(png, dest); print("copied", dest)
# also copy script and post into the repo folder
repo = Path("/workspace/whip-cards/2026-11-25-daily-venn")
src = Path("/home/box/whip/daily-venn/2026-11-25")
for name in ("make_card.py", "post.txt", "NOTES.md"):
    f = src / name
    if f.exists():
        shutil.copy(f, repo / name)
        print("copied", repo / name)
