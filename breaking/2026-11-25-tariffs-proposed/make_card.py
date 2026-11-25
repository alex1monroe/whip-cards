#!/usr/bin/env python3
"""UPDATE card v2 (TALL v4): USTR proposes Section 301 tariffs on 14 partners, +20% China.
Fixes: other side (China July paper), Federal Register moved into point 01, 14 partners attributed to Reuters.
Sources: AP, Reuters, BBC Nov 25; WSJ Nov 24; Federal Register 2026-05214. No Whip scores."""
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
