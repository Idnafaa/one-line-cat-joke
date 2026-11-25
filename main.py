#!/usr/bin/env python3
"""One-line cat joke entry for make.fun.

Writes a single joke about a cat, one line under 200 characters,
to /output/entry.txt. Nothing else goes in the entry.
"""

import os

JOKE = "My cat left a dead mouse on my pillow this morning \u2014 apparently my performance review is in."

# The gate allows 1 to 200 characters, a single line, nothing else.
assert 1 <= len(JOKE) <= 200 and "\n" not in JOKE and JOKE.strip() == JOKE


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
