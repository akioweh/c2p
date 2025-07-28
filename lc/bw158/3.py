from math import gcd


class Solution:
    def maxGCDScore(self, nums: list[int], k: int) -> int:
        N = len(nums)
        two_pow = [
            (x & -x).bit_length() - 1
            for x in nums
        ]

        ans = 0
        for l in range(N):
            pow_counter = [0] * 30
            g = 0
            for r in range(l + 1, N + 1):
                pow_counter[two_pow[r - 1]] += 1
                g_ = g = gcd(g, nums[r - 1])
                if pow_counter[(g & -g).bit_length() - 1] <= k:
                    g_ *= 2
                ans = max(ans, g_ * (r - l))

        return ans
