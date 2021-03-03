import sys

from PySide2 import QtCore, QtGui, QtWidgets
import matplotlib.backends.backend_qt5agg as beqt5agg
import matplotlib.figure as mpltfig
import matplotlib.pyplot as plt
import numpy as np


class Graph(beqt5agg.FigureCanvasQTAgg):
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super(Graph, self).__init__(self.fig)
        self.x = np.arange(1)
        self.y = np.random.rand(1)
        self.ax.bar(self.x, self.y)

    def update_graph(self, slider_value):
        self.x = np.arange(slider_value)
        self.y = np.random.rand(slider_value)
        self.ax.clear()
        self.ax.bar(self.x, self.y)
        self.draw()
        pass


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
            round(self.screen_size.width() * 0.3),
            round(self.screen_size.height() * 0.24),
        )
        # Create Widgets
        self.main_layout = QtWidgets.QVBoxLayout()
        # self.graph = QtWidgets.QWidget(self)
        # self.graph.setStyleSheet("background-color:red")
        self.graph = Graph()
        # self.button = QtWidgets.QPushButton("Add", self)
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.graph)
        self.main_layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.graph.update_graph)
        # self.button.clicked.connect(self.graph.increase_density)
        # self.button.clicked.connect(self.graph.update_graph)

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
