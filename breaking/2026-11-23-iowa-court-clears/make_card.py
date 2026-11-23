#!/usr/bin/env python3
"""UPDATE card: 8th Circuit denies stay and lifts pause on Iowa lead-azide EPA permit (Mon Nov 23, 2026).
Sources: 8th Circuit per curiam in 26-3374 (Nov 23); CourtListener docket; CBS2 Iowa; NBC News. Illustration. No Whip scores. No unconfirmed date."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-iowa-court-clears"
FOLDER = "breaking/2026-11-23-iowa-court-clears"
W = 568
RED, YEL, BLU, INK, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#09090b", "#f4f0e6", "#8a867c"
parts = []
parts.append(f'<text x="0" y="22" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">IOWA ARMY AMMUNITION PLANT</text>')
parts.append(f'<text x="0" y="44" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">Per the 8th Circuit, CBS2 Iowa and CourtListener</text>')
rows = [("NOV 19", "Permit paused", "8th Circuit stays the EPA emergency permit (court)", MUTE),
        ("NOV 23", "Trump: hold off", "Orders Army to wait for court and Sand (AP)", BLU),
        ("NOV 23", "Stay denied", "Emergency stay denied; admin stay lifted (court)", YEL),
        ("OPEN", "No new date", "Army has not confirmed when it would proceed (CBS2)", RED)]
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
<div class="footer"><span>Sources: 8th Circuit per curiam, 26-3374 (Nov. 23); CBS2 Iowa; CourtListener docket. Illustration.</span><span>Whip illustration &middot; not an Army or news graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; IOWA BLAST</div>
<div class="left">
  <div class="h1">COURT CLEARS<br><span class="y">IOWA BLAST</span></div>
  <div class="h2">8TH CIRCUIT DENIES STAY<br>AND LIFTS EPA PERMIT PAUSE</div>
  <div class="att">A per curiam panel &mdash; Shepherd, Grasz and Justin D. Smith &mdash; denied a stay of the EPA permit for 68 drums of degraded lead azide. The petition for review is still pending.</div>
</div>
<div class="panel">
  <div class="ph">THE TIMELINE &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>The ruling:</b> 8th Circuit denied the emergency stay and lifted its pause on the EPA permit.</div></div>
  <div class="b"><div class="n">02</div><div><b>The finding:</b> Groups &ldquo;failed to show that they are likely to prevail&rdquo; on the petition (court).</div></div>
  <div class="b"><div class="n">03</div><div><b>Still open:</b> The Army has not confirmed a new detonation date (CBS2 Iowa).</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#4a1f08 0%,#2a1206 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ff2d2a;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:64px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
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
