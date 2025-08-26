from typing import Optional, SupportsIndex


class STNode:
    """Spanning Tree Node, for use in DGPS"""

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

    def __eq__(self, other: SupportsIndex):
        return self.v == int(other)

    def __repr__(self):
        return str(self.v)


class DGPS:
    """Directed Graph Path Search
    (and Transitive Closure) Algorithm

    Implementation of https://doi.org/10.1016/0304-3975(86)90098-8

    This data structure incrementally calculates
    the transitive closure of a directed (possible cyclic)
    graph and is optimized for querying.
    It also keeps track of an arbitrary path between
    all pairs of connected vertices, avaiable for querying.

    Deletion is not supported.

    Complexity:
      - Reachability query: O(1)
      - Path query: O(k), for a path of length k
      - Insertion, edge: O(|V|) amortized
      - Space: O(|V|^2) upper bound

    I.e. it is of O(|V| * |E|) = O(|V|^3) to construct from scratch.
    (Since |E| <= |V|^2)

    """

    __slots__ = ('dgps',)

    def __init__(self, n: int):
        # dgps[u][v] is a reference to
        # v in the descendant tree of u,
        # or None if v is not reachable from u
        self.dgps: list[list[Optional[STNode]]] = [
            [None] * n
            for _ in range(n)
        ]
        for i in range(n):  # initial state: self-reachability
            self.dgps[i][i] = STNode(i)

    def reachable(self, u: int, v: int) -> bool:
        return self.dgps[u][v] is not None

    def search_path(self, u: int, v: int) -> list[int]:
        """Returns a path from u to v.

        If v is reachable from u, returns a sequence of adjacent
        vertices starting from u and ending at v.
        Otherwise, returns an empty list.
        """
        p = self.dgps[u][v]
        if p is None:
            return []
        res = [p]
        while p != u:
            p = p.parent
            res.append(p)
        res.reverse()
        return res

    def _update_st(self, x: int, t: int, u: int, v: int):
        """Internal. Update the descentant trees when there's an update
        in the transitive closure.
        """
        new_node = STNode(v)
        desc_x = self.dgps[x]
        desc_x[v] = new_node
        desc_x[u].add_child(new_node)
        subtree = self.dgps[t][v]
        if subtree is not None:
            for w in subtree:
                if desc_x[w] is None:
                    self._update_st(x, t, v, w)

    def add(self, u: int, v: int):
        """Add an edge u -> v"""
        if self.dgps[u][v] is not None:
            return
        for i, desc_i in enumerate(self.dgps):
            if desc_i[u] is not None and desc_i[v] is None:
                self._update_st(i, v, u, v)
