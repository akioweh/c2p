from fractions import Fraction


def solve():
    N, C, P, Q = read_ints()
    S = list(map(lambda x: x == 'Y', read_str()))
    S.append(False)
    req = Fraction(P, Q)
    if C > N:
        write_int(0)
        return

    cur_ratio = Fraction(sum(S[:C]), C)
    l, r = 0, C - 1
    rank = 0
    while r < N:
        if cur_ratio >= req:
            rank += 1
            l = r + 1
            r = l + C - 1
            cur_ratio = Fraction(sum(S[l:r + 1]), C)
            continue
        r += 1
        if S[r]:
            if S[l]:
                l += 1
            else:
                while r - l + 1 >= C and not S[l]:
                    l += 1
                    cur_ratio += Fraction(1, cur_ratio.denominator)
        else:
            if S[l]:
                cur_ratio = Fraction(cur_ratio.numerator, cur_ratio.denominator + 1)
            else:
                l += 1

    write_int(rank)


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
