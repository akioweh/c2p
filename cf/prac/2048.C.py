def solve():
    s = read_str()
    N = len(s)
    v = int(s, 2)
    if v.bit_length() == v.bit_count():
        print(1, N, 1, 1)
        return
    target = bin((1 << v.bit_length()) - 1 - v)[2:]
    M = len(target)
    max_match_len = 0
    max_match_l = 0
    for l in range(N - M):
        for match_len in range(M):
            if target[match_len] != s[l + match_len]:
                if match_len > max_match_len:
                    max_match_len = match_len
                    max_match_l = l
                break
        else:
            max_match_len = M
            max_match_l = l
            break

    print(1, N, max_match_l + 1, max_match_l + M)


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
