"""
100566. Maximum Difference Between Even and Odd Frequency I
"""


class Solution:
    def maxDifference(self, s: str) -> int:
        freqs = [0] * 26
        for c in s:
            freqs[ord(c) - 97] += 1

        even_freqs = []
        odd_freqs = []

        for freq in freqs:
            if freq == 0:
                continue
            if freq % 2 == 0:
                even_freqs.append(freq)
            else:
                odd_freqs.append(freq)


        return max(odd_freqs) - min(even_freqs)
