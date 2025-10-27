class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])

        def inbound(ro, co):
            return 0 <= ro < n and 0 <= co < m

        memo = [[-1] * m for _ in range(n)]
        def findlong(r, c):
            if memo[r][c] != -1:
                return memo[r][c]
            dirn = [(-1,0), (1,0), (0,-1), (0,1)]
            max_path = 1

            for dr, dc in dirn:
                nr, nc = r+dr, c+dc
                if inbound(nr, nc) and matrix[r][c] < matrix[nr][nc]:
                    max_path = max(max_path, 1 + findlong(nr, nc))
                
            memo[r][c] = max_path
            return max_path
        ans = 0
        for i in range(n):
            for j in range(m):
                ans = max(findlong(i, j), ans)
        return ans