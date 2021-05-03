import numpy as np

# from . import algo_utils


class BinarySort:
    def __init__(self, input_array):
        # self.gui = kwargs.get("gui")
        # self.signals = algo_utils.Signals()
        self.time_complexity = "O(n\u00b2)"
        self.space_complexity = "O(1)"
        self.input_array = input_array
        self.sort_array = self.input_array.copy()
        self.solving = 0
        self.solved = 0
        self.iterations = 0

    def solve(self):
        if self.solving == 1:
            return

        if self.solved == 1:
            return

        self.solving = 1
        self.insertion_sort(self.sort_array)
        self.solving = 0
        self.solved = 1

    def update_sort_array(self, x_data):
        if not self.gui:
            return
        self.iterations += 1
        self.signals.signal_iterations.emit(self.iterations)
        self.signals.signal_sort_array.emit(self.sort_array)
        self.signals.signal_current.emit(x_data)

    def binary_search(self, array, value, left, right):
        """Perform binary search on sorted array.

        Args:
            array (np.ndarray): Array in which to find the value
            value (float): Value to find in the array
            left (int): Left pointer
            right (int): Right pointer

        Returns:
            int: Index of searched value
        """
        if right < left:
            return -1

        middle = left + (right - left) // 2

        if array[middle] == value:
            return middle

        if array[middle] < value:
            return self.binary_search(array, value, middle + 1, right)

        if array[middle] > value:
            return self.binary_search(array, value, left, middle - 1)

    def insertion_sort(self, input_array):

        for i in range(1, len(input_array)):
            val = input_array[i]
            index = self.binary_search(input_array, val, 0, i - 1)

