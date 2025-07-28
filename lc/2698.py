"""
2698. Find the Punishment Number of an Integer
"""


class Solution:
    @staticmethod
    def can_match(target: int, num: int = None) -> bool:
        if num is None:
            num = target * target
        if target == num:
            return True
        i = 10
        while True:
            l, r = divmod(num, i)
            if not l:
                break
            if Solution.can_match(target - l, r):
                return True
            i *= 10
        return False

    def punishmentNumber(self, n: int) -> int:
        return sum(
            i * i
            for i in filter(Solution.can_match, range(1, n + 1))
        )
