"""
81. Search in Rotated Sorted Array II
"""

from bisect import bisect_left


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        N = len(nums)
        if N <= 100:  # lin search for short inputs
            return target in nums

        # first, find pivot point
        l, r = 0, N - 1
        v_l, v_r = nums[l], nums[r]
        while l < r - 1:
            m = (l + r) // 2
            v_m = nums[m]
            if v_m > v_r:  # left half sorted
                l = m
                v_l = v_m
            elif v_m < v_l:  # right half sorted
                r = m
                v_r = v_m
            elif v_l < v_m or v_m < v_r:  # entire array sorted
                l = r - 1
                break
            else:  # v_l == v_m == v_r; no meaningful info gained
                # shucks man, gotta lin search
                m_l = l + 1
                while m_l < m:
                    if nums[m_l] == v_m:
                        m_l += 1
                    else:
                        break
                if m_l < m:  # break triggered; lower-left sorted
                    l = m_l
                    v_l = nums[m_l]
                    r = m
                    continue
                m_r = r - 1
                while m_r > m:
                    if nums[m_r] == v_m:
                        m_r -= 1
                    else:
                        break
                if m_r > m:  # upper-right sorted
                    r = m_r
                    v_r = nums[m_r]
                    l = m
                    continue
                # entire array is a single value
                return target == v_m

        # at this point, l = r - 1
        # and pivot is r... or r+1
        if nums[l] > nums[r]:
            x = r
        else:
            x = r + 1

        if target >= nums[0]:
            idx = bisect_left(nums, target, 0, x)
        else:
            idx = bisect_left(nums, target, x, N)

        return idx < N and nums[idx] == target
