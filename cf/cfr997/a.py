from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N, M = read_ints()
    x, y = [], []
    read_ints()
    for _ in range(N - 1):
        a, b = read_ints()
        x.append(a)
        y.append(b)

    PERI = 4 * M
    tot_peri = PERI

    for x_, y_ in zip(x, y):
        tot_peri += PERI - 2 * (2 * M - x_ - y_)

    print(tot_peri)

