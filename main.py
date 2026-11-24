#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — one line, under 200 characters.

Writes one original excuse, in the dog's own voice, to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
Python 3.13 standard library only; no network, no randomness.

Draft line: the dog reads "ruff draft" on the homework's cover and takes
it as a letter addressed to him — a piece of dog logic where a spelling
detail becomes a property claim, and "finished it" does double duty
(ate it / completed it) so the dog sounds proud, not sorry.

Revision 2: the first draft landed the "ruff draft" pun but ended flat —
"before the teacher could" only repeats the setup. Rewrote the line so
it builds in three beats and ends on defiance: the cover addresses the
dog, the dog "finishes" the homework, and then he would do it again.
That last clause is the laugh — the brief says the best excuse sounds
like a dog who believes it has done nothing wrong, and an unrepentant
dog is funnier than a merely clever one. Tightened the opening too
("The cover said" instead of "It said ... right on the cover") so the
pun arrives sooner and the line stays a single breath.
"""
import os

LINE = (
    "The cover said 'ruff draft', so obviously it was addressed to me. "
    "I finished it before the teacher could \u2014 and I'd do it again."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} characters"
    assert "\n" not in text, "entry must be one line"
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
