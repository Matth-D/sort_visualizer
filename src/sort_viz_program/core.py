import os
import random

import numpy as np

ALGORITHMS = ["Merge Sort", "Bubble Sort", "Insert Sort", "Quick Sort", "Tim Sort"]


def create_array_random(array_length):
    """Create an array filled with random values from 0 to 1 of length array_length.

    Args:
        array_length (int): Length of array to create.

    Returns:
        np.ndarray: 2d array index, value.
    """
    if not isinstance(array_length, int):
        print("Length parameter must be integer")
        return None
    index = np.array(range(array_length))
    values = np.round(np.random.random_sample(array_length), decimals=3)
    merge = np.column_stack((index, values))
    return merge


# array_length = 10
# index = np.array(range(array_length))
# # values = np.round(np.random.uniform(low=0, high=1), decimals=3)
# values = np.random.uniform(low=0, high=1, size=array_length)

# values = np.random.uniform(low=0, high=1, size=2)
# values = np.random.random_sample(5)
# print(values)
# merge = np.column_stack((index, values))
# print(values)
