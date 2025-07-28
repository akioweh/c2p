from itertools import tee


def solve():
    N = read_int()
    lengths = list(read_ints())
    lengths.sort()

    # find the largest number that appears at least
    sides = None
    sides_idx = None
    for i in range(N - 1, 0, -1):
        if lengths[i] == lengths[i - 1]:
            sides = lengths[i]
            sides_idx = i
            break
    else:
        write_int(-1)
        return

    # find any two numbers a, b, such that min(a, b) + 2 * sides > max(a, b)
    it = (lengths[i] for i in range(N) if i != sides_idx and i != sides_idx - 1)
    it0, it1 = tee(it)
    next(it1)
    for a, b in zip(it0, it1):  # a < b
        if a + 2 * sides > b:
            write_ints((sides, sides, a, b))
            return
    write_int(-1)


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
