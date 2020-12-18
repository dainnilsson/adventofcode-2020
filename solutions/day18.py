import re


def run(line, ops=("+", "*")):
    res = []
    ts = line.split()
    while ts:
        t = ts.pop(0)
        if t in ops:
            a = int(res.pop())
            b = int(ts.pop(0))
            t = str(a + b if t == "+" else a * b)
        res.append(t)
    return " ".join(res)


def solve(data, log):
    p = re.compile(r"\([^()]+\)")

    for s in (run, lambda x: run(run(x, ("+",)))):
        a = 0
        for line in data.splitlines():
            while m := p.search(line):  # Goo goo g'joob, melon farmer!
                line = line[: m.start()] + s(m[0][1:-1]) + line[m.end() :]
            a += int(s(line))
        yield a
