# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        d = {1:[(0,-1),(0,1)],2:[(-1,0),(1,0)],3:[(0,-1),(1,0)],4:[(0,1),(1,0)],5:[(0,-1),(-1,0)],6:[(0,1),(-1,0)]}

        stack, visited = [(0,0)], set((0,0))

        while stack:
            i,j = stack.pop()

            if i == m-1 and j == n-1:
                return True

            for c in d[grid[i][j]]:
                if 0 <= i+c[0] < m and 0 <= j+c[1] < n and (i+c[0],j+c[1]) not in visited and (-c[0],-c[1]) in d[grid[i+c[0]][j+c[1]]]:
                    stack.append((i+c[0],j+c[1]))
                    visited.add((i+c[0],j+c[1]))

        return False