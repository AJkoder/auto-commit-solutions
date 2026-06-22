# Problem  : Single Element in a Sorted Array
# Difficulty: Medium
# Tags     : Array, Binary Search
# URL      : https://leetcode.com/problems/single-element-in-a-sorted-array/
# Solved on: 2026-06-22 23:55
# ──────────────────────────────────────────────────

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        l=0
        n=len(nums)
        r=n-1

        if nums[0]!=nums[1]:
            return nums[0]
        if nums[n-2]!=nums[n-1]:
            return nums[n-1]

        while l<=r:
            mid=(r+l)//2

            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if mid%2==0:
                if nums[mid-1]==nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid-1]==nums[mid]:
                    l=mid+1
                else:
                    r=mid-1
            
                
