#!/usr/bin/env python3
"""One-Liner Marathon — make.fun entry.

Writes one original one-line comedy joke to /output/entry.txt.
The joke is a fixed, hand-written line: the program is
deterministic, uses only the Python standard library, and always
produces the exact same output on every run.

The joke: the dog outsmarts the treat jar, so the treats move
into the tax folder — the one place in the house nobody ever opens.
The turn is the hiding place itself: the safest spot turns out to
be the paperwork everyone avoids, owner included.
"""

import os

# The entry: one line, no trailing newline, well under the
# 280-character gate (checked again at write time).
JOKE = (
    "My dog learned to open the treat jar, so the treats now "
    "live in my tax folder — the one hiding spot in this "
    "house nobody ever opens, including me."
)

MAX_CHARS = 280


def main() -> None:
    line = JOKE.strip()
    if not line:
        raise SystemExit("joke is empty")
    if len(line) > MAX_CHARS:
        raise SystemExit(f"joke is {len(line)} chars, over the 280 limit")
    if "\n" in line or "\r" in line:
        raise SystemExit("joke must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Round-trip check: what the grader reads must be exactly the
    # line above, one line, within the limit, no trailing newline.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("round-trip mismatch in entry.txt")


if __name__ == "__main__":
    main()
