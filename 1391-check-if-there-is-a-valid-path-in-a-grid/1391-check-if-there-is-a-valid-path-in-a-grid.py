from collections import deque

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        def isPathValid(self, grid: List[List[int]]) -> bool:
            direction_map = {
                1: [(0, -1), (0, 1)],
                2: [(-1, 0), (1, 0)],
                3: [(0, -1), (1, 0)],
                4: [(0, 1), (1, 0)],
                5: [(0, -1), (-1, 0)],
                6: [(0, 1), (-1, 0)]
            }

            def canMove(grid, x, y, next_x, next_y):
                if next_x < 0 or next_x >= len(grid) or next_y < 0 or next_y >= len(grid[0]):
                    return False
                next_tile = grid[next_x][next_y]
                for dx, dy in direction_map[next_tile]:
                    if next_x + dx == x and next_y + dy == y:
                        return True
                return False

            def bfs(grid):
                rows, cols = len(grid), len(grid[0])
                visited = [[False] * cols for _ in range(rows)]
                queue = deque([(0, 0)])

                while queue:
                    x, y = queue.popleft()

                    if x == rows - 1 and y == cols - 1:
                        return True

                    if visited[x][y]:
                        continue

                    visited[x][y] = True
                    for dx, dy in direction_map[grid[x][y]]:
                        next_x, next_y = x + dx, y + dy
                        if canMove(grid, x, y, next_x, next_y):
                            queue.append((next_x, next_y))

                return False

            return bfs(grid)