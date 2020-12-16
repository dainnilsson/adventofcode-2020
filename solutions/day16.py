from .day1 import prod
import re


def solve(data, log):
    d1, d2, d3 = data.split("\n\n")
    rs = {
        m[0]: (range(int(m[1]), int(m[2]) + 1), range(int(m[3]), int(m[4]) + 1))
        for m in re.findall(r"([ a-z]+): (\d+)-(\d+) or (\d+)-(\d+)", d1)
    }
    mine = [int(v) for v in d2.splitlines()[1].split(",")]
    tks = [[int(v) for v in l.split(",")] for l in d3.splitlines()[1:]]

    s = 0
    rn = list(sum(rs.values(), ()))
    for t in tks.copy():
        err = False
        for v in t:
            if not any(v in r for r in rn):
                err = True
                s += v
        if err:
            tks.remove(t)
    yield s

    tks.append(mine)
    cs = [
        [f for f, r in rs.items() if all(any(t[i] in x for x in r) for t in tks)]
        for i in range(len(rs))
    ]
    while any(len(c) > 1 for c in cs):
        for c in cs:
            if len(c) == 1:
                for c2 in cs:
                    if c[0] in c2 and c2 != c:
                        c2.remove(c[0])
    fs = [c[0] for c in cs]
    yield prod(v for f, v in zip(fs, mine) if f.startswith("departure"))
