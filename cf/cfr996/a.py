from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N, a, b = read_ints()
    if abs(b - a) % 2:
        print('NO')
    else:
        print('YES')
