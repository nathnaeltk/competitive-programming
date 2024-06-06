# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        subset = []
        def findSubsets(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            findSubsets(i + 1)
            
            subset.pop()
            findSubsets(i + 1)
            
        findSubsets(0)
        return result