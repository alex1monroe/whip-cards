#!/usr/bin/env python3
"""UPDATE card: officials assured Nvidia board Huang faced no criminal charges (Tue Nov 24, 2026).
Sources: ABC News Nov 24 6:38 AM ET (NYT first); AP Nov 23 (reinstatement, Dec 3 Senate Banking hearing); Washington Post Nov 24 (Democrats' probes incl. Trump's role). Illustration. No Whip scores."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-huang-assurances"
FOLDER = "breaking/2026-11-24-huang-assurances"
W = 568
RED, YEL, BLU, INK, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#09090b", "#f4f0e6", "#8a867c"
parts = []
parts.append(f'<text x="0" y="22" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">NVIDIA &#183; JENSEN HUANG</text>')
parts.append(f'<text x="0" y="44" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">Per AP, ABC News and the Washington Post</text>')
rows = [("NOV 23", "Board reinstates Huang", "Nvidia's board brings back its CEO (AP)", MUTE),
        ("NOV 24", "Assurances reported", "Officials told board: no criminal charges (ABC)", RED),
        ("DEC 3", "Senate hearing", "Huang testifies publicly to Senate Banking (AP)", BLU),
        ("JAN", "Democrats take control", "Plan probes that include Trump's role (WaPo)", YEL)]
y = 62
for d, lab, note, col in rows:
    parts.append(f'<rect x="0" y="{y}" width="{W}" height="54" rx="4" fill="#15151b" stroke="{col}" stroke-width="{3 if col==RED else 1.5}"/>')
    parts.append(f'<text x="18" y="{y+38}" font-family="Anton" font-size="26" fill="{col}">{d}</text>')
    parts.append(f'<text x="130" y="{y+23}" font-family="Archivo Black" font-size="15" letter-spacing="1.2" fill="{PAPER}">{lab.upper()}</text>')
    parts.append(f'<text x="130" y="{y+43}" font-family="Inter" font-size="13.5" font-weight="600" fill="#c8c4ba">{note}</text>')
    y += 62
H = y
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: ABC News (Nov. 24; NYT first); AP (Nov. 23); Washington Post (Nov. 24). Illustration.</span><span>Whip illustration &middot; not a news graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; NVIDIA</div>
<div class="left">
  <div class="h1">NO CHARGES,<br><span class="y">OFFICIALS TOLD BOARD</span></div>
  <div class="h2">REPORT: OFFICIALS VOUCHED<br>FOR HUANG TO NVIDIA'S BOARD</div>
  <div class="att">Top administration officials told Nvidia's board that CEO Jensen Huang was not facing criminal charges and that they believed he was not a national security risk, sources told ABC News.</div>
</div>
<div class="panel">
  <div class="ph">THE TIMELINE &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>New:</b> Officials gave the board two assurances: no criminal charges, and not a security risk, officials believed (ABC; NYT first).</div></div>
  <div class="b"><div class="n">02</div><div><b>Next:</b> Huang testifies publicly before the Senate Banking Committee on Dec. 3 (AP).</div></div>
  <div class="b"><div class="n">03</div><div><b>Congress:</b> Democrats plan probes in January that include Trump's role in his return (WaPo).</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0f3a1c 0%,#08200f 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ff2d2a;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:56px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:28px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:112px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #ffcc00;padding:12px 16px 10px}
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
for f in (src, Path(__file__).resolve(), OUT / "tweet.md"):
    if f.exists(): shutil.copy(f, dest / f.name); print("copied", dest / f.name)
