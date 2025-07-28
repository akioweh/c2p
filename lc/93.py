"""
93. Restore IP Addresses
"""


class Solution:
    @staticmethod
    def valid_s(s):
        N = len(s)
        if not 1 <= N <= 3:
            return False
        if N > 1 and s[0] == '0':
            return False
        if not int(s) <= 255:
            return False
        return True


    def restoreIpAddresses(self, s: str) -> list[str]:

        res = []
        def yessir(s_, n=4, pre=''):
            N = len(s_)
            if n == 1:
                if self.valid_s(s_):
                    res.append(pre + s_)
                return
            if N < n:
                return
            if N > 3 * n:
                return
            for i in range(1, 4):
                seg = s_[:i]
                if self.valid_s(seg):
                    yessir(s_[i:], n - 1, pre + seg + '.')
                else:
                    break

        yessir(s)
        return res
