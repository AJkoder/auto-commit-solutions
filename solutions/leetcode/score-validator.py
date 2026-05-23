# Problem  : Score Validator
# Difficulty: Easy
# Tags     : Array, String, Simulation
# URL      : https://leetcode.com/problems/score-validator/
# Solved on: 2026-05-23 19:16
# ──────────────────────────────────────────────────

class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score=0
        counter=0

        for i in events:
            if i=="W":
                counter+=1
                if counter==10:
                    return [score,counter]
            elif i=="WD":
                score+=1
            elif i=="NB":
                score+=1
            else:
                i=int(i)
                score+=i
        return [score,counter]
