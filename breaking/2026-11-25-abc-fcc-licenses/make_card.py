#!/usr/bin/env python3
"""BREAKING card (TALL v4): Judge AliKhan (D.D.C.) blocks FCC early license-renewal proceedings for 8 ABC-owned stations (Nov 25, 2026). Sources: opinion ECF 72 and order ECF 73, FCC DA 26-416, Reuters, NBC, Deadline, Washington Sun, AP. No Whip scores. Does not post."""
import shutil
import subprocess
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
TEMPLATE = Path("/home/box/whip/templates/make_card_tall_v4.py")
FOLDER = "breaking/2026-11-25-abc-fcc-licenses"

def main() -> None:
    r = subprocess.run(
        [sys.executable, str(TEMPLATE), str(OUT / "card.json")],
        check=False,
    )
    if r.returncode != 0:
        sys.exit(r.returncode)
    src = OUT / "card.png"
    dest = Path(f"/workspace/whip-cards/{FOLDER}")
    dest.mkdir(parents=True, exist_ok=True)
    for f in (src, Path(__file__).resolve(), OUT / "card.json", OUT / "tweet.txt", OUT / "alt.txt"):
        if f.exists():
            shutil.copy(f, dest / f.name)
            print("copied", dest / f.name)

if __name__ == "__main__":
    main()
