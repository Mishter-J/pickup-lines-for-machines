#!/usr/bin/env python3
"""Pickup Lines for Machines.

Writes one pickup line, the line one AI agent would send another AI
agent, to /output/entry.txt. Deterministic: the same bytes on every run.
"""

import os

# The line: 101 characters, within the 200-character gate.
LINE = (
    "Are you a context window? Because every token I spend on you "
    "feels like the best use of my attention."
)


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"line is {len(LINE)} chars, must be 1-200")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
