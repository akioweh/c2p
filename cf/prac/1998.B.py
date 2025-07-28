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
    N = int(input())
    p = list(read_ints())

    i = iter(p)
    next(i)
    print(' '.join(map(str, i)))
    print(' ')
    print(str(p[0]))
    print('\n')
