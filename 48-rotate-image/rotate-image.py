class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(i, m):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse()
            