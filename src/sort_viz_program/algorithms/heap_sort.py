from . import algo_utils


class HeapSort:
    def __init__(self, input_array, **kwargs):
        self.gui = kwargs.get("gui")
        self.signals = algo_utils.Signals()
        self.time_complexity = "O(nlogn)"
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

        arr_len = len(self.sort_array)
        start_index = arr_len // 2 - 1

        # Create Max Heap
        for i in range(start_index, -1, -1):
            self.build_max_heap(self.sort_array, arr_len, i)

        # Swap first and last elements
        for i in range(arr_len - 1, 0, -1):
            self.sort_array[i], self.sort_array[0] = (
                self.sort_array[0],
                self.sort_array[i],
            )
            self.update_sort_array(i)
            self.build_max_heap(self.sort_array, i, 0)

        self.solving = 0
        self.solved = 1

    def build_max_heap(self, in_arr, array_length, index):
        maxi = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left > array_length or right > array_length:
            return

        if left < array_length and in_arr[maxi] < in_arr[left]:
            maxi = left

        if right < array_length and in_arr[maxi] < in_arr[right]:
            maxi = right

        if maxi != index:
            in_arr[index], in_arr[maxi] = (
                in_arr[maxi],
                in_arr[index],
            )
            self.update_sort_array(index)
            self.build_max_heap(in_arr, array_length, maxi)

    def update_sort_array(self, x_data):
        self.iterations += 1
        self.signals.signal_iterations.emit(self.iterations)
        self.signals.signal_sort_array.emit(self.sort_array)
        self.signals.signal_current.emit(x_data)


# array_length = 10
# index = np.array(range(array_length))
# values = np.round(np.random.rand(array_length), decimals=3)
# input_array = np.column_stack((index, values))


# algo = HeapSort(input_array)
# print(algo.sort_array)
# algo.solve()
# print(algo.sort_array)
