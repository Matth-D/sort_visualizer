import os
import random

import numpy as np

ALGORITHMS = ["Merge Sort", "Bubble Sort", "Insert Sort", "Quick Sort", "Tim Sort"]


def create_array_random(array_length):

    if not isinstance(array_length, int):
        print("Length parameter must be integer")
        return
    index = np.array(range(array_length))
    values = np.round(np.random.rand(array_length), decimals=3)
    # values = np.random.randint(25, size=array_length)
    merge = np.column_stack((index, values))
    return merge


list1 = np.array([0, 1, 2, 3, 4], dtype=float)
list1 = list1 * 0.1
print(list1)
