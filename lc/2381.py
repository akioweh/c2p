"""
2381. Shifting Letters II
"""

from itertools import accumulate
from operator import iadd


class Solution:
    shiftingLetters = lambda _, s, shifts: ''.join(map(
        chr,
        ((c - 97 + shift) % 26 + 97
         for c, shift in zip(map(ord, s), accumulate(
            sum(
                1 for x in shifts
                if (x[2] and x[0] == i) or (not x[2] and x[1] == i - 1)
            ) -
            sum(
                1 for x in shifts
                if (x[2] and x[1] == i - 1) or (not x[2] and x[0] == i)
            )
            for i in range(len(s) + 1)
        )))
    ))
