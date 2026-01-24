#!/usr/bin/python3
"""
Module for dividing all elements of a matrix.

This module provides a function to divide all elements of a matrix
by a given divisor, with proper validation and error handling.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.

    Args:
        matrix: A list of lists of integers or floats
        div: The divisor (must be a number, cannot be 0)

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimals

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows of matrix have different sizes
        TypeError: If div is not a number
        ZeroDivisionError: If div is 0
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(error_msg)

    if not all(len(row) > 0 for row in matrix):
        raise TypeError(error_msg)

    if not all(isinstance(elem, (int, float))
               for row in matrix for elem in row):
        raise TypeError(error_msg)

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
