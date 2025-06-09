class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        orginal = image[sr][sc]
        def inbound(r, c):
            return 0 <= r < n and 0 <= c < m
        
        visted = [[False] * m for _ in range(n)]

        def dfs(r,c):
            dirn = [(-1,0),(0,-1),(0,1),(1,0)]

            if not inbound(r,c) or visted[r][c] or image[r][c] != orginal:
                return
            visted[r][c] = True
            image[r][c] = color
            for dr,dc in dirn:
                dfs(r+dr, c+dc)
        
        dfs(sr,sc)

        return image
                