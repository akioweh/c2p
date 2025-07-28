"""
2364. Count Number of Bad Pairs
"""

from bisect import bisect
from collections import defaultdict
from operator import sub


class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        N = len(nums)
        tot_n_pairs = (N ** 2 - N) // 2
        good_pairs = 0

        nums = list(map(sub, nums, range(N)))
        idxs_of_val: dict[int, list[int]] = defaultdict(list)
        for i, v in enumerate(nums):
            idxs_of_val[v].append(i)

        for i, v in enumerate(nums):
            good_indices = idxs_of_val[v]
            n_goods = len(good_indices)
            if n_goods == 1:
                continue
            good_pairs += n_goods - bisect(good_indices, i)

        return tot_n_pairs - good_pairs
