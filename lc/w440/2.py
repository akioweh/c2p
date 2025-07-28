from heapq import heapify, heappop


class Solution:
    def findMaxSum(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        N = len(nums2)

        nums1_idx = list(range(N))
        nums1_idx.sort(key=nums1.__getitem__)
        nums2_yes = [(-v, i) for i, v in enumerate(nums2)]
        heapify(nums2_yes)
        good = [True] * N

        def get_next_largest() -> tuple[int, int]:
            while nums2_yes and not good[nums2_yes[0][1]]:
                heappop(nums2_yes)
            if not nums2_yes:
                return -1, -1
            _v_, _i_ = heappop(nums2_yes)
            return -_v_, _i_

        ans = [0] * N
        r = N - 1
        cur_group: set[int] = set()
        cur_sum = 0
        for i in reversed(nums1_idx):
            thresh = nums1[i]
            while r >= 0 and nums1[nums1_idx[r]] >= thresh:
                idx = nums1_idx[r]
                if idx in cur_group:
                    cur_sum -= nums2[idx]
                    cur_group.remove(idx)
                good[idx] = False
                r -= 1

            for _ in range(k - len(cur_group)):
                _v, _i = get_next_largest()
                if _v == -1:
                    break
                cur_group.add(_i)
                cur_sum += _v

            ans[i] = cur_sum

        return ans
