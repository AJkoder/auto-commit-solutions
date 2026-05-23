# Problem  : Minimum Flips to Make Binary String Coherent
# Difficulty: Medium
# Tags     : String
# URL      : https://leetcode.com/problems/minimum-flips-to-make-binary-string-coherent/
# Solved on: 2026-05-23 20:32
# ──────────────────────────────────────────────────

class Solution:
    def minFlips(self, s: str) -> int:
        one=0
        zero=0
        n=len(s)
        if n==1:
            return 0
        for num in s:
            if num=="0":
                zero+=1
            else:
                one+=1
        flip_all_zero=one
        flip_all_one=zero

        if flip_all_zero>0:
            flip_one_one=flip_all_zero-1
        else:
            flip_one_one=flip_all_zero

        if s[0]=="1" and s[-1]=="1":
            flip_two_one=flip_all_zero-2
        else:
            flip_two_one=flip_all_zero

        return min(flip_all_zero,flip_all_one,flip_one_one,flip_two_one)
        
        
