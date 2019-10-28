#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

# Реализация задания 2
data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2 = gen_random(1, 3, 10)
data4 = [1, 1, 1, 1, 1, 2, 'a', 'A', 'b', 'c', 'C']

print(*Unique(data1))
print(*Unique(data2))
print(*Unique(data3, ignore_case=True))
print(*Unique(data4, ignore_case=True))