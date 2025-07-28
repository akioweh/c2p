"""
87. Scramble String
"""

from functools import cache


class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        l = len(s1)
        assert l == len(s2)
        if l == 1:
            return s1 == s2

        # find possible swapping division points
        s1_tot_freqs, s2_tot_freqs = [0] * 26, [0] * 26
        idxs_swap = []
        for i, (c_s1, c_s2) in enumerate(zip(s1, reversed(s2))):
            s1_tot_freqs[ord(c_s1) - 97] += 1
            s2_tot_freqs[ord(c_s2) - 97] += 1
            if s1_tot_freqs == s2_tot_freqs:
                idxs_swap.append(i)

        if s1_tot_freqs != s2_tot_freqs:
            return False
        if idxs_swap and idxs_swap[-1] == l - 1:
            idxs_swap.pop()

        # find possible non-swapping division points
        s1_tot_freqs, s2_tot_freqs = [0] * 26, [0] * 26
        idxs_noswap = []
        for i, (c_s1, c_s2) in enumerate(zip(s1, s2)):
            s1_tot_freqs[ord(c_s1) - 97] += 1
            s2_tot_freqs[ord(c_s2) - 97] += 1
            if s1_tot_freqs == s2_tot_freqs:
                idxs_noswap.append(i)
        if idxs_noswap and idxs_noswap[-1] == l - 1:
            idxs_noswap.pop()

        if not idxs_swap and not idxs_noswap:
            return False

        return any(
            self.isScramble(s1[:i + 1], s2[-1 - i:]) and self.isScramble(s1[i + 1:], s2[:-1 - i])
            for i in idxs_swap
        ) or any(
            self.isScramble(s1[:i + 1], s2[:i + 1]) and self.isScramble(s1[i + 1:], s2[i + 1:])
            for i in idxs_noswap
        )
