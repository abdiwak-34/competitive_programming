class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        def inbound(ro, co):
            return 0 <= ro < row and 0 <= co < col

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        dirn = [(-1,0),(0,-1),(1,0),(0,1)]
        time = 0
        flag =True
        while queue and fresh > 0:
            for _ in range(len(queue)):
                rows, cols = queue.popleft()
                for a,b in dirn:
                    if inbound(rows+a, cols+b) and grid[rows+a][cols+b] == 1:
                        grid[rows+a][cols+b] = 2
                        fresh -= 1
                        queue.append((rows+a, cols+b))
            time += 1

        return time if fresh == 0 else -1