#!/usr/bin/env python3
"""UPDATE card: NSA says NSANet is back to "normal conditions" (Nov 20, 2026; The Record, WTOP, NY Post).
Draft only. Illustration, not a screenshot.
Adapted from 2026-11-20-faa-update-ancient-50b/make_card.py; uses the shared Whip v4 base."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent

NAME = "update-nsa-restored"
FOLDER = "2026-11-20-nsa-update-restored"

# --- graphic: Mon-Fri status strip for the week of Nov 16 (only dated facts labeled) ---
W = 568
RED, YEL, GRN, GRY = "#ff2d2a", "#ffcc00", "#2fd27a", "#4a4a54"
days = [  # (dow, date, state, line1, line2)
    ("MON", "NOV 16", "none",  "",                 ""),
    ("TUE", "NOV 17", "down",  "Disruption",       "reported"),
    ("WED", "NOV 18", "down",  "Day two",          ""),
    ("THU", "NOV 19", "down",  "Disrupted",        ""),
    ("FRI", "NOV 20", "up",    "\u201cNormal, with", "exceptions\u201d"),
]
CW, GAP = 104, 12
cells = []
for i, (dow, date, st, l1, l2) in enumerate(days):
    x = i * (CW + GAP)
    col = {"none": GRY, "down": RED, "up": GRN}[st]
    fill = {"none": "#16161b", "down": "rgba(255,45,42,.16)", "up": "rgba(47,210,122,.16)"}[st]
    status = {"none": "&mdash;", "down": "DISRUPTED", "up": "RESTORED"}[st]
    cells.append(
        f'<text x="{x}" y="22" font-family="Archivo Black" font-size="15" letter-spacing="2" fill="#f4f0e6">{dow}</text>'
        f'<text x="{x+CW}" y="22" text-anchor="end" font-family="Inter" font-size="12" font-weight="700" fill="#8a867c">{date}</text>'
        f'<rect x="{x}" y="34" width="{CW}" height="92" fill="{fill}" stroke="{col}" stroke-width="2"/>'
        f'<rect x="{x}" y="34" width="{CW}" height="10" fill="{col}"/>'
        f'<text x="{x+CW/2}" y="96" text-anchor="middle" font-family="Archivo Black" font-size="{12.5 if st!="none" else 22}" letter-spacing="0.6" fill="{col if st!="none" else "#6c6a64"}">{status}</text>'
        + (f'<text x="{x+CW/2}" y="154" text-anchor="middle" font-family="Inter" font-size="13.5" font-weight="700" fill="{col if st=="up" else "#c8c4ba"}">{l1}</text>' if l1 else "")
        + (f'<text x="{x+CW/2}" y="172" text-anchor="middle" font-family="Inter" font-size="13.5" font-weight="700" fill="{col if st=="up" else "#c8c4ba"}">{l2}</text>' if l2 else ""))

legend = (f'<line x1="0" y1="196" x2="{W}" y2="196" stroke="#3a3a44" stroke-width="1.2" stroke-dasharray="3 5"/>'
          f'<text x="0" y="224" font-family="Archivo Black" font-size="13" letter-spacing="2.2" fill="{RED}">NSANET DISRUPTED ~3 DAYS</text>'
          f'<text x="{W}" y="224" text-anchor="end" font-family="Inter" font-size="12.5" font-weight="600" fill="#8a867c">per The Record; NY Post: &ldquo;nearly 4-day&rdquo;</text>'
          f'<text x="0" y="250" font-family="Archivo Black" font-size="13" letter-spacing="2.2" fill="{GRN}">FRI: &ldquo;NORMAL CONDITIONS&rdquo;</text>'
          f'<text x="{W}" y="250" text-anchor="end" font-family="Inter" font-size="12.5" font-weight="600" fill="#8a867c">NSA spokesperson</text>')

graphic = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="262" viewBox="0 0 {W} 262">
{"".join(cells)}
{legend}
</svg>'''

html = wrap(f"""
<div class="footer"><span>Sources: The Record, WTOP, Nov. 20, 2026. Illustration.</span><span>Whip illustration &middot; not an NSA graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; NSA NETWORK</div>
<div class="left">
  <div class="h1">BACK TO<br><span class="g">NORMAL.</span></div>
  <div class="h2">NSANET RESTORED AFTER<br>MULTI-DAY DISRUPTION</div>
  <div class="att">An NSA spokesperson: &ldquo;can confirm that we are now operating under normal conditions.&rdquo; NSANet lets employees share classified information internally.</div>
</div>
<div class="panel">
  <div class="ph">THE WEEK OF NOV. 16 &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>Restored:</b> NSANet is operating under normal conditions, per an NSA spokesperson.</div></div>
  <div class="b"><div class="n">02</div><div><b>The cause:</b> officials tie it to PHP software patching and say it was not a cyberattack.</div></div>
  <div class="b"><div class="n">03</div><div><b>Still open:</b> some facilities remain on &ldquo;Code Orange&rdquo; delayed openings for non-essential staff.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0b2a3a 0%,#081a26 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:88px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:32px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.y{color:#ffcc00}
.g{color:#2fd27a}
.panel{position:absolute;right:48px;top:112px;width:600px;z-index:5;background:rgba(10,14,22,.88);border-top:4px solid #2fd27a;padding:12px 16px 10px}
.ph{font-family:'Archivo Black',sans-serif;font-size:13px;letter-spacing:.16em;color:#8a867c;margin-bottom:4px}
.panel svg{display:block}
.strip{position:absolute;left:48px;right:48px;top:470px;height:150px;z-index:5;background:rgba(14,14,18,.94);border-top:4px solid #ffcc00;display:grid;grid-template-columns:150px 1fr 1fr 1fr;gap:20px;padding:16px 22px}
.wt{font-family:'Anton',sans-serif;font-size:40px;line-height:.92;color:#f4f0e6}
.b{display:flex;gap:10px;font-weight:600;font-size:18px;line-height:1.16;color:#c8c4ba}
.b b{color:#ffcc00;font-weight:800}
.n{font-family:'Anton',sans-serif;font-size:30px;line-height:.9;color:#ff2d2a}
""")
def render(html):
    # Same headless-Chrome 2x render as v4base.render, written next to this script.
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
