class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1],[1,1]]
        if numRows == 2:
            return res
        for j in range(1,numRows-1):
            current_row = []
            for i in range(j):
                current_row.append(res[-1][i] + res [-1][i+1])
            res.append([1] + current_row + [1])
        return res