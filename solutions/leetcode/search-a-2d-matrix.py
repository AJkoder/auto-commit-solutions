# Problem  : Search a 2D Matrix
# Difficulty: Medium
# Tags     : Array, Binary Search, Matrix
# URL      : https://leetcode.com/problems/search-a-2d-matrix/
# Solved on: 2026-06-06 13:39
# ──────────────────────────────────────────────────

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])

        low=0
        high=m*n-1

        while low<=high:
            mid=(high+low)//2
            row=mid//n
            col=mid%n
            value = matrix[row][col]

            if value==target:
                return True
            elif value>target:
                high-=1
            else:
                low+=1
        return False


