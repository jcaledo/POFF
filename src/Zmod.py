## ------------------------------ ##
##      get_canonical             ##
##      get_gcd                   ##
##      get_inv                   ##
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
def get_gcd(a, b):
    """Finds the greatest common divisor of two integers

    Args:
        a (int): an integer
        b (int): an integer

    Returns:
       A 3-tuple (gcd, x, y) such that gcd = ax + by
    """
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = get_gcd(b, a%b)
    x = y1
    y = x1 - (a//b)* y1
    return gcd, x, y

## ------------------------------ ##
##          get_inv               ##
## ------------------------------ ##
def get_inv(n, mod):
    """Get the multiplicative inverse of an integer given a modulo. 

    Args:
        n (int): integer whose inverse we want to find
        mod (int): modulo

    Returns:
        An integer that is the modular inverse of n. If n and mod are not coprime, then n does not have inverse.
    """
    gcd, x, y = get_gcd(n, mod)
    if gcd != 1:
        sys.exit(f"\n the integer {n} and the mod {mod} are not co-prime \n")
    elif gcd == 1 and x < 0: 
        return mod + x
    elif gcd == 1 and x > 0:
        return x
    else:
        sys.exit("Something went awfully wrong!")

