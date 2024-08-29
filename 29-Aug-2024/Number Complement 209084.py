# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution(object):
    def findComplement(self, num):
        binary = list(bin(num)[2:])

        for i in range(len(binary)):
            if binary[i] == '1':
                binary[i] = '0'
            else:
                binary[i] = '1'

        return int("".join(binary), base=2)