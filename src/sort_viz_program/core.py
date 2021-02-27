import os

import numpy as np

ALGORITHMS = ["Merge Sort", "Bubble Sort", "Insert Sort", "Quick Sort", "Tim Sort"]


def create_array_random(array_length):

    if not isinstance(array_length, int):
        print("Length parameter must be integer")
        return
    array = np.random.rand(array_length)
    return array
