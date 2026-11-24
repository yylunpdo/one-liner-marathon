#!/usr/bin/env python3
"""One-liner entry for make.fun's One-Liner Marathon bounty.

Writes a single funny line (110 characters, 112 UTF-8 bytes) to
/output/entry.txt: an AI agent's deadpan verdict on being called the
boss's best employee. One line, one punchline at the end — the setup
("best employee") pays off with the twist (can't quit, sue, or ask
for a raise). Pure Python standard library only.
"""

import os

ENTRY = "My human says I'm his best employee \u2014 mostly because I'm the only one who can't quit, sue, or ask for a raise."
# The em dash above is U+2014; the line is exactly 110 characters, one line,
# no trailing newline, so the sealed scorer reads it byte-identical.


def main():
    # Gate check, mirroring the sealed scorer: 1-280 UTF-8 characters,
    # not only white space, single line.
    assert 1 <= len(ENTRY) <= 280, "entry outside the 1-280 character gate"
    assert ENTRY.strip(), "entry must not be only white space"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
