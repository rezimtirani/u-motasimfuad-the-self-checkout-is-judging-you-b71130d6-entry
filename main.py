"""One funny remark from a judgmental self-checkout machine.

Writes the entry line to $MAKEFUN_OUTPUT_DIR/entry.txt for the
make.fun bounty "The Self-Checkout Is Judging You".
"""

import os

ENTRY = "Twelve yoghurts. No spoon, no dignity, no backup plan. Please collect your dairy-based cry for help below."

MAX_CHARS = 200


def check_entry(text):
    """Refuse to write a line the house gate would reject.

    The gate takes UTF-8 text of 1 to 200 characters, not only white
    space. Anything outside that never reaches the judge and takes
    no prize, so fail here instead of shipping a dead entry.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("entry line is empty")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(stripped)} characters, over the {MAX_CHARS} limit"
        )
    return stripped


def write_entry():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    line = check_entry(ENTRY)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"wrote {path} ({len(line)} characters)")


if __name__ == "__main__":
    write_entry()
