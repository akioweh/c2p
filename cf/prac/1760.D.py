from itertools import groupby, tee, chain
from sys import stdin, stdout
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline
# noinspection PyShadowingBuiltins
print = stdout.write


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N = int(input())
    a = list(read_ints())

    prev = 10**9 + 1
    seen = False
    temp, temp1 = tee(groupby(a))
    next(temp1)
    temp1 = chain(temp1, [(10**9 + 1, None)])
    for (v, _), (next_v, _) in zip(temp, temp1):
        if prev > v < next_v:
            if seen:
                print('NO\n')
                break
            seen = True
        prev = v
    else:
        if seen:
            print('YES\n')
        else:
            print('NO\n')
