#!/usr/bin/env python3
"""Write the alien tourist's one-line review of Earth to /output/entry.txt.

The entry is a single line of plain text, at most 200 characters, with no
trailing newline. It reads as a real tourist review: an alien visitor's
baffled take on one ordinary Earth ritual (the birthday cake), ending with
a star verdict and a closing remark, with the punch landing on the
final words ("would be abducted again").
"""

import os

ENTRY = (
    "Earth: the locals set a cake on fire, sing at it, blow it out, "
    "then eat the burnt cake and call it a party. "
    "5 stars \u2014 would be abducted again."
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
