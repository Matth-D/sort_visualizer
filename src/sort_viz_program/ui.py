import sys

from PySide2 import QtCore, QtGui, QtWidgets
import matplotlib.backends.backend_qt5agg as beqt5agg
import matplotlib.figure as mpltfig
import matplotlib.pyplot as plt
import numpy as np


class ArrayGraph(beqt5agg.FigureCanvasQTAgg):
    def __init__(self, default_array_length):
        self.fig = plt.figure()
        # self.ax = self.fig.add_subplot(111)
        self.ax = self.fig.add_axes([0, 1], [0, 1])
        self.x = np.arange(default_array_length)
        self.y = np.random.rand(default_array_length)
        self.plot_graph()
        super(ArrayGraph, self).__init__(self.fig)

    def plot_graph(self):
        self.ax.bar(self.x, self.y, width=0.1)

    # def plot_values(self, value_range):
    #     # self.fig.clear()
    #     self.x = np.arange(value_range)
    #     self.y = np.random.rand(value_range)
    #     self.fig.canvas.draw()
    #     self.fig.canvas.flush_events()
    #     self.update()
    # self.plot_graph()
    # self.show()
    # return x, y


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
            round(self.screen_size.width() * 0.6),
            round(self.screen_size.height() * 0.54),
        )
        # Create Widgets
        self.main_layout = QtWidgets.QVBoxLayout()

        default_array_length = 15
        self.array_graph = ArrayGraph(default_array_length)
        # self.array_viewer.setStyleSheet("background-color:teal")
        self.array_length_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)

        self.layout_h1 = QtWidgets.QHBoxLayout()

        self.layout_v1 = QtWidgets.QVBoxLayout()
        self.algorithm_list = QtWidgets.QComboBox()
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
        self.main_layout.addWidget(self.array_length_slider)
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
        self.array_length_slider.setValue(default_array_length)
        # self.array_length_slider.valueChanged.connect(self.array_graph.plot_values)

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

