class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visted = [[False for _ in range(len(grid[0]))] for i in range(len(grid))]

        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def dfs(row,col):
            dir = [(-1,0),(0,-1),(1,0),(0,1)]
            visted[row][col] = True
            
            for r,c in dir:
                if inbound(r+row, c+col) and grid[r+row][c+col] == "1" and not visted[r+row][c+col]:
                    dfs(r+row, c+col)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visted[i][j] and grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
         
        return count