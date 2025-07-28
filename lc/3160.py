"""
3160. Find the Number of Distinct Colors Among the Balls
"""


class Solution:
    def queryResults(self, limit: int, queries: list[tuple[int, int]]) -> list[int]:
        color: dict[int, int] = {}
        pos: dict[int, int] = {}

        ans = []
        for idx, new_color in queries:
            if idx in color:  # already colored; erase
                cur_color = color[idx]
                if cur_color == new_color:
                    ans.append(ans[-1])
                    continue  # nvm its a no-op
                pos[cur_color] -= 1
                if not pos[cur_color]:
                    del pos[cur_color]
            # set (new) color
            color[idx] = new_color
            if new_color not in pos:
                pos[new_color] = 0
            pos[new_color] += 1
            # record ans
            ans.append(len(pos))

        return ans
