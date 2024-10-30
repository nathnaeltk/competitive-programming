# Problem: Find Indices With Index and Value Difference I - https://leetcode.com/problems/find-indices-with-index-and-value-difference-i/description/

class Solution:
    def findIndices(self,nums,indexDiff,valueDifference):
        Initial=[]
        if indexDiff==0 and valueDifference==0:
            return [0,0]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)): 
                if abs(i-j)>=indexDiff  and abs(nums[i]-nums[j])>=valueDifference:
                    Initial=[i,j]
        if not Initial:return [-1,-1]
        else:return Initial