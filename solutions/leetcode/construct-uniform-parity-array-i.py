# Problem  : Construct Uniform Parity Array I
# Difficulty: Easy
# Tags     : Array, Math
# URL      : https://leetcode.com/problems/construct-uniform-parity-array-i/
# Solved on: 2026-04-15 20:18
# ──────────────────────────────────────────────────

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        e=0
        o=0
        for i in range(len(nums1)):
            if nums1[i]%2==0:
                e+=1
            o+=1
        if o>=1:
            return True
        
        return False
            
                
                
            
