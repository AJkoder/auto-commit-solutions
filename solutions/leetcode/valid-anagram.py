# Problem  : Valid Anagram
# Difficulty: Easy
# Tags     : Hash Table, String, Sorting
# URL      : https://leetcode.com/problems/valid-anagram/
# Solved on: 2026-05-21 15:32
# ──────────────────────────────────────────────────

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        arr=[0]*26
        
        for ch in s:
           idx = ord(ch) - ord('a')
           arr[idx]+=1
            
        for ch in t:
            idx = ord(ch) - ord('a')
            arr[idx]-=1
        
        for i in arr:
            if i!=0:
                return False
        return True
           
