import numpy as np

from . import algo_utils


class MergeSort:
    """Merge sort algorithm."""

    def __init__(self, input_array, **kwargs):
        """Class init.

        Args:
            input_array (np.ndarray): Array to sort.
        """
        self.gui = kwargs.get("gui")
        print(self.gui)
        self.signals = algo_utils.Signals()
        self.time_complexity = "O(nlogn)"
        self.space_complexity = "O(n)"
        self.input_array = input_array
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

        self.input_array = self.divide(self.input_array)

        self.solving = 0
        self.solved = 1

    def divide(self, input_array):
        """Recursively divide array to sort into half from top to bottom.

        Args:
            input_array (np.ndarray): Numpy array to split.

        Returns:
            np.ndarray: Reordered and merged array from bottom to top.
        """
        if len(input_array) <= 1:
            return input_array
        mid = len(input_array) // 2

        array_left = input_array[:mid]
        array_right = input_array[mid:]

        array_left = self.divide(array_left)
        array_right = self.divide(array_right)

        return self.merge(array_left, array_right)

    def update_sort_array(self, left_index, right_index, slice_array, x_data):
        """Update sort array with current left and right reordered slices.
        Left and right index are used to insert ordered slice in original array.
        Send signals to Graph.

        Args:
            left_index (int): Index of first element of left slice.
            right_index (int): Index of last element of right slice.
            slice_array (np.ndarray): Left and Right slices merged.
            x_data (int): Currently examined element's X value.
        """
        self.sort_array[left_index : right_index + 1] = slice_array
        self.sort_array[:, 0] = np.arange(len(self.sort_array))
        self.signals.signal_sort_array.emit(self.sort_array)
        self.iterations += 1
        self.signals.signal_iterations.emit(self.iterations)
        self.signals.signal_current.emit(x_data)

    def merge(self, left, right):
        """Merge left and right slices in a sorted array.

        Args:
            left (np.ndarray): Left slice.
            right (np.ndarray): Right slice.

        Returns:
            np.ndarray: Left and Right slices sorted in a single array.
        """
        merged_array = np.empty((0, 2))

        left_index = int(left[0][0])
        right_index = int(right[-1][0])

        slice_array = np.vstack((left, right))
        while left.size and right.size:
            if left[0][1] >= right[0][1]:
                x_data = right[0][0]
                merged_array = np.vstack((merged_array, right[0]))
                right = np.delete(right, 0, axis=0)
                slice_array[0 : len(merged_array)] = merged_array
                slice_array[:, 0] = np.arange(left_index, right_index + 1)
                self.update_sort_array(left_index, right_index, slice_array, x_data)
                continue
            if left[0][1] < right[0][1]:
                x_data = left[0][0]
                merged_array = np.vstack((merged_array, left[0]))
                left = np.delete(left, 0, axis=0)
                slice_array[0 : len(merged_array)] = merged_array
                slice_array[:, 0] = np.arange(left_index, right_index + 1)
                self.update_sort_array(left_index, right_index, slice_array, x_data)
                continue
        if not left.size:
            x_data = right[0][0]
            merged_array = np.vstack((merged_array, right))
            slice_array[0 : len(merged_array)] = merged_array
            slice_array[:, 0] = np.arange(left_index, right_index + 1)
            self.update_sort_array(left_index, right_index, slice_array, x_data)
        if not right.size:
            x_data = left[0][0]
            merged_array = np.vstack((merged_array, left))
            slice_array[0 : len(merged_array)] = merged_array
            slice_array[:, 0] = np.arange(left_index, right_index + 1)
            self.update_sort_array(left_index, right_index, slice_array, x_data)

        merged_array[:, 0] = np.arange(left_index, right_index + 1)
        return merged_array
