# Problem  : Minimum Operations to Make Array Modulo Alternating I
# Difficulty: Medium
# Tags     : 
# URL      : https://leetcode.com/problems/minimum-operations-to-make-array-modulo-alternating-i/
# Solved on: 2026-05-24 13:35
# ──────────────────────────────────────────────────

class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n=len(nums)
        result=float("inf")
        for i in range(k):
            for j in range(k):
                if i==j:
                    continue
                op=0

                for x in range(n):
                    remainder = nums[x] % k

                    if x % 2 == 0:
                        target = i
                    else:
                        target = j
                    diff = abs(remainder - target)
                    op += min(diff, k - diff)
                result = min(result, op)
        return result
