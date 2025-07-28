"""
2429. Minimize XOR
"""

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        n1_count = num1.bit_count()
        n2_count = num2.bit_count()
        ans = bin(num1)[:1:-1]
        if len(ans) < n2_count:
            ans += (n2_count - len(ans)) * '0'

        if n1_count > n2_count:
            ans = ans.replace('1', '0', n1_count - n2_count)
        elif n2_count != n1_count:
            ans = ans.replace('0', '1', n2_count - n1_count)

        return int(ans[::-1], 2)
