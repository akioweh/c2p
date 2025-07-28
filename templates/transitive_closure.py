from collections import defaultdict, deque
from itertools import filterfalse


def trans_closure_dag_bitset(graph: dict[int, list[int]]) -> list[int]:
    # first, topologically sort the graph, O(V + E)
    in_degree = defaultdict(int)
    inv_graph = defaultdict(list)  # for use in reverse traversal
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1
            inv_graph[v].append(u)
    q = deque(filterfalse(in_degree.__getitem__, graph))
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    # then, we iterate in reverse topological order
    # and update the transitive closure from the inverted adjacency list
    # O(E)... not O(V * E) due to the bitset representation
    n_V = len(graph)
    res_tc = [0] * n_V  # rows are represented as bitsets
    for v in reversed(topo_order):
        res_tc[v] |= 1 << v
        for u in inv_graph[v]:
            res_tc[u] |= res_tc[v]

    # at this point, conversion from bitset back to matrix
    # would take O(V^2)... so we dont.
    return res_tc


def trans_closure_dag(graph: dict[int, list[int]]) -> list[list[bool]]:
    temp_tc = trans_closure_dag_bitset(graph)
    n_V = len(graph)
    return [
        [
            bool(int(d))
            for d in bin(u)[2:].zfill(n_V)
        ] for u in temp_tc
    ]


def trans_closure_dag_edges_bitset(n_V: int, edges: list[tuple[int, int]]) -> list[int]:
    graph = defaultdict(list)
    inv_graph = defaultdict(list)
    in_degree = defaultdict(int)
    for u, v in edges:
        graph[u].append(v)
        inv_graph[v].append(u)
        in_degree[v] += 1

    q = deque(filterfalse(in_degree.__getitem__, graph))
    topo_order = []
    while q:
        u = q.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    res_tc = [0] * n_V  # rows are represented as bitsets
    for v in reversed(topo_order):
        res_tc[v] |= 1 << v
        for u in inv_graph[v]:
            res_tc[u] |= res_tc[v]

    return res_tc
