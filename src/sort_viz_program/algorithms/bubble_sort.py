from PySide2 import QtCore
import numpy as np

from . import algo_utils


class BubbleSort:
    def __init__(self, input_array):
        self.signals = algo_utils.Signals()
        self.time_complexity = "O(n\u00b2)"
        self.space_complexity = "O(1)"
        self.input_array = input_array
        self.sort_array = self.input_array.copy()
        self.solving = 0
        self.iterations = 0

    def solve(self):

        for i in range(len(self.input_array)):
            switch = False
            for j in range(0, len(self.input_array) - i - 1):
                if self.sort_array[j][1] > self.sort_array[j + 1][1]:
                    self.sort_array[j][1], self.sort_array[j + 1][1] = (
                        self.sort_array[j + 1][1],
                        self.sort_array[j][1],
                    )
                    self.update_sort_array()
                    switch = True
            if not switch:
                break

    def update_sort_array(self):
        self.iterations += 1
        self.sort_array[:, 0] = np.arange(len(self.input_array))
        self.signals.signal_iterations.emit(self.iterations)
        self.signals.signal_sort_array.emit(self.sort_array)


# array_length = 7
# index = np.array(range(array_length))
# values = np.round(np.random.rand(array_length), decimals=3)
# input_array = np.column_stack((index, values))

# print(input_array)
# bb = BubbleSort(input_array)
# bb.solve()
# print(bb.sort_array)


# np1 = np.array([2, 1, 4])

# i = 1

# np1[i], np1[i + 1] = np1[i + 1], np1[i]

# np2 = input_array
# print(np2)

# i = 1
# np2[i][1], np2[i + 1][1] = np2[i + 1][1], np2[i][1]

# print(np2)
