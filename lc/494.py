"""
494. Target Sum
"""


def iter_base2_mono_flip_idxs(bits: int):
    stack = []

    for i in range(bits):
        stack.append(i)
        stack.extend(stack)
        stack.pop()

    return stack


class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        N = len(nums)

        res = 0
        cur_sum = sum(nums)
        if cur_sum == target:
            res += 1
        op_mask = [True] * N
        for idx in iter_base2_mono_flip_idxs(N):
            if op_mask[idx]:
                op_mask[idx] = False
                cur_sum -= 2 * nums[idx]
            else:
                op_mask[idx] = True
                cur_sum += 2 * nums[idx]

            if cur_sum == target:
                res += 1

        return res
