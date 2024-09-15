import sys
import os
sys.path.append(os.path.abspath("/Users/jcaledo/Py_pkgs/POFF/src"))
import numpy as np
import row_echelon_form as ref

def test_find_nonzero_row():
    assert ref.find_nonzero_row(matrix = np.array([[ 2, -2,  4, -2],
                                                    [ 2,  1, 10,  7],
                                                    [-4,  4, -8,  4],
                                                    [ 4, -1, 14,  6]]), 
                                pivot_row = 1, col =2) == 1
    assert ref.find_nonzero_row(matrix = np.array([[ 2, -2,  4, -2],
                                                    [ 2,  1, 10,  7],
                                                    [-4,  4, 0,  4],
                                                    [ 4, -1, 0,  6]]), 
                                pivot_row = 2, col =2) == None

def test_swap_rows():
    M = np.array([[ 2, -2,  4, -2],
                  [ 2,  1, 10,  7],
                  [-4,  4, -8,  4],
                  [4, -1, 14,  6]])
    ref.swap_rows(matrix = M, row1 = 0, row2 = 3)
    assert np.array_equal(M, np.array([ [4, -1, 14,  6],
                             [2,  1, 10,  7],
                             [-4,  4, -8,  4],
                             [2, -2,  4, -2]]))
   
def test_make_pivot_one():
    M = np.array([[ 2, -2,  4, -2],
                  [ 2,  1, 10,  7],
                  [-4,  4, -8,  4],
                  [4, -1, 14,  6]])
    M_ = M.copy()
    ref.make_pivot_one(M, 0, 0)
    ref.make_pivot_one(M_, 0, 0, 3)
    assert sum(M[0] == [1, -1, 2, -1]) == 4
    assert sum(M_[0] == [1, 2, 2, 2]) == 4

