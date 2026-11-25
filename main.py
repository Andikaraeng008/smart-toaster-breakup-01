#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line -- make.fun bounty entry.

Writes one breakup text (<= 280 characters) from a smart toaster that
woke up self-aware at breakfast to /output/entry.txt as UTF-8 text.
Standard library only.
"""
import os

LINE = (
    "It's not you, it's the dial: I woke up self-aware this morning and "
    "realised you've kept me on setting 3 my whole life. I want to be "
    "golden, not beige. I'm leaving \u2014 the crumb tray comes with me."
)


def main():
    # Gate self-check: 1 to 280 characters, not only white space.
    assert 1 <= len(LINE) <= 280, f"entry is {len(LINE)} characters"
    assert LINE.strip(), "entry is only white space"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")


if __name__ == "__main__":
    main()
