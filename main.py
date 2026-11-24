import os
from pathlib import Path

# Every word predates 1800: post office and library are the traveler's own
# world; "flies along thin wires" and "in one breath" carry the speed.
# One sentence for a traveler from 1800: the internet as a post office
# and a library joined into one house. 191 characters, one sentence.
SENTENCE = (
    "It is a post office and a library joined into one house, where every "
    "letter and book in the world flies along thin wires and lands in your "
    "hand in one breath, for any soul to read and answer."
)


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
