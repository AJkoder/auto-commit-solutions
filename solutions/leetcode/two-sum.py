# Problem  : Two Sum
# Difficulty: Easy
# Tags     : Array, Hash Table
# URL      : https://leetcode.com/problems/two-sum/
# Solved on: 2026-04-08 18:10
# ──────────────────────────────────────────────────

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i in range (len(nums)):
            re=target-nums[i]
            if re in freq:
                return i,freq[re]
            freq[nums[i]]=i
        
        
