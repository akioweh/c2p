def solve():
    N, _ = read_ints()
    n_s = list(read_ints())
    m = read_int()
    n2_s = [m - n for n in n_s]
    prev = min(n_s[0], n2_s[0])
    for i in range(1, N):
        a, b = n_s[i], n2_s[i]
        a_ok, b_ok = a >= prev, b >= prev
        if not a_ok and not b_ok:
            write_str('NO')
            return
        if a_ok and b_ok:
            prev = min(a, b)
        elif a_ok:
            prev = a
        else:
            prev = b
    write_str('YES')


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
