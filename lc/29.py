"""
29. Divide Two Integers
"""

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        if divisor > divisor:
            return 0

        tot_sum = 0
        tot_quotient = 0

        # un-bounded binary search
        while tot_sum + divisor <= dividend:
            add_sum = divisor
            add_quo = 1
            while tot_sum + add_sum + add_sum <= dividend:
                add_quo <<= 1
                add_sum += add_sum

            tot_sum += add_sum
            tot_quotient += add_quo

        # lmao
        if positive and tot_quotient == 2147483648:
            tot_quotient -= 1

        return tot_quotient if positive else -tot_quotient
