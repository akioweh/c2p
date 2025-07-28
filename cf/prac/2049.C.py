def solve():
    N, x, y = read_ints()
    if x > y:
        x, y = y, x
    if N % 2:
        if x % 2:
            ans = [0, 1] * (N // 2 + 1)
        else:
            ans = [1, 0] * (N // 2 + 1)
        ans.pop(x - 1)
        ans[x - 1] = 2
    else:
        if x % 2:
            ans = [0, 1] * (N // 2)
        else:
            ans = [1, 0] * (N // 2)
        if x % 2 == y % 2:
            ans[x - 1] = 2

    write_ints(ans)


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
