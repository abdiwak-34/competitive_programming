class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_pos(s):
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if quot % 2 == 0 else n - 1 - rem
            return row, col
        
        jumps = {}
        for i in range(n):
            for j in range(n):
                if board[i][j] != -1:
                    row, col = get_pos(board[i][j])
                    quot = n - 1 - i
                    if quot % 2 == 0:
                        s = quot * n + j + 1
                    else:
                        s = quot * n + (n - 1 - j) + 1
                    jumps[s] = board[i][j]
        
        from collections import deque
        queue = deque()
        queue.append((1, 0))
        visited = set()
        visited.add(1)
        
        while queue:
            s, moves = queue.popleft()
            if s == n * n:
                return moves
            for i in range(1, 7):
                next_s = s + i
                if next_s > n * n:
                    continue
                if next_s in jumps:
                    next_s = jumps[next_s]
                if next_s not in visited:
                    visited.add(next_s)
                    queue.append((next_s, moves + 1))
        return -1