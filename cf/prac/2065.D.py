from itertools import chain
from operator import mul


def solve():
    N, M = read_ints()
    arrs = [
        tuple(read_ints())
        for _ in range(N)
    ]
    O = N * M
    # contirbution of element at index i (with flattened arrs) is
    # arrs[i] * (O - i)
    # contribution of a a segment in arrs, arrs[j] starting at index i is
    # map mul arrs[j] [O - i ... O - i + M)
    # so the difference of contribution between different starting positions for the same segment
    # is a multiple
    # so each segment can be statically evaluated... as a ~~weighted~~ sum

    arrs.sort(key=sum, reverse=True)
    write_int(
        sum(
            map(
                mul,
                chain(*arrs),
                range(O, 0, -1)
            )
        )
    )


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
