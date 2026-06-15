# Problem  : Assign Cookies
# Difficulty: Easy
# Tags     : Array, Two Pointers, Greedy, Sorting
# URL      : https://leetcode.com/problems/assign-cookies/
# Solved on: 2026-06-15 20:59
# ──────────────────────────────────────────────────

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i=0
        j=0
        while i<len(g) and j<len(s):
            if s[j]>=g[i]:
                i+=1
            j+=1
        return i
        

