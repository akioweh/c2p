def query(i, j) -> int:
    tmp = int(prompt(f'? {i} {j}'))
    return tmp


def solve():
    N = read_int()
    x_s = list(read_ints())
    _xs = set(x_s)

    if len(_xs) == N:  # no missing number
        u = x_s.index(1) + 1
        v = x_s.index(N) + 1
        res1 = query(u, v)
        res2 = query(v, u)
        if res1 == res2 >= N - 1:
            write_str('! B')
        else:
            write_str('! A')
    else:  # at least one vertex with outdegree 0
        for v in range(1, N + 1):
            if v not in _xs:
                u = _xs.pop()
                if query(v, u):
                    write_str('! B')
                else:
                    write_str('! A')
                break
    stdout.flush()


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
