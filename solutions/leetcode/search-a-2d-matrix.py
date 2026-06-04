# Problem  : Search a 2D Matrix
# Difficulty: Medium
# Tags     : Array, Binary Search, Matrix
# URL      : https://leetcode.com/problems/search-a-2d-matrix/
# Solved on: 2026-06-05 00:57
# ──────────────────────────────────────────────────

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])

        for i in range (m):
            for j in range (n):
                if matrix[i][j]==target:
                    return True
        return False

