# Problem: Unique Paths - https://leetcode.com/problems/unique-paths/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # memo = {} # coordinates: how many ways to get to that coordinate

        # def dp(x, y):
        #     if x > m or y > n:
        #         return 0
        #     if (x, y) == (m-1, n-1):
        #         return 1
        #     if (x, y) in memo:
        #         return memo[(x, y)]

        #     memo[(x, y)] = dp(x+1, y) + dp(x, y+1)
        #     return memo[(x, y)]

        # return dp(0, 0)

        grid = [[-1 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            grid[i][0] = 1 
        for j in range(n):
            grid[0][j] = 1 
        
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[m-1][n-1]