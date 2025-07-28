from math import log, ceil, floor


def solve():
    K, l1, r1, l2, r2 = read_ints()
    log_l1 = log(l1, K)
    log_r1 = log(r1, K)
    log_l2 = log(l2, K)
    log_r2 = log(r2, K)
    ans = 0
    for n in range(33):
        log_x_lower = max(log_l1, log_l2 - n)
        log_x_upper = min(log_r1, log_r2 - n)
        x_lower = ceil(round(K ** log_x_lower, 1))
        x_upper = floor(round(K ** log_x_upper, 1))
        if x_lower > x_upper:
            continue
        ans += x_upper - x_lower + 1
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
