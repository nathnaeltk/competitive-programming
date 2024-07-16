# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0
        for i, j in zip((numOnes, numZeros, numNegOnes), (1, 0, -1)):
            curr = min(i, k)
            ans += curr * j
            k -= curr
            if k == 0 :
                return ans

        return ans