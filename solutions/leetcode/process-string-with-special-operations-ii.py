# Problem  : Process String with Special Operations II
# Difficulty: Hard
# Tags     : String, Simulation
# URL      : https://leetcode.com/problems/process-string-with-special-operations-ii/
# Solved on: 2026-06-18 13:44
# ──────────────────────────────────────────────────

class Solution:
    def processStr(self, s: str, k: int) -> str:
        LIMIT = 10**15 + 1

        n = len(s)
        length = [0] * (n + 1)

        # Forward pass: store lengths
        for i in range(n):
            if s[i].islower():
                length[i + 1] = min(LIMIT, length[i] + 1)

            elif s[i] == '*':
                length[i + 1] = max(0, length[i] - 1)

            elif s[i] == '#':
                length[i + 1] = min(LIMIT, length[i] * 2)

            else:  # '%'
                length[i + 1] = length[i]

        if k >= length[n]:
            return '.'

        # Backward pass: trace kth character
        for i in range(n - 1, -1, -1):
            ch = s[i]

            if ch.islower():
                if k == length[i]:
                    return ch

            elif ch == '*':
                # deletion affects only the last character
                pass

            elif ch == '#':
                prev_len = length[i]
                k %= prev_len

            else:  # '%'
                k = length[i] - 1 - k

        return '.'
