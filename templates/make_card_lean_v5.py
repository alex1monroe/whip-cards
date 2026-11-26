#!/usr/bin/env python3
"""Whip LEAN v5 card renderer: one idea, one hero element, <=40 words.

Usage:
    python3 make_card_lean_v5.py spec.json [--formats tall,wide] [--lockup out.png]

Formats:
    tall  1220x1546 CSS -> 2440x3092 PNG (X feed, ~4:5)
    wide  1920x1080 CSS -> 3840x2160 PNG (16:9, Kick stream)

JSON spec:
    layout        "quote" | "gap"
    output        base path (no extension). tall -> <base>.png, wide -> <base>-16x9.png
    kicker        e.g. "BREAKING · FREE SPEECH"  (rendered by the reusable lockup)
    date          e.g. "Nov. 25, 2026"
    headline      small top line (tier 2), <=20 words
    quote         layout=quote: verbatim quote (no quote marks; they are drawn)
    attribution   layout=quote: e.g. "Judge Loren AliKhan, U.S. District Court"
    gap           layout=gap: {"from": {"date","text"}, "big": "1 DAY",
                               "big_sub": "optional", "to": {"date","text"}}
    finding       optional attributed line above other_side, e.g. "Judge: ..."
    other_side    one line, e.g. "FCC: Review grew out of its diversity probe."
                  Text before the first ":" is set bold as the speaker label.
    source        e.g. "Source: ABC v. FCC, D.D.C., Nov. 25 opinion"
    footer_right  default "Whip illustration"
    art           "tower" | "none"  (stylized graphic drawn in SVG, no photos)

Wrap 1-2 words in *asterisks* to set them in yellow (use yellow on 1-2 words only).
Type scale: hero (Anton / Source Serif Black, huge) > headline (Inter 800) > body (Inter 600).
No CSS text below 24px (=48px at output) — enforced by assert.
Prints word count (excluding brand, date, footer). Never posts or copies anywhere.
"""
from __future__ import annotations

import html as H
import json
import re
import subprocess
import sys
from pathlib import Path

import os
_CWD = Path.cwd()
sys.path.insert(0, "/home/box/whip/threads/2026-11-14-faa")
from v4base import FACE  # noqa: E402
os.chdir(_CWD)

SERIF = """
@font-face{font-family:'SSP';font-weight:900;src:url('file:///usr/share/fonts/truetype/sand-box/custom/Source Serif Pro/SourceSerifPro-Black.ttf')}
@font-face{font-family:'SSP';font-weight:700;src:url('file:///usr/share/fonts/truetype/sand-box/custom/Source Serif Pro/SourceSerifPro-Bold.ttf')}
"""
YEL, RED, PAPER, MUTE, INK = "#ffcc00", "#ff2d2a", "#f4f0e6", "#9a968c", "#08090a"
MIN_PX = 24
ART_W = {}
SIZES = {"tall": (1220, 1546), "wide": (1920, 1080)}


def esc(s):
    return H.escape(s or "", quote=True)


def mark(s):
    """escape + *word* -> yellow span"""
    out = re.sub(r"\*(.+?)\*", r'<span class="y">\1</span>', esc(s))
    return out.replace("|", "<br>")


def words(s):
    return len(re.findall(r"[A-Za-z0-9][\w'’.-]*", (s or "").replace("*", "").replace("|", " ")))


def tower_svg(cls="art"):
    # stylized broadcast tower: lattice mast + signal arcs, one yellow beacon
    arcs = "".join(
        f'<path d="M{200-r} {120} A{r} {r} 0 0 1 {200+r} 120" fill="none" stroke="#2c3b35" '
        f'stroke-width="10" stroke-linecap="round" opacity="{1-i*0.22:.2f}" transform="rotate(0 200 120)"/>'
        for i, r in enumerate((70, 120, 170, 220))
    )
    lattice = ""
    ys = [180, 300, 420, 540, 660, 780]
    for i in range(len(ys) - 1):
        y0, y1 = ys[i], ys[i + 1]
        w0, w1 = 20 + (y0 - 160) * 0.16, 20 + (y1 - 160) * 0.16
        lattice += f'<path d="M{200-w0} {y0} L{200+w1} {y1} M{200+w0} {y0} L{200-w1} {y1}" stroke="#24312c" stroke-width="7"/>'
        lattice += f'<path d="M{200-w1} {y1} H{200+w1}" stroke="#2c3b35" stroke-width="8"/>'
    return f'''<svg class="{cls}" viewBox="0 0 400 820" aria-hidden="true">
  {arcs}
  <path d="M200 120 V170" stroke="#2c3b35" stroke-width="10" stroke-linecap="round"/>
  <path d="M180 170 L{200-119} 800 M220 170 L{200+119} 800" stroke="#2c3b35" stroke-width="12" stroke-linecap="round"/>
  {lattice}
  <circle cx="200" cy="120" r="22" fill="{YEL}"/>
  <circle cx="200" cy="120" r="44" fill="none" stroke="{YEL}" stroke-width="4" opacity=".35"/>
</svg>'''


