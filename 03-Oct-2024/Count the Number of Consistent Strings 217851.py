# Problem: Count the Number of Consistent Strings - https://leetcode.com/problems/count-the-number-of-consistent-strings/

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        hash = set()
        for i in allowed:
            hash.update(i)

        for word in words:
            check = 1   
            for char in word:
                if char not in hash: 
                    check = 0
            if check == 1: res+=1
        return res