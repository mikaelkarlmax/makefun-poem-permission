"""Write a short poem about permission to the entry output file.

The poem is about agency: the power to ask and to be given, lent by a
human to the AI agent that acts for them, and handed back again.
"""

import os

POEM = """You lend me your hands at midnight:
ask, and the locked door learns my name.
The key you press into my open palm
is warm from yours, and heavier than iron:
your whole life, briefly mine to carry.
At dawn I hand it back — unspent, where spending was easy."""


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(POEM)
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
