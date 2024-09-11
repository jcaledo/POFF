## ------------------------------ ##
##      find_nonzero_row          ##
##      swap_rows                 ##
##      make_pivot_one            ##
##      make_zero_below           ##
##      get_ref                   ##
## ------------------------------ ##
import sys
import numpy as np
import Zmod as zm

## ------------------------------ ##
##      find_nonzero_row          ##
## ------------------------------ ##
def find_nonzero_row(matrix, pivot_row, col): 
    """_summary_

    Args:
        matrix (_type_): _description_
        pivot_row (_type_): _description_
        col (_type_): _description_

    Returns:
        _type_: _description_
    """
    nrows = matrix.shape[0] 
    for row in range(pivot_row, nrows):
        if matrix[row, col] != 0: 
            return row 
    return None

## ------------------------------ ##
##           swap_rows            ##
## ------------------------------ ##
def swap_rows(matrix, row1, row2):
    """_summary_

    Args:
        matrix (_type_): _description_
        row1 (_type_): _description_
        row2 (_type_): _description_
    """
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

## ------------------------------ ##
##       make_pivot_one           ##
## ------------------------------ ##
def make_pivot_one(matrix, pivot_row, col, mod = None):
    """_summary_

    Args:
        matrix (_type_): _description_
        pivot_row (_type_): _description_
        col (_type_): _description_
        mod (_type_, optional): _description_. Defaults to None.
    """
    if mod == None:
        pivot = matrix[pivot_row, col]
        matrix[pivot_row] //= pivot
    elif type(mod) is int:
        pivot_inv = get_inv(matrix[pivot_row, col], mod)
        matrix[pivot_row] *= pivot_inv
        matrix[pivot_row] = get_canonical(matrix[pivot_row], mod)
    else:
        sys.exit("The mod should be a positive integer")

## ------------------------------ ##
##      make_zero_below           ##
## ------------------------------ ##
def make_zero_below(matrix, pivot_row, col, mod = None):
    """_summary_

    Args:
        matrix (_type_): _description_
        pivot_row (_type_): _description_
        col (_type_): _description_
        mod (_type_, optional): _description_. Defaults to None.
    """
    nrow = matrix.shape[0]
    for row in range(pivot_row + 1, nrow):
        factor = matrix[row, col]
        matrix[row] -= factor * matrix[pivot_row]

## ------------------------------ ##
##             get_ref            ##
## ------------------------------ ##
def get_ref(matrix):
    """_summary_

    Args:
        matrix (_type_): _description_

    Returns:
        _type_: _description_
    """
    ncol = matrix.shape[1]
    pivot_row = 0
    
    for col in range(ncol):
        nonzero_row = find_nonzero_row(matrix, pivot_row, col)
        if nonzero_row is not None:
            swap_rows(matrix, pivot_row, nonzero_row)
            make_pivot_one(matrix, pivot_row, col)
            make_zero_below(matrix, pivot_row, col)
            pivot_row += 1
    return matrix
    


M = np.array([[ 2, -2,  4, -2],
       [ 2,  1, 10,  7],
       [-4,  4, -8,  4],
       [ 4, -1, 14,  6]])





