def print_queen(board):
    for row in board:
        print(" ".join(row))
    print()

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == "Q":
            return False
    for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
        if board[i][j] == "Q":
            return False
    for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
        if board[i][j] == "Q":
            return False
    return True

def solve_queen(board, row, n, count):
    if row == n:
        count[0] += 1
        print_queen(board)
        return
    for col in range(n):
        if is_safe(board, row, col, n):
            print(f"Placing queen at: ({row},{col})")
            board[row][col] = "Q"
            solve_queen(board, row + 1, n, count)   # ✅ fixed
            print(f"Backtrack from ({row},{col})")
            board[row][col] = "."

def n_queen(n):
    board = [["."] * n for _ in range(n)]
    count = [0]
    solve_queen(board, 0, n, count)
    print(f"Total solutions for {n}-Queens: {count[0]}")

n = int(input("Enter the value: "))
n_queen(n)
