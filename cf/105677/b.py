from itertools import accumulate


def solve():
    N, K = read_ints()
    K = min(N, K)  # fuck this shit
    arr = list(read_ints())

    idx = list(range(N))
    idx.sort(key=arr.__getitem__)
    y = list(map(arr.__getitem__, idx))
    pfs_y = list(accumulate(y, initial=0))
    pfs_y2 = list(accumulate((v ** 2 for v in y), initial=0))

    def err(l_: int, r_: int) -> int:
        y_s = pfs_y[r_] - pfs_y[l_]
        y2_s = pfs_y2[r_] - pfs_y2[l_]
        n = r_ - l_
        c_ = y[r_ - 1]
        return y2_s - 2 * c_ * y_s + n * c_ ** 2

    dp: list[list[int]] = [  # dp[i][k] == min error to divide y[:i] into k+1 parts
        [0] * (min(len_, K) + 1)
        for len_ in range(N + 1)
    ]
    dp_l_idx: list[list[int]] = [
        [0] * (min(len_, K) + 1)
        for len_ in range(N + 1)
    ]

    for r in range(1, N + 1):
        for k in range(min(r, K)):
            dp[r][k], dp_l_idx[r][k] = min(
                (dp[m][k - 1] + err(m, r), m)
                for m in range(k, r if k else 1)
            )

    ans = [-1] * N
    _l = N
    for k_idx in range(K - 1, -1, -1):
        _l, _r = dp_l_idx[_l][k_idx], _l
        c = y[_r - 1]
        for _i in map(idx.__getitem__, range(_l, _r)):
            ans[_i] = c

    write_ints(ans)


### Python 3.8-3.13 compatible competitive programming template ###
# 4 Mar 2025 Version
from sys import stdin, stdout
from typing import Callable, Iterable, Iterator, Type

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


def prompt(msg: str, prefix: str = '? ', reader: Callable = read_str) -> str:
    """Writes a string as a line and reads a line. Flushes output buffer.
    Prepends a default prefix to output."""
    swrt(prefix)
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return reader()


# Single-case format
if __name__ == '__main__':
    solve()
