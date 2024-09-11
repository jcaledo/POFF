## ------------------------------ ##
##      get_canonical             ##
##      get_gcd                   ##
##      get_inv                   ##
##      make_zero                 ##
## ------------------------------ ##
import sys
import numpy as np
# sys.modules[__name__].__dict__.clear()

## ------------------------------ ##
##      get_canonical             ##
## ------------------------------ ##
def get_canonical(matrix, mod):
    """Builds a matrix with entries that are representative, modulo 
    a selected value, of the original entries of the input matrix.

    Args:
        matrix (numpy.ndarray): a matrix of integers
        mod (int): modulo, it should be a positive integer

    Returns:
        matrix (numpy.ndarray): A new matrix is created based on the original
            input matrix, which remains conserved, with its entries replaced
            by their respective canonical representatives.
    """
    counter = 1
    for row in matrix:
        if counter == 1:
            M = np.array(row % mod)
        else:
            M = np.vstack([M, (row % mod)])
        counter += 1 
    return M
    

## ------------------------------ ##
##            get_gcd             ##
## ------------------------------ ##
""" 
usage: get_gcd(a, b)
a: integer
b: integer
example: get_gcd(7, 5) 
return: a 3-tuple (gcd, x, y) such that gcd = ax + byso
"""
def get_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = get_gcd(b, a%b)
    x = y1
    y = x1 - (a//b)* y1
    return gcd, x, y

## ------------------------------ ##
##          get_inv               ##
## ------------------------------ ##
"""
usage: get_inv(x, mod)
n: integer whose multiplicative inverse we want to find
mod: module (it should be a positive integer)
return: an integer being the inverse of n in the corresponding module
example: get_inv(3, 7) 
"""
def get_inv(n, mod):
    gcd, x, y = get_gcd(n, mod)
    if gcd != 1:
        sys.exit(f"\n the integer {n} and the mod {mod} are not co-prime \n")
    elif gcd == 1 and x < 0: 
        return mod + x
    elif gcd == 1 and x > 0:
        return x
    else:
        sys.exit("Something went awfully wrong!")

## ------------------------------ ##
##         make_zero              ##
## ------------------------------ ##
"""
usage: make_zero(matrix, pivot_row, pivot_col, mod)
matrix: a matrix (numpy.ndarray)
pivot_row: index of the row containing the pivot
pivot_col: index of the column containing the pivot
mod: module (it should be a positive integer)
return: a modified matrix where the entries below the pivot have been made zero
example: make_zero() 
"""
def make_zero(matrix, pivot_row, pivot_col, mod):
    """_summary_

    Args:
        matrix (_type_): _description_
        pivot_row (_type_): _description_
        pivot_col (_type_): _description_
        mod (_type_): _description_

    Returns:
        _type_: _description_
    """
    pos = indice - 1 
    # Make pivot = 1 normalizing row1 if needed 
    if row1[pos] == 0:
        sys.exit("0 cannot be a pivot!")
    elif row1[pos] != 1:
        inv = get_inv(row1[pos], mod)
        nrow1 = [inv * e for e in row1]
        nrow1 = canonical_row(nrow1, mod)
    elif row1[pos] == 1:
        nrow1 = row1 
    else:
        sys.exit("Something went awfully wrong!")
    # Make zero in row2
    scalar = (mod - row2[pos]) 
    nrow2 = []
    for i in range(len(nrow1)): 
        linear_comb = (scalar * nrow1[i]) + row2[i]
        nrow2.append(get_canonical(linear_comb, mod))
        
    return nrow2


