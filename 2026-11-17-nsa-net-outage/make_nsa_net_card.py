#!/usr/bin/env python3
"""BREAKING card: NSA Net classified network outage (CNN, Nov 17, 2026). Draft only."""
import shutil
from pathlib import Path
from v4base import wrap, render, HERE
html = wrap("""
<div class="footer"><span>Sources: CNN (via Reuters, Mediaite), Nov 17, 2026; earlier causes per Microsoft, FAA/DOT, JPMorgan Chase, United (Reuters, The Hill, AP)</span><span>Whip illustration</span></div>
<div class="tag"><span class="dot"></span>BREAKING &middot; NATIONAL SECURITY</div>
<div class="left">
  <div class="h1">NSA&rsquo;S<br>CLASSIFIED<br>NETWORK<br><span class="y">GOES DOWN.</span></div>
  <div class="att">CNN, citing people familiar with the matter: no evidence of a cyberattack so far.</div>
</div>
<div class="panel">
  <div class="ph">A WEEK OF U.S. OUTAGES &middot; STATED CAUSE</div>
  <div class="grid5">
    <div class="bk"><b>MICROSOFT</b><em>THU 11/12</em><span>Network capacity upgrade issue</span><i class="g">CAUSE GIVEN</i></div>
    <div class="bk"><b>FAA</b><em>FRI 11/13</em><span>Router install at Arkansas site</span><i class="g">CAUSE GIVEN</i></div>
    <div class="bk"><b>UNITED</b><em>MON 11/16</em><span>&ldquo;Technology issue&rdquo;</span><i class="o">NOT DISCLOSED</i></div>
    <div class="bk"><b>CHASE</b><em>MON 11/16</em><span>Software bug in on-premise hardware</span><i class="g">CAUSE GIVEN</i></div>
    <div class="bk hot"><b>NSA NET</b><em>TUE 11/17</em><span>Under assessment</span><i>UNKNOWN</i></div>
  </div>
  <div class="legend"><span class="sw r"></span>New today <span class="sw gr"></span>Earlier outages, separate incidents</div>
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>What&rsquo;s down:</b> the internal network NSA staff use to share classified information.</div></div>
  <div class="b"><div class="n">02</div><div><b>Cause:</b> unknown. Staff were told to stagger arrivals; the NSA hasn&rsquo;t commented.</div></div>
  <div class="b"><div class="n">03</div><div><b>Earlier today:</b> DHS Sec. Mullin said the prior outages weren&rsquo;t cyberattacks (CNBC).</div></div>
</div>
""", """
body{background:radial-gradient(ellipse at 72% 40%,#0b2a24 0%,#071a17 45%,#09090b 80%)}
.tag{position:absolute;top:76px;left:48px;display:flex;align-items:center;gap:10px;background:#ff2d2a;color:#f4f0e6;font-family:'Archivo Black',sans-serif;font-size:18px;letter-spacing:.18em;padding:7px 14px 6px;z-index:5}
.dot{width:10px;height:10px;border-radius:50%;background:#ffcc00}
.left{position:absolute;left:48px;top:122px;width:440px;z-index:5}
.h1{font-family:'Anton',sans-serif;font-size:60px;line-height:.95;color:#f4f0e6}
.att{font-family:'Inter',sans-serif;font-size:15px;color:#8a867c;margin-top:14px;width:400px}
.y{color:#ffcc00}
.panel{position:absolute;right:48px;top:118px;width:640px;z-index:5}
.ph{font-family:'Archivo Black',sans-serif;font-size:14px;letter-spacing:.16em;color:#8a867c;margin-bottom:10px}
.grid5{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;height:240px}
.bk em{font-style:normal;font-family:'Archivo Black',sans-serif;font-size:12px;letter-spacing:.1em;color:#ffcc00}
.bk i.o{background:#b5651d}
.grid{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;height:230px}
.ic{font-size:34px;color:#ffcc00;line-height:1}
.bk.ok .ic{color:#8a867c}
.bk i.g{background:#5a5a62}
.flow{display:grid;grid-template-columns:1fr 50px 1.1fr;gap:8px;height:230px;align-items:stretch}
.col{display:grid;grid-template-rows:1fr 1fr;gap:10px}
.arr{font-size:46px;color:#ffcc00;display:flex;align-items:center;justify-content:center}
.bk{background:repeating-linear-gradient(135deg,#2e2e35 0 12px,#25252b 12px 24px);border:3px solid #5a5a62;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:6px;padding:8px}
.bk b{font-family:'Anton',sans-serif;font-size:26px;color:#f4f0e6;line-height:1}
.bk.sm b{font-size:26px}
.bk span{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:18px;color:#c8c4ba;line-height:1.05}
.bk.sm span{font-size:16px}
.bk i{font-style:normal;font-family:'Archivo Black',sans-serif;font-size:12px;letter-spacing:.1em;background:#ff2d2a;color:#f4f0e6;padding:4px 7px 3px;margin-top:4px}
.bk.hot{border-color:#ff2d2a;background:repeating-linear-gradient(135deg,#3a1c1c 0 12px,#2c1515 12px 24px)}
.legend{margin-top:12px;font-family:'Inter',sans-serif;font-size:13px;color:#8a867c;display:flex;align-items:center;gap:8px}
.sw{display:inline-block;width:14px;height:14px}.sw.r{background:#ff2d2a}.sw.gr{background:#5a5a62;margin-left:14px}
.strip{position:absolute;left:48px;right:48px;top:448px;height:162px;z-index:5;background:rgba(14,14,18,.94);border-top:4px solid #ffcc00;display:grid;grid-template-columns:150px 1fr 1fr 1fr;gap:20px;padding:18px 22px}
.wt{font-family:'Anton',sans-serif;font-size:40px;line-height:.92;color:#f4f0e6}
.b{display:flex;gap:10px;font-weight:600;font-size:19px;line-height:1.16;color:#c8c4ba}
.b b{color:#ffcc00;font-weight:800}
.n{font-family:'Anton',sans-serif;font-size:30px;line-height:.9;color:#ff2d2a}
""")
render("nsa-net-outage", html)
src = HERE/"cards"/"nsa-net-outage.png"
for dest in [Path("/home/box/whip/breaking/2026-11-17-nsa-net-outage/card.png"), Path("/workspace/whip-cards/2026-11-17-nsa-net-outage/card.png")]:
    dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy(src, dest); print("copied", dest)
