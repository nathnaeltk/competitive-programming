# Problem: Knight Probability in Chessboard - https://leetcode.com/problems/knight-probability-in-chessboard/

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        memo = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(k + 1)]
        directions = (
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        )
        def dfs(r, c, k):
            if k == 0:
                return 1
            if memo[k][r][c] != -1:
                return memo[k][r][c]
            prob = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not (0<=nr<n and 0<=nc<n): continue
                prob += dfs(nr,nc,k-1)/8.0
            memo[k][r][c] = prob
            return memo[k][r][c]
        return dfs(row,column,k)