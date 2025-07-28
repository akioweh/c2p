def mex(arr, lo, hi, target):
    for i in range(lo, hi):
        if arr[i] != target:
            return True
    return False



def solve():
    N, K = read_ints()
    arr = list(read_ints())
    cur_ans = 1
    pt = 2
    while pt <= K:
        lo, hi = pt - 1, N - (K - pt)
        if lo + 1 == hi:
            if arr[lo] != cur_ans:
                write_int(cur_ans)
                return
        else:
            if mex(arr, lo, hi, cur_ans):
                write_int(cur_ans)
                return
            else:
                write_int(cur_ans + 1)
                return
        cur_ans += 1
        pt += 2
    write_int(K // 2 + 1)


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
