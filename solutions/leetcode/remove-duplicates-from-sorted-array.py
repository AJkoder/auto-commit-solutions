# Problem  : Remove Duplicates from Sorted Array
# Difficulty: Easy
# Tags     : Array, Two Pointers
# URL      : https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Solved on: 2026-06-15 15:37
# ──────────────────────────────────────────────────

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        j=i+1

        if n==1:
            return 1

        while j<n:
            if nums[j]!=nums[i]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
            j+=1
        return i+1

