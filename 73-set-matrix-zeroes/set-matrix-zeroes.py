class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        place  = []
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    place.append((i,j))
        
        for x, y in place:
            for k in range(m):
                matrix[x][k] = 0
        
        for x, y in place:
            for k in range(n):
                matrix[k][y] = 0
        