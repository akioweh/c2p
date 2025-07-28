from bisect import bisect_left


def solve():
    N = read_int()
    candies = list(read_ints())
    M = read_int()
    shyness = list(read_ints())

    candies.sort()
    idxs = list(range(M))
    idxs.sort(key=shyness.__getitem__)

    ans = [0] * M
    for rank, i in enumerate(idxs):
        val = shyness[i] + rank
        ans[i] = N - bisect_left(candies, val)

    for v in ans:
        write_int(v)


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
