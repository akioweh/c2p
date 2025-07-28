"""
1462. Course Schedule IV
"""

from typing import Optional


class STNode:
    __slots__ = ('v', 'parent', 'children')

    def __init__(self, v: int):
        self.v = v
        self.parent = None
        self.children = []

    def add_child(self, child: 'STNode'):
        self.children.append(child)
        child.parent = self

    def __iter__(self):
        yield self.v
        for child in self.children:
            yield from child

    def __index__(self):
        return self.v

    def __eq__(self, other):
        return self.v == int(other)


class DGPS:
    def __init__(self, n: int):
        # dgps[u][v] is a pointer to
        # v in the descendant tree of u,
        # or None if v is not reachable from u
        self.dgps: list[list[Optional[STNode]]] = [
            [None] * n
            for _ in range(n)
        ]
        for i in range(n):
            self.dgps[i][i] = STNode(i)

    def _update_st(self, x: int, j: int, u: int, v: int):
        new_node = STNode(v)
        self.dgps[x][v] = new_node
        self.dgps[x][u].add_child(new_node)
        subtree = self.dgps[j][v]
        if subtree is not None:
            for w in subtree:
                if self.dgps[x][w] is None:
                    self._update_st(x, j, v, w)

    def add(self, u: int, v: int):
        if self.dgps[u][v] is not None:
            return
        for i, desc in enumerate(self.dgps):
            if desc[u] is not None and desc[v] is None:
                self._update_st(i, v, u, v)


class Solution:
    def checkIfPrerequisite(
            self,
            numCourses: int,
            prerequisites: list[list[int]],
            queries: list[list[int]]
    ) -> list[bool]:
        dgps = DGPS(numCourses)
        for u, v in prerequisites:
            dgps.add(u, v)

        return [
            dgps.dgps[u][v] is not None
            for u, v in queries
        ]
