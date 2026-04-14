# Problem  : Mirror Frequency Distance
# Difficulty: Medium
# Tags     : Hash Table, String, Counting
# URL      : https://leetcode.com/problems/mirror-frequency-distance/
# Solved on: 2026-04-14 21:03
# ──────────────────────────────────────────────────

class Solution:
    def mirrorFrequency(self, s: str) -> int:
        if len(s)==1:
            return 1
        freq={}
        c=0
        seen=set()
        for i in s:
          freq[i]=freq.get(i,0)+1
        for ch in s:
            if ch in "0123456789":
                mirror=str(9-int(ch))
            else:
                mirror=chr(219-ord(ch))
            first=freq.get(ch,0)
            second=freq.get(mirror,0)
            pair = tuple(sorted([ch,mirror]))
            if pair not in seen:
                diff=abs(first-second)
                c+=diff
            seen.add(pair)
        return c
            
      
    
