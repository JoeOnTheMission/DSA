class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pre = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        last_row = [0]*len(matrix[0])
        for i in range(len(matrix)):
            last = 0
            for j in range(len(matrix[0])):
                last += matrix[i][j]
                last_row[j] += last
                self.pre[i][j] = last_row[j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.pre[row2][col2]
        b = self.pre[row1 - 1][col2] if row1 != 0 else 0
        c = self.pre[row2][col1 - 1] if col1 != 0 else 0
        d = self.pre[row1-1][col1-1] if col1 != 0 and row1 != 0 else 0
        return a - b - c + d
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)