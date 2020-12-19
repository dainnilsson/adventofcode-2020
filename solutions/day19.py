def solve(data, log):
    a, b = data.split("\n\n")
    rs = {
        int(k): v[1]
        if '"' in v
        else [[int(y) for y in x.split(" ")] for x in v.split(" | ")]
        for k, v in (r.split(": ") for r in a.splitlines())
    }
    ws = b.splitlines()

    def match(w, p):
        if not p:
            return not w
        r = rs[p.pop(0)]
        if isinstance(r, str):
            return w.startswith(r) and match(w[len(r) :], p)
        return any(match(w, nr + p) for nr in r)

    yield sum(1 for w in ws if match(w, [0]))
    rs[8] = [[42], [42, 8]]
    rs[11] = [[42, 31], [42, 11, 31]]
    yield sum(1 for w in ws if match(w, [0]))
