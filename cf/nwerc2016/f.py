def solve():
    N = read_int()
    r1 = list(read_ints())
    r2 = list(read_ints())

    def check(v: int) -> bool:
        _r1 = list(filter(lambda x: x > v, r1))
        _r2 = list(filter(lambda x: x > v, r2))
        if len(_r1) % 2 or len(_r2) % 2:
            return False
        for i in range(0, len(_r1), 2):
            if _r1[i] != _r1[i + 1]:
                return False
        for i in range(0, len(_r2), 2):
            if _r2[i] != _r2[i + 1]:
                return False
        return True

    l = 0
    r = 10**9
    while l < r:
        m = (l + r) // 2
        _r = check(m)
        if _r:
            r = m
        else:
            l = m + 1
    write_int(l)


### Python 3.10-3.13 compatible competitive programming template ###
# 23 July 2025 Version
from collections.abc import Callable, Iterable, Iterator
from sys import stdin, stdout
from typing import TypeVar

T = TypeVar('T')

srdl = stdin.readline
swrt = stdout.write


def read_ints(int_t: type[int] = int) -> Iterator[int]:
    """Reads a line as space-separated integers"""
    return map(int_t, srdl().split())


def read_int(int_t: type[int] = int) -> int:
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


def prompt(msg: str, prefix: str = '? ', reader: Callable[[], T] = read_str) -> T:  # type: ignore[assignment]
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
