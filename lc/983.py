"""
983. Minimum Cost For Tickets
"""


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        N = len(days)
        if N == 1:
            return min(costs)

        dp = [0] * (365 + 31)
        for i, day in enumerate(days):
            next_day = days[i + 1] if i != N - 1 else 366
            cost = min(
                dp[day - 1] + costs[0],
                dp[day - 7] + costs[1],
                dp[day - 30] + costs[2]
            )
            dp[day:next_day] = [cost] * (next_day - day)

        return dp[365]
