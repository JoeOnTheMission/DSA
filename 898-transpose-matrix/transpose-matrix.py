class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        length = len(matrix)
        width = len(matrix[0])
        transpose = []
        current_list = []
        i = 0
        while i < width:
            for j in matrix:
                current_list.append(j[i])
            transpose.append(current_list)
            current_list = []
            i = i + 1
        return transpose