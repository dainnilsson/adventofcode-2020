from functools import partial, reduce
from itertools import combinations
import operator


prod = partial(reduce, operator.mul)


def solve(data, log):
    values = [int(line) for line in data.splitlines()]

    def solve_for(n, s):
        return prod(next(c for c in combinations(values, n) if sum(c) == s))

    yield solve_for(2, 2020)
    yield solve_for(3, 2020)
