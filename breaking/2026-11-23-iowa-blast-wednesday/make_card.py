#!/usr/bin/env python3
"""UPDATE card: Army sets Iowa lead-azide detonation for Wednesday morning (late Mon Nov 23, 2026).
Sources: AP (Army statement late Monday, Telle quote); Army.mil Nov 22 (Nov 25 schedule); WOWT/Gray Media (Sand: decision is the administration's). Illustration. No Whip scores."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-iowa-blast-wednesday"
FOLDER = "breaking/2026-11-23-iowa-blast-wednesday"
W = 568
RED, YEL, BLU, INK, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#09090b", "#f4f0e6", "#8a867c"
parts = []
parts.append(f'<text x="0" y="22" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">IOWA ARMY AMMUNITION PLANT</text>')
parts.append(f'<text x="0" y="44" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">Per AP, the U.S. Army and Gray Media (WOWT)</text>')
rows = [("NOV 23", "Trump: hold off", "Wait for the 8th Circuit and Gov.-elect Sand (AP)", MUTE),
        ("NOV 23", "Stay denied", "8th Circuit lifts its pause on the EPA permit (court)", BLU),
        ("NOV 23", "Sand responds", "Says the decision is the administration's (WOWT)", BLU),
        ("WED", "Army: proceeding", "Controlled detonation set for Wednesday morning (AP)", RED)]
y = 62
for d, lab, note, col in rows:
    parts.append(f'<rect x="0" y="{y}" width="{W}" height="54" rx="4" fill="#15151b" stroke="{col}" stroke-width="{3 if col==YEL else 1.5}"/>')
    parts.append(f'<text x="18" y="{y+38}" font-family="Anton" font-size="26" fill="{col}">{d}</text>')
    parts.append(f'<text x="130" y="{y+23}" font-family="Archivo Black" font-size="15" letter-spacing="1.2" fill="{PAPER}">{lab.upper()}</text>')
    parts.append(f'<text x="130" y="{y+43}" font-family="Inter" font-size="13.5" font-weight="600" fill="#c8c4ba">{note}</text>')
    y += 62
H = y
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: AP (Nov. 23); U.S. Army, Nov. 22; Gray Media / WOWT (Nov. 23). Illustration.</span><span>Whip illustration &middot; not an Army or news graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; IOWA BLAST</div>
<div class="left">
  <div class="h1">IOWA BLAST<br><span class="y">SET FOR WEDNESDAY</span></div>
  <div class="h2">ARMY SAYS IT IS PROCEEDING<br>AFTER COURT APPROVAL</div>
  <div class="att">The Army says it will remove 68 barrels of degraded lead azide by controlled detonation Wednesday morning, in coordination with state, local and federal authorities (AP).</div>
</div>
<div class="panel">
  <div class="ph">THE TIMELINE &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>When:</b> The Army set the controlled detonation for Wednesday morning, Nov. 25 (AP, Army).</div></div>
  <div class="b"><div class="n">02</div><div><b>The Army:</b> &ldquo;This is a consensus decision,&rdquo; acting Army Secretary Adam Telle posted (AP).</div></div>
  <div class="b"><div class="n">03</div><div><b>Sand:</b> The gov.-elect says the call is the administration&rsquo;s and wants federal info made public (WOWT).</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#4a1f08 0%,#2a1206 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ff2d2a;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:60px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
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
