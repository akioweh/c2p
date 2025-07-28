"""
tbh i still dont understand this problem but ok
"""


def solve():
    L, R = read_ints()

    diff = L ^ R
    msdf = diff.bit_length()

    r_fill = R & ((1 << 32) - 1 << (msdf - 1))  # discard lower bits; largest number of 0b1..10..0 that < R
    l_fill = r_fill - 1  # lower 0-bits all flip to 1
    useless = R if r_fill != R else R - 2

    write_str(f'{r_fill} {l_fill} {useless}')


### Python 3.8-3.13 compatible competitive programming template ###
# 21 Jan 2025 Version
from sys import stdin, stdout
from typing import Iterable, List

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


def read_strs() -> List[str]:
    """Reads a line as space-separated strings"""
    return srdl().split()


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


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
