class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        index_map = {num: i for i, num in enumerate(nums)}
        
        # {number: its index}

        for operation in operations:
            old_num, new_num = operation[0], operation[1]
            idx = index_map[old_num]
            nums[idx] = new_num
            index_map[new_num] = idx
            del index_map[old_num]

        return nums