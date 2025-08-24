"""
Tree Isomorphism
"""

from collections import deque, defaultdict


def iso(graph: list[list[int]], roots: list[int]) -> bool:
    """Checks if all trees in the forest ``graph``
    rooted at ``roots`` are isomorphic to each other.

    Graph is assumed to be undirected (every edge has a back edge).

    O(V log V) AHU algorithm.
    O(V) if cur_lvl sort uses radix sort (but can be slower in practice).
    """
    n = len(graph)
    lvl = [-1] * n
    levels: list[list[int]] = []
    par = [-1] * n

    def calc_height(_r: int) -> int:
        q = deque([_r])
        lvl[_r] = 0
        res = 0
        while q:
            u = q.popleft()
            d = lvl[u]
            p = par[u]
            if len(levels) == d:
                levels.append([])
            levels[d].append(u)
            res = max(res, d)
            for v in graph[u]:
                if v == p:
                    continue
                par[v] = u
                lvl[v] = d + 1
                q.append(v)
        return res + 1

    heights = (calc_height(r) for r in roots)
    h = next(heights)
    if not all(_h == h for _h in heights):
        return False

    v_hash = [0] * n  # default hash for leaves is 0
    for l in reversed(range(h - 1)):
        prev_lvl = levels[l + 1]
        cur_lvl = levels[l]
        children = defaultdict(list)
        for u in prev_lvl:
            children[par[u]].append(v_hash[u])
        # re-hash
        cur_lvl.sort(key=children.__getitem__)
        idx = 0
        prev = children[cur_lvl[0]]
        for v in cur_lvl:
            if (cur := children[v]) != prev:
                idx += 1
                prev = cur
            v_hash[v] = idx

    return len(set(v_hash[r] for r in roots)) == 1
