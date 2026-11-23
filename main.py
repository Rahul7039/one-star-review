"""One-star review of an everyday essential.

Writes the chosen one-line deadpan review to /output/entry.txt.
Pure standard library, Python 3.13.
"""

import os

REVIEW = (
    "Gravity never takes a day off, never gets thanked, "
    "and spends all of it dropping my phone face-down."
)

MAX_CHARS = 160
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    review = REVIEW
    assert review.strip(), "review must not be empty"
    assert "\n" not in review, "review must be a single line"
    assert len(review) <= MAX_CHARS, (
        f"review is {len(review)} characters, over the {MAX_CHARS} limit"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(review)


if __name__ == "__main__":
    main()
