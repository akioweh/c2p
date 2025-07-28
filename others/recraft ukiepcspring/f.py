from math import atan2


def solve():
    read_int()
    points = [
        tuple(read_ints())
        for _ in range(4)
    ]

    if any(p == (0, 0) for p in points):
        write_str('NO')
        return

    # sort by angle
    points.sort(key=lambda p: atan2(p[1], p[0]))

    # do the rotate thing
    points[1] = points[1][1], -points[1][0]
    points[3] = -points[3][1], points[3][0]
    points[2] = -points[2][0], -points[2][1]

    # haha lin alg moment
    for i in range(4):
        for j in range(i + 1, 4):
            p1 = points[i]
            p2 = points[j]
            dot = p1[0] * p2[0] + p1[1] * p2[1]
            if dot <= 0:
                write_str('NO')
                return
    write_str('YES')


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
