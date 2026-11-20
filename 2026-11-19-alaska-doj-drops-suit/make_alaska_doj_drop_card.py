#!/usr/bin/env python3
"""UPDATE card: DOJ moves to drop Alaska Senate certification suit (Nov 19, 2026). Draft only."""
import shutil
from pathlib import Path
from v4base import wrap, render, HERE
CSS = open('/tmp/whip_common_css.txt').read()
html = wrap("""
<div class="footer"><span>Sources: AP, Nov 19, 2026; DOJ 9th Cir. filing via Democracy Docket; Alaska Division of Elections via ADN</span><span>Whip illustration &middot; timeline not to scale</span></div>
<div class="tag"><span class="dot"></span>UPDATE &middot; ALASKA SENATE</div>
<div class="left">
  <div class="h1">DOJ MOVES<br>TO DROP<br><span class="y">ALASKA SUIT.</span></div>
  <div class="att">The Trump administration told the 9th Circuit its challenge to certifying Democrat Mary Peltola&rsquo;s win is now moot, per AP.</div>
</div>
<div class="panel">
  <div class="ph">HOW THE CHALLENGE PLAYED OUT</div>
  <div class="tl">
    <div class="st"><div class="dt">OCT</div><div class="pt"></div><div class="tx"><b>DOJ sues</b> to block certification over a 2nd &ldquo;Dan Sullivan&rdquo; on the ballot</div></div>
    <div class="st"><div class="dt">PRE-VOTE</div><div class="pt"></div><div class="tx"><b>Judge dismisses</b>; DOJ appeals to the 9th Circuit</div></div>
    <div class="st"><div class="dt">NOV 17</div><div class="pt"></div><div class="tx"><b>AP calls race</b> for Peltola at 50.1% of first-choice votes</div></div>
    <div class="st now"><div class="dt">NOV 19</div><div class="pt"></div><div class="tx"><b>DOJ: case is moot</b>; asks court to vacate the dismissal</div></div>
    <div class="st nx"><div class="dt">NOV 25</div><div class="pt"></div><div class="tx"><b>Certification target</b> set by Alaska&rsquo;s Division of Elections</div></div>
  </div>
</div>
<div class="strip">
  <div class="wt">WHAT THIS<br><span class="y">MEANS</span></div>
  <div class="b"><div class="n">01</div><div><b>Path to certify:</b> Alaska&rsquo;s election director says the state will certify the Senate result.</div></div>
  <div class="b"><div class="n">02</div><div><b>Not fully closed:</b> DOJ still wants the lower-court dismissal wiped from the record.</div></div>
  <div class="b"><div class="n">03</div><div><b>No concession yet:</b> Sullivan&rsquo;s campaign says it will wait until the race is certified.</div></div>
</div>
""", CSS + """
.tl{position:relative;margin-top:22px;padding-left:4px}
.tl:before{content:'';position:absolute;left:107px;top:10px;bottom:10px;width:3px;background:#3a3a42}
.st{display:grid;grid-template-columns:90px 30px 1fr;align-items:center;margin-bottom:13px;position:relative}
.dt{font-family:'Archivo Black',sans-serif;font-size:13px;letter-spacing:.08em;color:#8a867c;text-align:right;padding-right:6px}
.pt{width:16px;height:16px;border-radius:50%;background:#5a5a62;border:3px solid #09090b;margin-left:4px;z-index:2}
.tx{font-family:'Inter',sans-serif;font-size:14px;line-height:1.25;color:#c8c4ba}
.tx b{color:#f4f0e6;font-weight:800}
.st.now .pt{background:#ffcc00;width:22px;height:22px;margin-left:1px;box-shadow:0 0 0 4px rgba(255,204,0,.25)}
.st.now .dt,.st.now .tx b{color:#ffcc00}
.st.nx .pt{background:#09090b;border:3px dashed #ff2d2a}
.st.nx .dt{color:#ff2d2a}
""")
render("alaska-doj-drop-update", html)
src = HERE/"cards"/"alaska-doj-drop-update.png"
for dest in [Path("/home/box/whip/breaking/2026-11-19-alaska-doj-drops-suit/card.png"), Path("/workspace/whip-cards/2026-11-19-alaska-doj-drops-suit/card.png")]:
    dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy(src, dest); print("copied", dest)
