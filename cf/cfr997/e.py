from functools import cache
from sys import stdin, setrecursionlimit
from typing import Iterable


setrecursionlimit((1 << 16) - 1)

# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


MOD = 998_244_353


@cache
def n_ways(n: int) -> int:
    if n == 1:
        return 1
    return (sum(
        n_ways(n - i_) * n_ways(i_)
        for i_ in range(1, n)
    ) + 1) % MOD


T = int(input())

for _ in range(T):
    N, M = read_ints()  # max val and current number of segments
    segments = [
        tuple(read_ints())
        for _ in range(M)
    ]

    rightmost = 0
    ans = 1
    for l, r in segments:
        if l > rightmost:
            ans = (ans * n_ways(l - rightmost)) % MOD
        rightmost = max(rightmost, r)

    if rightmost < N:
        ans = (ans * n_ways(N - rightmost)) % MOD

    print(ans)

