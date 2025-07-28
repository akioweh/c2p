def solve():
    N = read_int()
    nums = list(read_ints())

    # monotonic increasing stack
    stack = []
    idxs_stack = []
    smallest_moved = 10 ** 9 + 1
    for i, num in enumerate(nums):
        while stack and stack[-1] > num:
            smallest_moved = min(smallest_moved, stack.pop())
            idxs_stack.pop()
        stack.append(num)
        idxs_stack.append(i)
    smallest_moved += 1

    idxs_stack.reverse()
    for i in range(N):
        if i == idxs_stack[-1] and nums[i] <= smallest_moved:
            idxs_stack.pop()
            continue
        nums[i] += 1

    nums.sort()
    write_ints(nums)


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
