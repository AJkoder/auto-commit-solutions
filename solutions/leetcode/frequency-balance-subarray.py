# Problem  : Frequency Balance Subarray
# Difficulty: Medium
# Tags     : 
# URL      : https://leetcode.com/problems/frequency-balance-subarray/
# Solved on: 2026-06-14 14:55
# ──────────────────────────────────────────────────

class Solution:
    def getLength(self, nums: List[int]) -> int:
        n=len(nums)
        res=1
        for i in range(n):
            freq={}
            count={}
            for j in range(i,n):
                num=nums[j]

                a=freq.get(num,0)
                if a>0:
                    count[a]-=1
                    if count[a]==0:
                        del count[a]
                
                freq[num]=a+1
                b=a+1
                count[b]=count.get(b,0)+1

                if len(freq)==1:
                    res=max(res,j-i+1)
                    continue
                    

                if len(count)!=2:
                    continue
                f,v=sorted(count.keys())

                if v==2*f:
                    res=max(res,j-i+1)
        return res
                
                    
