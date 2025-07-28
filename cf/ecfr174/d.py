from collections import Counter


def solve():
    s = read_str()
    N = len(s)
    for i in range(N // 2):
        if s[i] != s[N - i - 1]:
            break
    else:
        write_int(0)
        return

    for j in range(N // 2 - 1, -1, -1):
        if s[j] != s[N - j - 1]:
            break
    else:
        raise RuntimeError('balls')

    if Counter(s[i:j + 1]) == Counter(s[N - j - 1:N - i]):
        write_int(j - i + 1)
        return

    l_freqs = Counter(s[i:(N + 1) // 2])
    r_freqs = Counter(s[N // 2:N - i])
    tmp = l_freqs.copy()
    l_freqs.subtract(r_freqs)
    r_freqs.subtract(tmp)
    l_freqs = {k : v for k, v in l_freqs.items() if v < 0}
    r_freqs = {k : v for k, v in r_freqs.items() if v < 0}
    for k in range(N // 2, N - i):
        cur_l, cur_r = s[k], s[N - k - 1]
        if cur_l in l_freqs:
            l_freqs[cur_l] += 2
            if l_freqs[cur_l] >= 0:
                del l_freqs[cur_l]
        if cur_r in r_freqs:
            r_freqs[cur_r] += 2
            if r_freqs[cur_r] >= 0:
                del r_freqs[cur_r]

        if not l_freqs or not r_freqs:
            write_int(k - i + 1)
            return

    write_int(N - 2 * i)


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
