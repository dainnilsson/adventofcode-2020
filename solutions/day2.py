def parse(line):
    rule, password = line.split(": ")
    r, c = rule.split()
    a, b = r.split("-")
    return int(a), int(b), c, password


def solve(data, log):
    rows = [parse(l) for l in data.splitlines()]

    yield sum(1 for (a, b, c, p) in rows if a <= p.count(c) <= b)
    yield sum(1 for (a, b, c, p) in rows if (p[a - 1] == c) != (p[b - 1] == c))
