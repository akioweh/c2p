"""
2657. Find the Prefix Common Array of Two Arrays
"""

class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        N = len(A)
        seen = [False] * (N + 1)
        ans = 0
        arr = []
        for a, b in zip(A, B):
            if a == b:
                ans += 1
            else:
                if seen[a]:
                    ans += 1
                else:
                    seen[a] = True
                if seen[b]:
                    ans += 1
                else:
                    seen[b] = True

            arr.append(ans)

        return arr
