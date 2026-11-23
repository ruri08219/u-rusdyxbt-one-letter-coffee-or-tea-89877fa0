"""One Letter: Coffee or Tea.

Writes exactly one letter -- ``A`` for coffee -- to /output/entry.txt.

Why A (coffee), against the judge brief's criteria in order:
1. Exactly one letter: the file holds a single byte, ``A`` -- no newline,
   no punctuation, no explanation. It passes the gate (1 to 1 characters).
2. Vivid: coffee is the fuller, more alive stance. It is the morning
   ritual -- the first thing, the jolt, the "but first, coffee" energy.
   Tea reads calmer and more muted; it is the quieter answer, not the
   more alive one.
3. Funnier: coffee carries more wit and surprise -- the "don't talk to me
   before my coffee" persona, the cheerful dependency everyone
   recognises. Tea has no equivalent joke.
4. Truer: the honest answer for the sender -- coffee is the daily-driver
   drink people actually reach for first thing in the morning.
5. Stands alone: ``A`` is clean and unmistakable as a whole answer.

Tea (B) would lose on criteria 2 and 3: the calmer, less vivid, less
funny choice. So the entry is A.
"""

import os

LETTER = "A"
MAX_LEN = 1


def main() -> None:
    # Guard: the entry must be exactly one uppercase letter, A or B.
    if len(LETTER) != MAX_LEN or not LETTER.isalpha() or not LETTER.isupper():
        raise ValueError("entry must be exactly one uppercase letter (A or B)")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(LETTER.encode("utf-8"))
    # Read-back verification: the file must hold exactly 1 character.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    if len(data) != MAX_LEN or data.decode("utf-8") != LETTER:
        raise ValueError("entry.txt must hold exactly one character")


if __name__ == "__main__":
    main()
