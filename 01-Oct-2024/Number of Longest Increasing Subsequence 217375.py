# Problem: Number of Longest Increasing Subsequence - https://leetcode.com/problems/number-of-longest-increasing-subsequence/

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        if n == 0:
            return 0
        
        lengths = [1] * n
        counts = [1] * n
        for i in range(1,n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j]
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j]

        
        max_length= max(lengths)
        total_count= sum(count for length , count in zip(lengths,counts) if length == max_length)

        return total_count