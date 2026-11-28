#!/usr/bin/env python3
"""Lean v5 16:9 broadcast card for the Nov 28 AI-rules deep dive.

Who-holds-the-pen split: Congress, White House, States, with a 76% voter
stat as the hero band. Reuses /home/box/whip/templates/make_card_lean_v5.py
(chrome, CSS, brand, footer). Two-tone chip (DEEP DIVE in yellow,
TECHNOLOGY NEWS in white, no dot). Broadcast only: 1920x1080 CSS ->
3840x2160 PNG. Does not post, schedule or overwrite Producer's placeholder.
"""
import importlib.util
import json
import sys
from pathlib import Path

OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else Path(__file__).resolve().parent
spec_ = importlib.util.spec_from_file_location("lean", "/home/box/whip/templates/make_card_lean_v5.py")
L = importlib.util.module_from_spec(spec_)
spec_.loader.exec_module(L)
YEL, PAPER, MUTE = L.YEL, L.PAPER, L.MUTE


def lockup_nodot(kicker):
    k = L.esc(kicker)
    first, _, rest = k.partition(" · ")
    rest_h = f'<span class="lk-rest">{rest}</span>' if rest else ""
    return f'<div class="lockup"><span class="lk-main">{first}</span>{rest_h}</div>'


L.lockup = lockup_nodot


def cols_html(d):
    blocks = ""
    for c in d["columns"]:
        kcls = "ckick idfont" if c.get("kicker_font") == "id" else "ckick"
        lines = ""
        for i, line in enumerate(c["lines"]):
            gap = " gap" if c.get("break_before") and i == c["break_before"] else ""
            lines += f'<div class="cline{gap}">{L.esc(line)}</div>'
        blocks += (
            f'<div class="col">'
            f'<div class="clab">{L.esc(c["label"])}</div>'
            f'<div class="{kcls}">{L.esc(c["kicker"])}</div>'
            f'{lines}</div>'
        )
    return f'<div class="cols">{blocks}</div>'


def other_html(s):
    # Designed break after "vs." so "White House)." is not a widow.
    if ":" in s:
        lab, _, rest = s.partition(":")
        rest = L.esc(rest).replace(" vs. ", " vs.<br>")
        return f'<div class="other"><b>{L.esc(lab)}:</b>{rest}</div>'
    return f'<div class="other">{L.esc(s)}</div>'


def extra():
    return f"""
.headline{{font-size:56px;max-width:none;margin-top:20px}}
.page{{bottom:114px}}
.spacer{{flex:1}}
.mid{{display:flex;flex-direction:column;margin-top:10px}}
.hero.stat{{display:flex;align-items:center;gap:36px;margin:4px 0 12px 0}}
.stat{{font-family:'Anton',sans-serif;font-size:200px;line-height:.86;color:{YEL};letter-spacing:-.005em;margin-left:-6px}}
.statsub{{display:flex;align-items:center;gap:20px;font-family:'Inter',sans-serif;font-weight:800;font-size:40px;line-height:1.15;color:{PAPER};max-width:980px}}
.bar{{width:64px;height:8px;background:{YEL};flex:0 0 64px}}
.cols{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:0;border-top:2px solid #2a2d2b;padding-top:24px}}
.col{{padding:0 44px;border-left:2px solid #2a2d2b}}
.col:first-child{{padding-left:0;border-left:none}}
.col:last-child{{padding-right:0}}
.clab{{font-family:'Archivo Black',sans-serif;font-size:22px;letter-spacing:.14em;text-transform:uppercase;color:{MUTE};margin-bottom:12px}}
.ckick{{font-family:'Anton',sans-serif;font-size:72px;line-height:.92;color:{PAPER};letter-spacing:.01em;margin:0 0 16px}}
.ckick.idfont{{font-family:'Archivo Black',sans-serif;font-size:64px;letter-spacing:-.02em;line-height:1;padding-top:6px;padding-bottom:4px}}
.col:last-child .ckick{{color:{YEL}}}
.cline{{font-family:'Inter',sans-serif;font-weight:700;font-size:34px;line-height:1.22;color:#d8d4ca;margin-bottom:6px;letter-spacing:-.01em}}
.cline.gap{{margin-top:16px}}
.other{{margin-top:0;width:100%;max-width:none;box-sizing:border-box}}
"""


def build(d):
    hero = (
        f'<div class="hero stat"><div class="stat">{L.esc(d["stat"])}</div>'
        f'<div class="statsub"><span class="bar"></span>{L.esc(d["stat_sub"])}</div></div>'
    )
    mid = f'<div class="mid">{hero}{cols_html(d)}</div>'
    h = L.build(
        {
            **d,
            "layout": "quote",
            "quote": "",
            "attribution": "",
            "art": "none",
            "other_side": "",
        },
        "wide",
    )
    h = h.replace('<div class="hero quote">', mid + '<div class="hero quote" style="display:none">', 1)
    # Insert designed other-side before the spacer's close, after mid.
    h = h.replace('<div class="spacer"></div>', '<div class="spacer"></div>\n  ' + other_html(d["other_side"]), 1)
    h = h.replace("</style>", extra() + "</style>", 1)
    return h


def body_words(d):
    """Headline + hero + column copy (excl. brand, date, chip, labels, source, footer, other_side)."""
    parts = [d["headline"], d["stat"], d["stat_sub"]]
    for c in d["columns"]:
        parts.append(c["kicker"])
        parts.extend(c["lines"])
    return sum(L.words(p) for p in parts if p)


if __name__ == "__main__":
    d = json.loads((OUT / "card.json").read_text())
    out = OUT / "card-16x9.png"
    if "--debug" in sys.argv:
        Path("/tmp/card-ai-rules-wide.html").write_text(build(d))
        print("wrote /tmp/card-ai-rules-wide.html")
    print(L.chrome(build(d), out, *L.SIZES["wide"]))
    print("body words (excl. brand/date/chip/labels/source/footer/other_side):", body_words(d))
    print("other_side words:", L.words(d["other_side"]))
