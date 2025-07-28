"""
2127. Maximum Employees to Be Invited to a Meeting
"""

from array import array
from bisect import bisect_left
from collections import defaultdict


class Solution:
    def maximumInvitations(self, favorite: list[int]) -> int:
        N = len(favorite)
        inv_graph = defaultdict(list)
        for i in range(N):
            inv_graph[favorite[i]].append(i)

        def dfs(_i):
            nonlocal max_cycle_length
            visited[_i] = 1
            stack.append(_i)
            for _j in inv_graph[_i]:
                if not visited[_j]:
                    dfs(_j)
                elif visited[_j] == 1:
                    cyc_len = len(stack) - bisect_left(stack, _j)
                    if cyc_len == 2:
                        c2cles.append(stack[-2:])
                    else:
                        max_cycle_length = max(max_cycle_length, cyc_len)
            stack.pop()
            visited[_i] = 2

        # detect all cycles
        stack = []
        visited = array('b', [0]) * N
        max_cycle_length = 0
        c2cles = []
        for i in range(N):
            if not visited[i]:
                dfs(i)

        def diameter(_i):
            return max(map(diameter, inv_graph[_i]), default=0) + 1

        ans_2cycle = 0
        for cyc in c2cles:
            for u in cyc:
                ans_2cycle += max(
                    (diameter(v) for v in inv_graph[u] if v not in cyc),
                    default=0
                ) + 1

        return max(max_cycle_length, ans_2cycle)

