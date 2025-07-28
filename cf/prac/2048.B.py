from sys import stdin, stdout
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline
# noinspection PyShadowingBuiltins
print = stdout.write


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N, K = map(int, input().split())

    i = 1
    a, b = 1, N
    while i <= N:
        if i % K == 0:
            print(f'{a} ')
            a += 1
        else:
            print(f'{b} ')
            b -= 1
        i += 1
    print('\n')

stdout.flush()
