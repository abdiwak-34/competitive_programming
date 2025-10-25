class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque()
        queue.append((0, (0, 0, k)))
        visted = set([(0, 0, k)])

        dirn = [(-1,0), (1,0), (0,-1), (0,1)]
        def inbound(ro, co):
            return 0 <= ro < row and 0 <= co < col

        while queue:
            steps, (r, c, remain) = queue.popleft()

            if r== row-1 and c == col-1:
                return steps
            for dr, dc in dirn:
                nr, nc = r+dr, c+dc
                if not inbound(nr, nc):
                    continue
                
                if grid[nr][nc] == 1 and remain > 0:
                    new_state = (nr, nc, remain - 1)
                elif grid[nr][nc] == 0:
                    new_state = (nr, nc, remain)
                else:
                    continue
                
                if new_state not in visted:
                    visted.add(new_state)
                    queue.append((steps+1, new_state))
            
        return -1