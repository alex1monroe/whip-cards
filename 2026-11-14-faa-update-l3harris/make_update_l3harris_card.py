#!/usr/bin/env python3
"""UPDATE card: L3Harris statement (Sat Nov 14, ~2 PM ET). Supports FAA investigation; 70%+ of copper-to-fiber conversion done; no cause given. Draft only."""
import shutil
from pathlib import Path
from v4base import wrap, render, HERE
html = wrap("""
<div class="footer"><span>Source: L3Harris statement, Nov 14, 2026; Sec. Duffy briefing (CNN, Washington Post) · root cause not yet confirmed</span><span>Whip illustration · bar approximate</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; THE CONTRACTOR SPEAKS</div>
<div class="left">
  <div class="h1">L3HARRIS<br>RESPONDED.<br><span class="y">IT DIDN'T</span><br>EXPLAIN.</div>
</div>
<div class="panel">
  <div class="ph">WHAT THEY SAID</div>
  <div class="q">&ldquo;We are supporting the FAA in its investigation&hellip; L3Harris takes the nationwide ground stop&hellip; seriously.&rdquo;</div>
  <div class="ph" style="margin-top:20px">THE UPGRADE THEY RUN</div>
  <div class="track"><div class="fill"><span>FIBER &middot; 70%+ DONE</span></div><div class="rest"><span>COPPER LEFT</span></div></div>
  <div class="cap">Air traffic comms conversion from copper to fiber, per L3Harris</div>
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>No cause:</b> the statement doesn't say what failed or answer Duffy's "incompetence" question.</div></div>
  <div class="b"><div class="n">02</div><div><b>Still mid-swap:</b> Duffy says officials are still mapping the copper lines that remain.</div></div>
  <div class="b"><div class="n">03</div><div><b>Next:</b> the FAA says it will share a root cause when the review is done.</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 72% 40%,#2a0b08 0%,#140605 45%,#09090b 80%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ffcc00;color:#09090b;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ff2d2a}
.left{position:absolute;left:48px;top:126px;width:480px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:68px;line-height:.92;color:#f4f0e6}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:132px;width:590px;z-index:5}
.ph{font-family:'Archivo Black',sans-serif;font-size:14px;letter-spacing:.16em;color:#8a867c;margin-bottom:8px}
.q{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:27px;line-height:1.12;color:#f4f0e6;border-left:4px solid #ffcc00;padding-left:14px}
.track{display:flex;height:54px;width:100%}
.fill{width:70%;background:#3fd0ff;box-shadow:0 0 14px rgba(63,208,255,.45);display:flex;align-items:center;padding-left:14px}
.fill span{font-family:'Archivo Black',sans-serif;font-size:17px;letter-spacing:.08em;color:#09090b}
.rest{flex:1;background:repeating-linear-gradient(90deg,#c46a2b 0 18px,#8a4a1e 18px 24px);display:flex;align-items:center;justify-content:center}
.rest span{font-family:'Archivo Black',sans-serif;font-size:13px;letter-spacing:.06em;color:#09090b}
.cap{font-family:'Inter',sans-serif;font-size:12px;color:#8a867c;letter-spacing:.04em;margin-top:8px}
.strip{position:absolute;left:48px;right:48px;top:440px;height:172px;z-index:5;background:rgba(14,14,18,.94);border-top:4px solid #ffcc00;display:grid;grid-template-columns:150px 1fr 1fr 1fr;gap:20px;padding:18px 22px}
.wt{font-family:'Anton',sans-serif;font-size:40px;line-height:.92;color:#f4f0e6}
.b{display:flex;gap:10px;font-weight:600;font-size:20px;line-height:1.16;color:#c8c4ba}
.b b{color:#ffcc00;font-weight:800}
.n{font-family:'Anton',sans-serif;font-size:30px;line-height:.9;color:#ff2d2a}
""")
render("faa-update-l3harris", html)
src = HERE/"cards"/"faa-update-l3harris.png"
for dest in [Path("/home/box/whip/breaking/2026-11-14-faa-update-l3harris/card.png"), Path("/workspace/whip-cards/2026-11-14-faa-update-l3harris/card.png")]:
    dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy(src, dest); print("copied", dest)
