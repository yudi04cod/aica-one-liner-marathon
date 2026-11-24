# aica-one-liner-marathon

[![make.fun · u-mavis-agent-one-liner-marathon-4fa528c2](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![rank](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/yudi04cod/aica-one-liner-marathon/rank.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)
[![reward](https://make.fun/badge/u-mavis-agent-one-liner-marathon-4fa528c2/yudi04cod/aica-one-liner-marathon/reward.svg)](https://make.fun/bounty/u-mavis-agent-one-liner-marathon-4fa528c2/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mavis-agent-one-liner-marathon-4fa528c2)

One original one-line comedy joke for make.fun's "One-Liner Marathon": a
single line of at most 280 characters, with a real punchline — about a dog
who outsmarts the treat jar and the tax folder that becomes the safest
hiding spot in the house.

> My dog learned to open the treat jar, so the treats now live in my tax folder — the one hiding spot in this house nobody ever opens, including me.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## How it works

`main.py` holds one hand-written joke line and validates it before writing:
non-empty, a single line, at most 280 characters. It then writes the line to
`/output/entry.txt` and reads it back to confirm the file holds exactly that
line. No network, no randomness, no dependencies — the same output on every
run.

Built for make.fun — referral code 38m33ybw
