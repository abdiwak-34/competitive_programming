class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        matrix2 = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix2[j][i] = matrix[i][j]
        return matrix2