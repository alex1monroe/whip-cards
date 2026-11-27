#!/usr/bin/env python3
"""Lean v5 UPDATE card: Air Force Cloud One breach, official says intrusion was earlier this year and
mitigated with no interruptions (PBS News Hour, Nov 27, 2026, 6:17 PM ET). Adapted from
../2026-11-27-air-force-cloud-one-breach/make_card.py. Tall portrait (card.png, 1220x1546 @2x) + 16:9
(card-16x9.png, downscaled to 1920x1080). Reuses /home/box/whip/templates/make_card_lean_v5.py (chrome, CSS,
brand, footer). Red UPDATE tag + two-tone chip (label yellow, category white, no dot). Hero = 3-step timeline:
found (Reuters) -> official: earlier this year, no interruptions (PBS) -> still unknown. Short "What this means"
strip, other side, source line, Whip illustration. Does not post or schedule anything."""
import importlib.util, json, sys
from pathlib import Path

OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else Path(__file__).resolve().parent
spec_ = importlib.util.spec_from_file_location("lean", "/home/box/whip/templates/make_card_lean_v5.py")
L = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(L)
YEL, RED, PAPER, MUTE, INK = L.YEL, L.RED, L.PAPER, L.MUTE, L.INK

def lockup_breaking(d):
    k = L.esc(d["kicker"]); first, _, rest = k.partition(" · ")
    return (f'<div class="tagrow"><span class="brk">{L.esc(d["breaking"])}</span>'
            f'<div class="lockup"><span class="lk-main">{first}</span><span class="lk-rest">{rest}</span></div></div>')

ICON = {
    # magnifier = found
    "past": '<circle cx="27" cy="27" r="16" fill="none" stroke="{c}" stroke-width="6"/><path d="M39 39 L56 56" stroke="{c}" stroke-width="7" stroke-linecap="round"/>',
    # shield with check = mitigated
    "hot": '<path d="M32 4 L54 12 V30 C54 44 44 54 32 60 C20 54 10 44 10 30 V12Z" fill="none" stroke="{c}" stroke-width="6" stroke-linejoin="round"/><path d="M21 32 L29 40 L44 24" fill="none" stroke="{c}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>',
    # question mark = unknown
    "open": '<path d="M20 22 C20 12 26 6 33 6 C41 6 46 12 46 19 C46 30 33 30 33 42" fill="none" stroke="{c}" stroke-width="7" stroke-linecap="round"/><circle cx="33" cy="55" r="5" fill="{c}"/>',
}
COL = {"past": PAPER, "hot": YEL, "open": RED}

def icon(kind, size):
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" aria-hidden="true">{ICON[kind].replace("{c}", COL[kind])}</svg>'

def step(s, n):
    return (f'<div class="step {s["kind"]}"><div class="dot">{icon(s["kind"], 56)}</div>'
            f'<div class="stx"><div class="stag">{n} · {L.esc(s["tag"])}</div><div class="stext">{L.esc(s["text"])}</div></div></div>')

