# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        q = [entrance]
        vis = {(entrance[0], entrance[1])}
        ans = 0
        while(q):
            l = len(q)
            ans += 1
            for _ in range(l):
                [i, j] = q.pop(0)
                if((i == 0 or i == m-1 or j == 0 or j == n-1) and [i, j] != entrance):
                    return ans-1
                for x, y in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                    if(0<=i+x<m and 0<=j+y<n and maze[i+x][j+y] == "." and (i+x, j+y) not in vis):
                        vis.add((i+x, j+y))
                        q.append([i+x, j+y])
        return -1