# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit, curr = set(), deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visit.add((i, j))
                elif grid[i][j] == 2:
                    curr.append((i, j))
        result = 0
        while visit and curr:
            for _ in range(len(curr)):
                i, j = curr.popleft() 
                for coord in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if coord in visit: 
                        visit.remove(coord)
                        curr.append(coord)
            result += 1
		
        return -1 if visit else result