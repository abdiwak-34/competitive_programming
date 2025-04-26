class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m

        queue = deque([(sr, sc)])
        b_color = image[sr][sc]
        if b_color == color:
            return image
        dirn = [(-1,0),(0,-1),(0,1),(1,0)]
        
        while queue:
            r,c = queue.popleft()
            image[r][c] = color
            for nr, nc in dirn:
                if inbound(r+nr, c+nc) and image[r+nr][c+nc] == b_color:
                    queue.append((r+nr,c+nc))
                
        return image