#!/usr/bin/env python3
"""UPDATE card (TALL v4, 2440x3092): Iowa Gov. Reynolds declares state disaster emergency for Des Moines, Lee, Van Buren counties ahead of Nov 25 lead azide detonation.
Sources: Governor's office press release + proclamation, Nov 24, 2026 (governor.iowa.gov); ABC News. No Whip scores. Whip illustration.
"""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import FACE

OUT = Path(__file__).resolve().parent
NAME = "update-iowa-disaster-proclamation"
FOLDER = "breaking/2026-11-24-iowa-disaster-proclamation"
CW, CH = 1220, 1546  # CSS px; 2x screenshot = 2440x3092
GRN, YEL, RED, BLU, PAPER, MUTE = "#2fd28a", "#ffcc00", "#ff2d2a", "#3d8bff", "#f4f0e6", "#8a867c"

# Full-width flow + timeline graphic
GW, GH = 1100, 600

def box(x, y, w, h, col, t1, t2, t3):
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="#14141a" stroke="{col}" stroke-width="4"/>'
        f'<text x="{x+w/2}" y="{y+62}" text-anchor="middle" font-family="Anton" font-size="44" fill="{col}">{t1}</text>'
        f'<text x="{x+w/2}" y="{y+104}" text-anchor="middle" font-family="Inter" font-size="24" font-weight="700" fill="{PAPER}">{t2}</text>'
        f'<text x="{x+w/2}" y="{y+138}" text-anchor="middle" font-family="Inter" font-size="22" font-weight="600" fill="#c8c4ba">{t3}</text>'
    )

def arrow(x1, y):
    return (
        f'<line x1="{x1+8}" y1="{y}" x2="{x1+46}" y2="{y}" stroke="{PAPER}" stroke-width="5"/>'
        f'<polygon points="{x1+46},{y-10} {x1+62},{y} {x1+46},{y+10}" fill="{PAPER}"/>'
    )

p = []
p.append(f'<text x="0" y="32" font-family="Archivo Black" font-size="22" letter-spacing="2" fill="{PAPER}">DISASTER EMERGENCY &middot; 3 COUNTIES (SCHEMATIC, NOT TO SCALE)</text>')
cty = [(0, "VAN BUREN", MUTE), (395, "LEE", MUTE), (790, "DES MOINES", RED)]
for x, name, col in cty:
    p.append(f'<rect x="{x}" y="60" width="310" height="200" fill="#14141a" stroke="{col}" stroke-width="4"/>')
    p.append(f'<text x="{x+155}" y="130" text-anchor="middle" font-family="Anton" font-size="44" fill="{col if col==RED else PAPER}">{name}</text>')
    p.append(f'<text x="{x+155}" y="168" text-anchor="middle" font-family="Inter" font-size="22" font-weight="700" fill="#c8c4ba">COUNTY</text>')
p.append(f'<circle cx="945" cy="218" r="14" fill="{YEL}" stroke="{PAPER}" stroke-width="3"/>')
p.append(f'<text x="945" y="250" text-anchor="middle" font-family="Archivo Black" font-size="17" fill="{YEL}">AMMO PLANT, MIDDLETOWN</text>')
p.append(f'<text x="0" y="300" font-family="Inter" font-size="20" font-weight="600" fill="#c8c4ba">State emergency plans activated; all available state resources authorized.</text>')
ty = 400
p.append(f'<line x1="24" y1="{ty}" x2="{GW-24}" y2="{ty}" stroke="#4a4a54" stroke-width="5"/>')
steps = [
    ("NOV. 23", "DATE SET", "Army moves blast to Wed.", MUTE, 24),
    ("NOV. 24", "DISASTER DECLARED", "Gov. Reynolds", YEL, GW / 2),
    ("NOV. 25", "9 A.M. CT BLAST", "Controlled detonation", RED, GW - 24),
]
for i, (d, h, s, col, x) in enumerate(steps):
    r = 20 if i == 1 else 15
    p.append(f'<circle cx="{x}" cy="{ty}" r="{r}" fill="{col}" stroke="{PAPER}" stroke-width="3.5"/>')
    anchor = "start" if i == 0 else ("end" if i == 2 else "middle")
    xx = x + 22 if i == 0 else (x - 22 if i == 2 else x)
    dcol = YEL if i == 1 else PAPER
    p.append(f'<text x="{xx}" y="{ty+48}" text-anchor="{anchor}" font-family="Archivo Black" font-size="24" fill="{dcol}">{d}</text>')
    p.append(f'<text x="{xx}" y="{ty+90}" text-anchor="{anchor}" font-family="Anton" font-size="40" fill="{PAPER}">{h}</text>')
    p.append(f'<text x="{xx}" y="{ty+124}" text-anchor="{anchor}" font-family="Inter" font-size="20" font-weight="600" fill="#c8c4ba">{s}</text>')

graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{GW}" height="{GH}" viewBox="0 0 {GW} {GH}">{"".join(p)}</svg>'

