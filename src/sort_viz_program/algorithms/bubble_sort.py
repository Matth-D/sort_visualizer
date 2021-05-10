from . import algo_utils


class BubbleSort:
    """Bubble Sort algorithm."""

    def __init__(self, input_array, **kwargs):
        """Class init.

        Args:
            input_array (np.ndarray): Array to sort.
        """
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
        """Solve Bubble Sort algorithm."""
        if self.solving == 1:
            return

        if self.solved == 1:
            return

        self.solving = 1

        for i in range(len(self.input_array)):
            switch = False
            for j in range(0, len(self.input_array) - i - 1):
                if self.sort_array[j] > self.sort_array[j + 1]:
                    self.sort_array[j], self.sort_array[j + 1] = (
                        self.sort_array[j + 1],
                        self.sort_array[j],
                    )
                    self.update_sort_array(j + 2)
                    switch = True
            if not switch:
                break

        self.solving = 0
        self.solved = 1

    def update_sort_array(self, x_data):
        """Update sort_array variable, iterations and send signals during solve.

        Args:
            x_data (int): X coordinate of current element being switched.
        """
        if not self.gui:
            return
        self.iterations += 1
        self.signals.signal_iterations.emit(self.iterations)
        self.signals.signal_sort_array.emit(self.sort_array)
        self.signals.signal_current.emit(x_data)


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
