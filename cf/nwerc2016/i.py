def bfs(graph: list[list[int]], starts: list[int]) -> list[int]:
    n = len(graph)
    q = starts
    dist = [10**8] * n
    for v in q:
        dist[v] = 0
    cur_dist = 1
    while q:
        new_q = []
        for u in q:
            for v in graph[u]:
                if dist[v] != 10**8:
                    continue
                new_q.append(v)
                dist[v] = cur_dist
        q = new_q
        cur_dist += 1

    return dist


def solve():
    N, IRON, COAL = read_ints()
    irons = [v - 1 for v in read_ints()]
    coals = [v - 1 for v in read_ints()]
    graph = [[] for _ in range(N)]
    inv_g = [[] for _ in range(N)]
    for u in range(N):
        it = read_ints()
        next(it)
        for v in it:
            v -= 1
            graph[u].append(v)
            inv_g[v].append(u)

    dist_to_iron = bfs(inv_g, irons)
    dist_to_coal = bfs(inv_g, coals)
    dist = bfs(graph, [0])

    ans = min(map(sum, zip(dist_to_iron, dist_to_coal, dist)))

    if ans >= 10**8:
        write_str('impossible')
    else:
        write_int(ans)


### Python 3.10-3.13 compatible competitive programming template ###
# 23 July 2025 Version
from collections.abc import Callable, Iterable, Iterator
from sys import stdin, stdout
from typing import TypeVar

T = TypeVar('T')

srdl = stdin.readline
swrt = stdout.write


def read_ints(int_t: type[int] = int) -> Iterator[int]:
    """Reads a line as space-separated integers"""
    return map(int_t, srdl().split())


def read_int(int_t: type[int] = int) -> int:
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


def prompt(msg: str, prefix: str = '? ', reader: Callable[[], T] = read_str) -> T:  # type: ignore[assignment]
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