def lockup(kicker):
    k = esc(kicker)
    first, _, rest = k.partition(" · ")
    rest_h = f'<span class="lk-rest">{rest}</span>' if rest else ""
    return f'<div class="lockup"><span class="lk-main"><span class="lk-dot"></span>{first}</span>{rest_h}</div>'


LOCKUP_CSS = f"""
.lockup{{display:inline-flex;align-items:stretch;font-family:'Archivo Black',sans-serif;letter-spacing:.14em;line-height:1;width:max-content}}
.lk-main{{display:inline-flex;align-items:center;gap:14px;background:{YEL};color:{INK};padding:12px 20px 11px}}
.lk-dot{{width:16px;height:16px;border-radius:50%;background:{RED};display:inline-block;box-shadow:0 0 0 4px rgba(255,45,42,.25)}}
.lk-rest{{display:inline-flex;align-items:center;background:{PAPER};color:{INK};padding:12px 20px 11px}}
"""


def hero_quote(d, fmt):
    return f'''<div class="hero quote">
  <div class="qmark">“</div>
  <div class="qtext">{mark(d["quote"])}”</div>
  <div class="attr"><span class="bar"></span>{esc(d["attribution"])}</div>
</div>'''


def hero_gap(d, fmt):
    g = d["gap"]
    sub = f'<div class="bigsub">{mark(g["big_sub"])}</div>' if g.get("big_sub") else ""
    if fmt == "tall":
        return f'''<div class="hero gap tall">
  <div class="rail r1"><span class="fat-dot"></span><span class="fat-line"></span></div>
  <div class="beat b1"><div class="bd">{esc(g["from"]["date"])}</div><div class="bt">{mark(g["from"]["text"])}</div></div>
  <div class="rail r2"><span class="fat-line"></span></div>
  <div class="bigwrap"><div class="big">{mark(g["big"])}</div>{sub}</div>
  <div class="rail r3"><span class="fat-line"></span><span class="fat-dot y"></span><span class="fill"></span></div>
  <div class="beat b2"><div class="bd">{esc(g["to"]["date"])}</div><div class="bt">{mark(g["to"]["text"])}</div></div>
</div>'''
    return f'''<div class="hero gap {fmt}">
  <div class="beat b1"><div class="bd">{esc(g["from"]["date"])}</div><div class="bt">{mark(g["from"]["text"])}</div></div>
  <div class="link"><span class="fat-dot"></span><span class="fat-line"></span><div class="big">{mark(g["big"])}</div>{sub}<span class="fat-line"></span><span class="fat-dot y"></span></div>
  <div class="beat b2"><div class="bd">{esc(g["to"]["date"])}</div><div class="bt">{mark(g["to"]["text"])}</div></div>
</div>'''


def other_side(s, cls="other"):
    s = s or ""
    if ":" in s:
        lab, _, rest = s.partition(":")
        return f'<div class="other {cls}"><b>{esc(lab)}:</b>{esc(rest)}</div>'
    return f'<div class="other {cls}">{esc(s)}</div>'


