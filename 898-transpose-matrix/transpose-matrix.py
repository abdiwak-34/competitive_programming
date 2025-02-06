class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        transpose = [[0] * row for i in range(col)]
        for i in range(col):
            for j in range(row):
                transpose[i][j] = matrix[j][i]
        return transpose