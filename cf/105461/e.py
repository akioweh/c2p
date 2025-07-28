from functools import partial
from itertools import pairwise, starmap
from operator import le, sub


def solve():
    N, M, L = read_ints()
    pos = list(read_ints())
    dist = read_ints()

    pos.sort()
    max_dist = max(map(sub, pos[1:], pos), default=0) / 2
    # max_dist = min(starmap(sub, pairwise(pos)), default=0) / -2
    max_dist = max(max_dist, pos[0], L - pos[-1])

    write_int(min(
        filter(partial(le, max_dist), dist),
        default=-1
    ))


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
