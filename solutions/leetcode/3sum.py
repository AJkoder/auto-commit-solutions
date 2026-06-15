# Problem  : 3Sum
# Difficulty: Medium
# Tags     : Array, Two Pointers, Sorting
# URL      : https://leetcode.com/problems/3sum/
# Solved on: 2026-06-15 15:37
# ──────────────────────────────────────────────────

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res=[]
        n=len(nums)
        nums.sort()

        for i in range(n):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=n-1

            while j<k:
                target=nums[i]+nums[j]+nums[k]
                if target<0:
                    j+=1
                elif target >0:
                    k-=1
                else:
                    temp=[nums[i],nums[j],nums[k]]
                    res.append(temp)
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
        return res
        
