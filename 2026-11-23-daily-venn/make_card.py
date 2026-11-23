#!/usr/bin/env python3
"""Daily three-circle card, Nov 23, 2026. Megaspeed listing now confirmed via FR 2026-23999."""
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
  <div class="h1">U.S. CHIP<br><span class="y">EXPORTS TO CHINA.</span></div>
  <div class="it"><div class="n r">01</div><div><b>U.S. blacklists Megaspeed</b><br>Commerce added the Singapore firm tied to the Nvidia probe to the Entity List; U.S. sellers need a license. Megaspeed has denied wrongdoing.</div></div>
  <div class="it"><div class="n y">02</div><div><b>Nvidia brings back Jensen Huang</b><br>The board reinstated him as CEO, saying senior U.S. officials gave input and his return poses no national security risk.</div></div>
  <div class="it"><div class="n bl">03</div><div><b>Huang to testify Dec. 3</b><br>Senate Banking Chair Tim Scott set a public hearing, &ldquo;Oversight of U.S. Export Controls,&rdquo; with Huang the only witness.</div></div>
</div>
<div class="lab la" style="left:640px;top:200px"><span class="r">MEGASPEED<br>BLACKLISTED</span></div>
<div class="lab la" style="left:940px;top:200px"><span class="y">HUANG BACK<br>AS CEO</span></div>
<div class="lab la" style="left:790px;top:505px"><span class="bl">SENATE<br>HEARING DEC. 3</span></div>
<div class="lab ov" style="left:790px;top:222px">MEGASPEED IS<br>TIED TO THE<br>NVIDIA PROBE</div>
<div class="lab ov" style="left:706px;top:378px">BOTH ON U.S.<br>CHIP EXPORT<br>CONTROLS</div>
<div class="lab ov" style="left:874px;top:378px">HUANG IS THE<br>ONLY WITNESS</div>
<div class="lab ctr" style="left:790px;top:312px">U.S. CHIPS<br>AND CHINA</div>
<div class="footer"><span>Nov 23, 2026. Sources: Megaspeed listing: Commerce/BIS, Federal Register (Doc. 2026-23999, filed 4:15 p.m. ET) &middot; Denial: Reuters, CBS News &middot; Tied to Nvidia probe: Reuters &middot; Huang reinstated: Nvidia release (GlobeNewswire), WSJ &middot; Hearing: Sen. Tim Scott notice via The Hill, Bloomberg Law &middot; Overlaps: Megaspeed/Nvidia probe: Reuters; export controls: Commerce Entity List (FR 2026-23999) and hearing title (The Hill); sole witness: The Hill</span></div>
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
out_html = HERE/"cards"/"html"/"daily-venn-2026-11-23.html"; out_html.parent.mkdir(parents=True, exist_ok=True)
out_html.write_text(html)
png = HERE/"cards"/"daily-venn-2026-11-23.png"
r = subprocess.run(["google-chrome","--headless=new","--no-sandbox","--disable-gpu","--hide-scrollbars","--force-device-scale-factor=2","--window-size=1200,675",f"--screenshot={png}","file://"+str(out_html)],capture_output=True,text=True)
print("chrome rc", r.returncode)
if r.stderr:
    print("stderr", r.stderr[-500:])
for dest in [Path("/home/box/whip/daily-venn/2026-11-23/card.png"), Path("/workspace/whip-cards/2026-11-23-daily-venn/card.png")]:
    dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy(png, dest); print("copied", dest)
# also copy script and post into the repo folder
repo = Path("/workspace/whip-cards/2026-11-23-daily-venn")
src = Path("/home/box/whip/daily-venn/2026-11-23")
for name in ("make_card.py", "post.txt", "NOTES.md"):
    f = src / name
    if f.exists():
        shutil.copy(f, repo / name)
        print("copied", repo / name)
