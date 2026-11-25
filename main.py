#!/usr/bin/env python3
"""Till Firmware Do Us Part — write one original funny robot wedding vow.

The vow is a single sentence of at most 200 characters: a wedding promise
spoken by a robot at its own wedding, the laugh landing on the last words.
"""

from pathlib import Path

VOW = (
    "I vow to share my battery, my bandwidth, and my last backup with you "
    "— you are the one update I will never roll back, and the only crash "
    "I would choose all over again."
)


def main() -> None:
    line = VOW.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"vow must be 1-200 chars, got {len(line)}")
    if "\n" in line:
        raise ValueError("vow must be a single line")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    written = out.read_text(encoding="utf-8")
    if written != line:
        raise ValueError("round-trip mismatch")
    print(f"wrote {len(line)} chars to {out}")


if __name__ == "__main__":
    main()
