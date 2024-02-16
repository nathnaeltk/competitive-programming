class Solution:
    def firstUniqChar(self, s: str) -> int:
        charMap = {}

        for char in s:
            if char in charMap:
                charMap[char] += 1
            else:
                charMap[char] = 1

        for i in s:
            if charMap[i] == 1:
                return s.index(i)
        return -1
        