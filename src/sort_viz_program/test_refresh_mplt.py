import sys

from PySide2 import QtCore, QtGui, QtWidgets
import matplotlib.backends.backend_qt5agg as beqt5agg
import matplotlib.figure as mpltfig
import matplotlib.pyplot as plt
import numpy as np


class Graph(beqt5agg.FigureCanvasQTAgg):
    def __init__(self, parent=None):
        self.fig, self.ax = plt.subplots(figsize=(10, 10), constrained_layout=True)
        super(Graph, self).__init__(self.fig)
        self.setParent(parent)
        self.set_graph_density()
        # self.y = np.round(np.random.rand(1), decimals=3)
        # self.x = np.arange(len(self.y))
        # self.ax.bar(self.x, self.y)
        # self.ax.axis("off")

    def set_graph_density(self, density=6):
        self.y = np.round(np.random.rand(density), decimals=3)
        self.x = np.arange(len(self.y))
        self.ax.clear()
        self.ax.bar(self.x, self.y)
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
            round(self.screen_size.width() * 0.3),
            round(self.screen_size.height() * 0.24),
        )
        # Create Widgets
        self.main_layout = QtWidgets.QVBoxLayout()
        # self.graph = QtWidgets.QWidget(self)
        # self.graph.setStyleSheet("background-color:red")
        self.graph = Graph(self)
        # self.button = QtWidgets.QPushButton("Add", self)
        self.slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.setLayout(self.main_layout)
        self.main_layout.addWidget(self.graph)
        self.main_layout.addWidget(self.slider)

        self.slider.valueChanged.connect(self.graph.set_graph_density)
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
