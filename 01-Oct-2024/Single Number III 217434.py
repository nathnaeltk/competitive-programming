# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        numCounter = Counter(nums)
        for i,j in numCounter.most_common()[-2:]:
            res.append(i)
        return(res)