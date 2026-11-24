#!/usr/bin/env python3
"""UPDATE card: unclassified CIA open-source intelligence system breached (AP, Nov 24, 2026); ODNI: no disruptions to
critical capabilities or classified systems (Reuters/NYT). Follows FBI NCIC breach (our Nov 20-21 posts) and USDA incident.
Draft only. Whip illustration. No Whip scores. No hook."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-cia-breach"
FOLDER = "breaking/2026-11-24-cia-odni-breach"
W, H = 568, 300
RED, YEL, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#f4f0e6", "#8a867c"
parts = []
parts.append(f'<text x="0" y="20" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">FEDERAL CYBER INCIDENTS IN THE NEWS</text>')
parts.append(f'<text x="0" y="40" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">Recent reported incidents, per AP and other outlets. Illustration.</text>')
boxes = [("USDA", "Reported incident", "Agriculture Dept.", False), ("FBI", "NCIC breach", "Crime-records system", False), ("CIA", "Unclassified system", "Open-source intel", True)]
for i, (ag, l1, l2, hot) in enumerate(boxes):
    x = i * 190
    col = RED if hot else "#2a2a32"
    parts.append(f'<rect x="{x}" y="62" width="176" height="150" rx="6" fill="{col}" stroke="{YEL if hot else "#4a4a54"}" stroke-width="{3 if hot else 2}"/>')
    # shield icon
    cx = x + 88
    parts.append(f'<path d="M{cx} 78 l26 10 v18 c0 18 -12 28 -26 34 c-14 -6 -26 -16 -26 -34 v-18 z" fill="none" stroke="{PAPER}" stroke-width="3"/>')
    if hot:
        parts.append(f'<path d="M{cx-9} 100 l18 18 M{cx+9} 100 l-18 18" stroke="{YEL}" stroke-width="4"/>')
    parts.append(f'<text x="{cx}" y="168" text-anchor="middle" font-family="Anton" font-size="28" fill="{PAPER}">{ag}</text>')
    parts.append(f'<text x="{cx}" y="188" text-anchor="middle" font-family="Archivo Black" font-size="11.5" fill="{YEL if hot else PAPER}">{l1.upper()}</text>')
    parts.append(f'<text x="{cx}" y="204" text-anchor="middle" font-family="Inter" font-size="11.5" font-weight="600" fill="#c8c4ba">{l2}</text>')
parts.append(f'<text x="380" y="236" font-family="Archivo Black" font-size="12" fill="{YEL}">NEW &middot; REPORTED NOV. 24</text>')
parts.append(f'<text x="0" y="266" font-family="Inter" font-size="12.5" font-weight="600" fill="#c8c4ba">ODNI: &ldquo;no disruptions to critical capabilities or classified systems.&rdquo;</text>')
parts.append(f'<text x="0" y="286" font-family="Inter" font-size="11.5" font-weight="600" fill="{MUTE}">Who was responsible is not yet known.</text>')
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: AP; NYT via Reuters (Nov. 24, 2026). Illustration.</span><span>Whip illustration &middot; not a government or news graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; FEDERAL SYSTEMS</div>
<div class="left">
  <div class="h1">CIA SYSTEM<br><span class="y">BREACHED</span></div>
  <div class="h2">UNCLASSIFIED NETWORK<br>HIT IN CYBERATTACK</div>
  <div class="att">An unclassified CIA system that handles open-source intelligence was breached in a cyberattack, a person familiar with the incident told AP. No classified information was involved and the issue has been resolved, the person said.</div>
  <div class="chips"><span>No classified data</span><span>Attacker unknown</span></div>
</div>
<div class="panel">
  <div class="ph">THE PATTERN &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>What was hit:</b> a system for publicly available data from the internet and commercial databases, per AP.</div></div>
  <div class="b"><div class="n">02</div><div><b>What wasn&rsquo;t:</b> ODNI says no critical capabilities or classified systems were disrupted.</div></div>
  <div class="b"><div class="n">03</div><div><b>Still unknown:</b> who did it, and what data was taken. Other agencies&rsquo; data may be exposed, per NYT.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#4a0b14 0%,#300a12 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:74px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:28px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.chips{display:flex;gap:8px;margin-top:12px}
.chips span{font-family:'Archivo Black',sans-serif;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#09090b;background:#ff2d2a;color:#f4f0e6;padding:5px 9px 4px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:100px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #ff2d2a;padding:12px 16px 10px}
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
