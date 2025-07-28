"""
2467. Most Profitable Path in a Tree
"""

from collections import defaultdict


class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, cost: list[int]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # dfs to find path from bob to 0
        bob_path = []
        stack: list[tuple[int, int]] = [(bob, -1)]
        while stack:
            cur, prev = stack.pop()
            while bob_path and bob_path[-1] != prev:
                bob_path.pop()
            bob_path.append(cur)
            if cur == 0:
                break
            stack.extend((v, cur) for v in adj[cur] if v != prev)

        bob_len = len(bob_path)
        for v in bob_path[:bob_len // 2]:
            cost[v] = 0
        if bob_len % 2:
            cost[bob_path[bob_len // 2]] //= 2

        def max_dfs(_cur: int, _prev: int = -1) -> int:
            return cost[_cur] + max(
                (max_dfs(_next, _cur)
                for _next in adj[_cur]
                if _next != _prev),
                default=0
            )

        return max_dfs(0)
