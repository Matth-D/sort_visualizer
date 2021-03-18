import sys

from PySide2 import QtCore, QtGui, QtWidgets
import matplotlib.backends.backend_qt5agg as beqt5agg
import matplotlib.figure as mpltfig
import matplotlib.pyplot as plt
import numpy as np

# TODO Finish Case Study with mdev/custom_signal_algo_update exemple and figure out if update works with matplotlib


class Signals(QtCore.QObject):
    signal_print = QtCore.Signal(int)


class FakeAlgo:
    def __init__(self, start_array):
        self.start_array = start_array
        self.data_array = self.start_array.copy()

    def solve(self):
        for i in range(10):
            self.data_array *= 0.95


class ArrayGraph(beqt5agg.FigureCanvasQTAgg):
    def __init__(self, range_value):
        self.fig, self.ax = plt.subplots(figsize=(2, 2), constrained_layout=True)
        super(ArrayGraph, self).__init__(self.fig)
        self.range_value = range_value
        self.init_graph(range_value)

    def init_graph(self):
        x = np.arange(self.range_value)
        y = np.round(np.random.rand(len(self.range_value)), decimals=3)
        self.ax.bar(x, y)
        self.ax.axis("off")
        self.draw()


class SortVisualizer(QtWidgets.QDialog):
    def __init__(self):
        super(SortVisualizer, self).__init__()
        self.init_ui()
        self.setGeometry(300, 300, self.app_size[0], self.app_size[1])
        self.setWindowTitle("Sort Visualizer")
        self.center_window()

    def init_ui(self):
        self.screen_size = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        self.app_size = (
            round(self.screen_size.width() * 0.1),
            round(self.screen_size.height() * 0.2),
        )
        # Create Widgets
        self.main_layout = QtWidgets.QVBoxLayout()

        range_value = 10
        self.array_graph = ArrayGraph(10)
        self.solve_button = QtWidgets.QPushButton("SOLVE", self)

        # Arrange Layout
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.array_graph)
        self.main_layout.addWidget(self.solve_button)

        # Connects

    def center_window(self):
        """Centers window on screen."""
        app_geo = self.frameGeometry()
        center_point = (
            QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        )
        app_geo.moveCenter(center_point)
        self.move(app_geo.topLeft())


def main():
    """Set main program function."""
    app = QtWidgets.QApplication(sys.argv)
    sort_visualizer = SortVisualizer()
    sort_visualizer.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

