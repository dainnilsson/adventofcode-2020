dirs = [(x, y) for y in (-1, 0, 1) for x in (-1, 0, 1) if x or y]


def solve(data, log):
    seats = [list(l) for l in data.splitlines()]
    sx, sy = len(seats[0]), len(seats)

    def get(state, x, y):
        if 0 <= x < sx and 0 <= y < sy:
            return state[y][x]

    def stabilize(state, look, threshold):
        def mutate(x, y):
            s = state[y][x]
            if s != ".":
                c = sum(look(state, x, y, dx, dy) == "#" for dx, dy in dirs)
                if s == "L":
                    if not c:
                        return "#"
                elif s == "#":
                    if c >= threshold:
                        return "L"
            return s

        p, c = -1, 0
        while p != c:
            p = c
            state = [[mutate(x, y) for x in range(sx)] for y in range(sy)]
            c = sum(s == "#" for r in state for s in r)
        return c

    def look_a(state, x, y, dx, dy):
        return get(state, x + dx, y + dy)

    yield stabilize(seats, look_a, 4)

    def look_b(state, x, y, dx, dy):
        c = get(state, x + dx, y + dy)
        return c if c != "." else look_b(state, x + dx, y + dy, dx, dy)

    yield stabilize(seats, look_b, 5)
