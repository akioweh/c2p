"""
80. Remove Duplicates from Sorted Array II
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        N = len(nums)
        if N <= 2:
            return N

        n_deleted = 0
        write_ptr, read_ptr = 0, 0
        while read_ptr < N:
            cur_cnt = 1
            cur = nums[read_ptr]
            nums[write_ptr] = nums[read_ptr]
            write_ptr += 1
            while read_ptr < N - 1 and nums[read_ptr + 1] == cur:
                cur_cnt += 1
                if cur_cnt <= 2:
                    nums[write_ptr] = nums[read_ptr]
                    write_ptr += 1
                else:
                    n_deleted += 1
                read_ptr += 1
            read_ptr += 1

        return N - n_deleted
