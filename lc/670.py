"""
670. Maximum Swap
"""

class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num

        digits = []
        original = num
        while num:
            num, temp = divmod(num, 10)
            digits.append(temp)

        l = len(digits)
        idxs = list(range(l))
        idxs.sort(key=digits.__getitem__)
        pos = l
        for i, j in zip(reversed(idxs), range(l - 1, -1, -1)):
            if i == j:
                pos = i
            else:
                break
        else:
            return original

        substitute_idx = max(list(range(pos)), key=digits.__getitem__)
        digits[pos - 1], digits[substitute_idx] = digits[substitute_idx], digits[pos - 1]
        num = 0
        for i, v in enumerate(digits):
            num += (10 ** i) * v

        return num
