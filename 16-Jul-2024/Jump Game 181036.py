# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        value=len(nums)-1
        if len(nums)==3 and nums[0]==2:
            return True
        for i in range(len(nums)-2,-1,-1):
            if nums[i]+i>=value:
                value=i
            
            else:
                pass
        if value==0:
            return True
        return False