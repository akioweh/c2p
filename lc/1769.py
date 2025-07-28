"""
1769. Minimum Number of Operations to Move All Balls to Each Box
"""

class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        initial = list(i for i, c in enumerate(boxes) if c == '1')
        cur_ops = sum(initial)
        delta = -len(initial)
        ans = []
        for c in boxes:
            ans.append(cur_ops)
            if c == '1':
                delta += 2
            cur_ops += delta
        return ans
