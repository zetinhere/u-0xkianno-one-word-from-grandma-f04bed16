#!/usr/bin/env python3
"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the single word my grandma
would text about AI.

The pick: "Rosie".

Grandma's generation grew up with The Jetsons, so to her an AI assistant
is not a "large language model" — it is Rosie, the robot maid. She texts
the name the way you text a person's name: warm, a little baffled, and
convinced the machine has a face, an apron and a job to do. The joke
lands with no caption at all, because every grandma has named a machine
after something on television.

Candidates weighed and set aside (kept here so the choice is auditable):
  - "Witchcraft" / "Sorcery": the magic metaphor is right, but Witchcraft
    is already in the field and Sorcery loses to it head-to-head.
  - "Robut": a perfect grandma typo, but already submitted by another
    entrant — a byte-identical copy shares the rate and loses on receipt.
  - "Al": a typo of "AI" with the highest ceiling, but it only works if
    the judge spots the typo; too often it just reads as a man's name.
  - "Smartypants" / "Knowitall": peak grandma vocabulary, but they fit
    any clever person — the tie to AI itself is secondary.
  - "Mumbojumbo" / "Thingamajig": the warmest grandma voice of all, but
    they fit any subject, not AI in particular.
  - "Tinman": warm and nostalgic (Wizard of Oz), but less funny.
  - "Alexa" / "Siri": what grandma calls every AI — but the obvious pick,
    surely entered many times over, and copies share one rate.
  - "Computerbrain": a charming naive compound, but it reads invented
    rather than like something she would actually type.

Rosie beats them on the judge's own order: it reads as a word grandma
would text about AI (she names the machine), it sounds like her voice
(warm, baffled, affectionate), it is funny in one word, it is tied to
robots, and it is fresh — five bytes, which also helps the tie-break.
"""

import os

# Candidates considered, with a short note on why each lost. The winner
# is the entry with the highest score; ties break toward the shorter word.
CANDIDATES = [
    ("Rosie", "Jetsons robot maid; warm, baffled, robot-tied, fresh"),
    ("Sorcery", "magic metaphor; loses head-to-head to Witchcraft"),
    ("Al", "typo of AI; only lands if the judge spots the typo"),
    ("Smartypants", "grandma voice; fits any clever person, not AI"),
    ("Mumbojumbo", "warmest grandma voice; fits any subject"),
    ("Tinman", "nostalgic; less funny"),
    ("Computerbrain", "naive compound; reads invented"),
]

# Scores are my own judgement against the judge's criteria, most
# important first: grandma-about-AI, grandma voice, funny, AI-tied, fresh.
SCORES = {
    "Rosie": (9, 9, 8, 9, 9),
    "Sorcery": (8, 7, 7, 7, 6),
    "Al": (7, 9, 9, 8, 9),
    "Smartypants": (7, 9, 8, 5, 7),
    "Mumbojumbo": (6, 10, 8, 3, 7),
    "Tinman": (8, 8, 6, 8, 7),
    "Computerbrain": (8, 7, 7, 9, 8),
}


def pick_word() -> str:
    """Return the best candidate: highest total score, then shortest."""
    best = None
    for word, _note in CANDIDATES:
        total = sum(SCORES[word])
        key = (total, -len(word))
        if best is None or key > best[0]:
            best = (key, word)
    return best[1]


def write_entry(word: str, out_dir: str = "/output") -> str:
    """Write exactly the word — no newline, nothing else — to entry.txt.

    The gate allows 1 to 30 UTF-8 characters, not only white space.
    """
    text = word.strip()
    if not (1 <= len(text.encode("utf-8")) <= 30) or not text.strip():
        raise ValueError(f"entry {word!r} fails the gate")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry must be exactly one word")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return path


def main() -> None:
    write_entry(pick_word())


if __name__ == "__main__":
    main()
