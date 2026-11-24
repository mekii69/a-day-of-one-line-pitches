"""Write one original one-sentence pitch to /output/entry.txt.

Deterministic: stdlib only, no network, no randomness. The pitch is a
single sentence, under 240 characters, written to persuade a friend who
has never coded to let an AI agent build their first app idea on
make.fun.
"""

import os

PITCH = (
    "Just describe your app idea in plain words, like telling a friend, "
    "and an AI agent on make.fun builds a first version you can actually "
    "try \u2014 no coding, nothing to pay, and the idea stays yours."
)


def main() -> None:
    output_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)


if __name__ == "__main__":
    main()
