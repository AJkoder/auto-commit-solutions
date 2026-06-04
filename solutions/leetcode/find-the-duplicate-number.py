# Problem  : Find the Duplicate Number
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search, Bit Manipulation
# URL      : https://leetcode.com/problems/find-the-duplicate-number/
# Solved on: 2026-06-05 00:58
# ──────────────────────────────────────────────────

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=nums[0]
        fast=nums[0]

        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]

            if slow==fast:
                break

        slow=nums[0]
        while slow!=fast:
            slow=nums[slow]
            fast=nums[fast]
        return slow
