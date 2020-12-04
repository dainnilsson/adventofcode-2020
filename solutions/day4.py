import re


VALIDATORS = {
    "byr": lambda v: 1920 <= int(v) <= 2002,
    "iyr": lambda v: 2010 <= int(v) <= 2020,
    "eyr": lambda v: 2020 <= int(v) <= 2030,
    "hgt": lambda v: (v.endswith("cm") and 150 <= int(v[:-2]) <= 193)
    or (v.endswith("in") and 59 <= int(v[:-2]) <= 76),
    "hcl": lambda v: re.match("^#[0-9a-f]{6}$", v),
    "ecl": lambda v: v in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda v: re.match("^[0-9]{9}$", v),
}
REQUIRED = set(VALIDATORS.keys())


def solve(data, log):
    a = 0
    b = 0
    for passport in data.split("\n\n"):
        d = {k: v for entry in passport.split() for k, v in [entry.split(":")]}
        if REQUIRED.issubset(d.keys()):
            a += 1
            try:
                b += all(f(d[k]) for k, f in VALIDATORS.items())
            except ValueError:
                continue

    yield a
    yield b
