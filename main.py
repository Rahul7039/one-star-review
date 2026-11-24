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


def validate(review: str) -> str:
    """Return the review if it passes the gates, else raise.

    Explicit checks instead of assert, so validation still runs
    under `python -O`, where assert statements are stripped.
    """
    if not review.strip():
        raise ValueError("review must not be empty")
    if "\n" in review:
        raise ValueError("review must be a single line")
    if len(review) > MAX_CHARS:
        raise ValueError(
            f"review is {len(review)} characters, over the {MAX_CHARS} limit"
        )
    return review


def main() -> None:
    review = validate(REVIEW)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(review)


if __name__ == "__main__":
    main()
