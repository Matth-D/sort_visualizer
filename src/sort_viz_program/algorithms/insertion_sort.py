from . import algo_utils


class InsertionSort:
    def __init__(self, input_array, **kwargs):
        self.gui = kwargs.get("gui")
        self.signals = algo_utils.Signals()
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
        self.iterations += 1
        self.signals.signal_iterations.emit(self.iterations)
        self.signals.signal_sort_array.emit(self.sort_array)
        self.signals.signal_current.emit(x_data)

    def insertion_sort(self, sort_array):

        for i in range(1, len(sort_array)):
            while sort_array[i][1] < sort_array[i - 1][1] and i > 0:
                sort_array[i][1], sort_array[i - 1][1] = (
                    sort_array[i - 1][1],
                    sort_array[i][1],
                )
                self.update_sort_array(i)
                i -= 1
