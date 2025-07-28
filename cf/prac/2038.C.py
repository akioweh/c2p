def solve():
    N = read_int()
    arr = list(read_ints())
    arr.sort()
    # x1 = x4; x2 = x3
    # y1 = y2; y3 = y4
    # (x2, y2) = (x3, y1)
    # etc.
    # area = (x2 - x1) * (y2 - y3)

    # 2x of (n1, n2, n3, n4)
    # say, n1 <= n2 <= n3 <= n4,
    # area = (n4 - n2) * (n3 - n1)
    # or other formations of the product of two differences

    # obviously, n1 and n2 would be the two smallest numbers in arr
    # and n3 and n4 would be the two largest numbers in arr
    # (note that ns have to each appear at least twice in arr)
    # and that they do NOT have to be unique

    l, r = 0, N - 1
    # find n1
    while l < r - 6:
        if arr[l] == arr[l + 1]:
            n1 = arr[l]
            l += 2
            break
        l += 1
    else:  # impossible
        write_str('NO')
        return
    # find n2
    while l < r - 4:
        if arr[l] == arr[l + 1]:
            n2 = arr[l]
            l += 2
            break
        l += 1
    else:  # impossible
        write_str('NO')
        return
    # find n3
    while l < r - 2:
        if arr[r] == arr[r - 1]:
            n3 = arr[r]
            r -= 2
            break
        r -= 1
    else:  # impossible
        write_str('NO')
        return
    # find n4
    while l < r:
        if arr[r] == arr[r - 1]:
            n4 = arr[r]
            r -= 2
            break
        r -= 1
    else:  # impossible
        write_str('NO')
        return
    write_str('YES')
    arrangement_1 = (n3 - n1) * (n4 - n2)
    arrangement_2 = (n4 - n1) * (n3 - n2)
    if arrangement_1 >= arrangement_2:
        write_ints((
            n1, n2,
            n3, n2,
            n3, n4,
            n1, n4,
        ))
    else:
        write_ints((
            n2, n1,
            n3, n1,
            n3, n4,
            n2, n4,
        ))


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
