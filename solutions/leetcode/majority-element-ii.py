# Problem  : Majority Element II
# Difficulty: Medium
# Tags     : Array, Hash Table, Sorting, Counting
# URL      : https://leetcode.com/problems/majority-element-ii/
# Solved on: 2026-06-06 13:39
# ──────────────────────────────────────────────────

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        one=None
        c1=0
        two=None
        c2=0
        
        for num in nums:

            if num==one:
                c1+=1
            elif num==two:
                c2+=1
            elif c1==0:
                one=num
                c1=1
            elif c2==0:
                two=num
                c2=1
            else:
                c1-=1
                c2-=1
        
        c1=0
        c2=0

        for num in nums:
            if num==one:
                c1+=1
            elif num==two:
                c2+=1
        ans=[]

        if c1>len(nums)//3:
            ans.append(one)
        if c2>len(nums)//3:
            ans.append(two)

        return ans
        
            



        
