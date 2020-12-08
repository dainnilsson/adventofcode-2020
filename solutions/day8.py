def solve(data, log):
    pg = [(l.split()[0], int(l.split()[1])) for l in data.splitlines()]

    def prog():
        pc, acc = 0, 0
        seen = set()
        while pc not in seen and 0 <= pc < len(pg):
            seen.add(pc)
            cmd, arg = pg[pc]
            if cmd == "acc":
                acc += arg
            pc += arg if cmd == "jmp" else 1
        return pc, acc

    yield prog()[1]

    for i in range(len(pg)):
        cmd, arg = pg[i]
        if cmd != "acc":
            pg[i] = ("jmp" if cmd == "nop" else "nop", arg)
            pc, acc = prog()
            if pc == len(pg):
                break
            pg[i] = (cmd, arg)
    yield acc
