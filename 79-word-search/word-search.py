class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])

        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m

        def dfs(r, c, cur):
            if cur == len(word):
                return True
            if not inbound(r, c) or board[r][c] != word[cur]:
                return False

            temp = board[r][c]
            board[r][c] = '#'

            for dr, dc in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                if dfs(r + dr, c + dc, cur + 1):
                    return True

            board[r][c] = temp
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False
