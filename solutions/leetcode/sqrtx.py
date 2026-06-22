# Problem  : Sqrt(x)
# Difficulty: Easy
# Tags     : Math, Binary Search
# URL      : https://leetcode.com/problems/sqrtx/
# Solved on: 2026-06-22 14:24
# ──────────────────────────────────────────────────

class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        l=0
        r=x-1
        ans=0
        while l<=r:
            mid=(l+r)//2
            val=mid*mid

            if val==x:
                ans=mid
                return ans
            elif val<x:
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
        

