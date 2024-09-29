## ------------------------------ ##
##      make_pivot_one            ##
##      make_zero_below           ##
##      get_ref                   ##
## ------------------------------ ##
import sys
import numpy as np
from Zmod import get_inv
from Zmod import get_canonical

## ------------------------------ ##
##       make_pivot_one           ##
## ------------------------------ ##
def make_pivot_one(matrix, pivot_row, col, mod = None):
    """Modifies the given matrix in place to normalize the pivot row, 
    ensuring that the pivot value becomes 1. 

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
def make_zero_below(matrix, pivot_row, col, mod = None):
    """Modifies the given matrix in place to create zeros below the pivot. 

    Args:
        matrix (numpy.ndarray): a matrix
        pivot_row (int): index of the pivot row
        col (int): index of the pivot column
        mod (int_, optional): modulo. Defaults to None.
    """
    # Ensure that the pivot value is normalized to 1.
    make_pivot_one(matrix, pivot_row, col, mod)
    nrow = matrix.shape[0]
    if mod == None:
        for row in range(pivot_row + 1, nrow):
            factor = matrix[row, col]
            matrix[row] -= factor * matrix[pivot_row]
    else:
        for row in range(pivot_row + 1, nrow):
            factor = matrix[row, col]
            matrix[row] -= factor * matrix[pivot_row]
            M = get_canonical(matrix, mod)
            for i in range(M.shape[0]):
                matrix[i] = M[i]  


## ------------------------------ ##
##             get_ref            ##
## ------------------------------ ##
def get_ref(matrix, mod = None):
    """_summary_

    Args:
        matrix (_type_): _description_

    Returns:
        _type_: _description_
    """ 
    nrow, ncol = matrix.shape   
    # Pivot_row counter
    pivot_row = 0
    # Loop through each column
    for j in range(ncol):
        # Look for a non-zero pivot in the current column
        for i in range(pivot_row, nrow):
            if matrix[i, j] != 0:
                # Swap the current row with the pivot row if necessary
                matrix[[pivot_row, i]] = matrix[[i, pivot_row]]
                break
        else:
            # No pivot found in this column, move to the next column
            continue 
        # Normalize the pivot row (make the leading coefficient 1)
        make_pivot_one(matrix, pivot_row, j, mod)
        # Eliminate entries below the pivot
        make_zero_below(matrix, pivot_row, j, mod)
        # Move to the next pivot row
        pivot_row += 1

    return matrix