# Problem  : Find the Length of the Longest Common Prefix
# Difficulty: Medium
# Tags     : Array, Hash Table, String, Trie
# URL      : https://leetcode.com/problems/find-the-length-of-the-longest-common-prefix/
# Solved on: 2026-05-22 15:32
# ──────────────────────────────────────────────────

class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        
        prefixes = set()

        for num in arr1:
            s = str(num)

            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        ans = 0

        for num in arr2:
            s = str(num)

            for i in range(1, len(s) + 1):
                if s[:i] in prefixes:
                    ans = max(ans, i)

        return ans
