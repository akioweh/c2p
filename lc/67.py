"""
67. Add Binary
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a:
            return b
        if not b:
            return a

        res = ''
        l_a, l_b = len(a), len(b)
        if l_b < l_a:
            a, b = b, a
            l_a, l_b = l_b, l_a
        # l_a <= l_b

        i = 1
        carry = False
        while i <= l_b:
            if i > l_a:
                c_a, c_b = '0', b[-i]
            else:
                c_a, c_b = a[-i], b[-i]
            if c_a == '0':
                if c_b == '0':
                    if carry:
                        res = '1' + res
                        carry = False
                    else:
                        res = '0' + res
                else:  # c_b == '1'
                    if carry:
                        res = '0' + res
                        # still carry
                    else:
                        res = '1' + res
            else:  # c_a == '1'
                if c_b == '0':
                    if carry:
                        res = '0' + res
                        # still carry
                    else:
                        res = '1' + res
                else:  # c_b == '1'
                    if carry:
                        res = '1' + res
                        # still carry
                    else:
                        carry = True
                        res = '0' + res

            i += 1

        if carry:
            res = '1' + res

        return res
