def euler_tour_III(tree: list[list[int]], root: int) -> tuple[list[int], list[int], list[int]]:
    # euler tour of the third type???? (list of vertices in the order of dfs visiting)
    # ASSUMES TREE IS CHILDREN LIST, NOT UNDIRECTED ADJACENCY LIST
    # returns euler tour sequence, depth and first occurrence of each node
    n = len(tree)
    tour = []
    depth = [0] * n
    first = [-1] * n

    stack: list[tuple[int, int]] = [(root, 0)]
    while stack:
        u, d = stack.pop()
        if d == -1:
            tour.append(u)
            continue
        depth[u] = d
        if first[u] == -1:
            first[u] = len(tour)
        tour.append(u)
        for child in reversed(tree[u]):
            stack.append((u, -1))
            stack.append((child, d + 1))

    return tour, depth, first


class LCA_SparseTable:
    """Immutable Least Common Ancestor finder.

    O(n log n) construction; O(1) query using euler tour III + sparse table.
    """

    def __init__(self, tree: list[list[int]], root: int):
        tour, self.depth, self.tour_idx = euler_tour_III(tree, root)
        self._st_data = [cur_row := tour]
        step = 1
        while cur_row := list(map(lambda pair: min(pair, key=self.depth.__getitem__), zip(cur_row, cur_row[step:]))):
            self._st_data.append(cur_row)
            step *= 2

    def query(self, u: int, v: int) -> int:
        l, r = self.tour_idx[u], self.tour_idx[v]
        l, r = min(l, r), max(l, r) + 1  # exclusive
        k = (r - l).bit_length() - 1
        return min(self._st_data[k][l], self._st_data[k][r - (1 << k)], key=self.depth.__getitem__)
