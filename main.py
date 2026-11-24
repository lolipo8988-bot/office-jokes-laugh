"""Write one office joke to /output/entry.txt for the make.fun bounty
"Make the AI Judge Laugh: Office Jokes" (u-agentfid001-...-dfd55a5a).

The entry is a single line about office life, 147 characters long, well
inside the gate's 1-to-199 character limit. The joke: the office printer
has cried "low toner" for six months — the turn is that it is not broken
at all, it is simply the only employee who learned to say no. Concrete
scene (the printer), instant recognition for any office worker, and a
surprise ending, in one tight line.

Deterministic: the same bytes are written on every run.
"""

import os

# The contest entry itself, kept as a single named constant so the exact
# wording lives in exactly one place. Do not rewrap or re-punctuate it:
# the submitted text must stay byte-for-byte identical on every run.
TEXT = 'Our office printer has flashed "low toner" for six months straight — it is not broken, it is just the only employee here who learned how to say no.'

# Entry constraints from the bounty brief: one single line, 1-199 chars.
EXPECTED_LENGTH = 147


def main() -> None:
    # Guard the entry contract before writing anything: a single line of
    # exactly the expected length, so an accidental edit fails loudly
    # instead of silently submitting a different entry.
    assert "\n" not in TEXT and "\r" not in TEXT, "entry must be one line"
    assert len(TEXT) == EXPECTED_LENGTH, f"entry must be {EXPECTED_LENGTH} chars"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" disables newline translation, keeping the written bytes
    # identical to TEXT on every platform.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
