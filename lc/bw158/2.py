class Solution:
    def maximumProfit(self, prices: list[int], k: int) -> int:
        n = len(prices)

        none = [0] * (k + 1)  # dp([i])[j] = max profit with j trades in prices[:i + 1]
        long = [-1e11] * (k + 1)  # above but with an open long position
        short = [-1e11] * (k + 1)  # yes
        for i in range(n):
            new_none = [0] * (k + 1)
            new_long = [0] * (k + 1)
            new_short = [0] * (k + 1)
            for j in range(1, k + 1):
                new_none[j] = max(none[j], long[j] + prices[i], short[j] - prices[i])
                new_long[j] = max(long[j], none[j - 1] - prices[i])
                new_short[j] = max(short[j], none[j - 1] + prices[i])
            none, long, short = new_none, new_long, new_short

        return max(none)
