# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        # convert the string into digits.
        s = [int(i) for i in list(s)]
        
        def r(base, index, nums):
            d = 0
            acc = 0
            res = False
            for x in range(index,-1,-1):
                acc += (10**d)*nums[x]

                if base + 1 == acc:
                    if x-1 >= 0:
                        res = res or r(acc, x-1, s)
                    else:
                        res = True
                d+=1
            return res
                
        d = 0
        ans = False
        acc = 0
        for x in range(len(s)-1,-1,-1):
            acc += (10**d)*s[x]
            ans = ans or r(acc, x-1, s)
            d+=1
        return ans