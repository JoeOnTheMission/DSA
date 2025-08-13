class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        length = len(mat)
        width = len(mat[0])
        i = 0
        j = 0
        out = []
        now = []
        result = []

        for j in range(width):
            i = 0
            now.append(mat[i][j])
            while j > 0 and i < length - 1:
                j = j - 1
                i = i + 1
                now.append(mat[i][j])
            out.append(now[::1])
            now = []
        for i in range(1,length):
            j = width - 1
            now.append(mat[i][j])
            while i < length-1 and j > 0:
                i = i + 1
                j = j - 1
                now.append(mat[i][j])
            out.append(now[::1])
            now = []
        reverser = 0
        for group in out:
            if reverser % 2 == 0:
                x = -1
            else:
                x = 1
            result.extend(group[::x])
            reverser = reverser + 1
        return result