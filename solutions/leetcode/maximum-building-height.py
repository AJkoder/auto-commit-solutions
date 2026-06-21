# Problem  : Maximum Building Height
# Difficulty: Hard
# Tags     : Array, Math, Sorting
# URL      : https://leetcode.com/problems/maximum-building-height/
# Solved on: 2026-06-21 20:09
# ──────────────────────────────────────────────────

#translated using AI
class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        arr = [[1, 0]]

        arr.extend(restrictions)

        arr.sort()

        # Left to right pass
        for i in range(1, len(arr)):
            d = arr[i][0] - arr[i - 1][0]
            arr[i][1] = min(arr[i][1], arr[i - 1][1] + d)

        # Right to left pass
        for i in range(len(arr) - 2, -1, -1):
            d = arr[i + 1][0] - arr[i][0]
            arr[i][1] = min(arr[i][1], arr[i + 1][1] + d)

        ans = 0

        for i in range(1, len(arr)):
            x1, h1 = arr[i - 1]
            x2, h2 = arr[i]

            d = x2 - x1

            ans = max(ans, (h1 + h2 + d) // 2)

        lastPos, lastH = arr[-1]

        ans = max(ans, lastH + (n - lastPos))

        return ans
