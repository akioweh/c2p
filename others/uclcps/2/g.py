from collections import deque
from sys import maxsize


def solve():
    N, M = read_ints()
    maze = [
        read_str()
        for _ in range(N)
    ]
    start_dir = {
        'U': 0,
        'R': 1,
        'D': 2,
        'L': 3,
    }[read_str()]

    # find start, 'S', and end, 'E'
    start: tuple[int, int] = None
    end: tuple[int, int] = None
    for i, r in enumerate(maze):
        if not start and (j := r.find('S')) != -1:
            start = (i, j)
        if not end and (j := r.find('E')) != -1:
            end = (i, j)
        if start and end:
            break

    dist = [
        [
            [maxsize] * 4
            for _ in range(M)
        ]
        for _ in range(N)
    ]
    dist[start[0]][start[1]][start_dir] = 0

    # bfs shortest path
    # can: 1. move forward, 2. move forward then turn right

    q = deque([(start[0], start[1], start_dir)])
    while q:
        i, j, dir_ = q.popleft()
        d = dist[i][j][dir_]
        if (i, j) == end:
            write_int(d)
            return

        i += (-1, 0, 1, 0)[dir_]
        j += (0, 1, 0, -1)[dir_]
        if maze[i][j] == '#':
            continue
        if dist[i][j][dir_] == maxsize:
            dist[i][j][dir_] = d + 1
            q.append((i, j, dir_))
        dir_ = (dir_ + 1) % 4
        if dist[i][j][dir_] == maxsize:
            dist[i][j][dir_] = d + 1
            q.append((i, j, dir_))

    write_int(-1)


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
