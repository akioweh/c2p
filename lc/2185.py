"""
2185. Counting Words With a Given Prefix
"""

class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        return sum(s.startswith(pref) for s in words)
