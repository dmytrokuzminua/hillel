""" Homework 8 task 8
    run test: python -m doctest -v hw_8_8.py"""


from typing import List


def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Transposes a matrix

    >>> transpose_matrix([[1, 2], [3, 4]])
    [[1, 3], [2, 4]]
    >>> transpose_matrix([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    >>> transpose_matrix([[1]])
    [[1]]
    >>> transpose_matrix([])
    []
    """
    return list(map(list, zip(*matrix)))


def matrix_multiply(matrix1: List[List[int]], matrix2: List[List[int]]) -> List[List[int]]:
    """
    Multiplication of two matrices

    >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    [[19, 22], [43, 50]]
    >>> matrix_multiply([[1, 0], [0, 1]], [[1, 2], [3, 4]])
    [[1, 2], [3, 4]]
    >>> matrix_multiply([[2, 3, 4]], [[1], [0], [2]])
    [[10]]
    >>> matrix_multiply([[1,2],[3,4],[5,6]], [[7,8,9],[10,11,12]])
    [[27, 30, 33], [61, 68, 75], [95, 106, 117]]
    """
    if not matrix1 or not matrix2:
        return []

    m, n = len(matrix1), len(matrix1[0])
    n2, p = len(matrix2), len(matrix2[0])
    if n != n2:
        raise ValueError("Кількість стовпців першої матриці повинна дорівнювати кількості рядків другої")

    result = [[0 for _ in range(p)] for _ in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
