from random import getrandbits


class hish(int):
    salt = getrandbits(64)

    def __hash__(self):
        return super().__hash__() ^ hish.salt


def solve():
    N = read_int()
    arr = list(read_ints(hish))

    seen = set()
    has_dup = set()
    for v in arr:
        if v not in seen:
            seen.add(v)
        elif v not in has_dup:
            has_dup.add(v)

    ml, mr = -1, -1
    l = 0
    for i, v in enumerate(arr):
        if v in has_dup:
            if i - l > mr - ml:
                ml = l
                mr = i
            l = i + 1
    if len(arr) - l > mr - ml:
        ml = l
        mr = len(arr)

    if ml == -1:
        write_int(0)
        return
    write_ints((ml + 1, mr))


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
