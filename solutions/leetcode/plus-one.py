# Problem  : Plus One
# Difficulty: Easy
# Tags     : Array, Math
# URL      : https://leetcode.com/problems/plus-one/
# Solved on: 2026-05-28 19:39
# ──────────────────────────────────────────────────

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[-1] < 9:
            digits[-1] += 1
            return digits

        num = "".join(map(str, digits))
        new_num = int(num) + 1

        return list(map(int, str(new_num)))
            
