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
    def __init__(self, sort_array):
        self.time_complexity = "O(nlogn)"
        self.space_complexity = "O(n)"
        self.sort_array = sort_array
        self.inf = float("inf")

    def solve(self):
        self.sort_array = self.divide(self.sort_array)
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
        while left.size and right.size:
            if left[0][1] >= right[0][1]:
                merged_array = np.vstack((merged_array, right[0]))
                right = np.delete(right, 0, axis=0)
                continue
            if left[0][1] < right[0][1]:
                merged_array = np.vstack((merged_array, left[0]))
                left = np.delete(left, 0, axis=0)
                continue
        if not left.size:
            merged_array = np.vstack((merged_array, right))
        if not right.size:
            merged_array = np.vstack((merged_array, left))
        return merged_array


# arr1 = np.array([3, 2, 8, 1, 2, 9, 1])
arr1 = core.create_array_random(10)
# empty = np.empty((0, 2))
# extract1 = arr1[0]
# extract2 = arr1[1]
# empty = np.vstack((empty, extract1))
# empty = np.vstack((empty, extract2))
# empty = np.vstack((empty, extract2))
# print(empty)

# print(empty)
# result = np.append(empty, extract)

algo = MergeSort(arr1)
algo.solve()
result = algo.sort_array
print(result)


# backup merge
# def merge(self, left, right):
#     merged_array = np.empty(0)
#     while left.size and right.size:
#         if left[0] >= right[0]:
#             merged_array = np.append(merged_array, right[0])
#             right = np.delete(right, 0)
#             continue
#         if left[0] < right[0]:
#             merged_array = np.append(merged_array, left[0])
#             left = np.delete(left, 0)
#             continue
#     if not left.size:
#         merged_array = np.append(merged_array, right)
#     if not right.size:
#         merged_array = np.append(merged_array, left)
#     return merged_array
