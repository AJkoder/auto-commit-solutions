# Problem  : Two Sum II - Input Array Is Sorted
# Difficulty: Medium
# Tags     : Array, Two Pointers, Binary Search
# URL      : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Solved on: 2026-05-22 15:32
# ──────────────────────────────────────────────────

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=len(nums)-1

        while i<j:
            if nums[i]+nums[j]==target:
                return [i+1,j+1]
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                i+=1

