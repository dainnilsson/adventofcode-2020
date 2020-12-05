tr = str.maketrans({"F": "0", "B": "1", "L": "0", "R": "1"})


def solve(data, log):
    ids = {int(l, 2) for l in data.translate(tr).splitlines()}
    yield max(ids)

    for i in range(1024):
        if i not in ids and i - 1 in ids and i + 1 in ids:
            yield i
