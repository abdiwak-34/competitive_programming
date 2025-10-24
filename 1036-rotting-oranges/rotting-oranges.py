class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        time = 0
        def inbound(ro, co):
            return 0 <= ro < row and 0 <= co < col

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        dirn = [(0,-1),(1,0),(-1,0), (0,1)]
        while queue:
            new_rotten = 0
            for i in range(len(queue)):
                row1, col1 = queue.popleft()
                for dr, dc in dirn:
                    nr, nc = row1+dr, col1+dc
                    if inbound(nr, nc) and grid[nr][nc] == 1:
                        queue.append((nr,nc))
                        grid[nr][nc] = 2
                        fresh -= 1
                        new_rotten += 1

            if new_rotten > 0:
                time += 1
        return time if not fresh else -1