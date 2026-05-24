# Problem  : Minimum Swaps to Move Zeros to End
# Difficulty: Easy
# Tags     : 
# URL      : https://leetcode.com/problems/minimum-swaps-to-move-zeros-to-end/
# Solved on: 2026-05-24 13:35
# ──────────────────────────────────────────────────

class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        i=0
        j=len(nums)-1
        c=0
        while i<j:
            if nums[i]!=0:
                i+=1
            elif nums[j]==0:
                j-=1
            else:
                nums[i],nums[j]=nums[j],nums[i]
                c+=1
                i+=1
                j-=1
        return c
            
