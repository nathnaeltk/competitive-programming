class Solution:
    def minSubArrayLen(target, nums):
        if not nums:
            return 0
        
        min_length = len(nums) + 1
        
        for i in range(len(nums)):
            j = i
            total = 0
            while j < len(nums) and total < target:
                total += nums[j]
                j += 1
            if total >= target:
                min_length = min(min_length, j - i)
        
        return min_length if min_length <= len(nums) else 0
