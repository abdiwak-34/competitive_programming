class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                if i-1 >=0 and j-1 >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                elif i-1 >= 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[n-1][m-1]