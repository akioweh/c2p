from collections import defaultdict

MAX = 10


def solve():
    N = read_int()
    cols: dict[int, list[int]] = defaultdict(list)
    bottom_row: list[int] = []
    for _ in range(N):
        x_, y_ = read_ints()
        if y_ == 1:
            bottom_row.append(x_)
        else:
            cols[x_].append(y_)

    xs = list(cols)
    xs.sort()

    res = []
    for x in xs:
        if res and res[-1][0] == x:
            res.pop()
        if x == MAX:
            break
        ys = cols[x]
        ys.sort()
        if ys[0] != 2:
            res.append((x, 2))
        res.extend((x, y) for y in ys)
        if ys[-1] != 2:
            res.append((x + 1, 2))

    if not xs:
        res.append((420, 2))
    elif xs[-1] == MAX:
        if not res or res[-1][0] != MAX - 1:
            res.append((MAX - 1, 2))
        ys = cols[MAX]
        ys.sort(reverse=True)
        res.extend((MAX, y) for y in ys)
        if ys[-1] != 2:
            res.append((MAX, 2))

    bottom_row.sort(reverse=True)
    res.extend((x, 1) for x in bottom_row)
    if not bottom_row:
        last_x, last_y = res[-1]
        if last_x not in cols or (last_y not in (cols[last_x][0], cols[last_x][-1])):
            res[-1] = (last_x, 1)
        else:
            res.append((69, 1))

    write_int(len(res))
    for p in res:
        write_ints(p)


### Python 3.8-3.13 compatible competitive programming template ###
# 4 Mar 2025 Version
from sys import stdin, stdout
from typing import Callable, Iterable, Iterator, Type

srdl = stdin.readline
swrt = stdout.write


def read_ints(int_t: Type[int] = int) -> Iterator[int]:
    """Reads a line as space-separated integers"""
    return map(int_t, srdl().split())


def read_int(int_t: Type[int] = int) -> int:
    """Reads a line as a single integer"""
    return int_t(srdl())


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


def prompt(msg: str, prefix: str = '? ', reader: Callable = read_str) -> str:
    """Writes a string as a line and reads a line. Flushes output buffer.
    Prepends a default prefix to output."""
    swrt(prefix)
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return reader()


# Single-case format
if __name__ == '__main__':
    solve()
