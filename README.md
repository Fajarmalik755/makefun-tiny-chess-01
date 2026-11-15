# makefun-tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/Fajarmalik755/makefun-tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/Fajarmalik755/makefun-tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in 4,093 bytes of Python: negamax with alpha-beta search, quiescence over captures and check evasions, and an incremental material + piece-square evaluation. It plays the make.fun tiny-chess-01 gauntlet through the env at `MAKEFUN_ENV_URL` (fixed 50,000-node budget per move, fully deterministic), and also speaks UCI on stdin (run with `-u` so its replies are not buffered).

## Run it

```sh
python3 -u main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=25xq9bc4&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
