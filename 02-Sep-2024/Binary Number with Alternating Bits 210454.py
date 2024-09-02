# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:

        nu=bin(n)[2:]
        for i in range(len(nu)-1):
            if nu[i]==nu[i+1]:
                return False
        return True