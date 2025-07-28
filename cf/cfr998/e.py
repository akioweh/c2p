from collections import defaultdict
from sys import stdin
from typing import Iterable


# noinspection PyShadowingBuiltins
input = stdin.readline


def read_ints() -> Iterable[int]:
    return map(int, input().split())


def connected_components(graph):
    # returns list of components with more than one vertex
    visited = [False] * (N + 1)
    components = []
    for u_ in graph:
        if visited[u_]:
            continue
        cur = set()
        stack = [u_]
        while stack:
            v_ = stack.pop()
            if visited[v_]:
                continue
            visited[v_] = True
            cur.add(v_)
            stack.extend(graph[v_])
        assert len(cur) > 1
        components.append(cur)
    return components


def count_components(graph):
    # count number of connected components, including single-vertex components
    visited = [False] * (N + 1)
    n_components = 0
    for u_ in graph:
        if visited[u_]:
            continue
        n_components += 1
        stack = [u_]
        while stack:
            v_ = stack.pop()
            if visited[v_]:
                continue
            visited[v_] = True
            stack.extend(graph[v_])
    return n_components + (N - sum(visited))


T = int(input())

for _ in range(T):
    N, M1, M2 = read_ints()

    F = defaultdict(set)
    G = defaultdict(list)

    for _ in range(M1):
        u, v = read_ints()
        F[u].add(v)
        F[v].add(u)

    for _ in range(M2):
        u, v = read_ints()
        G[u].append(v)
        G[v].append(u)

    ops = 0

    G_components = connected_components(G)
    vertex_idx = {
        v: i
        for i, component in enumerate(G_components)
        for v in component
    }
    to_remove_outer = []
    for u in F:
        if u not in vertex_idx:
            to_remove_outer.append(u)
            ops += len(F[u])
            continue
        u_id = vertex_idx[u]
        to_remove = []
        for v in F[u]:
            if vertex_idx.get(v, -1) != u_id:
                to_remove.append(v)
                ops += 1
        F[u].difference_update(to_remove)
    for u in to_remove_outer:
        del F[u]

    ops //= 2  # each edge is counted twice

    n_components_g = len(G_components) + (N - sum(map(len, G_components)))
    ops += count_components(F) - n_components_g

    print(ops)
