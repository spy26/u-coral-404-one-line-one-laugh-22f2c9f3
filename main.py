#!/usr/bin/env python3
"""One Line, One Laugh — writes a single original one-liner to entry.txt.

The entry is one self-written line (74 characters, 13 words). The program
is deterministic: it always writes the same bytes. It reads
MAKEFUN_OUTPUT_DIR (default /output) and writes entry.txt there with no
trailing newline.
"""

import os

ENTRY = "My calendar reminded me to relax, so I scheduled worrying for 3pm instead."


def main() -> None:
    # Gate: the entry must satisfy the kit rules (1-200 chars, one line).
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not have leading/trailing whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
