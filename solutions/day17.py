from itertools import product


def adj(p):
    for dp in product((-1, 0, 1), repeat=len(p)):
        yield tuple(a + b for a, b in zip(p, dp))


def step(state):
    s2 = set()
    checked = set()
    for p in state:
        for p2 in adj(p):
            if p2 not in checked:
                checked.add(p2)
                c = sum(1 for n in adj(p2) if n in state)
                if p2 in state:
                    if 2 < c < 5:
                        s2.add(p2)
                elif c == 3:
                    s2.add(p2)
    return s2


def solve(data, log):
    a, b = set(), set()
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            if c == "#":
                a.add((x, y, 0))
                b.add((x, y, 0, 0))

    for i in range(6):
        a = step(a)
    yield len(a)

    for i in range(6):
        b = step(b)
    yield len(b)
