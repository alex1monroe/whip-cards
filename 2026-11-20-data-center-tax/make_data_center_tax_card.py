#!/usr/bin/env python3
"""BREAKING card: Trump says U.S. companies building data centers abroad will face "a tremendous tax"
(White House news conference, Nov 20, 2026; AP, Reuters, CNBC). Draft only. Illustration, not a screenshot.
Uses the shared Whip v4 base in /home/box/whip/threads/2026-11-14-faa/v4base.py."""
import shutil, sys
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
import subprocess
from v4base import wrap
OUT = Path(__file__).resolve().parent

NAME = "breaking-data-center-tax"
FOLDER = "2026-11-20-data-center-tax"
# Simplified lower-48 outline (Albers), 360x230 box, built from public-domain state shapes. Illustration only.
US = "M4,73L9,63L9,51L22,25L22,7L23,6L32,11L33,9L32,8L35,4L71,13L108,20L177,25L188,25L190,22L192,27L201,28L209,33L213,31L220,32L212,38L208,42L208,44L214,42L217,45L229,36L230,37L229,40L235,44L248,40L249,43L253,42L254,45L258,46L251,47L251,48L258,51L260,56L258,65L259,66L261,63L264,62L268,70L263,81L269,84L274,82L288,71L289,68L288,65L302,61L304,58L303,54L310,45L329,40L334,31L334,24L337,16L339,18L343,16L346,17L349,28L356,34L340,49L338,61L342,65L346,64L346,65L333,72L334,74L324,81L324,88L322,95L317,94L321,100L317,112L317,106L315,106L315,103L313,103L315,112L318,114L321,120L319,122L322,124L317,129L319,131L318,134L313,135L310,143L304,144L301,152L293,160L291,165L291,177L305,205L305,217L300,220L297,214L294,214L284,202L282,188L272,181L263,186L258,182L252,181L232,184L233,188L231,190L236,193L235,194L229,192L223,194L216,189L211,191L204,189L192,191L188,197L178,202L174,207L172,214L174,221L172,222L163,219L159,216L157,208L144,189L135,188L130,194L121,188L119,179L108,168L97,167L96,171L75,168L50,153L50,151L34,149L33,142L27,135L14,126L16,122L10,110L12,105L9,102L10,96L5,84L6,77L4,73Z"

def rack(x, y, s=1.0, c="#ffcc00"):
    # simple data-center / server-rack icon
    return (f'<g transform="translate({x},{y}) scale({s})">'
            f'<rect x="-15" y="-19" width="30" height="38" rx="3" fill="#09090b" stroke="{c}" stroke-width="2.4"/>'
            + "".join(f'<rect x="-10" y="{yy}" width="20" height="7" rx="1.5" fill="{c}"/>'
                      f'<circle cx="6" cy="{yy+3.5}" r="1.6" fill="#09090b"/>' for yy in (-14, -4, 6))
            + '</g>')

def stamp(x, y, rot):
    return (f'<g transform="translate({x},{y}) rotate({rot})">'
            f'<rect x="-30" y="-13" width="60" height="26" rx="3" fill="rgba(255,45,42,.18)" stroke="#ff2d2a" stroke-width="3"/>'
            f'<text x="0" y="8" text-anchor="middle" font-family="Archivo Black" font-size="19" letter-spacing="2" fill="#ff2d2a">TAX</text></g>')

inside = "".join(rack(x, y, 0.95) for x, y in [(95, 125), (175, 150), (255, 120)])
outside_pts = [(462, 70), (462, 158), (462, 246)]
arrows = "".join(
    f'<path d="M{sx},{sy} Q{(sx+ex)/2},{(sy+ey)/2 - 18} {ex},{ey}" fill="none" stroke="#f4f0e6" stroke-width="2.4" stroke-dasharray="7 6" marker-end="url(#ah)"/>'
    for (sx, sy), (ex, ey) in zip([(282, 108), (282, 145), (282, 182)], [(432, 74), (432, 158), (432, 242)]))
outside = "".join(rack(x, y, 1.05, "#ff2d2a") + stamp(x + 66, y + 2, -10) for x, y in outside_pts)

graphic = f'''<svg xmlns="http://www.w3.org/2000/svg" width="568" height="296" viewBox="0 0 568 296">
<defs><marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 Z" fill="#f4f0e6"/></marker></defs>
<g transform="translate(0,40)"><path d="{US}" fill="#1d1d24" stroke="#ffcc00" stroke-width="2" stroke-linejoin="round"/>
{inside}
<text x="0" y="-18" font-family="Archivo Black" font-size="13" letter-spacing="2.5" fill="#ffcc00">BUILT IN THE U.S.</text></g>
<line x1="398" y1="8" x2="398" y2="290" stroke="#3a3a44" stroke-width="1.5" stroke-dasharray="3 5"/>
<text x="568" y="22" text-anchor="end" font-family="Archivo Black" font-size="13" letter-spacing="2.5" fill="#ff2d2a">BUILT ABROAD</text>
{arrows}
{outside}
</svg>'''

html = wrap(f"""
<div class="footer"><span>Sources: AP, Reuters, CNBC, Nov. 20, 2026</span><span>Whip illustration &middot; not an official graphic</span></div>
<div class="tag"><span class="dot"></span>BREAKING &middot; DATA CENTERS</div>
<div class="left">
  <div class="h1">TRUMP: <span class="y">&ldquo;TREMENDOUS<br>TAX&rdquo;</span> ON U.S.<br>DATA CENTERS<br>BUILT ABROAD</div>
  <div class="att">&ldquo;We&rsquo;re not going to allow our companies to build data centers outside of our country,&rdquo; Trump said at a White House news conference after his Asia trip.</div>
</div>
<div class="panel">
  <div class="ph">WHAT TRUMP DESCRIBED &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>No details yet:</b> announced at a news conference Nov. 20; no bill, rule or tax rate released.</div></div>
  <div class="b"><div class="n">02</div><div><b>Staff not told:</b> Trump said his own staff hadn&rsquo;t heard it yet, per CNBC.</div></div>
  <div class="b"><div class="n">03</div><div><b>Who:</b> U.S. companies building data centers in other countries, per AP.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#3a0a08 0%,#1c0604 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:126px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:56px;line-height:.98;color:#f4f0e6}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:12px;width:470px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:112px;width:600px;z-index:5;background:rgba(18,12,14,.88);border-top:4px solid #ff2d2a;padding:12px 16px 10px}
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
for f in (src, Path(__file__).resolve()):
    shutil.copy(f, dest / f.name); print("copied", dest / f.name)
