class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs_recursive(i, j):
            if i == 0 or j == 0:
                return 0
            
            if text1[i - 1] == text2[j - 1]:
                return 1 + lcs_recursive(i - 1, j - 1)
            
            return max(lcs_recursive(i - 1, j), lcs_recursive(i, j - 1))
        
        m, n = len(text1), len(text2)
        return lcs_recursive(m, n)