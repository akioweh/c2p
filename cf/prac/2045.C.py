def solve():
    s = read_str()
    t = read_str()
    S, T = len(s), len(t)
    if S <= 1 or T <= 1:
        print(-1)
        return

    s_first_appearance = {}
    t_last_appearance = {}
    it = iter(enumerate(s))
    next(it)
    for i, c in it:
        if c not in s_first_appearance:
            s_first_appearance[c] = i

    it = iter(enumerate(reversed(t)))
    next(it)
    for i, c in it:
        if c not in t_last_appearance:
            t_last_appearance[c] = i

    min_len = S + T
    min_c = None
    for c in s_first_appearance:
        if c not in t_last_appearance:
            continue
        l = s_first_appearance[c] + t_last_appearance[c]
        if l < min_len:
            min_len = l
            min_c = c

    if min_c is None:
        print(-1)
    else:
        s_i = s_first_appearance[min_c]
        t_i = T - t_last_appearance[min_c] - 1
        print(s[:s_i] + t[t_i:])


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


# Single-case format
if __name__ == '__main__':
    solve()
