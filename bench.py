import sys
import os
sys.path.append("/Users/jcaledo/Py_pkgs/POFF/src")
# sys.path.append(os.path.abspath("Py_pkgs/POFF/src"))
import Zmod as zm
import numpy as np
import row_echelon_form as ref

names = ['Tom', 'Jerry', 'Spike']
colors = ['red', 'blue', 'green', 'yellow']
scores = [3, 6, 9, 12, 15, 18]
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
items = ['pen', 'pencil', 'book', 'eraser', 'ruler']
L = [[1, 2], [3, 4], [5, 6]]

for i, score in enumerate(scores):
    if i %2 == 1:
        print(score)