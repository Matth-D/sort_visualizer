from PySide2 import QtCore

# import algo_utils
import numpy as np

from . import algo_utils


class HeapSort(QtCore.QObject):
    def __init__(self, input_array):
        self.signals = algo_utils.Signals()
        self.time_complexity = "O(nlogn)"
        self.space_complexity = "O(1)"
        self.input_array = input_array
        self.sort_array = self.input_array.copy()
        self.solving = 0
        self.iterations = 0

    def solve(self):
        if self.solving == 1:
            return

        self.solving = 1

        arr_len = len(self.sort_array)
        start_index = arr_len // 2 - 1

        # Create Max Heap
        for i in range(start_index, -1, -1):
            self.build_max_heap(self.sort_array, arr_len, i)

        # Swap first and last elements
        for i in range(arr_len - 1, 0, -1):
            self.sort_array[i][1], self.sort_array[0][1] = (
                self.sort_array[0][1],
                self.sort_array[i][1],
            )
            self.update_sort_array()
            self.build_max_heap(self.sort_array, i, 0)

    def build_max_heap(self, in_arr, array_length, index):
        maxi = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left > array_length or right > array_length:
            return

        if left < array_length and in_arr[maxi][1] < in_arr[left][1]:
            maxi = left

        if right < array_length and in_arr[maxi][1] < in_arr[right][1]:
            maxi = right

        if maxi != index:
            in_arr[index][1], in_arr[maxi][1] = (
                in_arr[maxi][1],
                in_arr[index][1],
            )
            self.update_sort_array()
            self.build_max_heap(in_arr, array_length, maxi)

    def update_sort_array(self):
        self.iterations += 1
        self.sort_array[:, 0] = np.arange(len(self.input_array))
        self.signals.signal_iterations.emit(self.iterations)
        self.signals.signal_sort_array.emit(self.sort_array)


# array_length = 10
# index = np.array(range(array_length))
# values = np.round(np.random.rand(array_length), decimals=3)
# input_array = np.column_stack((index, values))


# algo = HeapSort(input_array)
# print(algo.sort_array)
# algo.solve()
# print(algo.sort_array)
