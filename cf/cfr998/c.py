from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


T = int(input())

for _ in range(T):
    N, K = read_ints()
    nums = list(read_ints())

    if K == 1:
        print(0)
        continue

    nums.sort()
    # count number of pairs of numbers that sum to K
    pairs = 0
    i, j = 0, N - 1
    while i < j:
        s = nums[i] + nums[j]
        if s == K:
            pairs += 1
            i += 1
            j -= 1
        elif s < K:
            i += 1
        else:
            j -= 1

    print(pairs)
