def game(cups, rounds):
    n = len(cups)
    h = cups[0]
    p = h
    nodes = {}
    for c in cups[1:]:
        nodes[p] = c
        p = c
    nodes[p] = h

    for _ in range(rounds):
        a = nodes[h]
        b = nodes[a]
        c = nodes[b]
        nodes[h] = nodes[c]
        rs = [h, a, b, c]
        d = rs[0]
        while d in rs:
            d = n if d == 1 else d - 1
        nodes[c] = nodes[d]
        nodes[d] = a
        h = nodes[h]

    p = nodes[1]
    while p != 1:
        yield p
        p = nodes[p]


def solve(data, log):
    cups = [int(c) for c in data.strip()]
    yield "".join(str(c) for c in game(cups, 100))

    g = game(cups + list(range(len(cups) + 1, 1000001)), 10000000)
    yield next(g) * next(g)
