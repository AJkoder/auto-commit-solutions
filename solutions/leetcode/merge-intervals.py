# Problem  : Merge Intervals
# Difficulty: Medium
# Tags     : Array, Sorting
# URL      : https://leetcode.com/problems/merge-intervals/
# Solved on: 2026-06-04 00:57
# ──────────────────────────────────────────────────

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        res = [intervals[0]]

        for i in range(1, len(intervals)):

            curr = intervals[i]
            last = res[-1]

            if curr[0] <= last[1]:
                last[1] = max(last[1], curr[1])
            else:
                res.append(curr)

        return res
