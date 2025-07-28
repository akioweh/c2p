from sys import stdin
from typing import Iterable
from itertools import groupby
from operator import mul


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N, M, x, y = read_ints()

    y = min(2 * x, y)

    tot = sum(
        sum(
            sum(
                map(mul, divmod(len(list(g)), 2), (y, x))
            ) for _, g in filter(lambda kg: kg[0] == '.', groupby(input()))
        ) for _ in range(N)
    )
    print(tot)
