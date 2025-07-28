"""
45. Jump Game II
"""

class Solution:
    def jump(self, nums: list[int]) -> int:
        N = len(nums)
        r_min, r_max = 0, 0
        n_jumps = 0
        while True:
            if r_max >= N - 1:
                break
            n_jumps += 1
            r_min, r_max = r_max + 1, max(i + nums[i] for i in range(r_min, r_max + 1))

        return n_jumps
