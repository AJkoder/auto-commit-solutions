# Problem  : Majority Element
# Difficulty: Easy
# Tags     : Array, Hash Table, Divide and Conquer, Sorting, Counting
# URL      : https://leetcode.com/problems/majority-element/
# Solved on: 2026-06-05 00:57
# ──────────────────────────────────────────────────

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote=0
        winner=None

        for num in nums:
            if vote==0:
                winner=num
            if num==winner:
                vote+=1
            else:
                vote-=1
        return winner

