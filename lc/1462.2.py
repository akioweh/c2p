from collections import defaultdict, deque
from itertools import filterfalse


def trans_closure(n_V: int, edges: list[tuple[int, int]]) -> list[int]:
    # first, build graph (adjacency list), inverse-graph, and count in-degrees
    graph = defaultdict(list)
    inv_graph = defaultdict(list)  # for use in reverse traversal
    in_degree = defaultdict(int)  # for use in topological sort
    for u, v in edges:  # O(E)
        graph[u].append(v)
        inv_graph[v].append(u)
        in_degree[v] += 1

    # second, topologically sort
    q = deque(filterfalse(in_degree.__getitem__, graph))
    topo_order = []
    while q:  # O(E)
        u = q.popleft()
        topo_order.append(u)
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                q.append(v)

    # third, calculate the transitive closure (DP algorithm)
    res_tc = [0] * n_V  # rows are represented as bitsets
    for v in reversed(topo_order):  # O(E)
        res_tc[v] |= 1 << v
        for u in inv_graph[v]:
            res_tc[u] |= res_tc[v]

    return res_tc


class Solution:
    def checkIfPrerequisite(
            self,
            numCourses: int,
            prerequisites: list[tuple[int, int]],
            queries: list[list[int]]
    ) -> list[bool]:

        tc = trans_closure(numCourses, prerequisites)  # O(E)
        return [tc[u] & 1 << v != 0 for u, v in queries]  # O(Q)
