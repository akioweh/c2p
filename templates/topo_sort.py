from collections import defaultdict, deque
from itertools import filterfalse


def topo_sort_kahn(graph: dict[int, list[int]]) -> list[int]:
    """Kahn's Topological Sort Algorithm,
    (de)queue-based implementation.

    Assumes the graph a DAG.
    """
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # we only need a regular queue,
    # but the stdlib queue is a deque
    q = deque(filterfalse(in_degree.__getitem__, graph))
    res = []
    while q:
        u = q.popleft()
        res.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    return res


def topo_sort_dfs(graph: dict[int, list[int]], source: int) -> list[int]:
    """Generalized Topological Sort,
    the reverse post-order DFS traversal.
    """

    visited = set()
    res = []

    def dfs(_u: int):
        visited.add(_u)
        for v in graph[_u]:
            if v not in visited:
                dfs(v)
        res.append(_u)

    dfs(source)

    res.reverse()
    return res


def unique_topo(graph: dict[int, list[int]]) -> bool:
    """Checks whether the topological sort of a DAG is unique.

    I.e., Hamiltonian Path check (a path that traverses all vertices exactly once).
    """
    in_degree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    tmp = filterfalse(in_degree.__getitem__, graph)
    u = next(tmp, None)
    if next(tmp, None):
        return False
    for _ in range(len(graph) - 1):
        if not u:
            return False
        next_u = None
        for v in graph[u]:
            in_degree[v] -= 1
            if not in_degree[v]:
                if next_u:
                    return False
                next_u = v
        u = next_u

    return True
