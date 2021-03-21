import sys

from PySide2 import QtCore, QtGui, QtWidgets
import matplotlib.backends.backend_qt5agg as beqt5agg
import matplotlib.figure as mpltfig
import matplotlib.pyplot as plt
import numpy as np

# TODO Finish Case Study with mdev/custom_signal_algo_update exemple and figure out if update works with matplotlib
# Reference: matplotlib_refreshYdata_EXAMPLE / custom_signals_algo_update


class Signals(QtCore.QObject):
    signal_ydata = QtCore.Signal(list)


class FakeAlgo:
    def __init__(self, start_array):
        self.start_array = start_array
        self.data_array = self.start_array.copy()
        self.signals = Signals()

    def solve(self):
        for i in range(30):
            self.data_array[0] *= 0.95
            self.data_array[2] *= 0.95
            self.signals.signal_ydata.emit(self.data_array)


class Graph(beqt5agg.FigureCanvasQTAgg):
    def __init__(self, range_value):
        self.fig, self.ax = plt.subplots(figsize=(2, 2), constrained_layout=True)
        super(Graph, self).__init__(self.fig)
        self.range_value = range_value
        self.random_array = self.create_array_random(self.range_value)
        self.x_data, self.y_data = None, None
        self.init_graph()
        self.algorithm = FakeAlgo(self.random_array[1])
        self._plot_ref = None
        self.signals = self.algorithm.signals
        self.signals.signal_ydata.connect(self.update_plot)

    def create_array_random(self, density):
        x = np.arange(density)
        y = np.round(np.random.rand(density), decimals=3)
        return x, y

    def init_graph(self):
        self.x_data = self.random_array[0]
        self.y_data = self.random_array[1]
        self.ax.bar(self.x_data, self.y_data)
        self.ax.axis("off")
        self.draw()

    def update_plot(self, value):
        print("update_plot")
        self.y_data = value

        if self._plot_ref is None:
            plot_refs = self.ax(self.x_data, self.y_data, "r")
            self._plot_ref = plot_refs[0]
        else:
            self._plot_ref.set_ydata(self.y_data)

        self.draw()
        self.flush_events()


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
        self.array_graph = Graph(range_value)
        self.solve_button = QtWidgets.QPushButton("SOLVE", self)

        # Arrange Layout
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.array_graph)
        self.main_layout.addWidget(self.solve_button)

        # Connects
        self.solve_button.clicked.connect(self.array_graph.algorithm.solve)

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
