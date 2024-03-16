class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        
        count_dict = {}
        for idx, num in enumerate(sorted_nums):
            if num not in count_dict:
                count_dict[num] = idx
        
        result = []
        for num in nums:
            result.append(count_dict[num])
        
        return result
