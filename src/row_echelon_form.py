## ------------------------------ ##
##      find_nonzero_row          ##
##      swap_rows                 ##
##      make_pivot_one            ##
##      make_zero_below           ##
##      get_ref                   ##
## ------------------------------ ##
import sys
import numpy as np
from Zmod import get_inv
from Zmod import get_canonical

# sys.modules[__name__].__dict__.clear()
# source .venv/bin/activate

## ------------------------------ ##
##      find_nonzero_row          ##
## ------------------------------ ##
"""
usage:  find_nonzero_row(matrix, pivot_row, col) 
matrix: a matrix (numpy.ndarray)
pivot_row: row for which we are searching a pivot
col: column in which we are searching the pivot
return: either an integer corresponding to the row containing the 
        first nonzero value (pivot) or None if any has been found
example: find_nonzero_row(matrix = np.array([[0,2],[2,1]]), 
                 pivot_row = 0, 
                 col = 0)

"""
def find_nonzero_row(matrix, pivot_row, col): 
    nrows = matrix.shape[0] 
    for row in range(pivot_row, nrows):
        if matrix[row, col] != 0: 
            return row 
    return None

## ------------------------------ ##
##      swap_rows          ##
## ------------------------------ ##
"""
usage:  swap_rows(matrix, row1, row2) 
matrix: a matrix (numpy.ndarray)
row1: first row to be interchanged
row2: second row to be interchanged
return: in the matrix, row1 will occupy the place of row2 
        and vice versa
example: swap_rows(matrix = np.array([[0,2],[2,1]]), 
                                    row1 = 0, row2 = 1)
"""
def swap_rows(matrix, row1, row2):
    matrix[row1], matrix[row2] = matrix[row2], matrix[row1]

## ------------------------------ ##
##       make_pivot_one           ##
## ------------------------------ ##
"""
usage: make_pivot_one(matrix, pivot_row, col, mod = None) 
matrix: a matrix (numpy.ndarray)
pivot_row: index of the pivot_row 
col: index of the col where the pivot is found
mod: if different to None, it should be a positive integer. Then,
     the elements of the matriz are converted to their canonical
     representatives in the indicated mod
return: in the matrix, the pivot row is normalized
example: makes_pivot_one(matrix = np.array([[2,2],[2,1]]), 
                                    pivot_row = 0, col = 0)
"""
def make_pivot_one(matrix, pivot_row, col, mod = None):
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
"""
usage: make_zero_below(matrix, pivot_row, col)
matrix: a matrix (numpy.ndarray)
pivot_row: index of the pivot_row 
col: index of the col where the pivot is found
return: in the matrix, the entry below the pivot are eliminated 
example: makes_zero_below(matrix = np.array([[2,2],[2,1]]), 
                                    pivot_row = 0, col = 0)
"""
def make_zero_below(matrix, pivot_row, col):
    """_summary_

    Args:
        matrix (_type_): _description_
        pivot_row (_type_): _description_
        col (_type_): _description_
    """
    nrow = matrix.shape[0]
    for row in range(pivot_row + 1, nrow):
        factor = matrix[row, col]
        matrix[row] -= factor * matrix[pivot_row]


## ------------------------------ ##
##             get_ref            ##
## ------------------------------ ##
def get_ref(matrix):
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
    
    
A = np.array([[2,1,1,1],[2,1,1,1],[2,1,1,1],[1,2,2,0]])

print(make_pivot_one(A, 1, 0, 3))
