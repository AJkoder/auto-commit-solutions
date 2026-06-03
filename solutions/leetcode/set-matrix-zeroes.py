# Problem  : Set Matrix Zeroes
# Difficulty: Medium
# Tags     : Array, Hash Table, Matrix
# URL      : https://leetcode.com/problems/set-matrix-zeroes/
# Solved on: 2026-06-03 13:39
# ──────────────────────────────────────────────────

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        row = [0]*m
        col = [0]*n

        for i in range (m):
            for j in range (n):
                if matrix[i][j]==0:
                    row[i]=-1
                    col[j]=-1
        for i in range (m):
            for j in range (n):
                if row[i]==-1 or col[j]==-1:
                    matrix[i][j]=0
                    
        


