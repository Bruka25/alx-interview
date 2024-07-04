#!/usr/bin/python3

"""Module for the n-queens puzzle challenge"""

import sys


def print_usage_and_exit():
    """Prints the usage message and exits with status 1"""
    print("Usage: nqueens N")
    sys.exit(1)


def is_valid_solution(solution, row, col):
    """
    Checks if placing a queen at (row, col) is valid
    Args:
        solution (list): Current board configuration
        row (int): Row index
        col (int): Column index
    Returns:
        bool: True if valid, False otherwise
    """
    for r, c in enumerate(solution):
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_nqueens(N, row, solution):
    """
    Solves the N Queens problem using backtracking
    Args:
        N (int): Size of the board (N x N)
        row (int): Current row being processed
        solution (list): Current board configuration
    """
    if row == N:
        formatted_solution = [[i, solution[i]] for i in range(N)]
        print(formatted_solution)
        return
    for col in range(N):
        if is_valid_solution(solution, row, col):
            solve_nqueens(N, row + 1, solution + [col])


def main():
    """Main function to parse arguments and solve the N Queens problem"""
    if len(sys.argv) != 2:
        print_usage_and_exit()

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(N, 0, [])


if __name__ == "__main__":
    main()
