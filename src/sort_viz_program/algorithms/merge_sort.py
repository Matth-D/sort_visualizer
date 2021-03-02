import numpy as np


class MergeSort:
    def __init__(self, sort_array):
        self.time_complexity = "O(nlogn)"
        self.space_complexity = "O(n)"
        self.sort_array = sort_array
        self.inf = float("inf")

    def solve(self):
        left_part = []
        right_part = []
        array_len = len(self.sort_array)
        if array_len <= 1:
            return self.sort_array


my_array = np.random.rand(6)
algo = MergeSort(my_array)
algo.solve()