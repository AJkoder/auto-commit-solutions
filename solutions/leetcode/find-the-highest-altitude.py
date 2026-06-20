# Problem  : Find the Highest Altitude
# Difficulty: Easy
# Tags     : Array, Prefix Sum
# URL      : https://leetcode.com/problems/find-the-highest-altitude/
# Solved on: 2026-06-20 13:34
# ──────────────────────────────────────────────────

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        mx=0
        total=0
        for num in gain:
            total+=num
            mx=max(mx,total)
        return mx
