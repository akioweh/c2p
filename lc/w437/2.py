class Solution:
    def maxWeight(self, pizzas: list[int]) -> int:
        pizzas.sort()
        N = len(pizzas)
        ans = 0
        days = N // 4
        for _ in range((days + 1) // 2):
            ans += pizzas.pop()
        for _ in range(days // 2):
            pizzas.pop()
            ans += pizzas.pop()
        return ans
