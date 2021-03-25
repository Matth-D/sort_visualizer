import sys

from PySide2 import QtCore, QtGui, QtWidgets
import algorithms.top_down_merge_sort as top_down_merge_sort
import core
import matplotlib.backends.backend_qt5agg as beqt5agg
import matplotlib.figure as mpltfig
import matplotlib.pyplot as plt
import numpy as np

# from . import core
# from .algorithms import top_down_merge_sort


class ArrayGraph(beqt5agg.FigureCanvasQTAgg):
    def __init__(self, algorithm_value, default_density):
        # self.fig, self.ax = plt.subplots(figsize=(0.1, 0.1), constrained_layout=True)
        self.fig, self.ax = plt.subplots(figsize=(1, 1), dpi=1, constrained_layout=True)
        plt.ioff()
        super(ArrayGraph, self).__init__(self.fig)
        self.algorithm_value = algorithm_value
        self.input_array = core.create_array_random(10)
        self.algorithm = None
        self.bars = None
        self.signals = None
        self.density = default_density
        self.set_graph_density(self.density)
        self.set_algorithm(self.algorithm_value)

    def set_graph_density(self, density):
        self.input_array = core.create_array_random(density)
        x = self.input_array[:, 0]
        y = self.input_array[:, 1]
        self.ax.clear()
        self.bars = self.ax.bar(x, y)
        self.ax.axis("off")
        self.draw()
        self.update()

    @QtCore.Slot(np.ndarray)
    def update_bars(self, sort_array):
        if not self.bars:
            return
        y_data = sort_array[:, 1]
        for i, elem in enumerate(self.bars):
            elem.set_height(y_data[i])

        self.flush_events()
        self.draw()

    def set_algorithm(self, value):
        self.algorithm_value = value
        algorithm_arg = self.input_array
        if self.algorithm_value == "Top Down Merge Sort":
            self.algorithm = top_down_merge_sort.MergeSort(algorithm_arg)
        self.signals = self.algorithm.signals
        self.signals.signal_sort_array.connect(self.update_bars)

    def solve_algorithm(self):
        self.set_algorithm(self.algorithm_value)
        self.algorithm.solve()


class SortVisualizer(QtWidgets.QDialog):
    def __init__(self):
        super(SortVisualizer, self).__init__()
        self.algorithms_list = [
            "Top Down Merge Sort",
            "Bubble Sort",
            "Heap Sort",
            "Insert Sort",
        ]
        self.algorithm_value = self.algorithms_list[0]
        self.algorithm = None
        self.init_ui()
        self.setGeometry(300, 300, self.app_size[0], self.app_size[1])
        # self.setGeometry(300, 300, self.app_size[0], self.app_size[1])
        self.setWindowTitle("Sort Visualizer")
        self.center_window()

    def init_ui(self):
        self.screen_size = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        w_width = 600
        w_height = 500
        self.app_size = (w_width, w_height)
        # Create Widgets
        self.main_layout = QtWidgets.QVBoxLayout()

        default_density = 40
        self.array_graph = ArrayGraph(self.algorithm_value, default_density)
        self.density_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)

        self.layout_h1 = QtWidgets.QHBoxLayout()

        self.layout_v1 = QtWidgets.QVBoxLayout()
        self.algorithm_list = QtWidgets.QComboBox()
        self.algorithm_list.addItems(self.algorithms_list)
        self.vertical_spacer1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )

        self.layout_v2 = QtWidgets.QVBoxLayout()

        self.layout_h2 = QtWidgets.QHBoxLayout()

        self.sort_button = QtWidgets.QPushButton("Sort", self)
        self.reset_button = QtWidgets.QPushButton("Reset", self)

        self.layout_v3 = QtWidgets.QVBoxLayout()
        self.infos_label = QtWidgets.QLabel("Infos:")
        self.array_length_label = QtWidgets.QLabel("Array Length:")
        self.iterations_label = QtWidgets.QLabel("Iterations:")
        self.time_complexity_label = QtWidgets.QLabel("Time Complexity:")
        self.space_complexity_label = QtWidgets.QLabel("Space Complexity:")

        # Arrange Layout
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.array_graph)
        self.main_layout.addWidget(self.density_slider)
        self.main_layout.addLayout(self.layout_h1)

        self.layout_h1.addLayout(self.layout_v1)
        self.layout_h1.setSpacing(25)
        self.layout_v1.addWidget(self.algorithm_list)
        self.layout_v1.addItem(self.vertical_spacer1)
        self.layout_h1.addLayout(self.layout_v2)
        self.layout_v2.addLayout(self.layout_h2)

        self.layout_h2.addWidget(self.sort_button)
        self.layout_h2.addWidget(self.reset_button)
        self.layout_h2.setSpacing(27)
        self.layout_v2.addItem(self.vertical_spacer1)

        self.layout_h1.addLayout(self.layout_v3)
        self.layout_v3.addWidget(self.infos_label)
        self.layout_v3.addWidget(self.array_length_label)
        self.layout_v3.addWidget(self.iterations_label)
        self.layout_v3.addWidget(self.time_complexity_label)
        self.layout_v3.addWidget(self.space_complexity_label)

        self.main_layout.setStretch(0, 4)
        self.main_layout.setStretch(2, 1)

        # Appearence
        square_button_size = 70
        self.sort_button.setMinimumHeight(square_button_size)
        self.sort_button.setMaximumWidth(square_button_size)
        self.reset_button.setMinimumHeight(square_button_size)
        self.reset_button.setMaximumWidth(square_button_size)
        self.algorithm_list.setMaximumWidth(300)
        self.density_slider.setMinimum(1)
        self.density_slider.setMaximum(300)
        self.density_slider.setValue(default_density)

        # Connects
        # self.density_slider.sliderReleased.connect(self.array_graph.set_graph_density)
        self.density_slider.valueChanged.connect(self.array_graph.set_graph_density)
        self.algorithm_list.currentTextChanged.connect(self.array_graph.set_algorithm)
        self.sort_button.clicked.connect(self.array_graph.solve_algorithm)

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
