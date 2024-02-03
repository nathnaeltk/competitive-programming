class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0; 
        for element in operations: 
            if element == "X++" or element == "++X":
                result += 1
            elif element == "X--" or element == "--X":
                result -= 1
        return result