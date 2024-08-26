# Problem: House Robber II - https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        dp = {}
        def getResult(a,i):
            if i>=len(a):
                return 0
            if i in dp:
                return dp[i]
            
            sum = 0
            if i<len(a)-1:
                sum+= max(a[i]+getResult(a,i+2),a[i+1]+getResult(a,i+3))
            else:
                sum+=a[i]+getResult(a,i+2)
            dp[i] = sum
            return sum
            
        x = getResult(nums[:len(nums)-1],0)
        dp = {}
        y = getResult(nums[1:],0)
            
        return max(x, y)