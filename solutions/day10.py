def solve(data, log):
    ns = [int(l) for l in data.splitlines()]
    ns.sort()
    ns.append(ns[-1] + 3)

    a = sum(1 for p, n in zip([0] + ns, ns) if n - p == 1)
    b = sum(1 for p, n in zip([0] + ns, ns) if n - p == 3)
    yield a * b

    buf = [(0, 1)]
    for n in ns:
        buf.append((n, sum(bn for b, bn in buf[-3:] if n - b <= 3)))
    yield buf[-1][1]
