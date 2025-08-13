"""
iterative implementations
of common recursive stuff
"""


def preorder(graph: list[list[int]], u: int) -> list[int]:
    n = len(graph)
    visited = [False] * n
    res = []
    stack = [u]
    while stack:
        u = stack.pop()
        if visited[u]:
            continue
        visited[u] = True
        res.append(u)
        for v in graph[u]:  # or reversed(graph[u])
            if visited[v]:
                continue
            stack.append(v)
    return res


def postorder(graph: list[list[int]], u: int) -> list[int]:
    n = len(graph)
    visited = [False] * n
    res = []
    stack = [(u, 0)]
    visited[u] = True
    while stack:
        u, idx = stack[-1]
        if idx == len(graph[u]):
            stack.pop()
            res.append(u)
            continue
        v = graph[u][idx]
        stack[-1] = (u, idx + 1)
        if visited[v]:
            continue
        visited[u] = True
        stack.append((v, 0))
    return res


def both_order(graph: list[list[int]], start: int) -> tuple[list[int], list[int]]:
    n = len(graph)
    visited = [False] * n
    preorder = []
    postorder = []
    stack = [(start, 0)]
    visited[start] = True
    while stack:
        u, idx = stack[-1]
        if idx == 0:
            preorder.append(u)  # preorder
        if idx == len(graph[u]):
            postorder.append(u)  # postorder
            stack.pop()
            continue
        v = graph[u][idx]
        stack[-1] = (u, idx + 1)
        if not visited[v]:
            visited[v] = True
            stack.append((v, 0))

    return preorder, postorder


def find_cycle(graph: list[list[int]]) -> list[int]:
    """Finds a cycle in an undirected graph"""
    n = len(graph)
    visited = [False] * n
    parent = [-1] * n
    start = end = -1
    stack = [(0, 0)]
    visited[0] = True
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

    if start == -1:
        return []

    cycle = [start]
    v = end
    while v != start:
        cycle.append(v)
        v = parent[v]
    return cycle


def dist_bfs(graph: list[list[int]], roots: list[int]) -> list[int]:
    n = len(graph)
    dist = [-1] * n
    for v in roots:
        dist[v] = 0
    q = roots
    cur_dist = 1
    while q:
        new_q = []
        for u in q:
            for v in graph[u]:
                if dist[v] != -1:
                    continue
                new_q.append(v)
                dist[v] = cur_dist
        q = new_q
        cur_dist += 1

    return dist


def topo_sort(graph: list[list[int]]):
    """Generalized Topological Sort,
    iterative implementation.
    """
    n = len(graph)
    visited = [False] * n
    res: list[int] = []

    def rev_topo(u: int):
        stack = [(u, 0)]
        while stack:
            u, idx = stack[-1]
            visited[u] = True
            if idx == len(graph[u]):
                stack.pop()
                res.append(u)
                continue
            v = graph[u][idx]
            stack[-1] = (u, idx + 1)
            if not visited[v]:
                stack.append((v, 0))

    for i in range(n):
        if visited[i]:
            continue
        rev_topo(i)
    res.reverse()
    return res
