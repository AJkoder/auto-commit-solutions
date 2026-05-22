# Problem  : Valid Sudoku
# Difficulty: Medium
# Tags     : Array, Hash Table, Matrix
# URL      : https://leetcode.com/problems/valid-sudoku/
# Solved on: 2026-05-22 15:32
# ──────────────────────────────────────────────────

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # ---------------- ROW CHECK ----------------
        for row in range(9):

            seen = set()

            for col in range(9):

                val = board[row][col]

                # Ignore empty cells
                if val == ".":
                    continue

                # Duplicate found
                if val in seen:
                    return False

                seen.add(val)

        # ---------------- COLUMN CHECK ----------------
        for col in range(9):

            seen = set()

            for row in range(9):

                val = board[row][col]

                if val == ".":
                    continue

                if val in seen:
                    return False

                seen.add(val)

        # ---------------- 3x3 BOX CHECK ----------------
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):

                seen = set()

                # Traverse inside one 3x3 box
                for i in range(3):
                    for j in range(3):

                        val = board[box_row + i][box_col + j]

                        if val == ".":
                            continue

                        if val in seen:
                            return False

                        seen.add(val)

        return True
