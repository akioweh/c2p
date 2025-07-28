from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    A, B = read_ints()

    if B == 1:
        print('NO')
        continue

    # find a, b, c satisfying either of:
    # aB + b = c  AND  b, c (mod B) != 0
    # b + c = aB  AND  b, c (mod B) != 0

    # then answer (x, y, z) = A * (a, b, c)

    for a in range(1, 10**18):
        target = a * B
        found = False
        for b in range(1, target):
            if b == a:
                continue
            c = target - b
            if a == c or b == c or not (b * c) % B:
                continue
            print('YES')
            print(b * A, c * A, target * A)
            break
        else:
            continue
        break
