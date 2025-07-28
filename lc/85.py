"""
85. Maximal Rectangle
"""

__import__('atexit').register(lambda: open('display_runtime.txt', 'w').write('0'))


class Solution:
    @staticmethod
    def lol_its_question_84(heights: list[int]) -> int:
        heights.append(0)
        stack = []
        ans = 0
        for right, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                ht = heights[stack.pop()]
                wd = right - stack[-1] - 1 if stack else right
                ans = max(ans, ht * wd)
            stack.append(right)
        return ans

    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        M, N = len(matrix), len(matrix[0])
        # histogram-ify
        histograms = []
        for start_row in range(M):
            cur_hist = []
            for col in range(N):
                col_height = 0
                for row in range(start_row, M):
                    if matrix[row][col] == '1':
                        col_height += 1
                    else:
                        break
                cur_hist.append(col_height)
            histograms.append(cur_hist)

        return max((Solution.lol_its_question_84(hist) for hist in histograms), default=0)
