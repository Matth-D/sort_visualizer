import os
import sys

from PySide2 import QtCore, QtGui, QtWidgets
import numpy as np


class Signals(QtCore.QObject):
    signal_sort_array = QtCore.Signal(np.ndarray)
    # signal_test = QtCore.Signal(int)


class MergeSort(QtCore.QObject):
    def __init__(self, input_array):
        self.signals = Signals()
        self.time_complexity = "O(nlogn)"
        self.space_complexity = "O(n)"
        self.input_array = input_array
        self.sort_array = self.input_array.copy()
        self.inf = float("inf")
        self.solving = 0

    def solve(self):
        self.solving = 1
        self.input_array = self.divide(self.input_array)
        self.solving = 0
        return

    def divide(self, input_array):
        if len(input_array) <= 1:
            return input_array
        mid = len(input_array) // 2

        array_left = input_array[:mid]
        array_right = input_array[mid:]

        array_left = self.divide(array_left)
        array_right = self.divide(array_right)

        return self.merge(array_left, array_right)

    def update_sort_array(self, left_index, right_index, slice_array):

        self.sort_array[left_index : right_index + 1] = slice_array
        self.sort_array[:, 0] = np.arange(len(self.sort_array))
        self.signals.signal_sort_array.emit(self.sort_array)
        # self.signals.signal_test.emit(self.test_var)

    def merge(self, left, right):
        merged_array = np.empty((0, 2))

        left_index = int(left[0][0])
        right_index = int(right[-1][0])

        slice_array = np.vstack((left, right))
        while left.size and right.size:
            if left[0][1] >= right[0][1]:
                merged_array = np.vstack((merged_array, right[0]))
                right = np.delete(right, 0, axis=0)
                slice_array[0 : len(merged_array)] = merged_array
                slice_array[:, 0] = np.arange(left_index, right_index + 1)
                self.update_sort_array(left_index, right_index, slice_array)
                continue
            if left[0][1] < right[0][1]:
                merged_array = np.vstack((merged_array, left[0]))
                left = np.delete(left, 0, axis=0)
                slice_array[0 : len(merged_array)] = merged_array
                slice_array[:, 0] = np.arange(left_index, right_index + 1)
                self.update_sort_array(left_index, right_index, slice_array)
                continue
        if not left.size:
            merged_array = np.vstack((merged_array, right))
            slice_array[0 : len(merged_array)] = merged_array
            slice_array[:, 0] = np.arange(left_index, right_index + 1)
            self.update_sort_array(left_index, right_index, slice_array)
        if not right.size:
            merged_array = np.vstack((merged_array, left))
            slice_array[0 : len(merged_array)] = merged_array
            slice_array[:, 0] = np.arange(left_index, right_index + 1)
            self.update_sort_array(left_index, right_index, slice_array)

        merged_array[:, 0] = np.arange(left_index, right_index + 1)
        return merged_array
