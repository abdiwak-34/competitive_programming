class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10**9 + 7
        m, n = len(target), len(words[0])
        freq = [defaultdict(int) for _ in range(n)]
        for word in words:
            for j, ch in enumerate(word):
                freq[j][ch] += 1
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for k in range(n + 1):
            dp[m][k] = 1
        for i in range(m - 1, -1, -1):
            for k in range(n - 1, -1, -1):
                dp[i][k] = dp[i][k + 1]
                if target[i] in freq[k]:
                    dp[i][k] += freq[k][target[i]] * dp[i + 1][k + 1]
                    dp[i][k] %= MOD
        return dp[0][0]