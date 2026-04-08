# Problem  : Lemonade Change
# Difficulty: Easy
# Tags     : Array, Greedy
# URL      : https://leetcode.com/problems/lemonade-change/
# Solved on: 2026-04-08 18:10
# ──────────────────────────────────────────────────

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        i=0
        while i<len(bills):
            if bills[i]==5:
                five+=1
                i+=1
            elif bills[i]==10:
                if five >0:
                    five-=1
                    ten+=1
                    i+=1
                else:
                    return False
            else:
                if five>0 and ten>0:
                    five-=1
                    ten-=1
                    i+=1
                elif five>=3:
                    five-=3
                    i+=1
                else:
                    return False
        return True


