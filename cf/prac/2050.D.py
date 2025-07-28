def solve():
    s = read_str()
    n = len(s)
    a = list(map(int, s))
    for i in range(1, n):
        cur, prev = a[i], a[i - 1]
        if not cur - 1 > prev:
            continue
        r_dist = 1
        while i - r_dist > 0 and cur - r_dist - 1 > a[i - r_dist - 1]:
            r_dist += 1
        tmp = a[i] - r_dist
        for j in range(i, i - r_dist, -1):
            a[j] = a[j - 1]
        a[i - r_dist] = tmp

    write_str(''.join(map(str, a)))


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
