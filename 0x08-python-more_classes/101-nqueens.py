#!/usr/bin/python3
import sys

def is_safe(board, row, colu):
    """Check if there is a queen in the same column"""
    for x in range(row):
        if board[x][colu] == 1:
            return False
    """Check upper left diagonal"""
    for x, y in zip(range(row, -1, -1), range(colu, -1, -1)):
        if board[x][y] == 1:
            return False
    """Check upper right diagonal"""
    for x, y in zip(range(row, -1, -1), range(colu, len(board))):
        if board[x][y] == 1:
            return False
    return True

def solve_nqueens(board, row):
    a = len(board)
    if row == a:
        """All queens are placed, print the solution"""
        for x in range(n):
            for y in range(n):
                if board[x][y] == 1:
                    print("[{}, {}]".format(x, y), end=" ")
        print()  # Add a newline after printing each solution
    else:
        for colu in range(n):
            if is_safe(board, row, colu):
                board[row][colu] = 1
                solve_nqueens(board, row + 1)
                board[row][colu] = 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])  # Fix variable name
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    """Initialize the chessboard"""
    chessboard = [[0 for _ in range(n)] for _ in range(n)]

    """Solve the N queens problem"""
    solve_nqueens(chessboard, 0)

