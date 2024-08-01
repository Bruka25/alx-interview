#!/usr/bin/python3


"""Moudle for finding island perimeter"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island in the grid.

    Args:
        grid (list of list of int): 2D grid representing the map,
                                    where 0 represents water and 1 represents
                                    land.

    Returns:
        int: Perimeter of the island.
    """
    # Initialize the perimeter to 0
    perimeter = 0

    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])

    # Iterate through each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the current cell is land
            if grid[i][j] == 1:
                # Check the cell above
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                # Check the cell below
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                # Check the cell to the left
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                # Check the cell to the right
                if j == cols-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
