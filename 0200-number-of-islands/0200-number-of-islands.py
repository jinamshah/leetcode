class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i,j):
            
            if i<0 or j<0 or i>=rows or j >=cols or grid[i][j] =='0':
                return
            
            grid[i][j] = '0'
            
            dfs(grid,i-1,j)
            dfs(grid,i+1,j)
            dfs(grid,i,j-1)
            dfs(grid,i,j+1)
            
        if not grid or len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        answer = 0
        for i in range(0, rows):
            for j in range(0,cols):
                if grid[i][j] == '1':
                    answer += 1
                    dfs(grid, i,j)
        return answer          