# Problem  : Maximum Ice Cream Bars
# Difficulty: Medium
# Tags     : Array, Greedy, Sorting, Counting Sort
# URL      : https://leetcode.com/problems/maximum-ice-cream-bars/
# Solved on: 2026-06-22 14:24
# ──────────────────────────────────────────────────

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        c=0
        for cost in costs:
             if cost<=coins:
                  c+=1
                  coins-=cost
        return c
