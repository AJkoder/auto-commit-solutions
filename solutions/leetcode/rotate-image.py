# Problem  : Rotate Image
# Difficulty: Medium
# Tags     : Array, Math, Matrix
# URL      : https://leetcode.com/problems/rotate-image/
# Solved on: 2026-06-04 00:24
# ──────────────────────────────────────────────────

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m=len(matrix)
        n=len(matrix[0])

        for i in range (m):
            for j in range (i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for row in matrix:
            row.reverse()

        
