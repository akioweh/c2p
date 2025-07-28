"""
31. Next Permutation
"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        l = len(nums)
        pos = -1
        for i in range(l - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pos = i
                break

        if pos == -1:
            nums.sort()
            return

        # find pos2 of smallest element larger than nums[pos] in nums[pos + 1:]
        pos_n = nums[pos]
        pos2 = min(filter(lambda i_: nums[i_] > pos_n, range(pos + 1, l)), key=nums.__getitem__)

        nums[pos], nums[pos2] = nums[pos2], nums[pos]
        nums[pos + 1:] = sorted(nums[pos + 1:])


if __name__ == '__main__':
    temp = Solution()
    arr = [2, 1, 3]
    temp.nextPermutation(
        arr
    )
    print(arr)
