from PySide2 import QtCore
import numpy as np


class Signals(QtCore.QObject):
    signal_sort_array = QtCore.Signal(np.ndarray)


class BubbleSort:
    def __init__(self, input_array):
        self.signals = Signals()
        self.time_complexity = "O(n\u00b2)"
        self.space_complexity = "O(1)"
        self.input_array = input_array
        self.sort_array = self.input_array.copy()

