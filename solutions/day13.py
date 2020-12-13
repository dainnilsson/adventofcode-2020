from itertools import count
from math import gcd


def solve(data, log):
    t, bs = data.splitlines()
    t, bs = int(t), bs.split(",")

    b = sorted([int(b) for b in bs if b != "x"], key=lambda v: v - (t % v))[0]
    yield b * (b - (t % b))

    ps = [(int(b), i) for i, b in enumerate(bs) if b != "x"]
    b, t = ps.pop(0)
    for b2, i in ps:
        b, t = next((b * b2 // gcd(b, b2), t) for t in count(t, b) if (t + i) % b2 == 0)
    yield t
