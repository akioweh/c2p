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
    a1, a2, a4, a5 = read_ints()

    # a3 = a5 - a4
    # a3 = a1 + a2
    # a3 = a4 - a2

    v1 = a5 - a4
    v2 = a1 + a2
    v3 = a4 - a2

    if v1 == v2 == v3:
        print("3\n")
    elif v1 == v2 or v1 == v3 or v2 == v3:
        print("2\n")
    else:
        print("1\n")
