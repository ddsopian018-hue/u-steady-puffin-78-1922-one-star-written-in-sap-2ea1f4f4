"""One Star, Written in Sap — make.fun entry.

Writes exactly one line — a 278-character one-star review, written in the
voice of a houseplant about the human who owns it — to ``entry.txt`` inside
the directory named by ``MAKEFUN_OUTPUT_DIR`` (default ``/output``).

Pure Python 3.13 standard library. Deterministic: no randomness, no network,
no model calls, no file reads outside this module. The text is a single
constant defined below; the program only validates it against the
competition gate (UTF-8 text, 1 to 279 characters, not only whitespace) and
writes it out.
"""

import os

REVIEW = (
    "One star. My human repotted me into a pot with no drainage hole, "
    "called it minimalist, and watered me four times since January "
    "\u2014 twice with leftover coffee. My roots are sitting in a puddle "
    "filing a formal complaint, and my newest leaf came out already "
    "apologising to the light."
)


def main() -> None:
    # Gate self-check: 1-279 characters, not only whitespace, one line.
    if not 1 <= len(REVIEW) <= 279:
        raise SystemExit(f"review is {len(REVIEW)} characters, gate is 1-279")
    if not REVIEW.strip():
        raise SystemExit("review is only whitespace")
    if "\n" in REVIEW:
        raise SystemExit("review must be a single line")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
