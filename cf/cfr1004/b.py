from collections import Counter, defaultdict
from heapq import heappop, heappush, heapify


def solve():
    N = read_int()
    nums = list(read_ints())
    freqs = Counter(nums)
    new_freqs = defaultdict(int)

    # we greedily "promote" values to their largest possible value
    vals = list(freqs.keys())
    heapify(vals)
    while vals:
        v = heappop(vals)
        tot = new_freqs[v] + freqs[v]
        if not tot:
            continue
        if tot < 2:  # ono
            write_str('NO')
            return
        extras = tot - 2
        new_freqs[v] = 2
        new_freqs[v + 1] += extras
        if v + 1 not in freqs:
            heappush(vals, v + 1)

    if all(cnt % 2 == 0 for cnt in new_freqs.values()):
        write_str('YES')
    else:
        write_str('NO')


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
