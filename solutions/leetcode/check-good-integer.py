# Problem  : Check Good Integer
# Difficulty: Easy
# Tags     : 
# URL      : https://leetcode.com/problems/check-good-integer/
# Solved on: 2026-06-14 14:55
# ──────────────────────────────────────────────────

class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        s=n*n
        ss=0
        ds=0
        while n>0:
            dig=n%10
            digs=dig*dig
            ds=dig+ds
            ss=digs+ss
            n=n//10
        
        diff=ss-ds

        if diff >=50:
            return True
        return False
            
