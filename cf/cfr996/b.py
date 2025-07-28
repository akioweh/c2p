from operator import sub
from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N = int(input())
    a = list(read_ints())
    b = list(read_ints())
    # a - b
    excess = map(sub, a, b)
    neg_val = None
    min_avail = 10**9
    for diff in excess:
        if diff < 0:
            if neg_val is None:
                neg_val = diff
            else:
                neg_val = 69
                break
        else:
            min_avail = min(min_avail, diff)
    if neg_val is None:
        print('YES')
    elif neg_val == 69:
        print('NO')
    else:
        print('YES' if min_avail >= -neg_val else 'NO')
