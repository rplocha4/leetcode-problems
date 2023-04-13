def isValidSudoku(board):
    def validRows():
        for row in board:
            seen = {}
            for num in row:
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen[num] = True
        return True

    def validCols():
        for col in range(9):
            seen = {}
            for row in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen[num] = True
        return True

    def validBox():
        for row in range(3):
            for col in range(3):
                seen = {}
                for i in range(3):
                    for j in range(3):
                        num = board[3 * row + i][3 * col + j]
                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen[num] = True
        return True

    return validRows() and validCols() and validBox()
