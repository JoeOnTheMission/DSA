from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        res = 0

        # choose row1
        for row1 in range(rows):
            arr = [0] * cols  # compressed column sums
            # extend down to row2
            for row2 in range(row1, rows):
                for c in range(cols):
                    arr[c] += matrix[row2][c]
                
                # now count subarrays of arr with sum == target
                prefix = 0
                count = defaultdict(int)
                count[0] = 1
                for n in arr:
                    prefix += n
                    if prefix - target in count:
                        res += count[prefix - target]
                    count[prefix] += 1
        
        return res
