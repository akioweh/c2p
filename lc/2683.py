"""
2683. Neighboring Bitwise XOR
"""

class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        return sum(derived) % 2 == 0
