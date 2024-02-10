class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        result = []
        for i in nums:
            if i > 0:
                positives.append(i)
            elif i < 0:
                negatives.append(i)
        for i in range(len(positives)):
            result.append(positives[i])
            result.append(negatives[i])
            
        return result