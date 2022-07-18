from collections import defaultdict

def isValidSudoku(board):

    s = set()

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val != ".":
                # values will be stored as ('', int), (int, ''), or (int, int, '')
                if (i, val) in s or (val, j) in s or (i//3, j//3, val) in s:
                    return False
                s.add((i, val))
                s.add((val, j))
                s.add((i//3, j//3, val))
    return True
    # rows = defaultdict(set)
    # cols = defaultdict(set)
    # suds = defaultdict(set)
    #
    # for row in range(9):
    #     for col in range(9):
    #         if board[row][col] == ".":
    #             continue
    #         if (board[row][col] in rows[row] or board[row][col] in cols[col]
    #                 or board[row][col] in suds[(row//3, col//3)]):
    #             return False
    #         rows[row].add(board[row][col])
    #         cols[col].add(board[row][col])
    #         suds[(row//3, col//3)].add(board[row][col])
    # return True

    # check row
    # check column
    # check 3x3


    print(mat_map)
    return True


if __name__ == "__main__":
    board1 = [["5","3",".",".","7",".",".",".","."], ["6",".",".","1","9","5",".",".","."], [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"], ["4",".",".","8",".","3",".",".","1"], ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."], [".",".",".","4","1","9",".",".","5"], [".",".",".",".","8",".",".","7","9"]]
    print(isValidSudoku(board1) == True)