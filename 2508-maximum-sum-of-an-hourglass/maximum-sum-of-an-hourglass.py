class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        length = len(grid)
        possible_v = length - 2
        possible_h = width - 2
        res = 0
        for i in range(possible_v):
            for j in range(possible_h):
                start_col = i
                start_row = j
                abc = grid[start_col][start_row:start_row + 3]
                d = [grid [start_col + 1][start_row+1]]
                efg = grid [start_col + 2][start_row : start_row + 3 ]
                abcdefg = []
                abcdefg.extend(abc)
                abcdefg.extend(d)
                abcdefg.extend(efg)
                if res < sum(abcdefg):
                    res = sum(abcdefg)
        return res