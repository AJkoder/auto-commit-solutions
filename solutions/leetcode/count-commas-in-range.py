# Problem  : Count Commas in Range
# Difficulty: Easy
# Tags     : Math
# URL      : https://leetcode.com/problems/count-commas-in-range/
# Solved on: 2026-05-29 20:05
# ──────────────────────────────────────────────────

class Solution:
    def countCommas(self, n: int) -> int:
        l=len(str(n))
        if l<4:
            return 0
        else:
            return int(n)-1000+1
