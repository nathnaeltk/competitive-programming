class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left_pointer, right_pointer = 0, len(height) - 1

        while left_pointer < right_pointer:
            h = min(height[left_pointer], height[right_pointer])
            width = right_pointer - left_pointer
            current_area = h * width

            max_area = max(max_area, current_area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area
