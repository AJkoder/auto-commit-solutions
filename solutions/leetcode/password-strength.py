# Problem  : Password Strength
# Difficulty: Medium
# Tags     : 
# URL      : https://leetcode.com/problems/password-strength/
# Solved on: 2026-05-24 15:17
# ──────────────────────────────────────────────────

class Solution:
    def passwordStrength(self, password: str) -> int:
        seen=set()
        score=0
        for ch in password:
            if ch in seen:
                continue
            elif ch in "abcdefghijklmnopqrstuvwxyz":
                score+=1
            elif ch in "0123456789":
                score+=3
            elif ch in "!@#$":
                score+=5
            else:
                score+=2
            seen.add(ch)
        return score
            
