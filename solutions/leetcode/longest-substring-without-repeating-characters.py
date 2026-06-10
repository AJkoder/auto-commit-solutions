# Problem  : Longest Substring Without Repeating Characters
# Difficulty: Medium
# Tags     : Hash Table, String, Sliding Window
# URL      : https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Solved on: 2026-06-10 20:49
# ──────────────────────────────────────────────────

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        l=0
        mx=0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])

            mx = max(mx, r-l+1)
        return mx



