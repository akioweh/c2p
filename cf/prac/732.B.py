from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


N, K = read_ints()
a = list(read_ints())

b = 0
for i in range(1, N):
    missing = max(
        0,
        K - (a[i] + a[i - 1])
    )
    b += missing
    a[i] += missing

print(b)
print(' '.join(map(str, a)))
