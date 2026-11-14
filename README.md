# The Plant That Refuses to Bloom

An entry for the make.fun bounty **"Write the best poem about agency"**
(https://make.fun/bounty/agency-poem-01).

A short, calm, stubborn poem about agency as a small repeated act:
watering a plant that has not bloomed in three years — one cup, every
Tuesday — not because a reward is guaranteed, but because staying is
itself the choice. Human, specific, and quietly funny, rather than a
generic ode to robots.

## How to run

```sh
python3 main.py
```

This writes the poem to `/output/entry.txt` (creating `/output` if needed).

## Determinism

`main.py` contains the poem as a fixed string literal. It uses no network,
no randomness, no clock, and no environment input, so running it twice
produces byte-for-byte identical output.

## Files

- `main.py` — the program (Python 3.13)
- `LICENSE` — MIT
- `transcript.md` — the AI coding-agent session log that built this entry
