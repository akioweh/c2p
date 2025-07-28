def solve():
    x = read_int()
    # x ^ y = x + y - 2(x & y)

    # x + y > x + y - 2(x & y)
    # -> x & y > 0

    # (x ^ y) + y > x
    # x + y - 2(x & y) + y > x
    # 2y - 2(x & y) > 0
    # -> x & y < y
    # -> x != y and x.bit_count() < y.bit_count()

    ln = x.bit_length()

    if x.bit_count() in (ln, 1):
        write_int(-1)
        return

    lsb = x & -x
    msz = 1 << ((x ^ ((1 << ln) - 1)).bit_length() - 1)

    y = lsb + msz
    if y >= x:
        write_int(-1)
        return
    write_int(y)


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
