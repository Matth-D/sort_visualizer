from PySide2 import QtCore
import numpy as np


class Signals(QtCore.QObject):
    signal_sort_array = QtCore.Signal(np.ndarray)
    signal_iterations = QtCore.Signal(int)
