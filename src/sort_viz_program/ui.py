import sys

from PySide2 import QtCore, QtGui, QtWidgets
import algorithms.top_down_merge_sort as top_down_merge_sort
import core
import matplotlib.backends.backend_qt5agg as beqt5agg
import matplotlib.figure as mpltfig
import matplotlib.pyplot as plt
import numpy as np

# from .algorithms import top_down_merge_sort


class ArrayGraph(beqt5agg.FigureCanvasQTAgg):
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(2, 2), constrained_layout=True)
        super(ArrayGraph, self).__init__(self.fig)
        self.sort_array = core.create_array_random(10)
        self.set_graph_density()

    def set_graph_density(self, density=10):
        self.sort_array = core.create_array_random(density)
        # self.y = np.round(np.random.rand(density), decimals=3)
        # self.x = np.arange(len(self.y))
        # self.x = self.sort_array
        x = self.sort_array[:, 0]
        y = self.sort_array[:, 1]
        self.ax.clear()
        self.ax.bar(x, y)
        self.ax.axis("off")
        self.draw()

    def set_algorithm(self, value):
        self.algorithm_value = value
        print(self.algorithm_value)


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
        self.setWindowTitle("Sort Visualizer")
        self.center_window()

    def init_ui(self):
        self.screen_size = QtGui.QGuiApplication.primaryScreen().availableGeometry()
        self.app_size = (
            round(self.screen_size.width() * 0.6),
            round(self.screen_size.height() * 0.6),
        )
        # Create Widgets
        self.main_layout = QtWidgets.QVBoxLayout()

        self.array_graph = ArrayGraph()
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

        self.main_layout.setStretch(0, 3)
        self.main_layout.setStretch(2, 1)

        # Appearence
        self.sort_button.setMinimumHeight(self.app_size[0] * 0.07)
        self.sort_button.setMaximumWidth(self.app_size[0] * 0.07)
        self.reset_button.setMinimumHeight(self.app_size[0] * 0.07)
        self.reset_button.setMaximumWidth(self.app_size[0] * 0.07)
        self.algorithm_list.setMaximumWidth(self.app_size[0] * 0.25)

        # Connects
        self.density_slider.valueChanged.connect(self.array_graph.set_graph_density)
        self.algorithm_list.currentTextChanged.connect(self.array_graph.set_algorithm)
        self.density_slider.setMinimum(1)
        self.density_slider.setMaximum(300)
        self.density_slider.setValue(10)

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
    # app = QtWidgets.QApplication(sys.argv)
    # graph = ArrayGraph()
    # graph.show()
    # sys.exit(app.exec_())
    main()
