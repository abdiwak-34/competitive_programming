class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        result = [[-1] * n for _ in range(m)]
        queue = deque()
        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    queue.append((i, j))

        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if inbound(nx, ny) and result[nx][ny] == -1:
                    result[nx][ny] = result[x][y] + 1
                    queue.append((nx, ny))

        return result