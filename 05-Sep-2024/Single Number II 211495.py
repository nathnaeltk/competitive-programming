# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            j = 0
            while j < len(nums):
                if nums[i] == nums[j] and i != j:
                    break
                j += 1
            if j == len(nums):
                return nums[i]
        return -1  