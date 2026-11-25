#!/usr/bin/env python3
"""One Line, One Laugh — make.fun entry.

Writes one funny line of text to /output/entry.txt. The line is fixed and
deterministic: the same line on every run. Two beats: a setup (two years of
paying for a gym I never visited) and a reveal in the final clause.
Chosen over six other variants by internal pairwise judging (judge criteria +
margin): the single-word punch "Founding member" reframes absence as
seniority, the fastest laugh of the set.
"""

import os

LINE = (
    "I paid my gym $19 a month for two years without going. Last Tuesday "
    "I finally went. 'New here?' asked the desk. 'Founding member,' I said."
)


def main() -> None:
    if not LINE.strip() or len(LINE) > 140 or "\n" in LINE:
        raise SystemExit("entry line must be one non-blank line of 1-140 chars")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
