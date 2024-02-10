class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
    
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                count += 1

                if count > 1:
                    return False

                # Choose which element to modify
                if i >= 2 and nums[i - 2] > nums[i]:
                    nums[i] = nums[i - 1]  # Modify the current element
                else:
                    nums[i - 1] = nums[i]  # Modify the previous element

        return True