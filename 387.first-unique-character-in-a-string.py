#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start
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
        
# @lc code=end

