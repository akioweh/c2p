"""
65. Valid Number
"""


class Solution:
    @staticmethod
    def is_integer(s: str) -> bool:
        if not s:
            return False
        if s[0] in '+-':
            s = s[1:]
        return s.isdigit()

    @staticmethod
    def is_decimal(s: str) -> bool:
        if not s:
            return False
        if s[0] in '+-':
            s = s[1:]
        parts = s.split('.')
        if len(parts) != 2:
            return False
        return all(p.isdigit() or not p for p in parts) and any(parts)

    def isNumber(self, s: str) -> bool:
        s = s.strip()
        parts = s.split('e')
        if len(parts) == 1:
            parts = s.split('E')

        if len(parts) == 1:
            return self.is_integer(parts[0]) or self.is_decimal(parts[0])
        if len(parts) != 2:
            return False
        return (self.is_integer(parts[0]) or self.is_decimal(parts[0])) and self.is_integer(parts[1])
