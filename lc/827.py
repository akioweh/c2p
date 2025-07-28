"""
827. Making A Large Island
"""


class DisjointSetSparse:
    """Same as DisjointSet,
    but sets are indexed by arbitrary hashable objects
    instead of a contiguous range of integers.
    """

    __slots__ = ('parent', 'size', 'len')

    def __init__(self, ns = None):
        self.parent = {n: n for n in ns} if ns else {}
        self.size = {n: 1 for n in ns} if ns else {}
        self.len = len(self.parent)

    def add(self, n) -> bool:
        if n in self.parent:
            return False
        self.parent[n] = n
        self.size[n] = 1
        self.len += 1
        return True

    def find(self, x):
        parent_of = self.parent
        while parent_of[x] != x:
            x, parent_of[x] = parent_of[x], parent_of[parent_of[x]]
        return x

    def union(self, x, y) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False

        if self.size[x] < self.size[y]:
            x, y = y, x

        self.parent[y] = x
        self.size[x] += self.size[y]
        self.len -= 1
        return True

    def union_add(self, x, y) -> bool:
        """Shortcut for add(x) + add(y) + union(x, y)"""
        self.add(x)
        self.add(y)
        return self.union(x, y)

    def same(self, *args) -> bool:
        roots = map(self.find, args)
        r0 = next(roots, None)
        return all(r == r0 for r in roots)

    def size_of(self, x):
        return self.size[self.find(x)]

    def __len__(self) -> int:
        return self.len

    def __contains__(self, x):
        return x in self.parent


class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        N = len(grid)
        neighboring_blanks = []

        dsu = DisjointSetSparse()

        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dsu.add((r, c))
                    if r > 0 and grid[r - 1][c]:
                        dsu.union((r - 1, c), (r, c))
                    if c > 0 and grid[r][c - 1]:
                        dsu.union((r, c - 1), (r, c))
                else:
                    for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc]:
                            neighboring_blanks.append((r, c))
                            break

        if not neighboring_blanks:
            return N * N if grid[0][0] else 1

        ans = 0
        for r, c in neighboring_blanks:
            neighbors = set()
            for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc]:
                    neighbors.add(dsu.find((nr, nc)))

            ans = max(ans, sum(map(dsu.size_of, neighbors)) + 1)

        return ans
