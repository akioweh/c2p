"""
77. Combinations
"""


class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        # return all n-choose-k combinations for n in range(1, n+1)

        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path)
                return
            for i in range(start, n + 1):
                backtrack(i + 1, path + [i])

        backtrack(1, [])
        return res
