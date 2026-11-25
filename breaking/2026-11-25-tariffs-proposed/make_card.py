#!/usr/bin/env python3
"""UPDATE card (TALL v4): USTR proposes Section 301 tariffs on 14 partners, +20% China. Sources: AP, Reuters, BBC Nov 25. No Whip scores."""
import shutil
import subprocess
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
TEMPLATE = Path("/home/box/whip/templates/make_card_tall_v4.py")
FOLDER = "breaking/2026-11-25-tariffs-proposed"

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
