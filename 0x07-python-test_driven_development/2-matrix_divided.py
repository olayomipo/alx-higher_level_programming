

def matrix_divided(matrix, div):
    """ Function that divides the integer/float numbers of a matrix[]

    Args:
        matrix: list of a lists of integers/floats
        div: number which divides the matrix

    Returns:
        A new matrix with the result of the division

    Raises:
        TypeError: If the elements of the matrix aren't lists
                   If the elemetns of the lists aren't integers/floats
                   If div is not an integer/float number
                   If the lists of the matrix don't have the same size

        ZeroDivisionError: If div is zero

    """
    
    # Check that input is a matrix (list of lists) of integers/floats
    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError('matrix must be a matrix (list of lists) of integers/floats')

    # Check that all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    # Check that div is a number
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    # Check that div is not equal to 0
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # Divide all elements of the matrix by div and round to 2 decimal places
    return list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix)) 

