from bisect import bisect_left


def solve():
    N, M = read_ints()
    n_s = list(read_ints())
    m_s = list(read_ints())
    m_s.sort()

    prev = min(n_s[0], m_s[0] - n_s[0])
    for i in range(1, N):
        # for x = m - n, find smallest x that is not less than prev
        # => m - n >= prev
        # => m >= prev + n
        cur = n_s[i]
        cur_good = cur >= prev
        idx = bisect_left(m_s, prev + cur)
        alt_good = idx < M
        if not cur_good and not alt_good:
            write_str('NO')
            return
        if cur_good and alt_good:
            prev = min(cur, m_s[idx] - cur)
        elif cur_good:
            prev = cur
        else:
            prev = m_s[idx] - cur
    write_str('YES')


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


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
