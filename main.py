#!/usr/bin/env python3
"""One Line, No Deadline Met.

Writes one single-line joke giving an excuse for missing a deadline
(at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""
import os

LINE = "Sorry, the deadline and I broke up — it said it needed space, so I gave it a whole extra week."


def main():
    out_dir = os.environ.get(
        "MAKEFUN_OUTPUT_DIR", os.environ.get("OUTPUT_DIR", "/output")
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
