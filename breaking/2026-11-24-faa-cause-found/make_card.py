#!/usr/bin/env python3
"""UPDATE card: FAA probe recreates Nov. 13 ground stop failure in a lab; overlooked router setting (CNN exclusive, Rene Marsh, Nov 24, 2026).
Source: CNN via ABC17 https://abc17news.com/politics/national-politics/cnn-us-politics/2026/11/24/exclusive-faa-probe-zeros-in-on-culprit-of-nationwide-ground-stop-but-agency-still-faces-tough-questions/
Draft only. Whip illustration. No Whip scores. No hook."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-faa-cause-found"
FOLDER = "breaking/2026-11-24-faa-cause-found"
W, H = 568, 300
GRN, YEL, RED, BLU, PAPER, MUTE = "#2fd28a", "#ffcc00", "#ff2d2a", "#3d8bff", "#f4f0e6", "#8a867c"
p = []
p.append(f'<text x="0" y="18" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">WHAT INVESTIGATORS FOUND</text>')
# node boxes
def box(x, y, w, h, col, t1, t2, t3):
    p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#14141a" stroke="{col}" stroke-width="2.5"/>')
    p.append(f'<text x="{x+w/2}" y="{y+30}" text-anchor="middle" font-family="Anton" font-size="21" fill="{col}">{t1}</text>')
    p.append(f'<text x="{x+w/2}" y="{y+52}" text-anchor="middle" font-family="Inter" font-size="12" font-weight="700" fill="{PAPER}">{t2}</text>')
    p.append(f'<text x="{x+w/2}" y="{y+70}" text-anchor="middle" font-family="Inter" font-size="11" font-weight="600" fill="#c8c4ba">{t3}</text>')
box(0, 34, 168, 84, YEL, "NEW ROUTER", "Remote radio site", "El Dorado, Ark.")
box(200, 34, 168, 84, MUTE, "OLD ROUTERS", "Decades-old", "Being retired by FAA")
box(400, 34, 168, 84, RED, "DATA FLOOD", "Radar &amp; radio gaps", "Nationwide ground stop")
for x1 in (168, 368):
    p.append(f'<line x1="{x1+4}" y1="76" x2="{x1+22}" y2="76" stroke="{PAPER}" stroke-width="3"/>')
    p.append(f'<polygon points="{x1+22},70 {x1+30},76 {x1+22},82" fill="{PAPER}"/>')
p.append(f'<text x="184" y="140" text-anchor="middle" font-family="Archivo Black" font-size="11" letter-spacing="1" fill="{YEL}">OVERLOOKED SETTING</text>')
# timeline
ty = 196
p.append(f'<line x1="20" y1="{ty}" x2="548" y2="{ty}" stroke="#4a4a54" stroke-width="3"/>')
steps = [("NOV. 13", "GROUND STOP", "Router swap in Arkansas", RED),
         ("NOV. 24", "LAB FINDINGS", "Reported by CNN", YEL),
         ("NEXT WEEK", "HEARINGS", "Duffy, Bedford testify", BLU)]
for i, (d, h, s, col) in enumerate(steps):
    x = 20 + i * 264
    last = i == 2
    p.append(f'<circle cx="{x}" cy="{ty}" r="{12 if i==1 else 9}" fill="{col}" stroke="{PAPER}" stroke-width="2"/>')
    anchor = "start" if i == 0 else ("end" if last else "middle")
    xx = x - 12 if i == 0 else (x + 12 if last else x)
    p.append(f'<text x="{xx}" y="{ty+32}" text-anchor="{anchor}" font-family="Archivo Black" font-size="13" fill="{YEL if i==1 else PAPER}">{d}</text>')
    p.append(f'<text x="{xx}" y="{ty+54}" text-anchor="{anchor}" font-family="Anton" font-size="19" fill="{PAPER}">{h}</text>')
    p.append(f'<text x="{xx}" y="{ty+72}" text-anchor="{anchor}" font-family="Inter" font-size="11.5" font-weight="600" fill="#c8c4ba">{s}</text>')
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(p)}</svg>'
html = wrap(f"""
<div class="footer"><span>Source: CNN (Ren&eacute; Marsh), citing a source familiar with the investigation, Nov. 24, 2026. FAA statement via CNN.</span><span>Whip illustration &middot; not an FAA or news graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; AIR TRAVEL</div>
<div class="left">
  <div class="h1">GROUND STOP<br><span class="y">CAUSE FOUND?</span></div>
  <div class="h2">FAILURE RECREATED<br>IN A LAB</div>
  <div class="att">Investigators recreated the Nov. 13 failure and believe an overlooked setting on a new router at an Arkansas radio site clashed with decades-old FAA routers, flooding the system with data, a source told CNN. A report is being prepared.</div>
  <div class="chips"><span>Patches expected</span><span>Not final yet</span></div>
</div>
<div class="panel">
  <div class="ph">HOW IT FAILED &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>The cause:</b> an overlooked router setting, per the source. The source says it likely was not an attack; the FBI took part.</div></div>
  <div class="b"><div class="n">02</div><div><b>The fix:</b> software updates, which investigators believe will prevent a repeat. Router upgrades were paused during the probe.</div></div>
  <div class="b"><div class="n">03</div><div><b>Next:</b> Duffy and Bedford face Capitol Hill hearings next week. The FAA says contractor L3Harris owns and maintains the network.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0a2a4a 0%,#0a1a2e 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:74px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:28px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.chips{display:flex;gap:8px;margin-top:12px}
.chips span{font-family:'Archivo Black',sans-serif;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#09090b;background:#2fd28a;padding:5px 9px 4px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:100px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #3d8bff;padding:12px 16px 10px}
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
for f in (src, Path(__file__).resolve()):
    if f.exists(): shutil.copy(f, dest / f.name); print("copied", dest / f.name)
