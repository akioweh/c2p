from functools import reduce
from sys import stdin
from itertools import groupby
from operator import mul


MOD = 10**9 + 7

s = stdin.readline().strip()

section_lengths = []
for c, g in groupby(s):
    if c == 'm' or c == 'w':
        print(0)
        exit(0)
    if c == 'u' or c == 'n':
        l = sum(1 for _ in g)
        if l > 1:
            section_lengths.append(l)

if not section_lengths:
    print(1)
    exit(0)

cache = {}


fib = [1, 1]
for _ in range(len(s) - 2):
    fib.append((fib[-1] + fib[-2]) % MOD)


print(reduce(
    mul,
    map(fib.__getitem__, section_lengths)
) % MOD)