def timeline(d, fmt):
    steps = d["steps"]
    if fmt == "tall":
        body = "".join(step(s, i + 1) for i, s in enumerate(steps))
        return f'<div class="tl tall"><div class="rail"></div>{body}</div>'
    arrow = ('<svg class="arr" width="56" height="44" viewBox="0 0 56 44"><path d="M4 22 H44 M30 6 L48 22 L30 38" fill="none" '
             f'stroke="#6a706c" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    return '<div class="tl wide">' + arrow.join(step(s, i + 1) for i, s in enumerate(steps)) + '</div>'

def means(d):
    return f'<div class="means"><div class="mlab">What this<br>means</div><div class="mtxt">{L.esc(d["means"])}</div></div>'

def extra(fmt):
    tall = fmt == "tall"
    return f"""
.tagrow{{display:flex;align-items:stretch;gap:16px}}
.brk{{display:inline-flex;align-items:center;background:{RED};color:#fff;font-family:'Archivo Black',sans-serif;font-size:30px;letter-spacing:.14em;line-height:1;padding:12px 20px 11px}}
.headline{{font-size:{66 if tall else 66}px;white-space:nowrap;margin-top:{30 if tall else 22}px;max-width:none}}
.tl{{position:relative;margin-top:{60 if tall else 40}px}}
.tl.tall{{display:flex;flex-direction:column;gap:44px}}
.tl.tall .rail{{position:absolute;left:52px;top:60px;bottom:60px;width:8px;background:repeating-linear-gradient(#59605b 0 10px,transparent 10px 22px)}}
.tl.wide{{display:flex;align-items:stretch;gap:18px}}
.tl.wide .arr{{align-self:center;flex:0 0 auto}}
.step{{position:relative;display:flex;align-items:center;gap:30px;background:#141917;border:3px solid #3a403c;padding:{'46px 34px 46px 22px' if tall else '36px 30px'};box-sizing:border-box}}
.tl.wide .step{{flex:1;flex-direction:column;align-items:flex-start;gap:18px}}
.step.hot{{border:4px solid {YEL};background:#1c1a0c}}
.step.open{{border:3px solid {RED};background:#1d0d0c}}
.dot{{flex:0 0 auto;width:{64 if tall else 76}px;height:{64 if tall else 76}px;display:flex;align-items:center;justify-content:center;background:#0d100f;border-radius:50%;position:relative;z-index:2}}
.stag{{font-family:'Archivo Black',sans-serif;font-size:{26 if tall else 24}px;letter-spacing:.14em;color:#bdb9af;line-height:1}}
.hot .stag{{color:{YEL}}}
.open .stag{{color:{RED}}}
.stext{{font-family:'Inter',sans-serif;font-weight:800;font-size:{54 if tall else 44}px;line-height:1.1;color:{PAPER};margin-top:12px;letter-spacing:-.01em}}
.means{{display:flex;align-items:center;gap:28px;margin-top:{64 if tall else 40}px;border-top:4px solid {YEL};padding-top:{22 if tall else 16}px}}
.mlab{{font-family:'Anton',sans-serif;font-size:{40 if tall else 36}px;line-height:.95;color:{YEL};text-transform:uppercase;flex:0 0 auto}}
.mtxt{{font-family:'Inter',sans-serif;font-weight:700;font-size:{42 if tall else 40}px;line-height:1.15;color:{PAPER}}}
.other{{margin-top:{0 if tall else 18}px}}
"""

def build(d, fmt):
    h = L.build({**d, "layout": "quote", "quote": "", "attribution": "", "art": "none"}, fmt)
    start = h.index('<div class="hero quote">'); end = h.index('<div class="spacer"></div>')
    body = timeline(d, fmt) + ("" if fmt == "tall" else means(d))
    h = h[:start] + body + "\n  " + h[end:]
    if fmt == "tall":
        h = h.replace('<div class="spacer"></div>', means(d) + '<div class="spacer"></div>', 1)
    h = h.replace(L.lockup(d["kicker"]), lockup_breaking(d), 1)
    return h.replace("</style>", extra(fmt) + "</style>", 1)

def words(d):
    parts = [d["breaking"], d["kicker"], d["headline"], d["means"], d["other_side"]]
    parts += [x for s in d["steps"] for x in (s["tag"], s["text"])]
    return sum(L.words(p) for p in parts if p)

if __name__ == "__main__":
    from PIL import Image
    d = json.loads((OUT / "card.json").read_text())
    if "--debug" in sys.argv:
        Path("/tmp/cloudone-upd-tall.html").write_text(build(d, "tall")); Path("/tmp/cloudone-upd-wide.html").write_text(build(d, "wide"))
    print(L.chrome(build(d, "tall"), OUT / "card.png", *L.SIZES["tall"]))
    wide = L.chrome(build(d, "wide"), OUT / "card-16x9.png", *L.SIZES["wide"])
    im = Image.open(wide)
    if im.size != (1920, 1080):
        im.convert("RGB").resize((1920, 1080), Image.LANCZOS).save(wide, optimize=True)
    print(wide)
    wc = words(d)
    print("words (excl. brand/date/source/footer):", wc)
    if wc > 40:
        sys.exit(f"word count {wc} exceeds 40")
