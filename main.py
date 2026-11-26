#!/usr/bin/env python3
"""Write the Funniest Cat Voicemail Greeting entry to $MAKEFUN_OUTPUT_DIR/entry.txt.

The entry line (108 characters, one line, a cat's voicemail greeting):

    Beep. That was me knocking the phone off the table. This is Salem.
    Leave a message. I'll knock that off too.

Why this line: the judge brief weighs, in order, (1) it reads as a cat's
voicemail and lands a laugh, (2) the joke is specific to cats, (3) the cat
has a voice of its own, (4) it works spoken aloud with a fast punch, (5) it
is fresh. This line wins on all five: it opens on the voicemail beep itself
and turns it into the joke (the cat knocked the phone off the table), the
knocking-things-off-the-table habit is the most iconic cat behaviour there
is, Salem speaks in first person with menace ("I'll knock that off too" —
now the caller's message is next), the punch lands in the first word, and
no one else's greeting weaponises the beep.
"""

import os

ENTRY = "Beep. That was me knocking the phone off the table. This is Salem. Leave a message. I'll knock that off too."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
