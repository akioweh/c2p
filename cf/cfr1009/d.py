from math import isqrt
from operator import itemgetter


def solve():
    N, M = read_ints()
    xs = list(read_ints())
    rs = list(read_ints())

    max_r = max(rs)
    intervs = [[] for _ in range(max_r + 1)]
    rowz = []
    for x0, ra in zip(xs, rs):
        rowz.append((x0 - ra, x0 + ra))
        r2 = ra ** 2
        for y in range(1, ra):
            dx = isqrt(r2 - y ** 2)
            intervs[y].append((x0 - dx, x0 + dx))
        intervs[ra].append((x0, x0))

    ans = 0
    for row in intervs:
        row.sort(key=itemgetter(0))
        last_r = -10**19
        for l, r in row:
            if r <= last_r:
                continue
            if l > last_r:
                ans += r - l + 1
            else:
                ans += r - last_r
            last_r = r

    ans *= 2
    last_r = -10**19
    rowz.sort()
    for l, r in rowz:
        if r <= last_r:
            continue
        if l > last_r:
            ans += r - l + 1
        else:
            ans += r - last_r
        last_r = r

    write_int(ans)


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


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
