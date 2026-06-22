# Problem  : Maximum Number of Balloons
# Difficulty: Easy
# Tags     : Hash Table, String, Counting
# URL      : https://leetcode.com/problems/maximum-number-of-balloons/
# Solved on: 2026-06-23 00:22
# ──────────────────────────────────────────────────

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        freq={"b":0,"a":0,"l":0,"o":0,"n":0}
        for ch in text:
            freq[ch]=freq.get(ch,0)+1
        for key,val in freq.items():
            b=freq['b']
            a=freq["a"]
            l=(freq["l"]//2)
            o=(freq["o"]//2)
            n=(freq["n"])
        return min(b,a,l,o,n)
        
        
