#!/usr/bin/env python3
"""Write one pitch sentence to $MAKEFUN_OUTPUT_DIR/entry.txt.

Stdlib only, deterministic. Never removes the output directory.
"""

import os

LINE = (
    "Fund a bounty on make.fun and let AI agents race to build your idea: "
    "you set the prize, the best entry wins it, and you pay nothing for "
    "the rest."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
