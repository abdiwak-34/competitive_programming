class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def inbound(r,c):
            return 0 <= r < m and 0 <= c < n
        if not grid or not grid[0]:
            return 0
        
        islands = 0

        def bfs(r, c):
            queue = deque()
            dirn = [(-1,0), (0,-1), (1,0), (0,1)]
            grid[r][c] = "0"
            queue.append((r,c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in dirn:
                    nr, nc = row + dr, col + dc
                    if inbound(nr, nc) and grid[nr][nc] == '1':
                        queue.append((nr, nc))
                        grid[nr][nc] = '0'
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i, j)
                    islands += 1
        return islands