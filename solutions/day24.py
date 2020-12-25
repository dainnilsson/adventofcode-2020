def travel(line, x=0, y=0):
    line = list(line)
    while line:
        c = line.pop(0)
        if c in "sn":
            y += 1 if c == "s" else -1
            x += 1 if line.pop(0) == "e" else -1
        else:
            x += 2 if c == "e" else -2
    return x, y


def adj(x, y):
    return [
        (x - 1, y - 1),
        (x + 1, y - 1),
        (x - 2, y),
        (x + 2, y),
        (x - 1, y + 1),
        (x + 1, y + 1),
    ]


def step(black):
    checked = set()
    black2 = set()
    for b in black:
        for c in [b] + adj(*b):
            if c not in checked:
                checked.add(c)
                bs = sum(1 for x in adj(*c) if x in black)
                if c in black:
                    if 0 < bs < 3:
                        black2.add(c)
                elif bs == 2:
                    black2.add(c)
    return black2


def solve(data, log):
    black = set()
    for line in data.splitlines():
        tile = travel(line)
        if tile in black:
            black.remove(tile)
        else:
            black.add(tile)
    yield len(black)

    for _ in range(100):
        black = step(black)
    yield len(black)
