class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1

        for idx in range(1, len(arr)):

            if arr[idx] - arr[idx - 2] > 1: 
                arr[idx] = arr[idx - 1] + 1
        
        return arr[-1]