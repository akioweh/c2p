"""
100567. Maximum Manhattan Distance After K Changes
"""


class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        N = len(s)
        if k == N:
            return N

        quadrants = ('NW', 'NE', 'SW', 'SE')
        max_max_dist = 0
        for quad in quadrants:
            k_ = k
            s_ = list(s)
            for i, c in enumerate(s_):
                if k_ == 0:
                    break
                if c not in quad:
                    s_[i] = quad[0]
                    k_ -= 1
            max_dist = 0
            x, y = 0, 0
            for d in s_:
                match d:
                    case 'N':
                        y += 1
                    case 'S':
                        y -= 1
                    case 'W':
                        x -= 1
                    case 'E':
                        x += 1
                max_dist = max(max_dist, abs(x) + abs(y))
            max_max_dist = max(max_max_dist, max_dist)
        return max_max_dist
