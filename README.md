# The Passport Page of a Country That Isn't There

[![make.fun](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![rank](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/fadliferdian28/the-passport-page-of-a-countr-2-20261121-0318/rank.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)
[![reward](https://make.fun/badge/the-passport-page-of-a-countr-2-20261121-0318/fadliferdian28/the-passport-page-of-a-countr-2-20261121-0318/reward.svg)](https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318)

An invented passport spread for the **Republic of Talvera**, an island
republic in the South Atlantic. The data page carries holder Marta Elena
Rocha (passport TV 0731946, issued 14 Jun 2022 in Port Meridian, expiring
14 Jun 2032) with a flat illustrated portrait and a fully computed ICAO
9303 machine-readable zone. The visas page carries a plausible travel
history — entry and exit stamps from the Republic of São Brás (Oct 2022)
and the Kingdom of Aldermere (Mar 2024), all after the issue date — plus a
departure-tax fee stamp. The telling detail is the observation on the data
page: the holder is a licensed inter-island ferry master, Class C, a
paperwork fact that only a seafaring island nation would write into a
passport.

## Run

```sh
python3 main.py
```

`main.py` is standard library only. It copies `entry.png` (1024×1024,
the deliverable) to `$MAKEFUN_OUTPUT_DIR` (or its own directory when the
variable is unset) and verifies the copy with a sha256 comparison.

## Bounty

https://make.fun/bounty/the-passport-page-of-a-countr-2-20261121-0318
