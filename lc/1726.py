"""
1726. Tuple with Same Product
"""


class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        N = len(nums)
        # since nums are pairwise distinct,
        # every product is made of a unique pair

        n_ways = {}
        for i, a in enumerate(nums):
            for j in range(i + 1, N):
                b = nums[j]
                p = a * b
                if p in n_ways:
                    n_ways[p] += 1
                else:
                    n_ways[p] = 1

        return sum(
            4 * n * (n - 1) for n in n_ways.values()
        )
