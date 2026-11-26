#!/usr/bin/env python3
"""Daily three-circle card, Nov 26, 2026. Thread: the Thanksgiving storm."""
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
  <div class="h1">THE<br><span class="y">THANKSGIVING STORM.</span></div>
  <div class="it"><div class="n r">01</div><div><b>850,000+ without power</b><br>More than 850,000 homes and businesses lost power as of 5 p.m. ET, led by Virginia, Maryland and Pennsylvania, per PowerOutage.us.</div></div>
  <div class="it"><div class="n y">02</div><div><b>420+ flights canceled</b><br>Nearly 2,000 more were delayed, per FlightAware. Airports serving Washington and New York were among the hardest hit.</div></div>
  <div class="it"><div class="n bl">03</div><div><b>Macy&rsquo;s parade moved</b><br>The 100th parade moved to Saturday, 8:30 a.m. ET, its first weather postponement, with gusts up to 65 mph forecast.</div></div>
</div>
<div class="lab la" style="left:640px;top:200px"><span class="r">850,000+<br>WITHOUT POWER</span></div>
<div class="lab la" style="left:940px;top:200px"><span class="y">420+ FLIGHTS<br>CANCELED</span></div>
<div class="lab la" style="left:790px;top:505px"><span class="bl">MACY&rsquo;S PARADE<br>MOVED TO SAT.</span></div>
<div class="lab ov" style="left:790px;top:222px">D.C. AREA<br>HIT HARD</div>
<div class="lab ov" style="left:712px;top:372px">WIND GUSTS<br>UP TO<br>65 MPH</div>
<div class="lab ov" style="left:868px;top:372px">STORM<br>HITS<br>NEW YORK</div>
<div class="lab ctr" style="left:790px;top:312px">THE<br>THANKSGIVING<br>STORM</div>
<div class="footer"><span>Nov 26, 2026. Sources: Power: PowerOutage.us via The Hill and NBC News; AP &middot; Flights: FlightAware via The Hill and NBC News &middot; Parade: Macy&rsquo;s via AP, NBC News &middot; Overlaps: D.C. area hit hard: The Hill (Va./Md. outages, D.C. airports); gusts up to 65 mph: NBC News (NYC forecast), Reuters/National Weather Service; storm hits New York: The Hill (NYC airports), AP</span></div>
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
out_html = HERE/"cards"/"html"/"daily-venn-2026-11-26.html"; out_html.parent.mkdir(parents=True, exist_ok=True)
out_html.write_text(html)
png = HERE/"cards"/"daily-venn-2026-11-26.png"
r = subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=2","--window-size=1200,675",f"--screenshot={png}","file://"+str(out_html)],capture_output=True,text=True)
print("chrome rc", r.returncode)
if r.stderr:
    print("stderr", r.stderr[-500:])
for dest in [Path("/home/box/whip/daily-venn/2026-11-26/card.png"), Path("/workspace/whip-cards/2026-11-26-daily-venn/card.png")]:
    dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy(png, dest); print("copied", dest)
# also copy script and post into the repo folder
repo = Path("/workspace/whip-cards/2026-11-26-daily-venn")
src = Path("/home/box/whip/daily-venn/2026-11-26")
for name in ("make_card.py", "post.txt", "NOTES.md"):
    f = src / name
    if f.exists():
        shutil.copy(f, repo / name)
        print("copied", repo / name)
