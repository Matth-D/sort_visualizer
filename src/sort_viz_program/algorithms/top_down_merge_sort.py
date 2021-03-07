import numpy as np
from . import algo_utils

print(algo_utils)


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
        merged_array = np.empty(0)
        while left.size and right.size:
            if left[0] >= right[0]:
                print("left:", left, "left[0]:", left[0])
                print("right:", right, "right[-1]:", right[-1])
                merged_array = np.append(merged_array, right[0])
                right = np.delete(right, 0)
                continue
            if left[0] < right[0]:
                merged_array = np.append(merged_array, left[0])
                left = np.delete(left, 0)
                continue
        if not left.size:
            merged_array = np.append(merged_array, right)
        if not right.size:
            merged_array = np.append(merged_array, left)
        return merged_array


arr1 = np.array([3, 2, 8, 1, 2, 9, 1])
algo = MergeSort(arr1)
algo.solve()
result = algo.sort_array
print(result)