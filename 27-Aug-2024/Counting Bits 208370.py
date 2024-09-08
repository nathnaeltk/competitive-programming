# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(0,n+1):
            ans[i] = ans[i>>1] + (i & 1)
        return ans
            