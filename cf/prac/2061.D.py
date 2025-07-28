from heapq import heapify, heappop, heappush
from operator import neg


def solve():
    N, M = read_ints()
    # negate for max-heap (heapq is min-heap)
    n_s = list(map(neg, read_ints()))
    t_s = list(map(neg, read_ints()))
    heapify(n_s)
    heapify(t_s)

    ops = N - M
    while n_s and t_s:
        n = -n_s[0]
        t = -t_s[0]
        if n == t:
            heappop(n_s)
            heappop(t_s)
        elif t > n:
            if ops == 0 or t == 1:
                write_str('NO')
                return
            ops -= 1
            heappop(t_s)
            a = b = t // 2
            if t % 2:
                b += 1
            heappush(t_s, -a)
            heappush(t_s, -b)
        else:  # n > t
            write_str('NO')
            return

    if n_s or t_s:
        write_str('NO')
    else:
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
