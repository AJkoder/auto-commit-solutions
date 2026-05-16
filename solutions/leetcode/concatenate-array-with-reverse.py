# Problem  : Concatenate Array With Reverse
# Difficulty: Easy
# Tags     : 
# URL      : https://leetcode.com/problems/concatenate-array-with-reverse/
# Solved on: 2026-05-16 22:03
# ──────────────────────────────────────────────────

class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        ans=nums
        n=len(nums)
        for i in range (n-1,-1,-1):
            ans.append(nums[i])
        return ans
