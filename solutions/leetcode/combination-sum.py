# Problem  : Combination Sum
# Difficulty: Medium
# Tags     : Array, Backtracking
# URL      : https://leetcode.com/problems/combination-sum/
# Solved on: 2026-06-19 19:42
# ──────────────────────────────────────────────────

class Solution:
    def solve(self, nums, index, total, subset, result, target):
        if total==target:
            return result.append(subset.copy())
        elif total>target:
            return
        if index>=len(nums):
            return
        Sum=total+nums[index]
        subset.append(nums[index])
        self.solve(nums, index, Sum, subset, result, target)
        subset.pop()
        Sum=total
        self.solve(nums, index+1, Sum, subset, result, target)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]
        self.solve(candidates,0,0,[],result,target)
        return result
        
