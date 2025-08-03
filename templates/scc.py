def kosaraju(graph: list[list[int]]) -> tuple[list[list[int]], list[int]]:
    """Returns SCCs in topological order (of the condensation graph)
    and an array mapping vertices to their SCCs.
    """
    n = len(graph)

    # iterative to avoid recursion (PyPy issue :( )
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