html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>
{FACE}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{CW}px;height:{CH}px;background:#09090b;color:#f4f0e6;overflow:hidden;position:relative}}
body{{font-family:'Barlow Condensed',sans-serif;background:radial-gradient(ellipse at 50% 22%,#4a1a0a 0%,#2e120a 42%,#09090b 82%)}}
.grain{{position:absolute;inset:0;pointer-events:none;opacity:.045;mix-blend-mode:overlay;z-index:8;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}}
.topbar{{position:absolute;top:0;left:0;right:0;height:7px;background:linear-gradient(90deg,#ffcc00 0%,#ff2d2a 55%,#ffcc00 100%);z-index:4}}
.brand{{position:absolute;top:28px;left:48px;right:48px;display:flex;align-items:center;gap:12px;z-index:4}}
.logo{{background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:16px;letter-spacing:.14em;padding:5px 10px 4px;line-height:1}}
.handle{{color:#8a867c;font-weight:700;font-size:17px;letter-spacing:.16em;text-transform:uppercase;font-family:'Barlow Condensed',sans-serif}}
.brand-rule{{flex:1;height:1px;background:#222226;margin-left:8px}}
.footer{{position:absolute;left:48px;right:48px;bottom:16px;z-index:4;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #1c1c20;padding-top:10px;font-family:'Inter',sans-serif;font-size:13px;font-weight:500;letter-spacing:.03em;color:#6c6a64}}
.frame{{position:absolute;top:78px;left:48px;right:48px;bottom:58px;display:flex;flex-direction:column;z-index:5}}
.tag{{display:inline-flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;width:fit-content}}
.dot{{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}}
.head{{margin-top:16px}}
.h1{{font-family:'Anton',sans-serif;font-size:96px;line-height:.92;color:#f4f0e6;letter-spacing:.01em}}
.h2{{font-family:'Anton',sans-serif;font-size:40px;line-height:1.05;color:#f4f0e6;margin-top:12px}}
.att{{font-family:'Inter',sans-serif;font-size:24px;line-height:1.36;color:#c8c4ba;margin-top:14px;max-width:1100px}}
.chips{{display:flex;gap:10px;margin-top:16px}}
.chips span{{font-family:'Archivo Black',sans-serif;font-size:17px;letter-spacing:.1em;text-transform:uppercase;color:#09090b;background:#2fd28a;padding:8px 13px 7px}}
.y{{color:#ffcc00}}
.panel{{margin-top:18px;flex:1;min-height:0;display:flex;flex-direction:column;background:rgba(10,14,18,.88);border-top:4px solid #ff2d2a;padding:16px 20px 10px}}
.ph{{font-family:'Archivo Black',sans-serif;font-size:15px;letter-spacing:.16em;color:#8a867c;margin-bottom:8px}}
.panel svg{{display:block;width:100%;height:auto;margin-top:auto;margin-bottom:auto}}
.strip{{margin-top:16px;flex:0 0 auto;background:rgba(14,14,18,.94);border-top:4px solid #ffcc00;display:grid;grid-template-columns:190px 1fr 1fr 1fr;gap:24px;padding:22px 24px 26px;align-items:start}}
.wt{{font-family:'Anton',sans-serif;font-size:58px;line-height:.9;color:#f4f0e6}}
.b{{display:flex;gap:12px;font-family:'Inter',sans-serif;font-weight:600;font-size:22px;line-height:1.3;color:#c8c4ba}}
.b b{{color:#ffcc00;font-weight:800}}
.n{{font-family:'Anton',sans-serif;font-size:44px;line-height:.9;color:#ff2d2a;flex:0 0 auto}}
</style></head>
<body>
<div class="topbar"></div>
<div class="brand"><div class="logo">WHIP</div><div class="handle">@whipcampaigns</div><div class="brand-rule"></div></div>
<div class="frame">
  <div class="tag"><span class="dot"></span>UPDATE &middot; IOWA DETONATION</div>
  <div class="head">
    <div class="h1">IOWA DECLARES<br><span class="y">DISASTER EMERGENCY</span></div>
    <div class="h2">3 COUNTIES, HOURS BEFORE THE ARMY&rsquo;S BLAST</div>
    <div class="att">Gov. Kim Reynolds declared a state disaster emergency for Des Moines, Lee and Van Buren counties ahead of the Army&rsquo;s controlled detonation of degraded lead azide at the Iowa Army Ammunition Plant, set for 9 a.m. CT Wednesday, her office said.</div>
    <div class="chips"><span>State resources activated</span><span>Guard deployed</span></div>
  </div>
  <div class="panel">
    <div class="ph">WHERE &amp; WHEN &middot; WHIP ILLUSTRATION</div>
    {graphic}
  </div>
  <div class="strip">
    <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
    <div class="b"><div class="n">01</div><div><b>The order:</b> activates state emergency plans and authorizes all available state resources for the three counties.</div></div>
    <div class="b"><div class="n">02</div><div><b>On the ground:</b> up to 100 Iowa National Guard soldiers will help reach about 150 nearby households.</div></div>
    <div class="b"><div class="n">03</div><div><b>Guidance:</b> FEMA says some within 5 miles southwest may be evacuated; 5 to 20 miles southwest, stay indoors.</div></div>
  </div>
</div>
<div class="footer"><span>Sources: Office of Gov. Kim Reynolds press release and proclamation, Nov. 24, 2026; FEMA guidance via the governor&rsquo;s office.</span><span>Whip illustration &middot; not a government map</span></div>
<div class="grain"></div>
</body></html>
"""

def render(html):
    out_html = OUT / f"{NAME}.html"
    out_html.write_text(html)
    png = OUT / "card.png"
    r = subprocess.run([
        "google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=2", f"--window-size={CW},{CH}",
        f"--screenshot={png}", "file://" + str(out_html),
    ], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit("render failed: " + (r.stderr or r.stdout or "")[-800:])
    out_html.unlink()
    return png

src = render(html)
print(src, src.stat().st_size)
try:
    from PIL import Image
    im = Image.open(src)
    print("size", im.size, im.mode)
except Exception as e:
    print("pil", e)
# Copy to the repo folder only after this script is invoked intentionally.
# Still copy so the working tree stays in sync with a good render.
dest = Path(f"/workspace/whip-cards/{FOLDER}")
dest.mkdir(parents=True, exist_ok=True)
for f in (src, Path(__file__).resolve(), OUT / "tweet.txt", OUT / "alt.txt"):
    if f.exists():
        shutil.copy(f, dest / f.name)
        print("copied", dest / f.name)
