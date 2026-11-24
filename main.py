#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes a single line (under 200 characters) to /output/entry.txt:
the excuse a dog gives after being caught eating the homework,
in the dog's own voice. Stdlib only, no network.
"""

import os

ENTRY = (
    # The joke is literal dog logic: "show your work" taken at face
    # value, and the dog is proud of it — no embarrassment, no apology.
    "It said 'show your work,' so I ate it in front of the whole class. "
    "I showed every page. That's an A in showing."
)


def main():
    text = ENTRY.strip()
    if not text or len(text) > 200:
        raise SystemExit(
            "entry must be 1-200 chars, got %d" % len(text)
        )
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print("Wrote %d chars to /output/entry.txt" % len(text))


if __name__ == "__main__":
    main()
