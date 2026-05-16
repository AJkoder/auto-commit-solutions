# Problem  : Palindrome Number
# Difficulty: Easy
# Tags     : Math
# URL      : https://leetcode.com/problems/palindrome-number/
# Solved on: 2026-05-16 22:03
# ──────────────────────────────────────────────────

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        original=x
        rev=0
        while x>0:
            dig=x%10
            rev=rev*10+dig
            x//=10
        return original==rev
        


