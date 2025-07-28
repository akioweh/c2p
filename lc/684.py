"""
684. Redundant Connection
"""


class DisjointSet:
    __slots__ = ('parent', 'size', 'len')

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n
        self.len = n

    def find(self, x: int) -> int:
        # Here we use a better Path Splitting algorithm
        # by Tarjan / Van Leeuwen
        # instead of the standard recursive implementation.
        # This uses O(1) space and has a better practical runtime
        # ... and, of course, is not recursive!
        parent_of = self.parent
        while parent_of[x] != x:
            x, parent_of[x] = parent_of[x], parent_of[parent_of[x]]
        return x

    def union(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False

        if self.size[x] < self.size[y]:
            x, y = y, x

        self.parent[y] = x
        self.size[x] += self.size[y]
        self.len -= 1
        return True

    def same(self, *args: int) -> bool:
        # returns True for 0 or 1 arguments
        roots = map(self.find, args)
        r0 = next(roots, None)
        return all(r == r0 for r in roots)

    def __len__(self) -> int:
        return self.len


class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        dsu = DisjointSet(len(edges))
        ans = None
        for u, v in edges:
            if not dsu.union(u - 1, v - 1):
                ans = [u, v]
                break
        return ans
