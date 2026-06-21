# Problem  : Maximum Manhattan Distance After All Moves
# Difficulty: Medium
# Tags     : 
# URL      : https://leetcode.com/problems/maximum-manhattan-distance-after-all-moves/
# Solved on: 2026-06-21 20:09
# ──────────────────────────────────────────────────

class Solution:
    def maxDistance(self, moves: str) -> int:
        
        x=0
        y=0
        k=0
        
        for ch in moves:
            if ch=="U":
                y+=1
            elif ch=="R":
                x+=1
            elif ch=="L":
                x-=1
            elif ch=="D":
                y-=1
            else:
                k+=1

        ans=abs(x)+abs(y)+k
        return ans
            
                

