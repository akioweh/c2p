"""
88. Merge Sorted Array
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        nums1[n:] = nums1[:m]
        write_ptr = 0
        read_ptr1 = n
        read_ptr2 = 0
        n1 = nums1[read_ptr1] if read_ptr1 < m + n else float('inf')
        n2 = nums2[read_ptr2] if read_ptr2 < n else float('inf')
        while write_ptr < m + n:
            if n1 < n2:
                nums1[write_ptr] = n1
                read_ptr1 += 1
                n1 = nums1[read_ptr1] if read_ptr1 < m + n else float('inf')
            else:
                nums1[write_ptr] = n2
                read_ptr2 += 1
                n2 = nums2[read_ptr2] if read_ptr2 < n else float('inf')
            write_ptr += 1
