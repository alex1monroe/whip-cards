#!/usr/bin/env python3
"""Lean v5 Daily @America card: Nathan v. Trump / EO 14418 classwide preliminary injunction.

Tall portrait (card.png, 2440x3092) + 16:9 broadcast (card-16x9.png, 1920x1080).
Reuses /home/box/whip/templates/make_card_lean_v5.py (chrome, CSS, brand, footer).
Two-tone chip (COURT RULING in yellow, IMMIGRATION & COURTS in white, no dot).
Hero = 3-step 2026 timeline: June 30 SCOTUS Trump v. Barbara 6-3 → Aug. 6 EO 14418
signed → Nov. 25 Nathan v. Trump classwide preliminary injunction (highlighted).
Scope strip + White House other side. Source: Nathan v. Trump, D.D.C., Nov. 25, 2026.
Whip illustration. Does not post or schedule anything.
"""
import importlib.util, json, sys
from pathlib import Path
from PIL import Image

OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else Path(__file__).resolve().parent
spec_ = importlib.util.spec_from_file_location("lean", "/home/box/whip/templates/make_card_lean_v5.py")
L = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(L)
YEL, RED, PAPER, MUTE, INK = L.YEL, L.RED, L.PAPER, L.MUTE, L.INK


def lockup_nodot(kicker):
    k = L.esc(kicker)
    first, _, rest = k.partition(" · ")
    rest_h = f'<span class="lk-rest">{rest}</span>' if rest else ""
    return f'<div class="lockup"><span class="lk-main">{first}</span>{rest_h}</div>'


def timeline(d, fmt):
    tall = fmt == "tall"
    items = ""
    n = len(d["steps"])
    for i, s in enumerate(d["steps"]):
        hot = s.get("hot")
        cls = "step hot" if hot else "step"
        connector = "" if i == n - 1 else '<div class="rail"></div>'
        items += (
            f'<div class="{cls}">'
            f'<div class="marker"><span class="dot"></span>{connector}</div>'
            f'<div class="beat"><div class="bd">{L.esc(s["date"])}</div>'
            f'<div class="bt">{L.mark(s["text"]).replace("first order", "<span class=\"nowrap\">first order</span>")}</div></div></div>'
        )
    return f'<div class="timeline {fmt}">{items}</div>'


def means(d):
    # Designed break after the first sentence so "Aug. 6." is not a widow.
    raw = L.esc(d["means"])
    raw = raw.replace(". ", ".<br>", 1)
    return f'<div class="means"><div class="mtxt">{raw}</div></div>'



def extra(fmt):
    tall = fmt == "tall"
    return f"""
.headline{{font-size:{58 if tall else 54}px;max-width:{1040 if tall else 1700}px;margin-top:{28 if tall else 18}px}}
.timeline{{margin-top:{48 if tall else 36}px;display:flex;flex-direction:{"column" if tall else "row"};gap:0}}
.timeline.wide{{align-items:stretch;justify-content:space-between;gap:0;width:100%}}
.step{{display:flex;align-items:stretch;gap:{28 if tall else 20}px;{"flex:1;" if not tall else ""}}}
.timeline.wide .step{{flex-direction:column;align-items:flex-start;position:relative;padding-right:36px;flex:1}}
.marker{{display:flex;flex-direction:column;align-items:center;flex:0 0 {"36px" if tall else "auto"};{"width:100%;flex-direction:row;align-items:center;" if not tall else ""}}}
.dot{{width:{36 if tall else 32}px;height:{36 if tall else 32}px;border-radius:50%;background:{PAPER};flex:0 0 {36 if tall else 32}px;display:block}}
.step.hot .dot{{background:{YEL};box-shadow:0 0 0 8px rgba(255,204,0,.18)}}
.rail{{{"width:14px;flex:1;min-height:36px;background:#3a403c;margin:8px 0;" if tall else "height:12px;flex:1;background:#3a403c;margin:0 0 0 10px;"}}}
.timeline.wide .marker .rail{{position:absolute;left:32px;right:-8px;top:10px;height:12px;margin:0;flex:none;width:auto}}
.timeline.wide .step:last-child .rail{{display:none}}
.beat{{{("padding-bottom:28px;" if tall else "margin-top:22px;")}}}max-width:980px}}
.step:last-child .beat{{padding-bottom:0}}
.step.hot .beat{{background:#16140a;border:3px solid {YEL};padding:{28 if tall else 20}px {32 if tall else 24}px {30 if tall else 22}px;{"width:100%;" if tall else "min-height:170px;"}}}
.step.hot{{{"align-items:center;" if tall else ""}}}
.timeline.wide .step.hot .beat{{margin-top:8px}}
.nowrap{{white-space:nowrap}}
.bd{{font-family:'Anton',sans-serif;font-size:{52 if tall else 48}px;letter-spacing:.04em;color:{MUTE};line-height:1;text-transform:uppercase}}
.step.hot .bd{{color:{YEL}}}
.bt{{font-family:'Inter',sans-serif;font-weight:800;font-size:{46 if tall else 38}px;line-height:1.15;color:{PAPER};margin-top:10px;letter-spacing:-.015em}}
.means{{margin-top:{28 if tall else 28}px;border-top:4px solid {YEL};padding-top:{22 if tall else 18}px}}
.mtxt{{font-family:'Inter',sans-serif;font-weight:700;font-size:{42 if tall else 36}px;line-height:1.2;color:{PAPER}}}
.other{{margin-top:{20 if tall else 14}px}}
.page{{bottom:{120 if tall else 110}px}}
"""


def build(d, fmt):
    h = L.build({**d, "layout": "quote", "quote": "", "attribution": "", "art": "none"}, fmt)
    start = h.index('<div class="hero quote">')
    end = h.index('<div class="spacer"></div>')
    body = timeline(d, fmt)
    h = h[:start] + body + "\n  " + h[end:]
    # Leftover air sits between the timeline and the scope/other-side cluster
    # (lower-third on the 16:9 broadcast frame).
    h = h.replace('<div class="spacer"></div>', '<div class="spacer"></div>' + means(d), 1)
    h = h.replace(L.lockup(d["kicker"]), lockup_nodot(d["kicker"]), 1)
    return h.replace("</style>", extra(fmt) + "</style>", 1)


def words(d):
    # Visible card copy except brand, date, source, footer. Scope label "The scope" is on-card.
    parts = [d["kicker"], d["headline"], d["means"], d["other_side"]]
    for s in d["steps"]:
        parts += [s["date"], s["text"]]
    return sum(L.words(p) for p in parts if p)


if __name__ == "__main__":
    d = json.loads((OUT / "card.json").read_text())
    if "--debug" in sys.argv:
        Path("/tmp/nathan-tall.html").write_text(build(d, "tall"))
        Path("/tmp/nathan-wide.html").write_text(build(d, "wide"))
    tall = L.chrome(build(d, "tall"), OUT / "card.png", *L.SIZES["tall"])
    print(tall)
    # Render wide at 1920x1080 CSS @ 2x (3840x2160), then downsample to 1920x1080 broadcast.
    wide_hi = OUT / "_card-16x9-2x.png"
    L.chrome(build(d, "wide"), wide_hi, *L.SIZES["wide"])
    im = Image.open(wide_hi)
    im.resize((1920, 1080), Image.Resampling.LANCZOS).save(OUT / "card-16x9.png", "PNG", optimize=True)
    wide_hi.unlink(missing_ok=True)
    print(OUT / "card-16x9.png")
    wc = words(d)
    print("words (excl. brand/date/source/footer):", wc)
    if wc > 40:
        sys.exit(f"word count {wc} exceeds 40")
