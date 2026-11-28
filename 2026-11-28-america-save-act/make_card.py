#!/usr/bin/env python3
"""Lean v5 gap-hero card for the Nov 28 @America SAVE America Act reply.

Renders card.png (2440x3092) and card-16x9.png (3840x2160).
Uses /home/box/whip/templates/make_card_lean_v5.py. Chip has no dot
(SAVE ACT yellow, Elections white). Does not post.
"""
import importlib.util
import json
import sys
from pathlib import Path

OUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 and not sys.argv[1].startswith("-") else Path(__file__).resolve().parent
spec_ = importlib.util.spec_from_file_location("lean", "/home/box/whip/templates/make_card_lean_v5.py")
L = importlib.util.module_from_spec(spec_)
spec_.loader.exec_module(L)

def lockup_nodot(kicker):
    k = L.esc(kicker)
    first, _, rest = k.partition(" · ")
    rest_h = f'<span class="lk-rest">{rest}</span>' if rest else ""
    return f'<div class="lockup"><span class="lk-main">{first}</span>{rest_h}</div>'

L.lockup = lockup_nodot

_ORIG_BUILD = L.build

def build(d, fmt):
    def oside(s, cls="other"):
        s = s or ""
        if ":" not in s:
            return f'<div class="other {cls}">{L.esc(s)}</div>'
        lab, _, rest = s.partition(":")
        sep = "<br>" if fmt == "tall" else " "
        return f'<div class="other {cls}"><b>{L.esc(lab)}:</b>{sep}{L.esc(rest).lstrip()}</div>'

    L.other_side = oside
    dd = dict(d)
    if fmt == "tall":
        # Balanced two-line headline on the 4:5 card only.
        dd["headline"] = "Lee wants the *SAVE Act*|back on the floor"
    h = _ORIG_BUILD(dd, fmt)
    if fmt == "tall":
        css = """
.hero.gap{margin-top:40px}
.bigwrap{padding:28px 0 24px}
.page{bottom:160px}
.other{margin-top:8px}
"""
        h = h.replace("</style>", css + "</style>", 1)
    return h

L.build = build

if __name__ == "__main__":
    d = json.loads((OUT / "card.json").read_text())
    if "--debug" in sys.argv:
        Path("/tmp/save-act-tall.html").write_text(L.build(d, "tall"))
        Path("/tmp/save-act-wide.html").write_text(L.build(d, "wide"))
        print("wrote /tmp/save-act-tall.html /tmp/save-act-wide.html")
    print(L.chrome(L.build(d, "tall"), OUT / "card.png", *L.SIZES["tall"]))
    print(L.chrome(L.build(d, "wide"), OUT / "card-16x9.png", *L.SIZES["wide"]))
    print("words (excl. brand/date/source/footer):", L.word_count(d))
