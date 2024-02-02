class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store the indices of numbers as we iterate through the array
        num_indices = {}

        for i, num in enumerate(nums):
            complement = target - num

            # Check if the complement is in the dictionary
            if complement in num_indices:
                # Return the indices of the two numbers that add up to the target
                return [num_indices[complement], i]
            
            # Store the current number's index in the dictionary
            num_indices[num] = i

        # If no solution is found
        return []
