def search_empty(sudoku, empty):
    for r in range(9):
        for c in range(9):
            if sudoku[r][c] == 0:
                empty[0] = r
                empty[1] = c
                return True
    return False


def is_valid_row(sudoku, row, num):
    for i in range(9):
        if sudoku[row][i] == num:
            return True
    return False


def is_valid_col(sudoku, col, num):
    for i in range(9):
        if sudoku[i][col] == num:
            return True
    return False


def is_valid_box(sudoku, row, col, num):
    for i in range(3):
        for j in range(3):
            if sudoku[i + row][j + col] == num:
                return True
    return False


def is_safe(sudoku, row, col, num):
    return not is_valid_row(sudoku, row, num) and not is_valid_col(sudoku, col, num) and not is_valid_box(sudoku, row - row % 3, col - col % 3, num)


def solve_sudoku(sudoku):
    empty = [0, 0]

    if not search_empty(sudoku, empty):
        return True

    r = empty[0]
    c = empty[1]

    for num in range(1, 10):
        if is_safe(sudoku, r, c, num):
            sudoku[r][c] = num
            if solve_sudoku(sudoku):
                return True
            sudoku[r][c] = 0
    return False


if __name__ == "__main__":
    sudoku_board = []
    for i in range(9):
        row_numbers = list(map(int, input().strip().split()))
        sudoku_board.append(row_numbers)

    if solve_sudoku(sudoku_board):
        for i in range(9):
            solution = ' '.join(map(str, sudoku_board[i]))
            print(solution)
