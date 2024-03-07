#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        for i in range(len(s)):
            if s[i] == 'I' and s[i+1] == 'V':
                s = s.replace('IV', 'IIIII')
            if s[i] == 'I' and s[i+1] == 'X':
                s = s.replace('IX', 'VIIII')
            if s[i] == 'X' and s[i+1] == 'L':
                s = s.replace('XL', 'XXXXX')
            if s[i] == 'X' and s[i+1] == 'C':
                s = s.replace('XC', 'LXXXX')
            if s[i] == 'C' and s[i+1] == 'D':
                s = s.replace('CD', 'CCCCC')
            

            if s[i] == 'I':
                s = s.replace('I', '1')
            if s[i] == 'V':
                s = s.replace('V', '5')
            if s[i] == 'X':
                s = s.replace('X', '10')
            if s[i] == 'L':
                s = s.replace('L', '50')
            if s[i] == 'C':
                s = s.replace('C', '100')
            if s[i] == 'D':
                s = s.replace('D', '500')
            if s[i] == 'M':
                s = s.replace('M', '1000')
            
        return sum(map(int, s))


        
# @lc code=end

