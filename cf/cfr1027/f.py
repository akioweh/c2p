from collections import Counter
from itertools import accumulate
from math import gcd, isqrt
from operator import mul


def prime_factors(n: int) -> Counter[int]:
    res = Counter()
    while n % 2 == 0:
        res[2] += 1
        n //= 2
    for div in range(3, isqrt(n) + 1, 2):
        while n % div == 0:
            res[div] += 1
            n //= div
    if n > 2:
        res[n] += 1
    return res


def calc(x: int, lim: int) -> int:
    # bin packing problem with optimization for multiplicity
    pfac = prime_factors(x)
    if not pfac:
        return 0
    if max(pfac) > lim:
        return -1

    prm, cnt = zip(*pfac.items())
    t = len(prm)

    # state compression
    rdx = list(accumulate(map(lambda u: u + 1, cnt), func=mul, initial=1))  # radix array
    n = rdx[-1]

    # dp over subsets/states
    dp = [(sum(cnt) + 1, 1)] * n
    dp[0] = (1, 1)
    for state in range(n):
        n_bins, fill = dp[state]
        # de-compress state
        v = state
        s = [0] * t
        for i in reversed(range(t)):
            s[i], v = divmod(v, rdx[i])

        for k in range(t):
            if s[k] == cnt[k]:
                continue
            if fill * prm[k] <= lim:
                cand = (n_bins, fill * prm[k])
            else:
                cand = (n_bins + 1, prm[k])
            nxt = state + rdx[k]
            dp[nxt] = min(dp[nxt], cand)

    return dp[-1][0]


def solve():
    X, Y, lim = read_ints()
    g = gcd(X, Y)
    a, b = calc(X // g, lim), calc(Y // g, lim)
    if a == -1 or b == -1:
        write_int(-1)
        return
    write_int(a + b)


### Python 3.8-3.13 compatible competitive programming template ###
# 11 Mar 2025 Version
from sys import stdin, stdout
from typing import Callable, Iterable, Iterator, Type, TypeVar

T = TypeVar('T')

srdl = stdin.readline
swrt = stdout.write


def read_ints(int_t: Type[int] = int) -> Iterator[int]:
    """Reads a line as space-separated integers"""
    return map(int_t, srdl().split())


def read_int(int_t: Type[int] = int) -> int:
    """Reads a line as a single integer"""
    return int_t(srdl())


def read_str() -> str:
    """Reads a line as-is"""
    return srdl().strip()


def write_ints(arr: Iterable[int]):
    """Writes a list of integers as a space-separated line"""
    swrt(' '.join(map(str, arr)))
    swrt('\n')


def write_int(val: int):
    """Writes a single integer as a line"""
    swrt(str(val))
    swrt('\n')


def write_str(val: str):
    """Writes a single string as a line"""
    swrt(val)
    swrt('\n')


def prompt(msg: str, prefix: str = '? ', reader: Callable[[], T] = read_str) -> T:
    """Writes a string as a line and reads a line. Flushes output buffer.
    Prepends a default prefix to output."""
    swrt(prefix)
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return reader()


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
