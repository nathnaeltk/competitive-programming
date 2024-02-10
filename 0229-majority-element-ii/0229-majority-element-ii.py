class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums) // 3

        nums_freq_map = {}
        for num in nums:
            nums_freq_map[num] = nums_freq_map.get(num, 0) + 1

        return [x for x, y in nums_freq_map.items() if y > n]