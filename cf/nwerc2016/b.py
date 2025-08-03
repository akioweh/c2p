def kosaraju(graph: list[list[int]]):
    n = len(graph)

    def rev_topo(_u: int):
        stack = [(_u, 0)]
        while stack:
            _u, _i = stack[-1]
            visited[_u] = True
            if _i < len(graph[_u]):
                _v = graph[_u][_i]
                stack[-1] = (_u, _i + 1)
                if not visited[_v]:
                    stack.append((_v, 0))
            else:
                v_topo.append(_u)
                stack.pop()

    visited = [False] * n
    v_topo: list[int] = []
    for i in range(n):
        if visited[i]:
            continue
        rev_topo(i)
    v_topo.reverse()

    inv_g: list[list[int]] = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            inv_g[v].append(u)

    def find(_src: int):
        _res = []
        _stack = [_src]
        while _stack:
            _u = _stack.pop()
            if visited[_u]:
                continue
            visited[_u] = True
            _res.append(_u)
            for _v in inv_g[_u]:
                if visited[_v]:
                    continue
                _stack.append(_v)
        return _res

    sccs: list[list[int]] = []
    idx_scc = [n] * n
    visited = [False] * n
    for u in v_topo:
        if visited[u]:
            continue
        scc = find(u)
        idx = len(sccs)
        sccs.append(scc)
        for v in scc:
            idx_scc[v] = idx

    return sccs, idx_scc


def calc_the_thing(scc_idx: int, scc: list[int], graph: list[list[int]], idx_scc: list[int]):
    k = len(scc)
    cv_idx = {v: i for i, v in enumerate(scc)}
    visited = [False] * k
    dist = [[0] * k for _ in range(k)]
    for cu in range(k):
        dist[cu][cu] = 1

    def dfs(_cu: int, path_len: int, _src: int):
        dist[_src][_cu] = max(dist[_src][_cu], path_len)
        _u = scc[_cu]
        for _v in graph[_u]:
            if idx_scc[_v] != scc_idx:
                continue
            _cv = cv_idx[_v]
            if visited[_cv]:
                continue
            visited[_cv] = True
            dfs(_cv, path_len + 1, _src)
            visited[_cv] = False

    for cu in range(k):
        visited[cu] = True
        dfs(cu, 1, cu)
        visited[cu] = False

    return dist


def solve():
    V, E = read_ints()
    graph = [[] for _ in range(V)]
    for _ in range(E):
        a, b = read_ints()
        a -= 1
        b -= 1
        graph[a].append(b)

    sccs, idx_scc = kosaraju(graph)

    dp = [1] * V  # dp[v] = longest simple path ending at v

    # intra scc longest simple paths
    sccs_dist = [calc_the_thing(scc_i, scc, graph, idx_scc) for scc_i, scc in enumerate(sccs)]

    for scc_i, scc in enumerate(sccs):
        cdist = sccs_dist[scc_i]
        k = len(scc)

        # try to augment intra scc values
        temp_dp = [0] * k
        for cv in range(k):
            temp_dp[cv] = max(dp[u] + cdist[cu][cv] - 1 for cu, u in enumerate(scc))
        for cv, v in enumerate(scc):
            dp[v] = max(dp[v], temp_dp[cv])

        # push to adj sccs
        for u in scc:
            for v in graph[u]:
                if idx_scc[v] == scc_i:
                    continue
                dp[v] = max(dp[v], dp[u] + 1)

    write_int(max(dp))


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
