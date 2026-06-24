# Problem  : Number of ZigZag Arrays I
# Difficulty: Hard
# Tags     : Dynamic Programming, Prefix Sum
# URL      : https://leetcode.com/problems/number-of-zigzag-arrays-i/
# Solved on: 2026-06-24 15:01
# ──────────────────────────────────────────────────

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 1000000007
        m = r - l + 1
        dp = [1] * m

        for i in range(2, n + 1):
            dp.reverse()
            s = 0
            for j in range(m):
                dp[j], s = s, (s + dp[j]) % MOD

        return (sum(dp) % MOD << 1) % MOD
