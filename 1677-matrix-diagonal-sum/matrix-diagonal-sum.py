class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0
        x = 0
        y = len(mat) - 1
        for i in range(len(mat)):# primary
            res += mat[i][i]
            if x == y: # secondary 
                x += 1
                y -= 1
                continue
            else:
                res += mat[x][y]
                x += 1
                y -= 1
        return res