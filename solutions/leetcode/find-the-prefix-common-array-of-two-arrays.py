# Problem  : Find the Prefix Common Array of Two Arrays
# Difficulty: Medium
# Tags     : Array, Hash Table, Bit Manipulation
# URL      : https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/
# Solved on: 2026-05-21 15:32
# ──────────────────────────────────────────────────

class Solution:
    def findThePrefixCommonArray(self, A, B):
        freq = {}
        ans = []
        c = 0

        for i in range(len(A)):

            freq[A[i]] = freq.get(A[i], 0) + 1
            if freq[A[i]] == 2:
                c += 1

            freq[B[i]] = freq.get(B[i], 0) + 1
            if freq[B[i]] == 2:
                c += 1

            ans.append(c)

        return ans
