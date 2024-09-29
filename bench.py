import sys
import os
sys.path.append("/Users/jcaledo/Py_pkgs/POFF/src")
# sys.path.append(os.path.abspath("Py_pkgs/POFF/src"))
import Zmod as zm
import numpy as np
import row_echelon_form as ref

def row_echelon(matrix):
    # Convert the matrix to a float array to handle division properly
    matrix = matrix.astype(float)
    rows, cols = matrix.shape
    
    # Loop through each column to create pivots and eliminate below
    for i in range(min(rows, cols)):
        # Find the pivot row
        if matrix[i, i] == 0:
            # Swap with a row below if the pivot is zero
            for j in range(i + 1, rows):
                if matrix[j, i] != 0:
                    matrix[[i, j]] = matrix[[j, i]]
                    break
        
        # Normalize the pivot row (make the leading coefficient 1)
        if matrix[i, i] != 0:
            matrix[i] = matrix[i] / matrix[i, i]
        
        # Eliminate entries below the pivot
        for j in range(i + 1, rows):
            if matrix[j, i] != 0:
                matrix[j] = matrix[j] - matrix[j, i] * matrix[i]
    
    return matrix

# Example usage
""" 
A = np.array([[2, 4, -2],
              [4, 9, -3],
              [-2, -3, 7]])

A = np.array([[ 2, -2,  4, -2],
                  [ 2,  1, 10,  7],
                  [-4,  4, -8,  4],
                  [4, -1, 14,  6]])
print("Original matrix:")
print(A)

ref_matrix = row_echelon(A)

print("\nRow Echelon Form:")
print(ref_matrix)
"""
A = np.array([[0, 0, 0],
              [2, 4, -2],
              [4, 9, -3],
              [-2, -3, 7]])

B = np.array([[ 2, -2,  4, -2],
                  [ 2,  1, 10,  7],
                  [-4,  4, -8,  4],
                  [4, -1, 14,  6]])
# print("Original matrix:")
# print(A)
ref.get_ref(B, mod = 3)
print(B)

A = np.array([[0, 0, 0],
              [2, 4, -2],
              [4, 9, -3],
              [-2, -3, 7]])

