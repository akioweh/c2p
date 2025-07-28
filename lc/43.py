"""
43. Multiply Strings
"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        ORD0 = ord('0')  # 48

        l1, l2 = len(num1), len(num2)
        res = [0] * (l1 + l2)

        for offset in range(l2):
            # do multiplication
            temp_res = [0] * (l1 + 1)
            carry = 0
            num2_digit = ord(num2[-1 - offset]) - ORD0
            for i in range(-1, -l1 - 1, -1):
                carry, temp_res[i] = divmod(
                    (ord(num1[i]) - ORD0) * num2_digit + carry,
                    10
                )
            temp_res[-l1 - 1] = carry
            # add temp_res to res
            carry = 0
            for i in range(-1 - offset, -2 - offset - l1, -1):
                carry, res[i] = divmod(
                    res[i] + temp_res[i + offset] + carry,
                    10
                )
            if carry:
                res[-2 - offset - l1] += carry

        return ''.join(map(str, res)).lstrip('0')
