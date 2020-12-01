import os
import pytest
import importlib


@pytest.mark.parametrize(
    'day, part',
    [(day, part) for day in range(1, 26) for part in ("a", "b")]
)
def test_solution(day, part):
    in_f = "input/%d.txt" % day
    if not os.path.isfile(in_f):
        pytest.skip("No input")

    out_f = "output/%d%s.txt" % (day, part)
    if not os.path.isfile(out_f):
        pytest.skip("No output")

    with open(in_f) as f:
        data = f.read()

    with open(out_f) as f:
        out = f.read()

    module = importlib.import_module("aoc_20.day%d" % day)
    solver = module.solve(data, lambda *_: None)

    a = next(solver)
    if part == "a":
        assert "%s\n" % a == out
    else:
        b = next(solver)
        assert "%s\n" % b == out
