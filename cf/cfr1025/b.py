def log2(x: int) -> int:
    cnt = 0
    while x > 1:
        x = (x + 1) // 2
        cnt += 1
    return cnt


def solve():
    N, M, a, b = read_ints()

    first_cuts = [
        (N, b),
        (N, M - b + 1),
        (a, M),
        (N - a + 1, M),
    ]

    n, m = min(first_cuts, key=lambda x: log2(x[0]) + log2(x[1]))
    turns = 1
    while not (n == 1 and m == 1):
        if n % 2 == 0:
            n //= 2
        elif m % 2 == 0:
            m //= 2
        else:
            if n > 1:
                n = (n + 1) // 2
            else:
                m = (m + 1) // 2
        turns += 1

    write_int(turns)


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
