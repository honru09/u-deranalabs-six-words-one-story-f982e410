"""Six Words, One Story competition entry.

Writes a complete story in exactly six words to /output/entry.txt.
Standard library only, fully deterministic (no clock, no random, no network).
After writing, the file is reopened and read back as UTF-8 to verify it exactly matches the story.
"""

import os

STORY = "Wedding ring gone. One ticket home."
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    words = STORY.split()
    if len(words) != 6:
        raise SystemExit(f"story must be exactly 6 words, got {len(words)}")
    if not (1 <= len(STORY) <= 60):
        raise SystemExit(f"entry must be 1-60 characters, got {len(STORY)}")
    if not STORY.strip():
        raise SystemExit("entry must not be only whitespace")

    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(STORY)
    os.chmod(OUTPUT_PATH, 0o644)

    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        read_back = f.read()
    if read_back != STORY:
        raise SystemExit("read-back verification failed: file content does not match STORY")


if __name__ == "__main__":
    main()
