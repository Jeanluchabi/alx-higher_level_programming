#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    """Check if there is a queen in the same column"""
    for x in range(row):
        if board[x][col] == 1:
            return False
    """Check upper left diagonal"""
    for x, y in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[x][y] == 1:
            return False
    """Check upper right diagonal"""
    for x, y in zip(range(row, -1, -1), range(col, len(board))):
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
        print()
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
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """Initialize the chessboard"""
    chessboard = [[0 for _ in range(N)] for _ in range(N)]

    """Solve the N queens problem"""
    solve_nqueens(chessboard, 0)
