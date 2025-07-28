"""
1718. Construct the Lexicographically Largest Valid Sequence
"""


class Solution:
    def constructDistancedSequence(self, n: int) -> list[int]:
        N = 2 * n - 1
        res = [0] * N
        used = [False] * (n + 1)

        def _set(idx: int, num: int) -> bool:
            if num == 1:
                res[idx] = 1
                used[1] = True
                return True
            if idx + num >= N:
                return False
            if res[idx + num]:
                return False
            res[idx] = num
            res[idx + num] = num
            used[num] = True
            return True

        def _unset(idx: int):
            num = res[idx]
            res[idx] = 0
            if num != 1:
                res[idx + num] = 0
            used[num] = False

        def fill(idx: int) -> bool:
            if idx == N:
                return True
            if res[idx]:
                return fill(idx + 1)
            for num in range(n, 0, -1):
                if used[num]:
                    continue
                if not _set(idx, num):
                    continue
                if fill(idx + 1):
                    return True
                else:
                    _unset(idx)
            return False

        fill(0)
        return res

