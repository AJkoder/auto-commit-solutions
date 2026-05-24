# Problem  : Limit Occurrences in Sorted Array
# Difficulty: Easy
# Tags     : 
# URL      : https://leetcode.com/problems/limit-occurrences-in-sorted-array/
# Solved on: 2026-05-24 15:17
# ──────────────────────────────────────────────────

class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        freq={}
        ans=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for key,val in freq.items():
            x=min(val,k)
            for i in range(x):
                ans.append(key) 
        return ans
        
