# Problem  : Jump Game
# Difficulty: Medium
# Tags     : Array, Dynamic Programming, Greedy
# URL      : https://leetcode.com/problems/jump-game/
# Solved on: 2026-04-08 18:10
# ──────────────────────────────────────────────────

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mx_idx=0

        for i in range(len(nums)):
            if i>mx_idx:
                return False
            mx_idx=max(mx_idx,nums[i]+i)
        return True
