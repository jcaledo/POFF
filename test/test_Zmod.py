import sys
import os
import numpy as np
import Zmod as zm
# Add the src directory to sys.path:
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


def test_get_canonical():
    assert np.array_equal(zm.get_canonical(matrix = np.array([[ 2, -2,  4, -2],
       [ 2,  1, 10,  7],
       [-4,  4, -8,  4],
       [ 4, -1, 14,  6]]), mod = 3), np.array([[2, 1, 1, 1],
       [2, 1, 1, 1],
       [2, 1, 1, 1],
       [1, 2, 2, 0]]))


def test_get_gcd():
    assert zm.get_gcd(7, 5) == (1, -2, 3)
    assert zm.get_gcd(5, 7) == (1, 3, -2)
    assert zm.get_gcd(124, 68) == (4, -6, 11)

def test_get_inv():
    assert zm.get_inv(5, 7) == 3
    assert zm.get_inv(3, 5) == 2
    assert zm.get_inv(17,43) == 38
