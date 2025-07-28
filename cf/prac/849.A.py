from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


N = int(input())
a = list(read_ints())

if a[0] % 2 == 0 or a[-1] % 2 == 0:
    print('NO')
elif N % 2:
    print('YES')
else:
    print('NO')
