"""
2765. Longest Alternating Subarray
"""
from operator import sub


class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        N = len(nums)
        if N == 2:
            return 2 if nums[1] == nums[0] + 1 else -1

        max_len = -1
        cur_len = -1
        last_diff = 0
        for diff in map(sub, nums[1:], nums):
            is1 = abs(diff) == 1

            if not is1 or diff == last_diff:  # reset
                if cur_len != -1:
                    max_len = max(max_len, cur_len)
                    cur_len = -1
                    last_diff = 0

            if is1:
                if cur_len != -1:  # continuation
                    last_diff = diff
                    cur_len += 1
                elif diff == 1:  # init
                    last_diff = 1
                    cur_len = 2

        return max(max_len, cur_len)


if __name__ == '__main__':
    temp = Solution()
    print(temp.alternatingSubarray(
        [2,3,4,3,4]
    ))
