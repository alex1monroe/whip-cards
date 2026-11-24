#!/usr/bin/env python3
"""UPDATE card: DOT Sec. Duffy and FAA Admin. Bedford to testify Dec. 1-2 on the Nov. 13 ground stop and ATC money
(Tue Nov 24, 2026). Sources: Reuters (via AJOT/Forth), Politico live updates 12:49pm ET Nov 24.
Draft only. Whip illustration, not a screenshot. No Whip scores. No hook."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-faa-hearings-dec"
FOLDER = "breaking/2026-11-24-faa-hearings-dec"
W, H = 568, 300
RED, YEL, BLU, PAPER, MUTE, INK = "#ff2d2a", "#ffcc00", "#3d8bff", "#f4f0e6", "#8a867c", "#09090b"

def tower(x, y):
    """Generic control tower silhouette (no agency marks). x,y = top-left."""
    p = []
    p.append(f'<rect x="{x+6}" y="{y}" width="48" height="6" rx="2" fill="{MUTE}"/>')           # roof
    p.append(f'<polygon points="{x},{y+8} {x+60},{y+8} {x+54},{y+38} {x+6},{y+38}" fill="#1d2a3a" stroke="{YEL}" stroke-width="2.5"/>')  # cab
    for i in range(4):
        p.append(f'<rect x="{x+10+i*11}" y="{y+14}" width="7" height="18" fill="{YEL}" opacity=".85"/>')
    p.append(f'<rect x="{x+2}" y="{y+38}" width="56" height="6" fill="{MUTE}"/>')
    p.append(f'<polygon points="{x+18},{y+44} {x+42},{y+44} {x+46},{y+150} {x+14},{y+150}" fill="#2a3440"/>')  # shaft
    p.append(f'<rect x="{x+4}" y="{y+150}" width="52" height="8" fill="#3a4450"/>')
    p.append(f'<line x1="{x+30}" y1="{y}" x2="{x+30}" y2="{y-14}" stroke="{MUTE}" stroke-width="2"/>')
    p.append(f'<circle cx="{x+30}" cy="{y-16}" r="3.5" fill="{RED}"/>')
    return "".join(p)

parts = []
parts.append(f'<text x="0" y="20" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">THE HEARINGS</text>')
parts.append(f'<text x="0" y="40" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">Schematic timeline. Source: Reuters, Politico</text>')
parts.append(tower(4, 112))
# timeline
tx0, tx1, ty = 96, 562, 112
parts.append(f'<line x1="{tx0}" y1="{ty}" x2="{tx1}" y2="{ty}" stroke="#3a3a44" stroke-width="3"/>')
def node(x, date, chamber, who, lines, col):
    p = [f'<circle cx="{x}" cy="{ty}" r="11" fill="{col}" stroke="{INK}" stroke-width="3"/>',
         f'<text x="{x-11}" y="{ty-24}" font-family="Anton" font-size="34" fill="{col}">{date}</text>',
         f'<rect x="{x-11}" y="{ty+22}" width="224" height="150" rx="3" fill="#14161c" stroke="{col}" stroke-width="1.6"/>',
         f'<text x="{x+3}" y="{ty+48}" font-family="Archivo Black" font-size="16" letter-spacing="1.4" fill="{col}">{chamber}</text>',
         f'<text x="{x+3}" y="{ty+74}" font-family="Archivo Black" font-size="13.5" letter-spacing=".4" fill="{PAPER}">{who}</text>']
    for i, ln in enumerate(lines):
        p.append(f'<text x="{x+3}" y="{ty+98+i*18}" font-family="Inter" font-size="11.8" font-weight="600" fill="#c8c4ba">{ln}</text>')
    return "".join(p)
parts.append(node(108, "DEC. 1", "HOUSE", "FAA Admin. Bryan Bedford",
                  ["Transportation &amp; Infrastructure", "Committee. Topic: $12.5B from", "last year&rsquo;s law for ATC equipment;", "ground-stop questions expected"], YEL))
parts.append(node(340, "DEC. 2", "SENATE", "Sec. Sean Duffy (DOT)",
                  ["Commerce aviation subcommittee.", "Topics: the Nov. 13 ground stop", "and his $50B request for ATC", "&amp; airport modernization"], RED))

graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: Reuters, Politico (Nov. 24, 2026). Illustration.</span><span>Whip illustration &middot; not an FAA or congressional graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; FAA GROUND STOP</div>
<div class="left">
  <div class="h1">CONGRESS<br><span class="y">WANTS ANSWERS</span></div>
  <div class="h2">DOT &amp; FAA CHIEFS TESTIFY DEC. 1&ndash;2</div>
  <div class="att">After the Nov. 13 nationwide ground stop, Sec. Duffy raised his air traffic control and airport modernization request to $50 billion, up from $30 billion. Lawmakers from both parties say they need more answers before approving supplemental funding.</div>
</div>
<div class="panel">
  <div class="ph">ON THE HILL &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>First answers:</b> Congress gets its first public answers on the Nov. 13 ground stop before deciding on new air traffic money.</div></div>
  <div class="b"><div class="n">02</div><div><b>Both parties:</b> lawmakers say they need more answers before approving supplemental funding.</div></div>
  <div class="b"><div class="n">03</div><div><b>The ask grew:</b> Duffy raised his request to $50B from $30B after the outage.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0b2a4a 0%,#081a30 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:72px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:30px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:12px;width:470px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:100px;width:600px;z-index:5;background:rgba(10,14,22,.88);border-top:4px solid #ff2d2a;padding:12px 16px 10px}
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
