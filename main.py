#!/usr/bin/env python3
"""One Word From Your Ex — entry program.

Writes exactly one word to /output/entry.txt: the word the entrant's
ex would use to describe them.

Chosen word: "forgettable"
  - The sharp turn: an ex who is angry still remembers you. An ex who
    calls you forgettable does not. That is the sting.
  - It lands instantly, needs no explanation, and no near synonym
    ("unmemorable", "boring") keeps its edge.
  - It is painfully honest and self-deprecating: the entrant plainly
    knows it, and everyone has feared being exactly this to someone
    they once loved.

Words considered and rejected:
  - "exhausting": relatable and true, but common; every ex says it,
    so it has no surprise and no sharp turn.
  - "clingy": a real ex word, but it only insults; it does not sting
    with recognition the way erasure does.
  - "dramatic": funny, but it reads as a complaint about the ex
    rather than an honest self-portrait.
  - "unavailable": sharp, but it sounds like a status, not a word a
    person would say about a partner they once had.
  - "boring": honest, but flat; it has no turn and no laugh.

Python 3.13 standard library only. No network, no randomness, no
input files: the output is deterministic.
"""

import os

ENTRY = "forgettable"
OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """Mirror the competition gate: 1-24 chars, one word, not blank."""
    if not word or len(word) > 24:
        raise ValueError(f"entry must be 1-24 characters, got {len(word)}")
    if word != word.strip() or any(ch.isspace() for ch in word):
        raise ValueError("entry must be exactly one word, no whitespace")


def main() -> None:
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(ENTRY + "\n")
    print(f"wrote {OUTPUT_PATH}: {ENTRY!r} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()
