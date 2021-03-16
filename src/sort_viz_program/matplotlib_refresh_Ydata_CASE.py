import sys

from PySide2 import QtCore, QtGui, QtWidgets
import matplotlib.backends.backend_qt5agg as beqt5agg
import matplotlib.figure as mpltfig
import matplotlib.pyplot as plt
import numpy as np


class FakeAlgo:
    def __init__(self, start_value):
        self.start_value = start_value

    def solve(self):
        while self.start_value > 0:
            self.start_value -= 0.05
            print(self.start_value)
        # send signal refresh


class ArrayGraph(beqt5agg.FigureCanvasQTAgg):
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(2, 2), constrained_layout=True)
        super(ArrayGraph, self).__init__(self.fig)
        self.set_graph_density()

    def set_graph_density(self):
        x = 1
        y = 1
        self.ax.clear()
        self.ax.bar(x, y)
        self.ax.axis("off")
        self.draw()
        self.update()


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

        self.array_graph = ArrayGraph()
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

