import re

p = re.compile(r"(\d+) ([ \w]+) bag")


def solve(data, log):
    rules = {
        k: [(int(n), bag) for n, bag in p.findall(vs)]
        for k, vs in (l.split(" bags contain ") for l in data.splitlines())
    }

    def can_contain(bag):
        for k, vs in rules.items():
            if any(v == bag for _, v in vs):
                yield from can_contain(k)
                yield k

    yield len(set(can_contain("shiny gold")))

    def n_bags(bag):
        yield from (n * sum(n_bags(b)) for n, b in rules[bag])
        yield 1

    yield sum(n_bags("shiny gold")) - 1
