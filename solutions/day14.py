import re


def solve(data, log):
    a = {}
    b = {}
    for line in data.splitlines():
        if line.startswith("mask"):
            ds = line.split()[-1]
            ones = int(ds.replace("X", "0"), 2)
            nonzeros = int(ds.replace("X", "1"), 2)
            xs = nonzeros & ~ones
        else:
            m = re.match(r"^mem\[(\d+)\] = (\d+)$", line)
            addr = int(m.group(1))
            value = int(m.group(2))
            a[addr] = (value | ones) & nonzeros
            for i in range(1 << bin(xs).count("1")):
                maddr = addr | ones
                for o in range(xs.bit_length()):
                    bit = 1 << o
                    if bit & xs:
                        if i % 2:
                            maddr ^= bit
                        i >>= 1
                b[maddr] = value
    yield sum(a.values())
    yield sum(b.values())
