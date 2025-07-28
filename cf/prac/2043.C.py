from itertools import accumulate


def minmax_subarray(arr, lo, hi, f = max):
    best_sum = 0
    current_sum = 0
    for i in range(lo, hi):
        v = arr[i]
        current_sum = f(0, current_sum + v)
        best_sum = f(best_sum, current_sum)
    return best_sum


def solve():
    N = read_int()
    arr = list(read_ints())
    idx = N
    for i, v in enumerate(arr):
        if v != 1 and v != -1:
            idx = i
            break
    lower = min(minmax_subarray(arr, 0, idx, f = min), minmax_subarray(arr, idx + 1, N, f = min))
    upper = max(minmax_subarray(arr, 0, idx, f = max), minmax_subarray(arr, idx + 1, N, f = max))

    if idx != N:
        l_max, l_min = 0, 0
        if idx > 0:
            for s in accumulate(arr[idx - 1::-1]):
                l_max = max(l_max, s)
                l_min = min(l_min, s)
        r_max, r_min = 0, 0
        if idx < N - 1:
            for s in accumulate(arr[idx + 1:]):
                r_max = max(r_max, s)
                r_min = min(r_min, s)
        lower2 = l_min + r_min + arr[idx]
        upper2 = l_max + r_max + arr[idx]
    else:
        lower2 = upper2 = 0

    # see if intervals overlap
    if max(lower, lower2) <= min(upper, upper2):
        lower = min(lower, lower2)
        upper = max(upper, upper2)
        write_int(upper - lower + 1)
        write_ints(range(lower, upper + 1))
    else:
        write_int(upper - lower + 1 + upper2 - lower2 + 1)
        if lower2 < lower:
            write_ints(range(lower2, upper2 + 1), end = ' ')
            write_ints(range(lower, upper + 1))
        else:
            write_ints(range(lower, upper + 1), end = ' ')
            write_ints(range(lower2, upper2 + 1))



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


def write_ints(arr: Iterable[int], end = '\n'):
    """Writes a list of integers as a space-separated line"""
    swrt(' '.join(map(str, arr)))
    swrt(end)


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
