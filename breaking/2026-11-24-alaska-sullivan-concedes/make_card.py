#!/usr/bin/env python3
"""UPDATE card: Sen. Dan Sullivan (R) concedes Alaska Senate race to Mary Peltola (D), Tue Nov 24, 2026.
Sources: Anchorage Daily News (Nov 23 certification story; Nov 24 concession story). AP call ~Nov 17; DOJ dropped suit Nov 19 (AP).
Draft only. Whip illustration. No Whip scores. No hook."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-alaska-sullivan-concedes"
FOLDER = "breaking/2026-11-24-alaska-sullivan-concedes"
W, H = 568, 300
RED, YEL, BLU, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#f4f0e6", "#8a867c"
parts = []
parts.append(f'<text x="0" y="20" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">CERTIFIED RESULT &middot; ALASKA U.S. SENATE</text>')
rows = [("Mary Peltola (D)", 50.1, BLU), ("Dan Sullivan (R)", 45.8, RED), ("Gerald Heikes (R)", 2.1, MUTE), ("Dan J. Sullivan", 1.7, MUTE)]
y = 40
for name, pct, col in rows:
    w = pct / 55 * 330
    parts.append(f'<text x="0" y="{y+17}" font-family="Inter" font-size="14" font-weight="700" fill="{PAPER}">{name}</text>')
    parts.append(f'<rect x="150" y="{y+3}" width="{w:.1f}" height="20" fill="{col}"/>')
    parts.append(f'<text x="{150+w+8:.1f}" y="{y+19}" font-family="Anton" font-size="18" fill="{YEL if pct>50 else PAPER}">{pct}%</text>')
    y += 30
parts.append(f'<text x="0" y="{y+8}" font-family="Inter" font-size="11.5" font-weight="600" fill="{MUTE}">Outright majority, no ranked-choice tabulation. Source: Alaska Div. of Elections via ADN.</text>')
ty = y + 40
steps = [("NOV 3", "Election Day"), ("NOV 18", "Last ballots counted"), ("NOV 19", "DOJ drops appeal"), ("NOV 23", "State certifies"), ("NOV 24", "Concession")]
parts.append(f'<line x1="10" y1="{ty}" x2="550" y2="{ty}" stroke="#4a4a54" stroke-width="3"/>')
for i, (d, lab) in enumerate(steps):
    x = 10 + i * 135
    last = i == len(steps) - 1
    parts.append(f'<circle cx="{x}" cy="{ty}" r="{9 if last else 6}" fill="{YEL if last else PAPER}"/>')
    anchor = "end" if last else ("start" if i == 0 else "middle")
    xx = x + (8 if last else 0)
    parts.append(f'<text x="{xx}" y="{ty+26}" text-anchor="{anchor}" font-family="Archivo Black" font-size="12.5" fill="{YEL if last else PAPER}">{d}</text>')
    parts.append(f'<text x="{xx}" y="{ty+44}" text-anchor="{anchor}" font-family="Inter" font-size="12" font-weight="600" fill="#c8c4ba">{lab}</text>')
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: Anchorage Daily News (Nov. 23-24, 2026); AP. Illustration.</span><span>Whip illustration &middot; not an official or news graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; ELECTIONS</div>
<div class="left">
  <div class="h1">SULLIVAN<br><span class="y">CONCEDES</span></div>
  <div class="h2">PELTOLA WINS<br>ALASKA&rsquo;S SENATE SEAT</div>
  <div class="att">&ldquo;I accept the results certified by the Division of Elections,&rdquo; Republican Sen. Dan Sullivan said Tuesday, a day after Alaska certified Democrat Mary Peltola&rsquo;s win, per the Anchorage Daily News.</div>
  <div class="chips"><span>Certified Nov. 23</span><span>Conceded Nov. 24</span></div>
</div>
<div class="panel">
  <div class="ph">THE RESULT &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>Race over:</b> Sullivan accepted the certified result, a week after AP called the race.</div></div>
  <div class="b"><div class="n">02</div><div><b>First:</b> Peltola is set to be the first Alaska Native to serve in the U.S. Senate, per ADN.</div></div>
  <div class="b"><div class="n">03</div><div><b>Still open:</b> federal and state probes of the ballot-stacking allegations, which Peltola denies.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0b1f4a 0%,#0a1430 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:74px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:28px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.chips{display:flex;gap:8px;margin-top:12px}
.chips span{font-family:'Archivo Black',sans-serif;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#09090b;background:#3d8bff;padding:5px 9px 4px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:100px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #3d8bff;padding:12px 16px 10px}
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
