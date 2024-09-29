import sys
import os
sys.path.append(os.path.abspath("/Users/jcaledo/Py_pkgs/POFF/src"))
import numpy as np
import row_echelon_form as ref
 
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

def test_make_zero_below():
    M = np.array([[ 2, -2,  4, -2],
                  [ 2,  1, 10,  7],
                  [-4,  4, -8,  4],
                  [4, -1, 14,  6]])
    M_ = M.copy()
    ref.make_zero_below(M, 0, 0)
    assert np.array_equal(M, np.array([[ 1, -1,  2, -1],
                                       [ 0,  3,  6,  9],
                                       [ 0,  0,  0,  0],
                                       [ 0,  3,  6, 10]]))
    
def test_make_zero_below_mod():
    M = np.array([[ 2, -2,  4, -2],
                  [ 2,  1, 10,  7],
                  [-4,  4, -8,  4],
                  [4, -1, 14,  6]])
    M_ = M.copy()
    ref.make_zero_below(M, 0, 0, mod = 3)
    assert np.array_equal(M, np.array([[ 1, 2,  2, 2],
                                       [ 0,  0,  0,  0],
                                       [ 0,  0,  0,  0],
                                       [ 0,  0,  0,  1]]))
    

def test_get_ref_1():
    M = np.array([[ 2, -2,  4, -2],
                  [ 2,  1, 10,  7],
                  [-4,  4, -8,  4],
                  [4, -1, 14,  6]])
    assert np.array_equal(ref.get_ref(M), np.array([[1,-1,2,-1],
                                                    [0,1,2,3],
                                                    [0,0,0,1], 
                                                    [0,0,0,0]]))

def test_get_ref_2():
    A = np.array([[0, 0, 0],
              [2, 4, -2],
              [4, 9, -3],
              [-2, -3, 7]])
    assert np.array_equal(ref.get_ref(A), np.array([[1,2,-1],
                                                    [0,1,1],
                                                    [0,0,1], 
                                                    [0,0,0]]))

def test_get_ref_mod1():
    M = np.array([[ 2, -2,  4, -2],
                  [ 2,  1, 10,  7],
                  [-4,  4, -8,  4],
                  [4, -1, 14,  6]])
    assert np.array_equal(ref.get_ref(M, mod =3), np.array([[1,2,2,2],
                                                    [0,0,0,1],
                                                    [0,0,0,0], 
                                                    [0,0,0,0]]))

def test_get_ref_mod2():
    A = np.array([[0, 0, 0],
              [2, 4, -2],
              [4, 9, -3],
              [-2, -3, 7]])
    assert np.array_equal(ref.get_ref(A), np.array([[1,2,-1],
                                                    [0,1,1],
                                                    [0,0,1], 
                                                    [0,0,0]]))