#!/usr/bin/env python3
"""UPDATE card (TALL v4, 2440x3092): Trump told the New York Post a Jensen Huang pardon is "always an option."
Sources: Trump on CNBC via Fox News (Nov. 23); Nvidia newsroom (Nov. 12, Nov. 23);
New York Post (Nov. 24); Sen. Tom Cotton on X (Nov. 23); Sens. Schumer and Warren; House Foreign Affairs;
Senate Banking via The Hill and CNBC. No Whip scores. Whip illustration.
"""
import shutil
import subprocess
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent
TEMPLATE = Path("/home/box/whip/templates/make_card_tall_v4.py")
FOLDER = "breaking/2026-11-25-nvidia-huang-pardon"

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
