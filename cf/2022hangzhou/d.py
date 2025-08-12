def solve():
    N = read_int()
    arr = list(read_ints())
    t = sum(arr)
    v = t / (N + 1)
    res = [v] * N
    res[0] *= 2
    write_ints(res)


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
