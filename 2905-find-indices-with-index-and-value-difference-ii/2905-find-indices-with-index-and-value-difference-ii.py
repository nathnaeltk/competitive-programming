class Solution:
    def findIndices(
        self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        min, max = 0, 0
        for i in range(indexDifference, len(nums)):
            j = i - indexDifference
            if nums[j] < nums[min]:
                min = j
            if nums[j] > nums[max]:
                max = j
            if nums[i] - nums[min] >= valueDifference:
                return [min, i]
            if nums[max] - nums[i] >= valueDifference:
                return [max, i]
        return [-1, -1]