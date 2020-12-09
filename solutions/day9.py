from itertools import combinations


def solve(data, log):
    ns = [int(l) for l in data.splitlines()]

    for i in range(25, len(ns)):
        v = ns[i]
        if all(a + b != v for a, b in combinations(ns[i - 25 : i], 2)):
            break
    yield v

    s = 0
    rn = []
    while s != v or len(rn) < 2:
        if s > v:
            s -= rn.pop(0)
        else:
            n = ns.pop(0)
            rn.append(n)
            s += n
    yield min(rn) + max(rn)
