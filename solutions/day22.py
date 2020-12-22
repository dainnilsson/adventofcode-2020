def game_a(p1, p2):
    while p1 and p2:
        a, p1 = p1[0], p1[1:]
        b, p2 = p2[0], p2[1:]
        if a > b:
            p1 += (a, b)
        else:
            p2 += (b, a)
    return p1 or p2


def game_b(p1, p2):
    s = set()
    while p1 and p2:
        if (p1, p2) in s:
            return True, p1
        s.add((p1, p2))
        a, p1 = p1[0], p1[1:]
        b, p2 = p2[0], p2[1:]
        if len(p1) >= a and len(p2) >= b:
            if game_b(p1[:a], p2[:b])[0]:
                p1 += (a, b)
            else:
                p2 += (b, a)
        else:
            if a > b:
                p1 += (a, b)
            else:
                p2 += (b, a)
    return (True, p1) if p1 else (False, p2)


def solve(data, log):
    ds = tuple(tuple(int(c) for c in d.splitlines()[1:]) for d in data.split("\n\n"))
    yield sum((i + 1) * c for i, c in enumerate(reversed(game_a(*ds))))
    yield sum((i + 1) * c for i, c in enumerate(reversed(game_b(*ds)[1])))
