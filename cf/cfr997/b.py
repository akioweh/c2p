from functools import cmp_to_key
from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N = int(input())

    adj_mtx = [
        list(map(int, input().strip()))
        for _ in range(N)
    ]

    res = list(range(N))

    def cmp(a, b):
        if a < b:
            return -1 if adj_mtx[a][b] else 1
        else:
            return 1 if adj_mtx[a][b] else -1

    res.sort(key=cmp_to_key(cmp))
    for i in range(len(res)):
        res[i] += 1

    print(' '.join(map(str, res)))
