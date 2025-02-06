class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n, m = len(matrix), len(matrix[0])
        query = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    query.append([i,j])
        for quer in query:
            i, j = quer
            for k in range(n):
                matrix[k][j] = 0
            for l in range(m):
                matrix[i][l] = 0