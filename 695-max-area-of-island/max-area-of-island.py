class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirn = [(-1,0),(0,-1),(0,1),(1,0)]
        def inbound(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        
        def dfs(row,col):
            area = 1
            grid[row][col] = 0
            for r,c in dirn:
                if inbound(r+row, c+col) and grid[r+row][c+col] == 1:
                    area += dfs(r+row, c+col)
            return area


        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i,j))
        return max_area