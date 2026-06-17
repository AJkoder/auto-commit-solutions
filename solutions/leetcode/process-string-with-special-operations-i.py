# Problem  : Process String with Special Operations I
# Difficulty: Medium
# Tags     : String, Simulation
# URL      : https://leetcode.com/problems/process-string-with-special-operations-i/
# Solved on: 2026-06-17 16:13
# ──────────────────────────────────────────────────

class Solution:
    def processStr(self, s: str) -> str:
        res=[]
        
        for i in range (len(s)):
            if s[i].islower():
                res.append(s[i])
            elif len(res)!=0 and s[i]=="*":
                res.pop()
            elif s[i]=="#":
                res.extend(res)
            elif s[i]=="%":
                res=res[::-1]
        return "".join(res)
            



