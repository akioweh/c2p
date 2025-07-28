def solve():
    N, M = read_ints()
    colors = [
        list(read_ints())
        for _ in range(N)
    ]
    O = N * M
    has_neighbor: list[bool] = [False] * (O + 1)
    exists: list[bool] = [False] * (O + 1)
    for i in range(N):
        for j in range(M):
            c = colors[i][j]
            if has_neighbor[c]:
                continue
            exists[c] = True
            if (i > 0 and colors[i - 1][j] == c) or (j > 0 and colors[i][j - 1] == c):
                has_neighbor[c] = True

    n_colors = sum(exists)
    n_need2 = sum(has_neighbor)
    n_need1 = n_colors - n_need2

    if n_need2 <= 1:
        write_int(n_colors - 1)
    else:
        write_int(n_need1 + (n_need2 - 1) * 2)


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
