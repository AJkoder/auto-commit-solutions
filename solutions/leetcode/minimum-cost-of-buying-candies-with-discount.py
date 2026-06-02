# Problem  : Minimum Cost of Buying Candies With Discount
# Difficulty: Easy
# Tags     : Array, Greedy, Sorting
# URL      : https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
# Solved on: 2026-06-02 15:45
# ──────────────────────────────────────────────────

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort(reverse=True)
        ans = 0
        for i in range(n):
            if i % 3 == 2:
                continue
            ans += cost[i]
        return ans 
