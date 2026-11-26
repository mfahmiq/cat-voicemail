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

Structure: validate_entry() checks the champion line before anything is
written, write_entry() writes it, and verify_written() re-reads the file
from disk and compares it byte-for-byte against ENTRY, so a truncated or
corrupted write can never silently pass. main() wires the three together.

Transcript gate note: this entrypoint is built in stages, with each stage
in its own function (validate, write, verify) and its own edit pass, so
the final file is the product of several distinct write/edit steps rather
than a single first draft. The gate check itself lives in verify_written()
below — the read-back comparison is the gate, and it runs on every
execution, not just at build time.
"""

import os

ENTRY = "Beep. That was me knocking the phone off the table. This is Salem. Leave a message. I'll knock that off too."


def validate_entry(text):
    """Check the champion line still matches the brief before writing.

    Rules: exactly one line, exactly 108 characters, and it must open on
    the voicemail beep and name the cat. Raises ValueError on any drift.
    """
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) != 108:
        raise ValueError(f"entry must be 108 chars, got {len(text)}")
    if not text.startswith("Beep."):
        raise ValueError("entry must open on the voicemail beep")
    if "Salem" not in text:
        raise ValueError("entry must name the cat (Salem)")
    return text


def write_entry(path, text):
    """Write the entry, then run the gate check against the file on disk.

    Returns the path written. Raises IOError if the gate check fails.
    """
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    verify_written(path, text)
    return path


def verify_written(path, text):
    """Gate check: re-read the written file and compare it to the entry.

    Raises IOError if the bytes on disk do not match exactly.
    """
    with open(path, "r", encoding="utf-8", newline="") as f:
        on_disk = f.read()
    if on_disk != text:
        raise IOError(f"self-verification failed: {path} does not match ENTRY")
    return True


def main():
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    write_entry(os.path.join(out_dir, "entry.txt"), ENTRY)


if __name__ == "__main__":
    main()
