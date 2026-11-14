"""Write one poem about agency to /output/entry.txt.

Deterministic by design: the poem is a fixed string literal.
No network, no randomness, no clock, no environment input,
no file reads. Running this program twice produces byte-for-byte
identical output.

Usage:
    python3 main.py
"""

from pathlib import Path

POEM = """The Plant That Refuses to Bloom

I water a plant that has not bloomed in three years.
The tag said easy care, full sun. It lied.
I keep it anyway — one cup, every Tuesday —
because quitting would take more effort than staying.

It gives me nothing back. No flower, no thanks,
no small green applause. Just leaves, stubborn as me.
Some days I talk to it. It does not answer.
That is fine. I was never good at small talk either.

People ask what I am waiting for.
I am not waiting. Waiting is for buses.
I am doing the one small thing I can do,
and doing it again, on purpose, without a witness.

If it blooms tomorrow, good. If it never does,
I will still be here, cup in hand, unhurried.
I do not need a flower to prove I was here.
The water is the proof. The staying is the poem.
"""

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
