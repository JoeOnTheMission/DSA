class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        state = True

        length = len(matrix)
        width = max(len(row) for row in matrix)

        index_to_check = [(0, j) for j in range(width)] + [(i, 0) for i in range(1, length)]
        for i,j in index_to_check:
            a = matrix[i][j]
            while i + 1 < length and j + 1 < width:
                i += 1
                j += 1
                b = matrix[i][j]
                if a != b:
                    state = False
                    break
            if not state:
                break
        return state