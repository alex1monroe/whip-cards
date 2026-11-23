#!/usr/bin/env python3
"""UPDATE card: Trump tells Treasury to help Cassidy's $1.5T Social Security plan (Mon Nov 23, 2026).
Source: The Washington Sun (Jeff Stein, Nov 23, 2026, 5:00 AM). Draft only. Illustration. No Whip scores."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-socsec-cassidy"
FOLDER = "breaking/2026-11-23-socsec-cassidy-trump"
W = 568
RED, YEL, BLU, INK, PAPER, MUTE = "#ff2d2a", "#ffcc00", "#3d8bff", "#09090b", "#f4f0e6", "#8a867c"
parts = []
parts.append(f'<text x="0" y="22" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">THE CASSIDY PLAN · HOW IT WORKS</text>')
parts.append(f'<text x="0" y="44" font-family="Inter" font-size="13" font-weight="600" fill="{MUTE}">As described by The Washington Sun, Nov. 23, 2026</text>')
rows = [("1", "BORROW $1.5T", "The federal government takes on new debt", YEL),
        ("2", "INVEST IT", "A new fund buys stocks, real estate, infrastructure", BLU),
        ("3", "PAY FULL BENEFITS", "Social Security may borrow to pay full benefits", PAPER),
        ("4", "REPAY AFTER 75 YRS", "The fund is sold to refund Social Security's borrowing", MUTE)]
y = 62
for n, lab, note, col in rows:
    parts.append(f'<rect x="0" y="{y}" width="{W}" height="54" rx="4" fill="#15151b" stroke="{col}" stroke-width="2"/>')
    parts.append(f'<text x="18" y="{y+39}" font-family="Anton" font-size="30" fill="{col}">{n}</text>')
    parts.append(f'<text x="60" y="{y+23}" font-family="Archivo Black" font-size="15" letter-spacing="1.2" fill="{PAPER}">{lab}</text>')
    parts.append(f'<text x="60" y="{y+43}" font-family="Inter" font-size="13.5" font-weight="600" fill="#c8c4ba">{note}</text>')
    if n != "4": parts.append(f'<path d="M {W-40} {y+54} l 0 8 l -6 -6 m 6 6 l 6 -6" stroke="{YEL}" stroke-width="2" fill="none"/>')
    y += 62
H = y
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(parts)}</svg>'
html = wrap(f"""
<div class="footer"><span>Source: The Washington Sun (Nov. 23, 2026). Illustration.</span><span>Whip illustration &middot; not a government or news graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; SOCIAL SECURITY</div>
<div class="left">
  <div class="h1">TREASURY TOLD TO<br><span class="y">HELP CASSIDY PLAN</span></div>
  <div class="h2">A $1.5 TRILLION<br>SOCIAL SECURITY FIX</div>
  <div class="att">Odds of passage this Congress are very low, with a few weeks left, per The Washington Sun.</div>
</div>
<div class="panel">
  <div class="ph">THE MECHANICS &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>The deadline:</b> the retirement trust fund runs out in Q4 2032; then automatic cuts of over 20%.</div></div>
  <div class="b"><div class="n">02</div><div><b>Support:</b> Sen. Tim Kaine and AARP back it. Treasury staff give technical help.</div></div>
  <div class="b"><div class="n">03</div><div><b>Critics:</b> CRFB warns of market risk and much higher federal borrowing.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0b2a4a 0%,#0a1a2a 45%,#09090b 82%)}
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
