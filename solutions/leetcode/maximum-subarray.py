# Problem  : Maximum Subarray
# Difficulty: Medium
# Tags     : Array, Divide and Conquer, Dynamic Programming
# URL      : https://leetcode.com/problems/maximum-subarray/
# Solved on: 2026-06-03 13:39
# ──────────────────────────────────────────────────

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx=float("-inf")
        cs=0
        for i in range (len(nums)):
            cs+=nums[i]
            mx=max(cs,mx)
            if cs<0:
                cs=0
        return mx
            
