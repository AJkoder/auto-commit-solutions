# Problem  : Pascal's Triangle
# Difficulty: Easy
# Tags     : Array, Dynamic Programming
# URL      : https://leetcode.com/problems/pascals-triangle/
# Solved on: 2026-06-03 13:39
# ──────────────────────────────────────────────────

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res=[[1]]
        for i in range(1,numRows):
            prev=res[-1]
            curr=[1]
            for j in range (1,len(prev)):
                curr.append(prev[j-1]+prev[j])
            curr.append(1)
            res.append(curr)
        return res

    

