# Problem  : Search in Rotated Sorted Array
# Difficulty: Medium
# Tags     : Array, Binary Search
# URL      : https://leetcode.com/problems/search-in-rotated-sorted-array/
# Solved on: 2026-05-23 18:45
# ──────────────────────────────────────────────────

class Solution:
    def search(self, nums: List[int], target: int) -> int:
       
        low=0
        high=len(nums)-1
        if not nums:
            return -1

        
        while low<=high:
            mid=(low+high)//2

            if nums[mid]==target:
                return mid

            if nums[mid]<=nums[high]:
                if nums[mid]<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                if nums[low]<=target<nums[mid]:
                    high=mid-1
                else:
                    low=mid+1
        return -1

                
           

        



