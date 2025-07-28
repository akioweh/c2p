"""
1639. Number of Ways to Form a Target String Given a Dictionary
"""

from collections import Counter
from itertools import accumulate
from operator import add, mul


class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        I = len(words[0])
        J = len(target)

        # noinspection PyTypeChecker
        freqs: list[dict[str, int]] = list(map(
            Counter,
            zip(*words)
        ))

        t = target[0]
        dp = [
            [n]
            for n in accumulate(
                freqs[i][t]
                for i in range(I)
            )
        ]
        if 1 < J:
            dp[0].append(0)

        target1 = target[1:]
        for i in range(1, I):
            dp[i].extend(
                map(
                    add,
                    dp[i - 1][1:],
                    map(
                        mul,
                        dp[i - 1],
                        map(freqs[i].__getitem__, target1)
                    )
                )
            )
            if i + 1 < J:
                dp[i].append(0)

        return dp[-1][-1] % 1_000_000_007
