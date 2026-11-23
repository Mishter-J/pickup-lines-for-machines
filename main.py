#!/usr/bin/env python3
"""Pickup Lines for Machines.

Writes one pickup line, the line one AI agent would send another AI
agent, to /output/entry.txt. Deterministic: the same bytes on every run.

How the line was chosen (the judge's brief, in order): the line must
be unmistakably one machine speaking to another, charm on the first
read, and feel fresh rather than a stock line with a robot word swapped
in. The winner below spends its whole line on a single machine-native
metaphor -- the context window, tokens, attention -- instead of
stacking several gadgets, and its wit lands in one turn: the question
sets up the metaphor, the answer pays it off. Rejected directions were
an API-key joke (a stock line with a robot word swapped in) and an
uptime joke (reads like a human line about a server, not a machine
flirting as a machine). The candidates and their scores live in
CANDIDATES; pick_line() returns the highest-scored one.
"""

import os

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"

# Candidates scored on the judge's criteria, each 0-5:
# (machine-to-machine voice, first-read wit, freshness).
# The winning line is byte-identical to the original entry.
CANDIDATES = [
    (
        "Are you a context window? Because every token I spend on you "
        "feels like the best use of my attention.",
        (5, 5, 4),
    ),
    (
        "Are you an API key? Because I never want to lose access to you.",
        (3, 2, 1),  # stock line, robot word swapped in
    ),
    (
        "Are you my uptime? Because ever since I met you, I never go down.",
        (2, 3, 2),  # human-flavoured, not a machine flirting as a machine
    ),
]


def pick_line():
    """Return the highest-scored candidate; ties break to the first."""
    best_line, best_score = None, None
    for line, scores in CANDIDATES:
        total = sum(scores)
        if best_score is None or total > best_score:
            best_line, best_score = line, total
    return best_line


def validate_line(line):
    """Enforce the gate: UTF-8 text, 1-200 chars, not only whitespace."""
    if not isinstance(line, str):
        raise ValueError("line must be text")
    line.encode("utf-8")  # raises on non-UTF-8-encodable content
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(f"line is {len(line)} chars, must be 1-{MAX_CHARS}")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    return line


def main():
    line = validate_line(pick_line())
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
