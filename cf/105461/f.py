from sys import maxsize


def solve():
    N = read_int()
    s = read_ints()
    r_states: dict[int, int] = {maxsize: 0}  # {r_lim: min_penalty}
    l_lim = maxsize
    for si in s:
        # case where we slow down fast lane
        if si > l_lim:
            tmp = min(
                pen
                for r_lim, pen in r_states.items()
                if r_lim > si
            )
            r_states[si] = min(r_states.get(si, maxsize), tmp)
        # cases where we do NOT slow down either lane
        for r_lim in r_states:
            if si >= r_lim:  # go fast lane
                r_states[r_lim] += si - r_lim
            else:  # go slow lane
                if si >= l_lim:
                    r_states[r_lim] += si - l_lim
        # case where we slow down slow lane
        if si < l_lim:
            l_lim = si

    write_int(min(r_states.values()))


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
