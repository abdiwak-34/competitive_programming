class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        prefix = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        ans = [[0] * m for _ in range(n)]
        for i in range(1, len(prefix)):
            for j in range(1, len(prefix[0])):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + mat[i-1][j-1]
        def makevalid(g,h):
            start = [0,0]
            end = [n-1,m-1]
            start[0] = max(start[0], g-k)
            start[1] = max(start[1], h-k)
            end[0] = min(end[0], g+k)
            end[1] = min(end[1], h+k)
            return [start, end]
        for i in range(n):
            for j in range(m):
                start, end = makevalid(i,j)
                ans[i][j] = prefix[end[0]+1][end[1]+1] - prefix[end[0]+1][start[1]] - prefix[start[0]][end[1]+1] + prefix[start[0]][start[1]]
        return ans