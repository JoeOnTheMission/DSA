class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        current_row = []
        current_col = []
        rows = []
        cols = []
        state = True

        def checker(input_list):
            for li in input_list:
                counter = [0] * 10  # reset for each list
                for num in li:
                    if num != ".":  # skip empty cells
                        counter[int(num)] += 1
                        if counter[int(num)] > 1:
                            return False
            return True

        for i in range(9):#column
            for j in range(9):
                if board[i][j] != ".":
                    row_num = board[i][j]
                    current_row.append(row_num)

                if board[j][i] != ".":
                    col_num = board[j][i]
                    current_col.append(col_num)

            rows.append(current_row)
            current_row = []
            cols.append(current_col)
            current_col = []
        current_square = []
        squares = []
        for x in range(0,7,3):
            for y in range(0,7,3):
                for i in range(3):
                    for j in range(3):
                        if board[x+i][y+j] != ".":
                            current_square.append(board[x+i][y+j])
                squares.append(current_square)
                current_square = []
        x = checker(rows)
        y = checker(cols)
        z = checker(squares)
        return x and y and z
