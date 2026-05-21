# Problem  : Two Sum
# Difficulty: Easy
# Tags     : Array, Hash Table
# URL      : https://leetcode.com/problems/two-sum/
# Solved on: 2026-05-21 15:32
# ──────────────────────────────────────────────────

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in freq:
                return(i,freq[diff])
            else:
                freq[nums[i]]=i
            
        
        
