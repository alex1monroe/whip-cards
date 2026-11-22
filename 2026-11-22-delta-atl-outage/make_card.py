#!/usr/bin/env python3
"""BREAKING card: Delta weight-and-balance automation outage holds Delta flights into Atlanta (Sun Nov 22, 2026).
Sources: FOX 5 Atlanta (updated 9:58 AM ET), WSB-TV (9:14 AM ET), FAA advisory as reported by WSB-TV.
Draft only. Illustration, not a screenshot. Adapted from 2026-11-21-credit-card-cap-10pct/make_card.py."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "breaking-delta-atl-outage"
FOLDER = "2026-11-22-delta-atl-outage"
W = 568
RED, YEL = "#ff2d2a", "#ffcc00"
parts = []
# Timeline: morning ground stop -> ~8:40 AM ground delay -> ~1 PM scheduled end
y = 46
parts.append(f'<text x="0" y="16" font-family="Archivo Black" font-size="12" letter-spacing="1.6" fill="#c8c4ba">SUNDAY MORNING, ET</text>')
parts.append(f'<rect x="0" y="{y}" width="150" height="34" fill="{RED}"/>')
parts.append(f'<rect x="150" y="{y}" width="{W-150}" height="34" fill="{YEL}"/>')
parts.append(f'<text x="10" y="{y+23}" font-family="Archivo Black" font-size="13" letter-spacing="1.2" fill="#09090b">GROUND STOP</text>')
parts.append(f'<text x="160" y="{y+23}" font-family="Archivo Black" font-size="13" letter-spacing="1.2" fill="#09090b">GROUND DELAY · DELTA FLIGHTS INTO ATL</text>')
for x, lab, anchor in ((0, "MORNING", "start"), (150, "~8:40 AM", "middle"), (W, "~1 PM (SCHEDULED END)", "end")):
    parts.append(f'<line x1="{x}" y1="{y-8}" x2="{x}" y2="{y+42}" stroke="#f4f0e6" stroke-width="2"/>'
                 f'<text x="{x}" y="{y+62}" text-anchor="{anchor}" font-family="Inter" font-size="12.5" font-weight="700" fill="#f4f0e6">{lab}</text>')
# Delay bars (FlightAware via FOX 5): ~200 inbound, 164 departing
by = 150
MAX = 220.0
sx = lambda v: W * v / MAX
parts.append(f'<text x="0" y="{by}" font-family="Archivo Black" font-size="12" letter-spacing="1.6" fill="#c8c4ba">DELAYED FLIGHTS AT ATL · 364 TOTAL</text>'
             f'<text x="{W}" y="{by}" text-anchor="end" font-family="Inter" font-size="12" font-weight="600" fill="#8a867c">FlightAware, via FOX 5</text>')
for i, (v, lab, col) in enumerate(((200, "~200 INBOUND", RED), (164, "164 DEPARTING", YEL))):
    yy = by + 12 + i*44
    parts.append(f'<rect x="0" y="{yy}" width="{sx(v):.1f}" height="36" fill="{col}"/>'
                 f'<text x="10" y="{yy+25}" font-family="Anton" font-size="22" fill="#09090b">{lab}</text>')
legend = (f'<line x1="0" y1="262" x2="{W}" y2="262" stroke="#3a3a44" stroke-width="1.2" stroke-dasharray="3 5"/>'
          f'<text x="0" y="284" font-family="Archivo Black" font-size="13" letter-spacing="2" fill="{YEL}">AVG. DELAY: 57 MIN, PER FAA</text>'
          f'<text x="{W}" y="284" text-anchor="end" font-family="Inter" font-size="12.5" font-weight="600" fill="#8a867c">as of ~9:30 AM ET</text>')
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="292" viewBox="0 0 {W} 292">{"".join(parts)}{legend}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: FOX 5 Atlanta, WSB-TV, FAA advisory via WSB-TV (Nov. 22, 2026). Illustration.</span><span>Whip illustration &middot; not an FAA or Delta graphic</span></div>
<div class="tag"><span class="dot"></span>BREAKING &middot; AIR TRAVEL</div>
<div class="left">
  <div class="h1">DELTA SYSTEM<br><span class="r">OUTAGE HITS ATL</span></div>
  <div class="h2">FLIGHTS INTO ATLANTA HELD<br>THE SUNDAY BEFORE THANKSGIVING</div>
  <div class="att">Delta: &ldquo;Delta teams are using manual workarounds this morning to safely get flights departed while work continues to restore automation.&rdquo;</div>
</div>
<div class="panel">
  <div class="ph">WHAT HAPPENED THIS MORNING &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>The cause:</b> Delta&rsquo;s automated weight-and-balance system for departures went down.</div></div>
  <div class="b"><div class="n">02</div><div><b>The response:</b> FAA ground stop at Delta&rsquo;s request, eased to a ground delay.</div></div>
  <div class="b"><div class="n">03</div><div><b>The stakes:</b> 4M+ people expected through ATL over Thanksgiving, per FOX 5.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#3a0b10 0%,#22080c 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ff2d2a;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:74px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:28px;line-height:1.02;color:#f4f0e6;margin-top:8px}
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
