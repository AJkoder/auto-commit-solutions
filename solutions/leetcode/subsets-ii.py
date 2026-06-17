# Problem  : Subsets II
# Difficulty: Medium
# Tags     : Array, Backtracking, Bit Manipulation
# URL      : https://leetcode.com/problems/subsets-ii/
# Solved on: 2026-06-17 16:13
# ──────────────────────────────────────────────────

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        idx=0
        def solve(idx,subset):
            
            if idx>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[idx])
            solve(idx+1,subset)

            subset.pop()
            next_idx = idx + 1
            while next_idx < len(nums) and nums[next_idx] == nums[idx]:
                next_idx += 1
                
            solve(next_idx, subset)
        solve(0,[])
        return res


