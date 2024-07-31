# Problem: Maximum Element After Decreasing and Rearranging - https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1

        for idx in range(1, len(arr)):

            if arr[idx] - arr[idx - 1] > 1: 
                arr[idx] = arr[idx - 1] + 1
        
        return arr[-1]