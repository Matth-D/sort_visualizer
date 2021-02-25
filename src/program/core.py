import numpy as np


def create_array_random(array_length):

    if not isinstance(array_length, int):
        print("Length parameter must be integer")
        return
    array = np.random.rand(array_length)
    return array

