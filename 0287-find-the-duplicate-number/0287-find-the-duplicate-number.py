class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        newNums = nums
        newNums.sort()
        for i in range(len(newNums)-1):
            if newNums[i] == newNums[i+1]:
                return newNums[i]