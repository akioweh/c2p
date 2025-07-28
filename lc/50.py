"""
50. Pow(x, n)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # fast integer exponentiation
        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1
        return ans
