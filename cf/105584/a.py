from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


while True:
    if input() == '0\n':
        break
    arr = list(read_ints())

    tot = 0
    for v in arr:
        if v + tot <= 300:
            tot += v
        if tot == 300:
            break

    print(tot)
