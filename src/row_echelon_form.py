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
def find_nonzero_row(matrix, pivot_row, col): 
    """Finds the index of the non-zero pivot closest to 
        matrix(pivot_row, col).

    Args:
        matrix (numpy.ndarray): a matrix
        pivot_row (int): index of the pivot row
        col (int): index of the column

    Returns:
        int: index of the row where the first non-zero pivot 
            is found. If any, the function returns 'None'. 
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
    """Interchanges the indicated rows in the given matrix.

    Args:
        matrix (numpy.ndarray): matrix
        row1 (int): index of the first row
        row2 (int): index of the second row
    """
    matrix[[row1,row2]] = matrix[[row2,row1]]

## ------------------------------ ##
##       make_pivot_one           ##
## ------------------------------ ##
def make_pivot_one(matrix, pivot_row, col, mod = None):
    """Modifies in place the given matrix to normalize the pivot row in order
        to have 1 as the pivot value. 

    Args:
        matrix (numpy.ndarray): a matrix
        pivot_row (int): the index of the pivot row
        col (int): the index of the pivot column
        mod (int, optional): modulo. Defaults to None.

    """
    if mod == None:
        pivot = matrix[pivot_row, col]
        matrix[pivot_row] //= pivot
    elif type(mod) is int:
        pivot_inv = get_inv(matrix[pivot_row, col], mod)
        matrix[pivot_row] *= pivot_inv
        M = get_canonical(matrix, mod)
        for i in range(M.shape[0]):
            matrix[i] = M[i]  
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

def make_zero_below(matrix, pivot_row, col, mod = None):
    """_summary_

    Args:
        matrix (_type_): _description_
        pivot_row (_type_): _description_
        col (_type_): _description_
        mod (_type_, optional): _description_. Defaults to None.

    if mod == None:
        nrow = matrix.shape[0]
        for row in range(pivot_row + 1, nrow):
            factor = matrix[row, col]
            matrix[row] -= factor * matrix[pivot_row]
    else:


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




M = np.array([[ 2, -2,  4, -2],
                  [ 2,  1, 10,  7],
                  [-4,  4, -8,  4],
                  [4, -1, 14,  6]])

make_pivot_one(M, 0, 0, 3)

print("----------\n", M)

"""