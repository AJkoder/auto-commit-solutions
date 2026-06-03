# Problem  : Best Time to Buy and Sell Stock
# Difficulty: Easy
# Tags     : Array, Dynamic Programming
# URL      : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Solved on: 2026-06-03 13:39
# ──────────────────────────────────────────────────

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mx=0
        mn=float("inf")
        for i in range (len(prices)):
            mn=min(prices[i],mn)
            pf=prices[i]-mn
            mx=max(pf,mx)
        return mx
