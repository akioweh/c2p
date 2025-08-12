from collections import defaultdict, deque
from itertools import filterfalse


def topo_sort_kahn(graph: dict[int, list[int]]) -> list[int]:
    """Kahn's Topological Sort Algorithm,
    (de)queue-based implementation.

    Assumes the graph is acyclic.
    """
    in_degree: dict[int, int] = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

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
    aka. reverse post-order.

    Graph may be cyclic.
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


def topo_unique(graph: dict[int, list[int]]) -> bool:
    """Checks whether the topological sort of a DAG is unique.

    I.e., the existence of a Hamiltonian Path
    """
    in_degree: dict[int, int] = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    tmp = filterfalse(in_degree.__getitem__, graph)
    cur = next(tmp, None)
    if next(tmp, None) is not None:
        return False
    for _ in range(len(graph) - 1):
        if cur is None:
            return False
        next_u = None
        for v in graph[cur]:
            in_degree[v] -= 1
            if not in_degree[v]:
                if next_u is not None:
                    return False
                next_u = v
        cur = next_u

    return True
