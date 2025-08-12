from collections import defaultdict, deque
# from sys import setrecursionlimit

# setrecursionlimit(700000)


def iso(graph: list[list[int]], roots: list[int]) -> bool:
    n = len(graph)
    lvl = [-1] * n
    levels: list[list[int]] = []
    par = [-1] * n

    def calc_height(_r: int) -> int:
        q = deque([_r])
        lvl[_r] = 0
        res = 0
        while q:
            u = q.popleft()
            d = lvl[u]
            p = par[u]
            if len(levels) == d:
                levels.append([])
            levels[d].append(u)
            res = max(res, d)
            for v in graph[u]:
                if v == p:
                    continue
                par[v] = u
                lvl[v] = d + 1
                q.append(v)
        return res + 1

    heights = (calc_height(r) for r in roots)
    h = next(heights)
    if not all(_h == h for _h in heights):
        return False

    v_hash = [0] * n  # default hash for leaves is 0
    for l in reversed(range(h - 1)):
        prev_lvl = levels[l + 1]
        cur_lvl = levels[l]
        children = defaultdict(list)
        for u in prev_lvl:
            children[par[u]].append(v_hash[u])
        # re-hash
        cur_lvl.sort(key=children.__getitem__)  # children's sortedness is inherited from cur_lvl
        idx = 0
        prev = children[cur_lvl[0]]
        for v in cur_lvl:
            if (cur := children[v]) != prev:
                idx += 1
                prev = cur
            v_hash[v] = idx

    return len(set(v_hash[r] for r in roots)) == 1


def solve():
    V, E = read_ints()
    graph = [[] for _ in range(V)]
    for _ in range(E):
        u, v = read_ints()
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    if E == V - 1:
        # trivial: is a tree
        write_str('YES')
        return
    if E > V:
        # if there exits any minimal-cut-set(?) (bond?) containing > 2 edges,
        # then clearly the three possible STs cannot be isomorphic
        write_str('NO')
        return

    # one cycle, find it
    visited = [False] * V
    visited[0] = True
    parent = [-1] * V
    start = end = -1
    stack = [(0, 0)]
    while stack:
        u, idx = stack[-1]
        if idx == len(graph[u]):
            stack.pop()
            continue
        v = graph[u][idx]
        stack[-1] = (u, idx + 1)
        if v == parent[u]:
            continue
        if visited[v]:
            start, end = v, u
            break
        visited[v] = True
        parent[v] = u
        stack.append((v, 0))

    cycle = [start]
    v = end
    while v != start:
        cycle.append(v)
        v = parent[v]
    cycle.append(start)

    # break into trees
    for u, v in zip(cycle, cycle[1:]):
        graph[u].remove(v)
        graph[v].remove(u)

    # bruh
    if len(cycle) % 2:
        cycle.pop()

    if iso(graph, cycle[::2]) and iso(graph, cycle[1::2]):
        write_str('YES')
    else:
        write_str('NO')


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


# N-Testcases format
if __name__ == '__main__':
    for _ in range(read_int()):
        solve()
