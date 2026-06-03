# Problem  : Find the Duplicate Number
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search, Bit Manipulation
# URL      : https://leetcode.com/problems/find-the-duplicate-number/
# Solved on: 2026-06-04 00:57
# ──────────────────────────────────────────────────

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen=set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        
