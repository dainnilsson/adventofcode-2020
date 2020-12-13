def solve(data, log):
    ds = [(l[0], int(l[1:])) for l in data.splitlines()]
    dirs = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}
    for p in [[0, 0, 1, 0, 0], [0, 0, 10, 1, 2]]:
        for d in ds:
            if d[0] == "L":
                d = "R", 360 - d[1]
            if d[0] == "R":
                for _ in range(0, d[1], 90):
                    p[2], p[3] = p[3], -p[2]
            elif d[0] == "F":
                for i in range(2):
                    p[i] += p[2 + i] * d[1]
            else:
                for i, v in enumerate(dirs[d[0]]):
                    p[p[4] + i] += v * d[1]
        yield sum(abs(p[i]) for i in range(2))
