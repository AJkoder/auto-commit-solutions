# Problem  : Sort Colors
# Difficulty: Medium
# Tags     : Array, Two Pointers, Sorting
# URL      : https://leetcode.com/problems/sort-colors/
# Solved on: 2026-06-03 13:39
# ──────────────────────────────────────────────────

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 2 0 2 1 1 0..consider 0211 and check for lmh
        l=0
        m=0
        h=len(nums)-1

        while m<=h:
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[m],nums[h]=nums[h],nums[m]
                h-=1
                


        
