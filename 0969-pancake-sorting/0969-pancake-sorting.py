class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        flips = []
        n = len(arr)
        
        def flip(subarr_end):
            flips.append(subarr_end + 1)
            arr[:subarr_end + 1] = reversed(arr[:subarr_end + 1])
        
        for i in range(n - 1, 0, -1):
            max_index = arr.index(max(arr[:i + 1]))
            if max_index != i:
                if max_index != 0:
                    flip(max_index)
                flip(i)
            
        return flips
