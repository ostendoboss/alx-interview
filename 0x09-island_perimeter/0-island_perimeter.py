#!/usr/bin/python3
""" Calculate and return perimeter of island in the grid"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                """Start with 4 sides
                Check adjacent cells and subtract
                perimeter for shared sides"""
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
    return perimeter
