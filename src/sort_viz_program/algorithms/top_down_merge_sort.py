import os
import sys

import numpy as np

core_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if core_path not in sys.path:
    sys.path.append(core_path)

import sort_viz_program.core as core

# from . import algo_utils


# print(algo_utils)


class MergeSort:
    def __init__(self, input_array):
        self.time_complexity = "O(nlogn)"
        self.space_complexity = "O(n)"
        self.input_array = input_array
        self.sort_array = input_array
        self.inf = float("inf")

    def solve(self):
        self.input_array = self.divide(self.input_array)
        return

    def divide(self, sort_array):
        if len(sort_array) <= 1:
            return sort_array
        mid = len(sort_array) // 2

        array_left = sort_array[:mid]
        array_right = sort_array[mid:]

        array_left = self.divide(array_left)
        array_right = self.divide(array_right)

        return self.merge(array_left, array_right)

    def merge(self, left, right):
        merged_array = np.empty((0, 2))

        left_index = int(left[0][0])
        right_index = int(right[-1][0])

        slice_array = np.vstack((left, right))
        # print(compare_array.shape)
        while left.size and right.size:
            if left[0][1] >= right[0][1]:
                merged_array = np.vstack((merged_array, right[0]))
                right = np.delete(right, 0, axis=0)
                slice_array[0 : len(merged_array)] = merged_array
                slice_array[:, 0] = np.arange(left_index, right_index + 1)
                # self.sort_array[left_index : right_index + 1] = slice_array
                print(self.sort_array)
                # self.sort_array[:, 0] = np.arange(len(self.sort_array))
                continue
            if left[0][1] < right[0][1]:
                merged_array = np.vstack((merged_array, left[0]))
                left = np.delete(left, 0, axis=0)
                slice_array[0 : len(merged_array)] = merged_array
                slice_array[:, 0] = np.arange(left_index, right_index + 1)
                print(self.sort_array)
                # self.sort_array[left_index : right_index + 1] = slice_array
                # self.sort_array[:, 0] = np.arange(len(self.sort_array))
                continue
        if not left.size:
            merged_array = np.vstack((merged_array, right))
            slice_array[0 : len(merged_array)] = merged_array
            slice_array[:, 0] = np.arange(left_index, right_index + 1)
            print(self.sort_array)
            # self.sort_array[left_index : right_index + 1] = slice_array
            # self.sort_array[:, 0] = np.arange(len(self.sort_array))
        if not right.size:
            merged_array = np.vstack((merged_array, left))
            slice_array[0 : len(merged_array)] = merged_array
            slice_array[:, 0] = np.arange(left_index, right_index + 1)
            self.sort_array[left_index : right_index + 1] = slice_array
            print(self.sort_array)
            # self.sort_array[:, 0] = np.arange(len(self.sort_array))
        merged_array[:, 0] = np.arange(left_index, right_index + 1)
        print("----")
        return merged_array


values = np.array([3, 2, 1, 8, 5, 9])
index = np.array(range(len(values)))

arr1 = np.column_stack((index, values))

algo = MergeSort(arr1)
algo.solve()
print(algo.sort_array)

# TODO shit sorted? run bigger tests, cool cool cool and wrap up update sort array