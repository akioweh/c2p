"""
32. Longest Valid Parentheses
"""

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # cannot end with '(' or start with ')'
        s = s.rstrip('(').lstrip(')')
        max_len = 0
        l, r = 0, 0
        for c in s:
            if c == '(':
                l += 1
            else:
                r += 1
            if r > l:
                l, r = 0, 0
            elif r == l:
                max_len = max(max_len, r * 2)
        l, r = 0, 0
        for c in reversed(s):
            if c == ')':
                r += 1
            else:
                l += 1
            if l > r:
                l, r = 0, 0
            elif l == r:
                max_len = max(max_len, l * 2)

        return max_len


if __name__ == '__main__':
    temp = Solution()
    print(temp.longestValidParentheses(
        '()((())()'
    ))
