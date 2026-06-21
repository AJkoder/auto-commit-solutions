# Problem  : Create Grid With Exactly One Path
# Difficulty: Easy
# Tags     : 
# URL      : https://leetcode.com/problems/create-grid-with-exactly-one-path/
# Solved on: 2026-06-21 20:09
# ──────────────────────────────────────────────────

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid=[["#"]*n for i in range(m)]

        for i in range(m):
            grid[i][0]="."
        for i in range(n):
            grid[m-1][i]="."
        ans=[''.join(t) for t in grid]
        return ans
