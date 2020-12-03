from itertools import count


def solve(data, log):
    lines = data.splitlines()

    def trees(dx, dy):
        return sum(
            1
            for x, y in zip(count(0, dx), range(0, len(lines), dy))
            if lines[y][x % len(lines[y])] == "#"
        )

    a = trees(3, 1)

    yield a
    yield trees(1, 1) * a * trees(5, 1) * trees(7, 1) * trees(1, 2)
