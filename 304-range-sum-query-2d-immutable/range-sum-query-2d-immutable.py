class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.point = [1,2,2,4]
        self.pre = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        self.last_row = [0]*len(matrix[0])
        for i in range(len(matrix)):
            self.last = 0
            for j in range(len(matrix[0])):
                self.last += self.matrix[i][j]
                self.last_row[j] += self.last
                self.pre[i][j] = self.last_row[j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        self.a = self.pre[row2][col2]
        self.b = self.pre[row1 - 1][col2] if row1 != 0 else 0
        self.c = self.pre[row2][col1 - 1] if col1 != 0 else 0
        self.d = self.pre[row1-1][col1-1] if col1 != 0 and row1 != 0 else 0
        self.res = self.a - self.b - self.c + self.d
        return self.res
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)