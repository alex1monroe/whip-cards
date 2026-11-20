#!/usr/bin/env python3
"""UPDATE card: Trump calls U.S. air traffic control "ancient," backs $50B rebuild request
(White House news conference, Nov 20, 2026; BBC, PBS NewsHour, WBAY). Draft only. Illustration, not a screenshot.
Adapted from 2026-11-20-data-center-tax/make_data_center_tax_card.py; uses the shared Whip v4 base."""
import shutil, sys
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
import subprocess
from v4base import wrap
OUT = Path(__file__).resolve().parent

NAME = "update-faa-ancient-50b"
FOLDER = "2026-11-20-faa-update-ancient-50b"

# --- graphic: $12B allotted vs $50B requested (bars to scale) + 22 ATC centers, 17 hit on Nov 13 ---
W = 568
BAR_X, BAR_MAX = 0, 440          # 50B -> 440px, 12B -> 105.6px
def bar(y, val, label, sub, color, txtcol):
    w = BAR_MAX * val / 50
    return (f'<text x="0" y="{y-10}" font-family="Archivo Black" font-size="13" letter-spacing="2.2" fill="{txtcol}">{label}</text>'
            f'<rect x="{BAR_X}" y="{y}" width="{BAR_MAX}" height="46" fill="#1d1d24"/>'
            f'<rect x="{BAR_X}" y="{y}" width="{w:.1f}" height="46" fill="{color}"/>'
            f'<text x="{w+12:.1f}" y="{y+37}" font-family="Anton" font-size="38" fill="{color}">${val}B</text>'
            f'<text x="{W}" y="{y-10}" text-anchor="end" font-family="Inter" font-size="12.5" font-weight="600" fill="#8a867c">{sub}</text>')

bars = (bar(30, 12, "ALLOTTED TO DOT", "Trump: &ldquo;not enough&rdquo;", "#8a867c", "#c8c4ba")
        + bar(118, 50, "REQUESTED FROM CONGRESS", "to rebuild ATC", "#ffcc00", "#ffcc00"))

# 22 centers, 17 highlighted (illustrative order, not a map)
dots = []
for i in range(22):
    cx = 11 + i * 25.8
    hit = i < 17
    dots.append(f'<rect x="{cx-9:.1f}" y="232" width="18" height="18" rx="3" '
                f'fill="{"#ff2d2a" if hit else "#1d1d24"}" stroke="{"#ff2d2a" if hit else "#4a4a54"}" stroke-width="1.6"/>')
grid = ('<text x="0" y="220" font-family="Archivo Black" font-size="13" letter-spacing="2.2" fill="#ff2d2a">NOV 13: 17 OF 22 ATC CENTERS HIT</text>'
        f'<text x="{W}" y="220" text-anchor="end" font-family="Inter" font-size="12.5" font-weight="600" fill="#8a867c">voice &amp; ground comms, per BBC</text>'
        + "".join(dots))

graphic = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="262" viewBox="0 0 {W} 262">
{bars}
<line x1="0" y1="190" x2="{W}" y2="190" stroke="#3a3a44" stroke-width="1.2" stroke-dasharray="3 5"/>
{grid}
</svg>'''

html = wrap(f"""
<div class="footer"><span>Sources: BBC, PBS NewsHour, WBAY, Nov. 20, 2026.</span><span>Whip illustration &middot; not an FAA graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; FAA GROUND STOP</div>
<div class="left">
  <div class="h1"><span class="y">&ldquo;ANCIENT.&rdquo;</span></div>
  <div class="h2">TRUMP BACKS $50B<br>ATC REBUILD</div>
  <div class="att">At a White House news conference, Trump called the air traffic control system &ldquo;obsolete&rdquo; and at least &ldquo;55 years old.&rdquo; He said he told Sec. Duffy: &ldquo;Spend as little as you can to keep it going.&rdquo;</div>
</div>
<div class="panel">
  <div class="ph">THE MONEY &amp; THE OUTAGE &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>Rebuild, not patch:</b> the White House wants Congress to fund a full ATC rebuild. The $50B request still needs Congress.</div></div>
  <div class="b"><div class="n">02</div><div><b>Other outages:</b> Trump called this week&rsquo;s outages at Microsoft, Chase, Apple and others &ldquo;separate events,&rdquo; not a coordinated attack.</div></div>
  <div class="b"><div class="n">03</div><div><b>Still to come:</b> FAA officials planned to share more Friday on what caused the four-hour Nov. 13 ground stop, per BBC.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0b2a4a 0%,#081a30 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:112px;line-height:1;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:44px;line-height:1;color:#f4f0e6;margin-top:4px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:12px;width:470px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:112px;width:600px;z-index:5;background:rgba(10,14,22,.88);border-top:4px solid #ff2d2a;padding:12px 16px 10px}
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
