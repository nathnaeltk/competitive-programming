class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans=0
        def read(grid,i,j):
            if(i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1'):
                return
            grid[i][j]='0'
            read(grid,i-1,j)
            read(grid,i+1,j)
            read(grid,i,j-1)
            read(grid,i,j+1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j]=='1'):
                    ans+=1
                    read(grid,i,j)
        return ans