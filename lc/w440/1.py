class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        N = len(baskets)
        filled = [False] * N
        ans = 0
        for amt in fruits:
            for i in range(N):
                if filled[i] or baskets[i] < amt:
                    continue
                filled[i] = True
                break
            else:
                ans += 1

        return ans
