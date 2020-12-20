from .day1 import prod


M = [
    "                  # ",
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]


def rotate(t):
    return tuple(zip(*t[::-1]))


def orientations(t):
    for f in (t, t[::-1]):
        for _ in range(4):
            yield f
            f = rotate(f)


def positions(puz):
    d = set(puz)
    for x, y in puz:
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            p = (x + dx, y + dy)
            if p not in d:
                yield p
                d.add(p)


def fits(puz, t, x, y):
    n = puz.get((x, y - 1))
    if n is None or n[1][-1] == t[0]:
        s = puz.get((x, y + 1))
        if s is None or s[1][0] == t[-1]:
            rt = rotate(t)
            w = puz.get((x - 1, y))
            if w is None or rotate(w[1])[-1] == rt[0]:
                e = puz.get((x + 1, y))
                return e is None or rotate(e[1])[0] == rt[-1]


def solve(data, log):
    tiles = {}
    for block in data.split("\n\n"):
        ls = block.splitlines()
        k = int(ls.pop(0).split()[1][:-1])
        tiles[k] = tuple(tuple(l) for l in ls)

    done = len(tiles)
    explore = [{(0, 0): tiles.popitem()}]
    while explore:
        pz = explore.pop()
        if len(pz) == done:
            break
        for k, v in tiles.items():
            if not any(k == x for x, _ in pz.values()):
                explore.extend(
                    pz | {(x, y): (k, p)}
                    for p in orientations(v)
                    for x, y in positions(pz)
                    if fits(pz, p, x, y)
                )

    mnx, mny, mxx, mxy = 0, 0, 0, 0
    for x, y in pz.keys():
        mnx = min(mnx, x)
        mxx = max(mxx, x)
        mny = min(mny, y)
        mxy = max(mxy, y)
    yield prod(pz[pos][0] for pos in ((mnx, mny), (mxx, mny), (mnx, mxy), (mxx, mxy)))

    ts = {k: ["".join(l[1:-1]) for l in v[1][1:-1]] for k, v in pz.items()}
    h = len(ts[(0, 0)])
    img = []
    for y in range(mny, mxy + 1):
        chunk = [""] * h
        for x in range(mnx, mxx + 1):
            t = ts[(x, y)]
            for y2 in range(len(t)):
                chunk[y2] += t[y2]
        img.extend(chunk)

    for o in orientations(img):
        if ms := sum(
            all(
                o[y + dy][x + dx] == "#"
                for dy in range(len(M))
                for dx in range(len(M[0]))
                if M[dy][dx] == "#"
            )
            for y in range(len(o) - len(M))
            for x in range(len(o[0]) - len(M[0]))
        ):
            break
    a = sum(c == "#" for line in img for c in line)
    b = sum(c == "#" for line in M for c in line)
    yield a - ms * b
