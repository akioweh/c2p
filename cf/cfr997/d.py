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

    ans = 0

