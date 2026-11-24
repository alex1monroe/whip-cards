#!/usr/bin/env python3
"""UPDATE card: USDA Under Secretary Richard Fordyce says approximately 350 farms
could be impacted by a dust plume containing lead particles (Tue Nov 24, 2026).
Sources: Brownfield Ag News (Brent Barnett, Nov. 24) for the Fordyce figure and
USDA coordination with Iowa Ag Secretary Mike Naig and Missouri Ag Director
Chris Chinn. Army plume-path forecast also from that Brownfield report.
Draft only. Whip illustration; schematic, not a real map or official graphic.
No Whip scores. No hook. No CBS attribution."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-iowa-farms-fordyce"
FOLDER = "breaking/2026-11-24-iowa-farms-fordyce"
W, H = 568, 300
RED, YEL, PAPER, MUTE, INK = "#ff2d2a", "#ffcc00", "#f4f0e6", "#8a867c", "#09090b"

parts = []
parts.append(f'<text x="0" y="20" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">SCHEMATIC PLUME PATH &middot; NOT A MAP</text>')
parts.append(f'<text x="0" y="40" font-family="Inter" font-size="12.5" font-weight="600" fill="{MUTE}">Not to scale. Army forecast as reported by Brownfield Ag News</text>')

# simplified IA / MO blocks with a SW plume arrow; IL marked as "possibly"
# Iowa rectangle (left), Missouri (lower right)
parts.append(f'<rect x="16" y="56" width="200" height="128" rx="4" fill="#1a1510" stroke="#4a4a54" stroke-width="2"/>')
parts.append(f'<text x="116" y="80" text-anchor="middle" font-family="Archivo Black" font-size="16" letter-spacing="1.4" fill="{PAPER}">IOWA</text>')
# plant marker in SE of Iowa box
parts.append(f'<circle cx="176" cy="150" r="7" fill="{PAPER}"/>')
parts.append(f'<text x="128" y="154" text-anchor="end" font-family="Archivo Black" font-size="10" letter-spacing=".4" fill="{PAPER}">PLANT</text>')
parts.append(f'<text x="176" y="172" text-anchor="middle" font-family="Inter" font-size="10" font-weight="600" fill="{MUTE}">Middletown</text>')

parts.append(f'<rect x="300" y="100" width="200" height="110" rx="4" fill="#1a1510" stroke="#4a4a54" stroke-width="2"/>')
parts.append(f'<text x="400" y="128" text-anchor="middle" font-family="Archivo Black" font-size="16" letter-spacing="1.4" fill="{PAPER}">MISSOURI</text>')
parts.append(f'<text x="400" y="150" text-anchor="middle" font-family="Inter" font-size="12" font-weight="600" fill="#c8c4ba">Northeastern Missouri,</text>')
parts.append(f'<text x="400" y="168" text-anchor="middle" font-family="Inter" font-size="12" font-weight="600" fill="#c8c4ba">per the Army</text>')

# faint Illinois "possibly"
parts.append(f'<rect x="430" y="52" width="122" height="42" rx="4" fill="#14120e" stroke="#3a3a44" stroke-width="1.5" stroke-dasharray="5 4"/>')
parts.append(f'<text x="491" y="70" text-anchor="middle" font-family="Archivo Black" font-size="11" letter-spacing=".8" fill="{MUTE}">ILLINOIS</text>')
parts.append(f'<text x="491" y="86" text-anchor="middle" font-family="Inter" font-size="10" font-weight="600" fill="{MUTE}">possibly, far west</text>')

# SW plume arrow from plant into Missouri
parts.append(f'<path d="M 186 146 C 220 148 256 155 300 168" fill="none" stroke="{YEL}" stroke-width="4" stroke-linecap="round"/>')
parts.append(f'<polygon points="296,159 318,171 294,179" fill="{YEL}"/>')
parts.append(f'<text x="244" y="138" text-anchor="middle" font-family="Archivo Black" font-size="11" letter-spacing="1" fill="{YEL}">SW PLUME</text>')

# callout — use Fordyce's "approximately," not a tilde
parts.append(f'<text x="0" y="232" font-family="Archivo Black" font-size="12" letter-spacing="1.4" fill="{MUTE}">FORDYCE, PER BROWNFIELD AG NEWS</text>')
parts.append(f'<text x="0" y="262" font-family="Anton" font-size="24" fill="{YEL}">APPROXIMATELY 350 FARMS COULD BE IMPACTED</text>')
parts.append(f'<text x="0" y="284" font-family="Inter" font-size="12" font-weight="600" fill="#c8c4ba">He did not specify which states those farms are in.</text>')

graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: Brownfield Ag News (Nov. 24, 2026), citing Fordyce and the Army. Illustration.</span><span>Whip illustration &middot; not a USDA, Army or news graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; IOWA BLAST</div>
<div class="left">
  <div class="h1">FORDYCE:<br><span class="y">350 FARMS</span></div>
  <div class="h2">&ldquo;APPROXIMATELY 350 FARMS<br>COULD BE IMPACTED&rdquo;</div>
  <div class="att">USDA Under Secretary for Farm Production and Conservation Richard Fordyce says approximately 350 farms could be impacted by a dust plume containing lead particles, per Brownfield Ag News.</div>
</div>
<div class="panel">
  <div class="ph">THE PLUME &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>The figure:</b> Fordyce says approximately 350 farms could be impacted by a dust plume containing lead particles (Brownfield).</div></div>
  <div class="b"><div class="n">02</div><div><b>USDA:</b> working with Iowa Ag Secretary Mike Naig and Missouri Ag Director Chris Chinn to provide guidance and resources.</div></div>
  <div class="b"><div class="n">03</div><div><b>Army forecast:</b> the plume is likely to track southwest into northeastern Missouri and possibly far western Illinois.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#4a1f08 0%,#2a1206 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ff2d2a;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:72px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:24px;line-height:1.05;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:100px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #ffcc00;padding:12px 16px 10px}
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
