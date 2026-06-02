# Problem  : Digit Frequency Score
# Difficulty: Easy
# Tags     : 
# URL      : https://leetcode.com/problems/digit-frequency-score/
# Solved on: 2026-06-02 15:45
# ──────────────────────────────────────────────────

class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n=str(n)
        freq={}
        score=0
        for i in n:
            freq[i]=freq.get(i,0)+1
        for key,val in freq.items():
            score+=int(key)*int(val)
        return score
