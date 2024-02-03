class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0; 
        for element in operations: 
            if "++" in element:
                result += 1
            elif "--" in element:
                result -= 1
        return result