def css_for(fmt, layout):
    W, Hh = SIZES[fmt]
    tall = fmt == "tall"
    s = dict(
        logo=26, handle=26, lockup=30, date=28,
        headline=56 if tall else 50,
        qtext=184 if tall else 164, qmark=420 if tall else 320, attr=34 if tall else 32,
        big=380 if tall else 300, bd=44 if tall else 40, bt=50 if tall else 44,
        other=34 if tall else 32, source=26, footr=26,
    )
    assert min(s.values()) >= MIN_PX, s
    pad = 72 if tall else 88
    if tall:
        page = f".page{{position:absolute;left:{pad}px;right:{pad}px;top:120px;bottom:150px;display:flex;flex-direction:column;z-index:5}}"
        art = ".art{position:absolute;right:30px;bottom:150px;width:%dpx;opacity:.9;z-index:1}" % ART_W.get("tall", 400)
    else:
        page = f".page{{position:absolute;left:{pad}px;right:{pad}px;top:120px;bottom:130px;display:flex;flex-direction:column;z-index:5}}"
        art = ".art{position:absolute;right:60px;bottom:150px;height:%dpx;opacity:.9;z-index:1}" % ART_W.get("wide", 760)
    gap_css = ""
    if layout == "gap":
        if tall:
            gap_css = f"""
.hero.gap{{display:grid;grid-template-columns:44px 1fr;column-gap:40px;margin-top:56px}}
.rail{{display:flex;flex-direction:column;align-items:center}}
.r1{{padding-top:2px}} .r1 .fat-line{{flex:1}} .r2 .fat-line{{flex:1}} .r3 .fat-line{{height:2px}} .r3 .fill{{flex:1}}
.beat{{max-width:980px}}
.bigwrap{{padding:44px 0 40px}}
.b2{{padding-top:0}}
.bd{{font-family:'Anton',sans-serif;font-size:{s['bd']}px;letter-spacing:.04em;color:{MUTE};line-height:1}}
.bt{{font-family:'Inter',sans-serif;font-weight:700;font-size:{s['bt']}px;line-height:1.12;color:{PAPER};margin-top:12px;letter-spacing:-.01em}}
.fat-line{{width:14px;background:#4a504c;display:block}}
.fat-dot{{width:44px;height:44px;border-radius:50%;background:{PAPER};flex:0 0 44px;display:block}}
.fat-dot.y{{background:{YEL}}}
.big{{font-family:'Anton',sans-serif;font-size:{s['big']}px;line-height:.86;color:{PAPER};letter-spacing:-.005em;margin-left:-8px}}
"""
        else:
            gap_css = f"""
.hero.gap{{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:48px;flex:3;margin-top:20px}}
.beat{{}}
.b2{{text-align:left}}
.bd{{font-family:'Anton',sans-serif;font-size:{s['bd']}px;letter-spacing:.04em;color:{MUTE};line-height:1}}
.bt{{font-family:'Inter',sans-serif;font-weight:700;font-size:{s['bt']}px;line-height:1.12;color:{PAPER};margin-top:12px}}
.link{{display:flex;flex-direction:row;align-items:center;gap:18px}}
.fat-line{{width:46px;height:14px;background:#3a3f3c}}
.fat-dot{{width:40px;height:40px;border-radius:50%;background:{PAPER};flex:0 0 40px}}
.fat-dot.y{{background:{YEL}}}
.big{{font-family:'Anton',sans-serif;font-size:{s['big']}px;line-height:.9;color:{PAPER};white-space:nowrap}}
"""
    return f"""{FACE}{SERIF}{LOCKUP_CSS}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{Hh}px;overflow:hidden;position:relative;color:{PAPER}}}
body{{background:radial-gradient(ellipse at {80 if tall else 85}% {70 if tall else 40}%,#0b2f26 0%,#0a1c17 40%,{INK} 78%)}}
.grain{{position:absolute;inset:0;pointer-events:none;opacity:.04;mix-blend-mode:overlay;z-index:8;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}}
.topbar{{position:absolute;top:0;left:0;right:0;height:10px;background:{YEL};z-index:6}}
.brand{{position:absolute;top:40px;left:{pad}px;right:{pad}px;display:flex;align-items:center;gap:16px;z-index:6}}
.logo{{background:{PAPER};color:{INK};font-family:'Archivo Black',sans-serif;font-size:{s['logo']}px;letter-spacing:.14em;padding:7px 12px 6px;line-height:1}}
.handle{{color:{MUTE};font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:{s['handle']}px;letter-spacing:.14em;text-transform:uppercase}}
.datel{{margin-left:auto;font-family:'Inter',sans-serif;font-weight:700;font-size:{s['date']}px;color:{MUTE}}}
.lockup{{font-size:{s['lockup']}px}}
.headline{{font-family:'Inter',sans-serif;font-weight:800;font-size:{s['headline']}px;line-height:1.1;letter-spacing:-.015em;color:{PAPER};margin-top:34px;max-width:{1020 if tall else 1300}px}}
.y{{color:{YEL}}}
.hero.quote{{margin-top:{64 if tall else 56}px;position:relative;max-width:{1076 if tall else 1380}px}}
.qmark{{font-family:'SSP',serif;font-weight:900;font-size:{s['qmark']}px;line-height:.62;color:{YEL};height:{int(s['qmark']*0.30)}px;margin-left:-12px}}
.qtext{{font-family:'SSP',serif;font-weight:900;font-size:{s['qtext']}px;line-height:.98;letter-spacing:-.02em;color:{PAPER}}}
.attr{{display:flex;align-items:center;gap:20px;margin-top:40px;font-family:'Inter',sans-serif;font-weight:700;font-size:{s['attr']}px;color:#d8d4ca}}
.bar{{width:64px;height:8px;background:{YEL};flex:0 0 64px}}
.spacer{{flex:1}}
.other{{font-family:'Inter',sans-serif;font-weight:600;font-size:{s['other']}px;line-height:1.25;color:#cfcbc1;border-left:8px solid #4a4f4c;padding:10px 28px 10px 24px;width:max-content;max-width:{1000 if tall else 1300}px;background:rgba(8,9,10,.55)}}
.other b{{color:{PAPER};font-weight:800}}
.other.finding{{border-left-color:{PAPER};margin-bottom:18px;color:{PAPER}}}
.footer{{position:absolute;left:{pad}px;right:{pad}px;bottom:44px;display:flex;justify-content:space-between;align-items:center;gap:24px;border-top:2px solid #2a2d2b;padding-top:20px;z-index:6;font-family:'Inter',sans-serif;font-weight:600}}
.source{{font-size:{s['source']}px;color:#bdb9af}}
.footr{{font-size:{s['footr']}px;color:{MUTE};white-space:nowrap}}
{page}
{art}
{gap_css}
"""


