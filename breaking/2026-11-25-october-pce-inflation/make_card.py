#!/usr/bin/env python3
"""BREAKING card v2 (TALL v4): October PCE 3.8%, core 3.3%; Q3 GDP 4.3%.
v2: September y/y is 3.7% not 3.6%; box 3 no longer reads as causation; tweet attributes the forecast line to CNBC.
Sources: BEA, AP, CNBC Nov 25. No Whip scores."""
import shutil
import subprocess
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
TEMPLATE = Path("/home/box/whip/templates/make_card_tall_v4.py")
FOLDER = "breaking/2026-11-25-october-pce-inflation"

def main() -> None:
    r = subprocess.run(
        [sys.executable, str(TEMPLATE), str(OUT / "card.json")],
        check=False,
    )
    if r.returncode != 0:
        sys.exit(r.returncode)
    dest = Path(f"/workspace/whip-cards/{FOLDER}")
    dest.mkdir(parents=True, exist_ok=True)
    for name in (
        "card-v2.png",
        "card.json",
        "make_card.py",
        "tweet-v2.txt",
        "alt-v2.txt",
    ):
        f = OUT / name if name != "make_card.py" else Path(__file__).resolve()
        if f.exists():
            shutil.copy(f, dest / Path(name).name)
            print("copied", dest / Path(name).name)

if __name__ == "__main__":
    main()
