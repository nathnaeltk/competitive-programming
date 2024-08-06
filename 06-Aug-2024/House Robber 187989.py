# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i < 0:
                return 0
            if i in memo:
                return memo[i]
            # Choose to rob the current house or skip it
            memo[i] = max(dp(i-1), dp(i-2) + nums[i])
            return memo[i]

        memo = {}
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        return dp(len(nums) - 1)