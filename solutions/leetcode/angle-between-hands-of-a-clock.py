# Problem  : Angle Between Hands of a Clock
# Difficulty: Medium
# Tags     : Math
# URL      : https://leetcode.com/problems/angle-between-hands-of-a-clock/
# Solved on: 2026-06-19 12:46
# ──────────────────────────────────────────────────

class Solution:
    def angleClock(self, hour, minutes):

        angle = abs((30 * hour) - (5.5 * minutes))

        return min(angle, 360 - angle)
