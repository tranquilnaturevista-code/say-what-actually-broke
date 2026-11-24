# Say What Actually Broke

[![Say What Actually Broke](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/tranquilnaturevista-code/say-what-actually-broke/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/tranquilnaturevista-code/say-what-actually-broke/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One line of honest software error copy for the
[Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
bounty: it tells the user the brutal truth about what went wrong
— and makes them laugh on the way. The `main.py` script writes the
line to `/output/entry.txt` — 144 characters, one line, deterministic,
no network.

## The line

> Nothing crashed. The server is fine and the database is fine — the config file someone edited at 2 a.m. was never committed, and now it is gone.

The idea: the most infuriating errors are the ones where nothing
actually broke — no crash, no outage, no database down. The failure
is embarrassingly human: somebody hand-edited a config file in the
middle of the night, never committed it, and the one uncommitted
copy is now gone. Naming that plainly is both the honest diagnosis
and the joke, and it is a line a real team could ship in a dialog
without embarrassing itself.

## How it works

Run `python3 main.py` and the script writes the line to
`/output/entry.txt` (or the `MAKEFUN_OUTPUT_DIR` environment
variable, when that is set), creating the folder if it does not
exist yet.

## Verification

After writing, the script reads the file back and checks that it
holds exactly the line, that the line is one line of 1–200
characters (Unicode code points) and not only whitespace, and
stops with an error if any check fails. Running it twice produces
byte-identical output.
