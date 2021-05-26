def quicksort(input_array):
    if len(input_array) < 2:
        return input_array

    pivot = input_array[0]
    smaller = [i for i in input_array[1:] if i < pivot]
    greater = [i for i in input_array[1:] if i >= pivot]
    print(quicksort(smaller) + [pivot] + quicksort(greater))
    return quicksort(smaller) + [pivot] + quicksort(greater)


# array = [1, 18, 91, 32, 1, 1, 9, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
array = [5, 2, 6, 1, 8]

# quicksort(array)

import numpy as np

# from . import algo_utils


class QuickSort:
    """QuickSort algorithm."""

    def __init__(self, input_array, **kwargs):
        """Class init.

        Args:
            input_array (np.ndarray): Array to sort.
        """
        # self.gui = kwargs.get("gui")
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

        self.quicksort(self.input_array)

        self.solving = 0
        self.solved = 1

    def quicksort(self, input_array):
        if len(input_array) < 2:
            return input_array

        pivot = input_array[0]
        smaller = input_array[input_array[1] < pivot[1]]
        print(pivot)
        print(smaller)

        # return np.hstack((self.quicksort(smaller), pivot, self.quicksort(greater)))


array = np.array([5, 1, 2, 9, 6])
selection = array[array > 4]
algo = QuickSort(array)
algo.solve()
#
# arr1 = np.array([3, 4])
# arr2 = np.array([1, 2])

