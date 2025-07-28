"""
Observation: 2-d segtree node "walk"/"collection"
https://codeforces.com/blog/entry/18051

The optimal solution is unique, and you would never pick overlapping nodes.
"""


def count_collect_nodes(xl: int, xr: int, yl: int, yr: int) -> int:
    # right bounds are exclusive in the sense that 1x1 nodes are a point located at the bottom-left corner
    # similar to segment tree node walk (upwards)
    cnt = 0
    while xl < xr and yl < yr:
        if xl % 2:
            cnt += yr - yl
            xl += 1
        if xr % 2:
            xr -= 1
            cnt += yr - yl
        if yl % 2:
            cnt += xr - xl
            yl += 1
        if yr % 2:
            yr -= 1
            cnt += xr - xl
        xl //= 2
        xr //= 2
        yl //= 2
        yr //= 2
    return cnt


def solve():
    write_int(count_collect_nodes(*read_ints()))


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
