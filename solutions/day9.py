from itertools import combinations


def solve(data, log):
    ns = [int(l) for l in data.splitlines()]

    for i in range(25, len(ns)):
        v = ns[i]
        if all(a + b != v for a, b in combinations(ns[i - 25 : i], 2)):
            break
    yield v

    rn = []
    while v or len(rn) < 2:
        n = ns.pop(0)
        rn.append(n)
        v -= n
        while v < 0:
            v += rn.pop(0)
    yield min(rn) + max(rn)