def build(d, fmt):
    layout = d.get("layout", "quote")
    ART_W.clear(); ART_W.update(d.get("art_size") or {})
    hero = hero_quote(d, fmt) if layout == "quote" else hero_gap(d, fmt)
    art = tower_svg() if d.get("art", "tower") == "tower" and ART_W.get(fmt, 1) else ""
    return f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{css_for(fmt, layout)}</style></head><body>
<div class="topbar"></div>
<div class="brand"><div class="logo">WHIP</div><div class="handle">@whipcampaigns</div><div class="datel">{esc(d.get('date'))}</div></div>
{art}
<div class="page">
  {lockup(d.get('kicker', 'BREAKING'))}
  <div class="headline">{mark(d.get('headline'))}</div>
  {hero}
  <div class="spacer"></div>
  {other_side(d.get('finding'), 'finding') if d.get('finding') else ''}
  {other_side(d.get('other_side'))}
</div>
<div class="footer"><div class="source">{esc(d.get('source'))}</div><div class="footr">{esc(d.get('footer_right') or 'Whip illustration')}</div></div>
<div class="grain"></div>
</body></html>"""


def chrome(html_text, out_png, W, Hh, transparent=False):
    out_png = Path(out_png).resolve()
    out_png.parent.mkdir(parents=True, exist_ok=True)
    tmp = out_png.with_suffix(".tmp.html")
    tmp.write_text(html_text)
    cmd = ["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
           "--force-device-scale-factor=2", f"--window-size={W},{Hh}", f"--screenshot={out_png}"]
    if transparent:
        cmd.append("--default-background-color=00000000")
    r = subprocess.run(cmd + ["file://" + str(tmp)], capture_output=True, text=True)
    tmp.unlink(missing_ok=True)
    if r.returncode != 0:
        sys.exit("render failed: " + r.stderr[-800:])
    return out_png


def render_lockup(kicker, out_png):
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{FACE}{LOCKUP_CSS}
*{{margin:0;padding:0}} html,body{{background:transparent}} .lockup{{font-size:30px;margin:0}}</style></head>
<body>{lockup(kicker)}</body></html>"""
    p = chrome(html, out_png, 1000, 120, transparent=True)
    from PIL import Image
    im = Image.open(p).convert("RGBA")
    im.crop(im.getbbox()).save(p)
    return p


def word_count(d):
    parts = [d.get("kicker"), d.get("headline"), d.get("finding"), d.get("other_side")]
    if d.get("layout", "quote") == "quote":
        parts += [d.get("quote"), d.get("attribution")]
    else:
        g = d["gap"]
        parts += [g["from"]["date"], g["from"]["text"], g["big"], g.get("big_sub"), g["to"]["date"], g["to"]["text"]]
    return sum(words(p) for p in parts if p)


def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    spec = Path(args[0]).resolve()
    d = json.loads(spec.read_text())
    fmts = ["tall"]
    if "--formats" in args:
        fmts = args[args.index("--formats") + 1].split(",")
    base = Path(d.get("output") or spec.with_suffix(""))
    if not base.is_absolute():
        base = spec.parent / base
    for blk in ("headline", "finding", "other_side", "quote"):
        if words(d.get(blk)) > 20:
            print(f"WARNING: {blk} > 20 words")
    for f in fmts:
        W, Hh = SIZES[f]
        out = base.with_suffix(".png") if f == "tall" else base.parent / (base.name + "-16x9.png")
        print(chrome(build(d, f), out, W, Hh))
    if "--lockup" in args:
        print(render_lockup(d.get("kicker", "BREAKING"), args[args.index("--lockup") + 1]))
    print("words (excl. brand/date/footer):", word_count(d))


if __name__ == "__main__":
    main()
