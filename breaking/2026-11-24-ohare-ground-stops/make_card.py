#!/usr/bin/env python3
"""UPDATE card: O'Hare ground stops two days running (Nov 23 staffing at Chicago TRACON; Nov 24 equipment, surface radar outage).
Sources: NBC Chicago (Nov 24), Chicago Sun-Times (Nov 23, FAA statement). Draft only. Whip illustration, schematic not a map. No Whip scores."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-ohare-ground-stops"
FOLDER = "breaking/2026-11-24-ohare-ground-stops"
W, H = 568, 300
RED, YEL, BLU, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#f4f0e6", "#8a867c"
p = []
p.append(f'<text x="0" y="18" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">TUESDAY&rsquo;S STOP &middot; FLIGHTS HELD FROM</text>')
p.append(f'<text x="0" y="36" font-family="Inter" font-size="12" font-weight="600" fill="{MUTE}">Schematic, not to scale, not a map</text>')
ox, oy = 420, 120
p.append(f'<circle cx="{ox}" cy="{oy}" r="30" fill="{RED}" stroke="{YEL}" stroke-width="3"/><text x="{ox}" y="{oy+8}" text-anchor="middle" font-family="Anton" font-size="22" fill="{PAPER}">ORD</text>')
cities = [("MSP", 60, 62), ("GRB", 250, 52), ("MKE", 300, 188), ("DSM", 70, 170)]
for c, x, y in cities:
    p.append(f'<line x1="{x+30}" y1="{y}" x2="{ox-34}" y2="{oy}" stroke="{YEL}" stroke-width="2.5" stroke-dasharray="7 6"/>')
    p.append(f'<rect x="{x-26}" y="{y-16}" width="56" height="30" rx="3" fill="#2a2a32" stroke="#4a4a54"/><text x="{x+2}" y="{y+6}" text-anchor="middle" font-family="Anton" font-size="18" fill="{PAPER}">{c}</text>')
    mx, my = (x+30+ox-34)/2, (y+oy)/2
    p.append(f'<text x="{mx}" y="{my+5}" text-anchor="middle" font-family="Archivo Black" font-size="15" fill="{RED}">&#10005;</text>')
y0 = 212
p.append(f'<rect x="0" y="{y0}" width="272" height="80" fill="#1d1d24" stroke="#4a4a54"/><rect x="290" y="{y0}" width="278" height="80" fill="#1d1d24" stroke="{YEL}" stroke-width="2"/>')
p.append(f'<text x="12" y="{y0+22}" font-family="Archivo Black" font-size="13" fill="{PAPER}">MON., NOV. 23 &middot; STAFFING</text>')
p.append(f'<text x="12" y="{y0+44}" font-family="Inter" font-size="12" font-weight="600" fill="#c8c4ba">Arrivals paused ~10:40 a.m.&ndash;12:15 p.m. CT</text>')
p.append(f'<text x="12" y="{y0+62}" font-family="Inter" font-size="12" font-weight="600" fill="#c8c4ba">Staffing at Chicago TRACON, FAA said</text>')
p.append(f'<text x="302" y="{y0+22}" font-family="Archivo Black" font-size="13" fill="{YEL}">TUE., NOV. 24 &middot; EQUIPMENT</text>')
p.append(f'<text x="302" y="{y0+44}" font-family="Inter" font-size="12" font-weight="600" fill="#c8c4ba">Surface radar outage on some runways</text>')
p.append(f'<text x="302" y="{y0+62}" font-family="Inter" font-size="12" font-weight="600" fill="#c8c4ba">Stop set until 4:15 p.m., per NBC Chicago</text>')
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(p)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: NBC Chicago (Nov. 24, 2026); FAA via Chicago Sun-Times (Nov. 23). Illustration.</span><span>Whip illustration &middot; not an FAA graphic or flight tracker</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; AIR TRAVEL</div>
<div class="left">
  <div class="h1">O&rsquo;HARE<br><span class="y">STOPPED AGAIN</span></div>
  <div class="h2">2 GROUND STOPS<br>IN 2 DAYS</div>
  <div class="att">The FAA issued a ground stop at Chicago O&rsquo;Hare Tuesday afternoon after a surface radar outage on some runways, per NBC Chicago. Monday&rsquo;s stop was due to staffing constraints at Chicago TRACON, the FAA said.</div>
  <div class="chips"><span>Thanksgiving week</span><span>Equipment + staffing</span></div>
</div>
<div class="panel">
  <div class="ph">TWO DAYS AT ORD &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>Tuesday:</b> flights from Minneapolis, Milwaukee, Green Bay and Des Moines held while technicians repaired radar.</div></div>
  <div class="b"><div class="n">02</div><div><b>Monday:</b> arrivals paused about 90 minutes over staffing at Chicago TRACON, the FAA said.</div></div>
  <div class="b"><div class="n">03</div><div><b>Context:</b> it comes 11 days after the Nov. 13 nationwide ground stop, ahead of December hearings.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#3a2a05 0%,#22180a 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:74px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:28px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.chips{display:flex;gap:8px;margin-top:12px}
.chips span{font-family:'Archivo Black',sans-serif;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#09090b;background:#ffcc00;padding:5px 9px 4px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:100px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #ffcc00;padding:12px 16px 10px}
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
for f in (src, Path(__file__).resolve()):
    if f.exists(): shutil.copy(f, dest / f.name); print("copied", dest / f.name)
