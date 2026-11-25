#!/usr/bin/env python3
"""Entry for make.fun's "The 3AM Fridge Text" bounty.

Prints one line (at most 140 characters): the text a smart fridge
sends its owner at 3 a.m.
"""

import os

NEWS = "the milk has expired, the leftovers have formed a union"
COMPLAINT = "you've opened me six times tonight"
SIGN_OFF = "We need to talk. Also: buy eggs."


def build_line() -> str:
    """Assemble the fridge's message from its parts."""
    return f"3 a.m.: {NEWS}, and {COMPLAINT}. {SIGN_OFF}"


def main() -> None:
    line = build_line()
    assert len(line) <= 140, f"fridge text too long: {len(line)} chars"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        pass
    print(line)


if __name__ == "__main__":
    main()
