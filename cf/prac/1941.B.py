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
    arr = list(read_ints())

    for i in range(1, N - 1):
        ops = arr[i - 1]
        arr[i] -= 2 * ops
        arr[i + 1] -= ops
        if arr[i] < 0 or arr[i + 1] < 0:
            print('NO\n')
            break
    else:
        if arr[-1] == arr[-2] == 0:
            print('YES\n')
        else:
            print('NO\n')
