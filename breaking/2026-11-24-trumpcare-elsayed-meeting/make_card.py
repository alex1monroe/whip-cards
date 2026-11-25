#!/usr/bin/env python3
"""UPDATE card: Trump tells NY Post he'll meet Sen.-elect Abdul El-Sayed on 'Trumpcare' Medicare for All (Oval Office interview, Tue Nov 24, 2026).
Sources: New York Post Nov 24 (exclusive), Nov 22 (Truth Social repost), Nov 11/12 (El-Sayed pitch). Draft only. Whip illustration. No Whip scores. No hook."""
import shutil, sys, subprocess
from pathlib import Path
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import wrap
OUT = Path(__file__).resolve().parent
NAME = "update-trumpcare-meeting"
FOLDER = "breaking/2026-11-24-trumpcare-elsayed-meeting"
W, H = 568, 300
GRN, YEL, RED, BLU, PAPER, MUTE = "#2fd28a", "#ffcc00", "#ff2d2a", "#3d8bff", "#f4f0e6", "#8a867c"
p = []
p.append(f'<text x="0" y="18" font-family="Archivo Black" font-size="14" letter-spacing="1.6" fill="{PAPER}">HOW WE GOT HERE</text>')
steps = [("NOV. 12", "El-Sayed pitch", "Pitch posted on X", BLU),
         ("NOV. 22", "Trump repost", "Mock-up on Truth Social", RED),
         ("NOV. 24", "Meeting pledge", "Says he&rsquo;ll meet", YEL)]
ty = 70
p.append(f'<line x1="30" y1="{ty}" x2="530" y2="{ty}" stroke="#4a4a54" stroke-width="3"/>')
for i, (d, h, s, col) in enumerate(steps):
    x = 30 + i * 250
    last = i == 2
    p.append(f'<circle cx="{x}" cy="{ty}" r="{12 if last else 9}" fill="{col}" stroke="{PAPER}" stroke-width="2"/>')
    anchor = "start" if i == 0 else ("end" if last else "middle")
    xx = x - 12 if i == 0 else (x + 12 if last else x)
    p.append(f'<text x="{xx}" y="{ty+34}" text-anchor="{anchor}" font-family="Archivo Black" font-size="13" fill="{YEL if last else PAPER}">{d}</text>')
    p.append(f'<text x="{xx}" y="{ty+54}" text-anchor="{anchor}" font-family="Anton" font-size="19" fill="{PAPER}">{h.upper()}</text>')
    p.append(f'<text x="{xx}" y="{ty+72}" text-anchor="{anchor}" font-family="Inter" font-size="11.5" font-weight="600" fill="#c8c4ba">{s}</text>')
qy = 182
p.append(f'<rect x="0" y="{qy}" width="568" height="104" fill="#14141a" stroke="{GRN}" stroke-width="2"/>')
p.append(f'<text x="18" y="{qy+40}" font-family="Anton" font-size="27" fill="{PAPER}">&ldquo;MAYBE THERE&rsquo;S SOME PLACE IN</text>')
p.append(f'<text x="18" y="{qy+72}" font-family="Anton" font-size="27" fill="{GRN}">THE MIDDLE THAT WE COULD GO.&rdquo;</text>')
p.append(f'<text x="18" y="{qy+94}" font-family="Inter" font-size="12" font-weight="600" fill="{MUTE}">President Trump to the New York Post, Oval Office interview, Nov. 24</text>')
graphic = f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{"".join(p)}</svg>'
html = wrap(f"""
<div class="footer"><span>Sources: New York Post (Nov. 12, 22 &amp; 24, 2026). Illustration.</span><span>Whip illustration &middot; not a White House or news graphic</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; HEALTH CARE</div>
<div class="left">
  <div class="h1">TRUMP TO MEET<br><span class="y">EL-SAYED</span></div>
  <div class="h2">ON &ldquo;TRUMPCARE&rdquo;<br>MEDICARE FOR ALL</div>
  <div class="att">President Trump told the New York Post he will meet with Michigan Sen.-elect Abdul El-Sayed to discuss his Medicare for All plan, branded &ldquo;Trumpcare.&rdquo; Trump called the branding &ldquo;very smart.&rdquo; No date was given.</div>
  <div class="chips"><span>Single-payer plan</span><span>No date set</span></div>
</div>
<div class="panel">
  <div class="ph">THE PITCH &middot; WHIP ILLUSTRATION</div>
  {graphic}
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>The meeting:</b> Trump says it will happen; he did not give a date, per the Post.</div></div>
  <div class="b"><div class="n">02</div><div><b>The plan:</b> El-Sayed&rsquo;s single-payer Medicare for All proposal, which he has branded &ldquo;Trumpcare.&rdquo;</div></div>
  <div class="b"><div class="n">03</div><div><b>Next step:</b> any bill would need Congress, where Democrats are set to control both chambers in January.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 70% 38%,#0a3a2e 0%,#0a2a22 45%,#09090b 82%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a;display:inline-block}
.left{position:absolute;left:48px;top:122px;width:500px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:74px;line-height:.98;color:#f4f0e6;letter-spacing:.01em}
.h2{font-family:'Anton',sans-serif;font-size:28px;line-height:1.02;color:#f4f0e6;margin-top:8px}
.att{font-family:'Inter',sans-serif;font-size:15px;line-height:1.35;color:#c8c4ba;margin-top:10px;width:470px}
.chips{display:flex;gap:8px;margin-top:12px}
.chips span{font-family:'Archivo Black',sans-serif;font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#09090b;background:#2fd28a;padding:5px 9px 4px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:100px;width:600px;z-index:5;background:rgba(10,14,18,.88);border-top:4px solid #2fd28a;padding:12px 16px 10px}
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
