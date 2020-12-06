from functools import reduce
import operator


def solve(data, log):
    groups = [[set(p) for p in g.split()] for g in data.split("\n\n")]
    yield sum(len(reduce(operator.or_, g)) for g in groups)
    yield sum(len(reduce(operator.and_, g)) for g in groups)
