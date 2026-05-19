# Problem  : Merge Strings Alternately
# Difficulty: Easy
# Tags     : Two Pointers, String
# URL      : https://leetcode.com/problems/merge-strings-alternately/
# Solved on: 2026-05-19 17:59
# ──────────────────────────────────────────────────

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n=min(len(word1),len(word2))
        res=[]
        for i in range (n):
            res.append(word1[i])
            res.append(word2[i])
        if (len(word1)>len(word2)):
            res.append(word1[n:])
        else:
            res.append(word2[n:])

        result = "".join(res)

        return result

