def solve():
    N = read_int()
    if N <= 0:
        exit(-69)
    for _ in range(2):
        temp = prompt('digit', '', read_int)
        if temp != 1:
            exit(-1)
    # bin search
    lo = 1
    hi = 16
    for _ in range(4):
        if lo == hi:
            break
        mid = (lo + hi) // 2
        resp = prompt(f'add -{mid}', '', read_int)
        if resp == 1:  # > mid
            lo = 1
            hi -= mid
        elif resp == 0:  # <= mid
            hi = mid
        else:
            exit(-2)

    diff = N - lo
    temp = prompt(f'add {diff}', '', read_int)
    if temp != 1:
        exit(-3)
    temp = prompt('', '!', read_int)
    if temp != 1:
        exit(-4)


### Python 3.8-3.13 compatible competitive programming template ###
# 11 Mar 2025 Version
from sys import stdin, stdout
from typing import Callable, Iterable, Iterator, Type, TypeVar

T = TypeVar('T')

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


def prompt(msg: str, prefix: str = '? ', reader: Callable[[], T] = read_str) -> T:
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
