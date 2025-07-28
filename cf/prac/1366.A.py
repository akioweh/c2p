from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    a, b = read_ints()
    if b > a:
        a, b = b, a

    if a >= 2 * b:
        print(b)
    else:
        q, r = divmod(2 * b - a, 3)
        res = a - b + 2 * q
        if r == 2:
            res += 1
        print(res)
