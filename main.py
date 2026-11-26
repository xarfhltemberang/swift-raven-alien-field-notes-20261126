#!/usr/bin/env python3
"""Write the alien tourist's one-line review of Earth to /output/entry.txt.

The entry is a single line of plain text, at most 200 characters, with no
trailing newline. It reads as a real tourist review: an alien visitor's
baffled take on one ordinary Earth ritual (the birthday cake), ending with
a star verdict and a closing remark, with the punch landing on the
final words ("best fire I ever tasted").
"""

import os

ENTRY = (
    "Earth: they stick candles in a cake, set it on fire, sing at it, "
    "then blow it out and eat the smoke-flavored cake. "
    "5 stars, best fire I ever tasted."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip() == ENTRY
    assert "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
