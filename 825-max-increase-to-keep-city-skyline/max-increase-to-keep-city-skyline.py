class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        max_row = []
        for row in grid:
            max_row.append(max(row))
        max_col = []
        
        for i in range(n):
            maximum = 0
            for j in range(n):
                maximum = max(maximum, grid[j][i])
            max_col.append(maximum)
        
        total = 0
        for i in range(n):
            for j in range(n):
                total += (min(max_col[j], max_row[i]) - grid[i][j])
        return total
