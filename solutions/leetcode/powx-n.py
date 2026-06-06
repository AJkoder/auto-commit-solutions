# Problem  : Pow(x, n)
# Difficulty: Medium
# Tags     : Math, Recursion
# URL      : https://leetcode.com/problems/powx-n/
# Solved on: 2026-06-06 13:39
# ──────────────────────────────────────────────────

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
        ans=1

        while n>0:
            if n%2==1:
                ans*=x
            x*=x
            n//=2
        return ans
