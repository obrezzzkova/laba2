import random
from ex_1 import goods


def field(items, *args):
    assert len(args) > 0
    if args == 1:
        for item in items:
            if args[0] in item:
                return item[args[0]]
    else:
        for item in items:
            d = {arg: item[arg] for arg in args if arg in item}
            if len(d) > 0:
                return d


def gen_random(begin, end, num_count):
    for x in num_count:
        yield random.randint(begin, end)
    pass

