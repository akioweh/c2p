def solve():
    N, X = read_ints()
    if N == 1 and X == 0:
        write_int(-1)
        return
    ans = X
    N -= X.bit_count()
    if N <= 0:
        write_int(ans)
        return
    ans += N // 2 * 2
    if N % 2:
        min_slot = 2 if X <= 1 else 1
        ans += 2 * min_slot
    write_int(ans)


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
