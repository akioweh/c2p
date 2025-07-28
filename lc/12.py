"""
12. Integer to Roman
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ss = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']

        res = ''
        for val, s in zip(vals, ss):
            if val > num:
                continue
            n, num = divmod(num, val)
            res += s * n

        return res
