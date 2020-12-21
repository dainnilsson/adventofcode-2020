from functools import reduce


def solve(data, log):
    items = []
    for line in data.splitlines():
        a, b = line.split(" (contains ")
        items.append((set(a.split()), set(b[:-1].split(", "))))

    ins = reduce(set.union, (k for k, v in items))
    als = reduce(set.union, (v for k, v in items))
    b = [(a, reduce(set.intersection, (k for k, v in items if a in v))) for a in als]
    safe = ins - reduce(set.union, (v for k, v in b))
    yield sum(len(k & safe) for k, _ in items)

    while any(len(v) > 1 for _, v in b):
        for k, v in b:
            if len(v) == 1:
                for k2, v2 in b:
                    if k != k2:
                        v2 -= v
    yield ",".join(v for k, v in sorted([(k, v.pop()) for k, v in b]))
