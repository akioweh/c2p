from bisect import bisect_right
from itertools import accumulate


def solve():
    N, K = read_ints()
    arr = list(read_ints())

    def possible(target: float) -> bool:
        a = (x - target for x in arr)
        pfs = accumulate(a)
        # longest non-decreasing subsequence on pfs that includes the first and last values
        dp = [0]
        v = 0
        for v in pfs:
            if v < 0:
                continue
            if v >= dp[-1]:
                dp.append(v)
            else:
                dp[bisect_right(dp, v)] = v
        return bisect_right(dp, v) > K

    lo, hi = 1., 1000.
    for _ in range(30):  # ~= log2(1000 * 1e6)
        mid = (lo + hi) / 2
        if possible(mid):
            lo = mid
        else:
            hi = mid

    print(round(lo, 7))


### Python 3.8-3.13 compatible competitive programming template ###
# 11 Feb 2025 Version
from sys import stdin, stdout
from typing import Iterable

srdl = stdin.readline
swrt = stdout.write


def read_ints() -> Iterable[int]:
    """Reads a line as space-separated integers"""
    return map(int, srdl().split())


def read_int() -> int:
    """Reads a line as a single integer"""
    return int(srdl())


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


def prompt(msg: str) -> str:
    """Writes a string as a line and reads a line. Flushes buffer."""
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return srdl().strip()


# Single-case format
if __name__ == '__main__':
    solve()
