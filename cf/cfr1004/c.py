"""
You are given a positive integer n.
In one operation, you can add to n any positive integer
whose decimal representation contains only the digit 9,
possibly repeated several times.

What is the minimum number of operations needed
to make the number n contain at least one digit 7
in its decimal representation?
"""


def lmao(x, sus):
    cnt = 0
    while '7' not in str(x):
        x += sus
        cnt += 1
    return cnt


def solve():
    X = read_int()
    s = str(X)
    l = len(s)
    if '7' in s:
        write_int(0)
        return
    ans = 69420
    for l_ in range(1, l + 1):
        sus = int('9' * l_)
        ans = min(ans, lmao(X, sus))

    write_int(ans)


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
