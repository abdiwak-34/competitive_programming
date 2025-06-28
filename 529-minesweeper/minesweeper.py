class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        
        def count_mines(r, c):
            count = 0
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == 'M':
                    count += 1
            return count
        
        def dfs(r, c):
            if board[r][c] != 'E':
                return
            mine_count = count_mines(r, c)
            if mine_count == 0:
                board[r][c] = 'B'
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        dfs(nr, nc)
            else:
                board[r][c] = str(mine_count)
        
        r, c = click
        if board[r][c] == 'M':
            board[r][c] = 'X'
        else:
            dfs(r, c)
        
        return board