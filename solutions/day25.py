def solve(data, log):
    a, b = (int(l) for l in data.splitlines())
    p = 20201227
    yield pow(b, next(n for n in range(1, p) if a == pow(7, n, p)), p)
    yield None
