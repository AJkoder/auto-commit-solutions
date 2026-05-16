# Problem  : Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Tags     : Array, Binary Search
# URL      : https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Solved on: 2026-05-16 22:03
# ──────────────────────────────────────────────────

class Solution:
    def findMin(self, nums: List[int]) -> int:
        mn=float("inf")
        low=0
        high=len(nums)-1

        while low<=high:
            mid=(low+high)//2

            if nums[mid]<=nums[high]:
                mn=min(mn,nums[mid])
                high=mid-1
            else:
                mn=min(mn,nums[low])
                low=mid+1
        return mn
