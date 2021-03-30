from PySide2 import QtCore
import numpy as np

from . import algo_utils


class MergeSort(QtCore.QObject):
    def __init__(self, input_array):
        # self.signals = algo_utils.Signals()
        self.time_complexity = "O(nlogn)"
        self.space_complexity = "O(n)"
        self.input_array = input_array
        self.sort_array = self.input_array.copy()
        self.solving = 0
        self.iterations = 0
