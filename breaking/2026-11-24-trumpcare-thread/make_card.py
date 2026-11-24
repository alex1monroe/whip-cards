#!/usr/bin/env python3
"""Thread card (post 1): The name vs. the bill — TrumpCare / Medicare for All.
Tue Nov 24, 2026. Ranks and % moves only; no Whip scores.
Whip /civic/issues pulled 7:46 AM ET Nov 24; data day Nov 23; attention moves are Nov 21 to Nov 22.
Sources: NBC News Nov 21; FOX 2 Detroit Nov 21; Fox News Nov 17; USA Today Nov 23;
AP via PBS News Nov 13; Rand Paul Nov 22; Hasan Piker Nov 23; White House CEA Oct 2026 /
House Budget Committee Oct 20. Illustration."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "trumpcare-thread"
FOLDER = "breaking/2026-11-24-trumpcare-thread"
RED, YEL, BLU, INK, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#09090b", "#f4f0e6", "#8a867c"
html = wrap(f"""
<div class="footer"><span>Sources: NBC News; FOX 2 Detroit; Fox News; USA Today; AP via PBS News; Rand Paul; Hasan Piker; White House CEA / House Budget Committee. Whip /civic/issues pulled 7:46 AM ET Nov. 24; data day Nov. 23; attention moves Nov. 21&ndash;22. Ranks and % moves only; no scores. Illustration.</span><span>Whip illustration &middot; not a news graphic</span></div>
<div class="tag">HEALTH CARE</div>
<div class="left">
  <div class="h1">THE NAME<br><span class="y">VS. THE BILL</span></div>
  <div class="att">Washington spent the weekend arguing over &ldquo;TrumpCare.&rdquo; As of Nov. 23, health care costs ranked No. 1 of the 60 issues Whip tracks.</div>
</div>
<div class="panel">
  <div class="cols">
    <div class="box name">
      <div class="bh">THE NAME</div>
      <div class="row"><div class="k">NOV 12&ndash;17</div><div>El-Sayed pitches a gold &ldquo;TrumpCare&rdquo; card for universal coverage (AP, NBC, FOX 2).</div></div>
      <div class="row"><div class="k">NOV 21</div><div>Trump reposts it on Truth Social with no comment (NBC, FOX 2, USA Today).</div></div>
      <div class="row"><div class="k">NOV 17</div><div>The White House had already blasted the idea (Fox News).</div></div>
    </div>
    <div class="box bill">
      <div class="bh">THE BILL</div>
      <div class="row"><div class="k yel">NOV 23</div><div>As of Nov. 23, health care costs ranked <b>No. 1 of 60</b> issues Whip tracks.</div></div>
      <div class="row"><div class="k red">NOV 22</div><div>Medicare for All attention <b>up 99%</b> from Nov. 21.</div></div>
      <div class="row"><div class="k">NOV 22</div><div>Health care costs attention <b>down 3.4%</b> from Nov. 21.</div></div>
    </div>
  </div>
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">SHOWS</span></div>
  <div class="b"><div class="n">01</div><div><b>The pitch:</b> Brand Medicare for All as &ldquo;TrumpCare,&rdquo; gold card and all.</div></div>
  <div class="b"><div class="n">02</div><div><b>The other side:</b> Hasan Piker vs. Sen. Rand Paul&rsquo;s ~$47 trillion post; a White House 10-year estimate is $47.4 trillion.</div></div>
  <div class="b"><div class="n">03</div><div><b>Whip:</b> The bill still ranks No. 1 as of Nov. 23. Attention moves above are Nov. 22.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 72% 38%,#2a1f05 0%,#120d04 45%,#09090b 80%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.left{position:absolute;left:48px;top:126px;width:430px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:62px;line-height:.95;color:#f4f0e6;letter-spacing:.01em}
.att{font-family:'Inter',sans-serif;font-size:16px;line-height:1.35;color:#c8c4ba;margin-top:16px;width:410px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:110px;width:660px;z-index:5}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.box{background:rgba(10,14,18,.88);border-top:4px solid #ffcc00;padding:12px 14px 10px}
.box.bill{border-top-color:#ff2d2a}
.bh{font-family:'Archivo Black',sans-serif;font-size:15px;letter-spacing:.16em;color:#ffcc00;margin-bottom:8px}
.box.bill .bh{color:#ff4a47}
.row{display:grid;grid-template-columns:86px 1fr;gap:8px;padding:8px 0;border-top:1px solid #25252b;font-family:'Inter',sans-serif;font-size:13.5px;line-height:1.3;color:#c8c4ba}
.k{font-family:'Archivo Black',sans-serif;font-size:11px;letter-spacing:.08em;color:#8a867c;padding-top:2px}
.k.yel{color:#ffcc00}
.k.red{color:#ff4a47}
.row b{color:#f4f0e6;font-weight:800}
.strip{position:absolute;left:48px;right:48px;top:470px;height:150px;z-index:5;background:rgba(14,14,18,.94);border-top:4px solid #ffcc00;display:grid;grid-template-columns:150px 1fr 1fr 1fr;gap:18px;padding:16px 22px}
.wt{font-family:'Anton',sans-serif;font-size:40px;line-height:.92;color:#f4f0e6}
.b{display:flex;gap:10px;font-weight:600;font-size:16.5px;line-height:1.16;color:#c8c4ba}
.b b{color:#ffcc00;font-weight:800}
.n{font-family:'Anton',sans-serif;font-size:30px;line-height:.9;color:#ff2d2a}
.footer{align-items:flex-start;bottom:10px;font-size:10px;line-height:1.4;padding-top:8px}
.footer span:first-child{max-width:980px;padding-right:16px}
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
    if f.exists():
        shutil.copy(f, dest / f.name)
        print("copied", dest / f.name)
