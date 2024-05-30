#!/usr/bin/python3

def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list of lists: A list of lists representing Pascal's triangle.

    Raises:
        None.

    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        curr_row = [1]

        for j in range(1, i):
            curr_row.append(prev_row[j-1] + prev_row[j])

        curr_row.append(1)
        triangle.append(curr_row)

    return triangle
