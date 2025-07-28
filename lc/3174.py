"""
3174. Clear Digits
"""


class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s:
            if c in '1234567890':
                if stack:
                    stack.pop()
            else:
                stack.append(c)

        return ''.join(stack)

