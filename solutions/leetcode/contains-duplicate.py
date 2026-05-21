# Problem  : Contains Duplicate
# Difficulty: Easy
# Tags     : Array, Hash Table, Sorting
# URL      : https://leetcode.com/problems/contains-duplicate/
# Solved on: 2026-05-21 15:32
# ──────────────────────────────────────────────────

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for i in range (len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
            if freq[nums[i]]>=2:
                return True
        return False
