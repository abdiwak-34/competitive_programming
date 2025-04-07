class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        parameter = 0

        def count(i,j):
            nonlocal parameter
            dir = [[-1,0], [0,-1], [1,0], [0,1]]
            for r,c in dir:
                if inbound(i+r, j+c) and grid[i+r][j+c] == 1:
                    continue
                else:
                    parameter += 1
        

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    count(i,j)
        return parameter