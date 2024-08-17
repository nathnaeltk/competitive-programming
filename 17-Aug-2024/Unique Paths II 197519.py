# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0] or obstacleGrid[0][0] == 1:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        previous = [0] * n
        current = [0] * n
        
        previous[0] = 1
        
        for i in range(m):
            current[0] = 0 if obstacleGrid[i][0] == 1 else previous[0]
            
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    current[j] = 0
                else:
                    current[j] = current[j-1] + previous[j]
            
            previous[:] = current
        
        return previous[n-1]