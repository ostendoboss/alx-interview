#!/usr/bin/python3
"""Given an n x n 2D matrix, rotate it 90 degrees clockwise."""


def rotate_2d_matrix(matrix):
    """function to rotate matrix"""
    matrix.reverse()
    matr = [[row[i] for row in matrix] for i in range(len(matrix))]

    j = 0
    for row in matrix:
        for i in range(len(row)):
            row[i] = matr[j][i]
        j += 1
