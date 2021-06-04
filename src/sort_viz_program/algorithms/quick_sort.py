import random


def quicksort(input_array):
    if len(input_array) < 2:
        return input_array

    index = random.randint(0, len(input_array) - 1)
    pivot = input_array[index]
    smaller = [
        i
        for i in input_array[0:index] + input_array[index + 1 : len(input_array)]
        if i < pivot
    ]
    greater = [
        i
        for i in input_array[0:index] + input_array[index + 1 : len(input_array)]
        if i >= pivot
    ]
    print(quicksort(smaller) + [pivot] + quicksort(greater))
    return quicksort(smaller) + [pivot] + quicksort(greater)


# array = [1, 18, 91, 32, 1, 1, 9, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
# array = [5, 2, 6, 1, 8]

# quicksort(array)

import random

import numpy as np

# from . import algo_utils


class QuickSort:
    """QuickSort algorithm."""

    def __init__(self, input_array, **kwargs):
        """Class init.

        Args:
            input_array (np.ndarray): Array to sort.
        """
        self.gui = kwargs.get("gui")
        # self.signals = algo_utils.Signals()
        self.time_complexity = "O(nlogn)"
        self.space_complexity = "O(n)"
        self.input_array = input_array
        tmp_index = np.arange(len(self.input_array))
        self.input_array = np.column_stack((tmp_index, self.input_array))
        self.sort_array = self.input_array.copy()
        self.solving = 0
        self.solved = 0
        self.iterations = 0

    def solve(self):
        """Solve Merge sort algorithm."""
        if self.solving == 1:
            return

        if self.solved == 1:
            return

        self.solving = 1

        self.sort_array = self.quicksort(self.input_array)

        self.solving = 0
        self.solved = 1

    def quicksort(self, input_array):
        first_i = input_array[0][0]
        last_i = input_array[-1][0]

        size_input = len(input_array)
        if size_input < 2:
            return input_array

        index_pivot = random.randint(0, size_input - 1)
        pivot = input_array[index_pivot]
        no_pivot = self.concat_arrays(
            input_array[0:index_pivot], input_array[index_pivot + 1 : size_input]
        )
        smaller = no_pivot[(no_pivot[:, 1] < pivot[1])]
        greater = no_pivot[(no_pivot[:, 1] >= pivot[1])]

        # Set index values
        smaller[:, 0] = np.arange(first_i, len(smaller))
        pivot[0] = len(smaller)
        greater[:, 0] = np.arange(len(smaller) + 1, last_i + 1)

        return self.recur_quicksort(smaller, pivot, greater)

    def concat_arrays(self, arr1, arr2):
        if arr1.size == 0:
            return arr2
        if arr2.size == 0:
            return arr1

        return np.vstack((arr1, arr2))

    def recur_quicksort(self, smaller, pivot, greater):
        if smaller.size == 0:
            return np.vstack((pivot, self.quicksort(greater)))
        elif greater.size == 0:
            return np.vstack((self.quicksort(smaller), pivot))
        else:
            return np.vstack((self.quicksort(smaller), pivot, self.quicksort(greater)))


array = np.array([5, 1, 2, 9, 6])
algo = QuickSort(array, gui=True)
algo.solve()

# TODO: Range is done just need to implement signal + update sort array
