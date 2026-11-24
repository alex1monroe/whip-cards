#!/usr/bin/env python3
"""CLIP card: Rep. Hakeem Jeffries on Medicare at the Nov. 17 Capitol news conference.
Source: official House video posted by Rep. Jeffries (jeffries.house.gov / YouTube 3d1Km9hLlHg).
Clip: 00:18:23.000–00:18:51.050. No Whip scores. No predictions. Illustration."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "clip-jeffries-medicare"
FOLDER = "breaking/2026-11-24-jeffries-medicare"
W = 568
RED, YEL, BLU, INK, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#09090b", "#f4f0e6", "#8a867c"
parts = []
parts.append(f'<text x="0" y="18" font-family="Archivo Black" font-size="13" letter-spacing="1.6" fill="{MUTE}">THE REMARKS &#183; AS SAID</text>')
rows = [
    ("01", "Lower the Medicare age", "“We should lower the age of Medicare eligibility.”", YEL, True),
    ("02", "Vision, hearing, and dental", "“We should expand coverage to include vision, hearing, and dental.”", PAPER, False),
    ("03", "Cover all the kids", "“And we should cover all the kids in the United States of America.”", PAPER, False),
]
y = 32
for num, lab, note, col, hot in rows:
    h = 72
    if hot:
        parts.append(f'<rect x="0" y="{y}" width="{W}" height="{h}" rx="4" fill="#3a2e0c" stroke="{YEL}" stroke-width="2.5"/>')
    else:
        parts.append(f'<rect x="0" y="{y}" width="{W}" height="{h}" rx="4" fill="#15151b" stroke="#5a5a62" stroke-width="1.5"/>')
    parts.append(f'<text x="16" y="{y+44}" font-family="Anton" font-size="26" fill="{YEL if hot else RED}">{num}</text>')
    parts.append(f'<text x="58" y="{y+28}" font-family="Archivo Black" font-size="14" letter-spacing="1.0" fill="{PAPER}">{lab.upper()}</text>')
    parts.append(f'<text x="58" y="{y+50}" font-family="Inter" font-size="12.5" font-weight="600" fill="#c8c4ba">{note}</text>')
    y += h + 8
H = y
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Source: Rep. Hakeem Jeffries, official Nov. 17 Capitol news conference, posted by the Office of Democratic Leader Hakeem Jeffries (jeffries.house.gov; YouTube, “Leader Jeffries on House Democrats’ Priorities for the Next Congress”). Clip: 18:23–18:51 of that video.</span><span>Whip illustration</span></div>
<div class="tag"><span class="dot"></span>CLIP &middot; MEDICARE</div>
<div class="left">
  <div class="h1">&ldquo;WE SHOULD<br>LOWER THE AGE<br>OF <span class="y">MEDICARE.</span>&rdquo;</div>
  <div class="att">Rep. Hakeem Jeffries, Nov. 17 Capitol news conference. He also said coverage should include vision, hearing, and dental, “and we should cover all the kids in the United States of America.”</div>
</div>
<div class="panel">
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>On the record:</b> Jeffries said, “We should lower the age of Medicare eligibility. We should expand coverage to include vision, hearing, and dental. And we should cover all the kids in the United States of America.”</div></div>
  <div class="b"><div class="n">02</div><div><b>Context:</b> He was answering NBC’s Sahil Kapur at the official Nov. 17 conference. He did not name a specific eligibility age in the answer.</div></div>
  <div class="b"><div class="n">03</div><div><b>Also in the clip:</b> He said those steps come after “reversing the Medicaid cuts and extending the Affordable Care Act tax credits.”</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 72% 40%,#2a1f05 0%,#120d04 45%,#09090b 80%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a}
.left{position:absolute;left:48px;top:126px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:58px;line-height:.95;color:#f4f0e6}
.att{font-family:'Inter',sans-serif;font-size:16px;line-height:1.35;color:#c8c4ba;margin-top:16px;width:470px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:118px;width:600px;z-index:5}
.panel svg{display:block;width:100%;height:auto}
.strip{position:absolute;left:48px;right:48px;top:448px;height:162px;z-index:5;background:rgba(14,14,18,.94);border-top:4px solid #ffcc00;display:grid;grid-template-columns:150px 1.15fr 1fr 1fr;gap:16px;padding:16px 20px}
.wt{font-family:'Anton',sans-serif;font-size:40px;line-height:.92;color:#f4f0e6}
.b{display:flex;gap:10px;font-weight:600;font-size:16px;line-height:1.16;color:#c8c4ba}
.b b{color:#ffcc00;font-weight:800}
.n{font-family:'Anton',sans-serif;font-size:28px;line-height:.9;color:#ff2d2a;flex:none}
.footer span:first-child{max-width:980px;line-height:1.25}
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
