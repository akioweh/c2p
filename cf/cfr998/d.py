from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N = int(input())
    nums = list(read_ints())

    if nums[0] > nums[1]:
        print('NO')
        continue

    # greedily apply operation on every index
    for i in range(N - 1):
        if nums[i] > nums[i + 1]:
            break
        nums[i + 1] -= nums[i]
    else:
        print('YES')
        continue
    print('NO')
