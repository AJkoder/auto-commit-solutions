# Problem  : Single Element in a Sorted Array
# Difficulty: Medium
# Tags     : Array, Binary Search
# URL      : https://leetcode.com/problems/single-element-in-a-sorted-array/
# Solved on: 2026-06-20 13:34
# ──────────────────────────────────────────────────

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s=0
        for num in nums:
            s=s^num
        return s
