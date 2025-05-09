class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def inbound(row, col):
            return 0 <= row < len(matrix) and 0 <= col < len(matrix[0])
        @cache
        def dfs(r, c):
            res =1
            dirn = [(0,1),(1,0),(-1,0),(0,-1)]
            for dx, dy in dirn:
                x = r+dx
                y = c+ dy
                if inbound(x,y) and matrix[x][y] > matrix[r][c]:
                    res = max(res, 1+dfs(x,y))
            return res

        height = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                height = max(height, dfs(i,j))
        
        return height