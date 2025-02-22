class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.col = len(self.matrix[0])+1
        self.row = len(self.matrix)+1
        self.presum = [[0] * self.col for _ in range(self.row)]

        for i in range(1,self.row):
            for j in range(1,self.col):
                self.presum[i][j] = (
                    self.presum[i][j-1] +
                    self.presum[i-1][j] -
                    self.presum[i-1][j-1] +
                    self.matrix[i-1][j-1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.presum[row2+1][col2+1] - 
            self.presum[row1][col2+1] - 
            self.presum[row2+1][col1] +
            self.presum[row1][col1]
        )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)