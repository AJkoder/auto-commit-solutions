# Problem  : Reverse Integer
# Difficulty: Medium
# Tags     : Math
# URL      : https://leetcode.com/problems/reverse-integer/
# Solved on: 2026-05-16 22:03
# ──────────────────────────────────────────────────

class Solution:
    def reverse(self, x: int) -> int:
        n=abs(x)
        rev=0

        while n>0:
            dig=n%10
            if rev > (2**31 - 1) // 10:
                return 0
            rev=rev*10+dig
            n=n//10
        
        if x<0:
            return rev*-1
        return rev
