"""
36. Valid Sudoku
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        def is_valid(arr: list[str]) -> bool:
            seen = [False] * 9
            for c in arr:
                if c != '.':
                    idx = ord(c) - ord('1')
                    if seen[idx]:
                        return False
                    seen[idx] = True
            return True

        # check rows
        for row in board:
            if not is_valid(row):
                return False

        # check columns
        for col in range(9):
            if not is_valid([board[row][col] for row in range(9)]):
                return False

        # check 3x3 boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not is_valid([board[row][col] for row in range(i, i + 3) for col in range(j, j + 3)]):
                    return False

        return True
