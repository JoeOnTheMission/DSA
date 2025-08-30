class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        
        last_row = [0]*len(matrix[0])
        pre = [[] for _ in range(len(matrix))]

        for i in range(len(matrix)):
            total = 0
            for j in range(len(matrix[0])):
                total += matrix[i][j]
                last_row[j] += total
            pre[i].extend(last_row)

        res = 0
        for row_1 in range(len(matrix)):
            for row_2 in range(row_1,len(matrix)):
                check = defaultdict(int)
                check[0] = 1

                for c in range(len(matrix[0])):
                    row_sum = pre[row_2][c] - (pre[row_1 - 1][c] if row_1 > 0 else 0)
                    res += check[row_sum - target]
                    check[row_sum] += 1
        return res 