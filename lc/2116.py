"""
2116. Check if a Parentheses String Can Be Valid
"""

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        N = len(s)
        if N % 2:
            return False

        min_opens = 0
        max_opens = 0
        for p, l in zip(s, locked):
            if l == '1':  # locked
                if p == '(':
                    min_opens += 1
                    max_opens += 1
                else:
                    if min_opens > 0:
                        min_opens -= 1
                    if max_opens == 0:
                        return False
                    max_opens -= 1
            else:  # unlocked
                max_opens += 1
                if min_opens > 0:
                    min_opens -= 1

        return min_opens == 0
