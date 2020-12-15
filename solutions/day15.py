from itertools import islice


def game(ns):
    mem = {}
    for i, n in enumerate(ns):
        mem[n] = i
        last = n
        yield last
    while True:
        seen = mem.get(last)
        mem[last] = i
        last = 0 if seen is None else i - seen
        i += 1
        yield last


def solve(data, log):
    g = game(int(n) for n in data.split(","))
    yield next(islice(g, 2020 - 1, None))
    yield next(islice(g, 30000000 - 2020 - 1, None))
