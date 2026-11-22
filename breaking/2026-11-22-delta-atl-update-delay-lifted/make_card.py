#!/usr/bin/env python3
"""UPDATE card: FAA no longer lists a Delta ground delay program at Atlanta (Sun Nov 22, 2026).
Sources: FAA NAS status feed (nasstatus.faa.gov/api/airport-status-information, Update_Time 17:06:22 GMT = 12:06 PM ET;
user-verified 17:05:22 GMT = 12:05 PM ET), NBC News (delay program details, Delta statement).
Draft only. Illustration, not a screenshot. Adapted from 2026-11-22-delta-atl-outage/make_card.py."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-delta-atl-delay-lifted"
FOLDER = "breaking/2026-11-22-delta-atl-update-delay-lifted"
W = 568
RED, YEL, GRN, INK, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3ddc84", "#09090b", "#f4f0e6", "#8a867c"
parts = []
# Simple airport icon: control tower + plane
parts.append(f'''<g transform="translate(0,6)">
  <rect x="14" y="22" width="10" height="44" fill="{MUTE}"/>
  <path d="M4 10 h30 l-4 14 h-22 z" fill="{PAPER}"/>
  <rect x="9" y="13" width="20" height="6" fill="{INK}"/>
  <rect x="0" y="66" width="38" height="4" fill="{MUTE}"/>
</g>
<g transform="translate(60,20) scale(1.6)" fill="{YEL}">
  <path d="M2 12 l9 -1 l6 -9 h3 l-3 9 l7 -1 l2 -3 h2 l-1 5 l1 5 h-2 l-2 -3 l-7 -1 l3 9 h-3 l-6 -9 l-9 -1 z"/>
</g>
<text x="120" y="40" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">ATL · DELTA &amp; REGIONAL ARRIVALS</text>
<text x="120" y="62" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">FAA traffic program status, Sunday, Nov. 22</text>''')
# Timeline: ground stop -> ground delay -> no longer listed
ty = 128
steps = ((80, RED, "GROUND STOP", "Delta-requested"),
         (284, YEL, "GROUND DELAY", "FAA proj. avg. 57 min"),
         (488, GRN, "NOT LISTED", "FAA feed, 12:05 PM ET"))
parts.append(f'<line x1="80" y1="{ty}" x2="488" y2="{ty}" stroke="#3a3a44" stroke-width="6"/>')
parts.append(f'<line x1="80" y1="{ty}" x2="284" y2="{ty}" stroke="{RED}" stroke-width="6"/>')
parts.append(f'<line x1="284" y1="{ty}" x2="488" y2="{ty}" stroke="{YEL}" stroke-width="6"/>')
for i, (x, col, lab, sub) in enumerate(steps):
    parts.append(f'<circle cx="{x}" cy="{ty}" r="18" fill="{col}"/>'
                 f'<text x="{x}" y="{ty+6}" text-anchor="middle" font-family="Archivo Black" font-size="15" fill="{INK}">{i+1}</text>'
                 f'<text x="{x}" y="{ty+46}" text-anchor="middle" font-family="Anton" font-size="22" fill="{col}">{lab}</text>'
                 f'<text x="{x}" y="{ty+68}" text-anchor="middle" font-family="Inter" font-size="12.5" font-weight="600" fill="{PAPER}">{sub}</text>')
for x in (182, 386):
    parts.append(f'<path d="M{x-8} {ty-10} l12 10 l-12 10" fill="none" stroke="{PAPER}" stroke-width="3"/>')
legend = (f'<line x1="0" y1="232" x2="{W}" y2="232" stroke="#3a3a44" stroke-width="1.2" stroke-dasharray="3 5"/>'
          f'<text x="0" y="256" font-family="Archivo Black" font-size="13" letter-spacing="2" fill="{YEL}">FAA PROGRAMS NOW: LGA · EWR · SAN</text>'
          f'<text x="{W}" y="256" text-anchor="end" font-family="Inter" font-size="12.5" font-weight="600" fill="{MUTE}">as of 12:05 PM ET</text>')
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="264" viewBox="0 0 {W} 264">{"".join(parts)}{legend}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: FAA NAS status feed (12:05 PM ET), NBC News (Nov. 22, 2026). Illustration.</span><span>Whip illustration &middot; not an FAA, Delta or NBC graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; AIR TRAVEL</div>
<div class="left">
  <div class="h1">FAA ATL DELAY<br><span class="y">FOR DELTA ENDS</span></div>
  <div class="h2">PROGRAM NO LONGER ON<br>THE FAA&rsquo;S LIVE STATUS FEED</div>
  <div class="att">Delta said it was working to restore its automated weight-and-balance system and using manual procedures, per NBC News. It has not said the system is fully restored.</div>
</div>
<div class="panel">
  <div class="ph">HOW THE MORNING UNFOLDED &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>The status:</b> FAA no longer lists a Delta delay program at Atlanta.</div></div>
  <div class="b"><div class="n">02</div><div><b>The caveat:</b> Delta hasn&rsquo;t said its weight-and-balance system is fully restored.</div></div>
  <div class="b"><div class="n">03</div><div><b>The takeaway:</b> Check your flight status with Delta before heading out.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0b2a3a 0%,#081a22 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:74px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:28px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.y{color:#ffcc00}
.r{color:#ff2d2a}
.panel{position:absolute;right:48px;top:112px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #ffcc00;padding:12px 16px 10px}
.ph{font-family:'Archivo Black',sans-serif;font-size:13px;letter-spacing:.16em;color:#8a867c;margin-bottom:8px}
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
