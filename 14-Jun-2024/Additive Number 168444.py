# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def check_sequence(a: int, b: int, remaining: str) -> bool:
            if not remaining:
                return True
            
            c = a + b
            c_str = str(c)
            if remaining.startswith(c_str):
                return check_sequence(b, c, remaining[len(c_str):])
            
            return False
        
        length = len(num)
        
        for first_end in range(1, length):
            if first_end > 1 and num[0] == '0':
                break
            
            for second_end in range(first_end + 1, length):
                if second_end - first_end > 1 and num[first_end] == '0':
                    break
                
                first_num = int(num[:first_end])
                second_num = int(num[first_end:second_end])
                
                if check_sequence(first_num, second_num, num[second_end:]):
                    return True
        
        return False