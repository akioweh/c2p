def solve():
    n0, n1, k = read_ints()
    a, b = min(n0, n1), max(n0, n1)
    n = a + b
    if k < b - a or k > b:
        write_str('-1')
        return
    # now we construct
    if n0 > n1:
        pre = '0'
        mid = '10'
        suf = '1'
        x = n0 - k
        y = n1 - x
    else:
        pre = '1'
        mid = '01'
        suf = '0'
        x = n1 - k
        y = n0 - x
    write_str(pre * k + mid * x + suf * y)


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
