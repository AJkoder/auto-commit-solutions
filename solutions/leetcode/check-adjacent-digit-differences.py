# Problem  : Check Adjacent Digit Differences
# Difficulty: Easy
# Tags     : 
# URL      : https://leetcode.com/problems/check-adjacent-digit-differences/
# Solved on: 2026-05-17 23:55
# ──────────────────────────────────────────────────

class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        
        for i in range(len(s)-1):
            diff=abs(int(s[i])-int(s[i+1]))
            if diff>2:
                return False
        return True
