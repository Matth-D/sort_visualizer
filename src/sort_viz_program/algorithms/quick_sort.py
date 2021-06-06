import random

import numpy as np

from . import algo_utils


class QuickSort:
    """QuickSort algorithm."""

    def __init__(self, input_array, **kwargs):
        """Class init.

        Args:
            input_array (np.ndarray): Array to sort.
        """
        self.gui = kwargs.get("gui")
        self.signals = algo_utils.Signals()
        self.time_complexity = "O(nlogn)"
        self.space_complexity = "O(logn)"
        self.input_array = input_array
        tmp_index = np.arange(len(self.input_array))
        self.input_array = np.column_stack((tmp_index, self.input_array))
        self.sort_array = self.input_array.copy()
        self.solving = 0
        self.solved = 0
        self.iterations = 0

    def solve(self):
        """Solve Quick sort algorithm."""
        if self.solving == 1:
            return

        if self.solved == 1:
            return

        self.solving = 1

        self.quicksort(self.input_array)

        self.solving = 0
        self.solved = 1

    def quicksort(self, input_array):
        """Sort input_array using Quick Sort.

        Args:
            input_array (np.ndarray): Array to sort.

        Returns:
            [np.ndarray]: Sorted array
        """
        first_i = input_array[0][0]

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

        size_smaller = len(smaller)
        size_greater = len(greater)

        # Set index values
        if smaller.size > 0:
            smaller[:, 0] = self.create_range(first_i, first_i + size_smaller)
        if pivot.size > 0:
            pivot[0] = first_i + size_smaller
        if greater.size > 0:
            greater[:, 0] = np.arange(
                first_i + size_smaller + 1, first_i + size_smaller + 1 + size_greater
            )

        self.update_sort_array(smaller, pivot, greater)
        return self.recur_quicksort(smaller, pivot, greater)

    def create_range(self, start, end):
        """Create numpy range between start and end args.

        Args:
            start (int): range start
            end (end): range end

        Returns:
            [np.ndarray]: Numpy range from start to end,
        """
        if start == end:
            return np.array([start])
        return np.arange(start, end)

    def concat_arrays(self, *arrays):
        # TODO: Maybe move this one to algo utils?
        """Concatenates two numpy arrays.

        Returns:
            [np.ndarray]: Merged array
        """
        filter_empty = tuple([arr for arr in arrays if arr.size > 0])
        return np.vstack(filter_empty)

    def recur_quicksort(self, smaller, pivot, greater):
        if smaller.size == 0:
            return np.vstack((pivot, self.quicksort(greater)))
        if greater.size == 0:
            return np.vstack((self.quicksort(smaller), pivot))
        return np.vstack((self.quicksort(smaller), pivot, self.quicksort(greater)))

    def update_sort_array(self, smaller, pivot, greater):
        """Update sort array with current left and right reordered slices.
        Left and right index are used to insert ordered slice in original array.
        Send signals to Graph.

        Args:
            smaller (np.ndarray): Values smaller than current pivot.
            pivot (np.ndarray): Pivot
            greater (np.ndarray): Values greater than current pivot.
        """

        merged_arrays = self.concat_arrays(smaller, pivot, greater)
        left_index = int(merged_arrays[0][0])
        right_index = int(merged_arrays[-1][0])
        self.sort_array[left_index : right_index + 1] = merged_arrays
        if not self.gui:
            return
        x_data = pivot[0]
        self.signals.signal_sort_array.emit(self.sort_array[:, 1])
        self.iterations += 1
        self.signals.signal_iterations.emit(self.iterations)
        self.signals.signal_current.emit(x_data)
