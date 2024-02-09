class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num == 0:
            return [-1, 0, 1]
        
        if num % 3 != 0 or num < 3:
            return []


        middle = num // 3

        return [middle - 1, middle, middle + 1]