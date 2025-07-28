from collections import Counter, defaultdict, deque


def solve():
    V, E, L = read_ints()
    nums = list(read_ints())

    _graph = defaultdict(list)
    for _ in range(E):
        u, v = read_ints()
        _graph[u].append(v)
        _graph[v].append(u)

    # odd-even reachability
    # -v -> odd
    # +v -> even
    graph = defaultdict(list)
    for u in _graph:
        for v in _graph[u]:
            graph[-u].append(v)
            graph[v].append(-u)

    dist = defaultdict(lambda: 1 << 31)
    dist[1] = 0
    q = deque([1])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if dist[u] + 1 < dist[v]:
                dist[v] = dist[u] + 1
                q.append(v)

    ans = []
    max_dist = sum(nums)
    has_odd = False
    min_odd = max_dist + 69
    for n in sorted(nums):
        if n % 2 and not has_odd:
            has_odd = True
            min_odd = n
    max_even = max_dist - min_odd if max_dist % 2 else max_dist
    max_odd = max_dist if max_dist % 2 else max_dist - min_odd

    for dest in range(1, V + 1):
        if min(dist[dest], dist[-dest]) > max_dist:
            ans.append('0')
            continue
        if max_even >= 0 and dist[dest] <= max_even:
            ans.append('1')
            continue
        if max_odd >= 0 and dist[-dest] <= max_odd:
            ans.append('1')
            continue
        ans.append('0')

    write_str(''.join(ans))


### Python 3.8-3.13 compatible competitive programming template ###
# 11 Mar 2025 Version
from sys import stdin, stdout
from typing import Callable, Iterable, Iterator, Type, TypeVar

T = TypeVar('T')

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


def prompt(msg: str, prefix: str = '? ', reader: Callable[[], T] = read_str) -> T:
    """Writes a string as a line and reads a line. Flushes output buffer.
    Prepends a default prefix to output."""
    swrt(prefix)
    swrt(msg)
    swrt('\n')
    stdout.flush()
    return reader()


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
