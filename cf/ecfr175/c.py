from itertools import groupby


def solve():
    N, K = read_ints()
    s = read_str()
    penalty = list(read_ints())

    def check(_t: int) -> bool:
        return K >= sum(
            (1
             for ch, _ in groupby(filter(lambda i: penalty[i] > _t, range(N)), key=s.__getitem__)
             if ch == 'B'),
            start=0
        )

    if check(0):
        write_int(0)
        return

    pens = [-1]
    for p in sorted(penalty):
        if p != pens[-1]:
            pens.append(p)

    lo, hi = 0, len(pens) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if check(pens[mid]):
            hi = mid
        else:
            lo = mid + 1

    write_int(pens[lo])


### Python 3.8-3.13 compatible competitive programming template ###
# 21 Feb 2025 Version
from sys import stdin, stdout
from typing import Iterable, Iterator

srdl = stdin.readline
swrt = stdout.write


def read_ints() -> Iterator[int]:
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


def prompt(msg: str, prefix: str = '? ') -> str:
    """Writes a string as a line and reads a line. Flushes output buffer.
    Prepends a default prefix to output."""
    swrt(prefix)
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return read_str()


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
