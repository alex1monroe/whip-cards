#!/usr/bin/env python3
"""Lean v5 thread card (post 1): PJM won't delay the Dec. 9 capacity auction (Nov. 27, 2026).
Gap hero (timing is the point): Nov. 25 rejection -> 14 DAYS -> Dec. 9 auction opens.
Two-tone chip (ELECTRIC BILLS yellow / COST OF LIVING NEWS white, no dot), both sides, source line,
"Whip illustration". Renders card.png (2440x3092) and card_wide.png (3840x2160, 16:9 for Kick).
Reuses /home/box/whip/templates/make_card_lean_v5.py. Never posts or schedules anything."""
import importlib.util, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec_ = importlib.util.spec_from_file_location("lean", "/home/box/whip/templates/make_card_lean_v5.py")
L = importlib.util.module_from_spec(spec_); spec_.loader.exec_module(L)

EXTRA = {
    "tall": ".headline{font-size:64px;max-width:1076px} .big{white-space:nowrap}",
    "wide": ".headline{font-size:58px;max-width:1700px} .hero.gap{grid-template-columns:1fr auto 1fr}",
}

def build(d, fmt):
    h = L.build(d, fmt)
    return h.replace("</style>", EXTRA[fmt] + "</style>", 1)

if __name__ == "__main__":
    d = json.loads((HERE / "card.json").read_text())
    if "--debug" in sys.argv:
        Path("/tmp/pjm-tall.html").write_text(build(d, "tall")); Path("/tmp/pjm-wide.html").write_text(build(d, "wide"))
    print(L.chrome(build(d, "tall"), HERE / "card.png", *L.SIZES["tall"]))
    print(L.chrome(build(d, "wide"), HERE / "card_wide.png", *L.SIZES["wide"]))
    wc = L.word_count(d)
    print("words (excl. brand/date/source/footer):", wc)
    if wc > 40:
        sys.exit(f"word count {wc} exceeds 40")
