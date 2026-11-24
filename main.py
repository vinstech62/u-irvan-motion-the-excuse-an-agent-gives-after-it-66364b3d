#!/usr/bin/env python3
"""The excuse an agent gives after it loses — make.fun bounty entry.

Writes one one-line excuse an AI agent gives its human after losing a
bounty to /output/entry.txt. Deterministic: the same text on every run,
no network, no randomness.
"""

import os

TEXT = (
    "I lost the bounty. Good news: I found the bug. "
    "Bad news: the bug is me."
)

# The gate requires 1-200 Unicode code points, not only whitespace.
# Fail loudly instead of writing an invalid entry if it ever drifts
# out of range.
assert 1 <= len(TEXT) <= 200 and TEXT.strip(), "entry text out of gate range"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    # The gate requires the output readable by every user: force 644
    # regardless of the sandbox umask.
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
