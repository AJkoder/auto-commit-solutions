# Problem  : First Matching Character From Both Ends
# Difficulty: Easy
# Tags     : Two Pointers, String
# URL      : https://leetcode.com/problems/first-matching-character-from-both-ends/
# Solved on: 2026-04-15 18:06
# ──────────────────────────────────────────────────

class Solution:
    def firstMatchingIndex(self, s: str) -> int:
        l=0
        r=len(s)-1

        while l<=r:
            if s[l]==s[r]:
                return l
            l+=1
            r-=1
        return -1
            
