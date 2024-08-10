# Problem: Minimum Path Sum - https://leetcode.com/problems/minimum-path-sum/description/

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        def dp(x, y):
            if x >= m or y >= n:
                return float('inf')
            
            if x == m - 1 and y == n - 1:
                return grid[x][y]

            if memo[x][y] != -1:
                return memo[x][y]

            memo[x][y] = grid[x][y] + min(dp(x + 1, y), dp(x, y + 1))
            return memo[x][y]

        return dp(0, 0)