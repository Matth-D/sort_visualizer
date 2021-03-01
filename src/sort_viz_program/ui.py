import sys

from PySide2 import QtCore, QtGui, QtWidgets


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
            round(self.screen_size.width() * 0.4),
            round(self.screen_size.height() * 0.5),
        )
        self.main_layout = QtWidgets.QVBoxLayout()
        self.array_viewer = QtWidgets.QWidget()
        self.array_length_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.layout_h1 = QtWidgets.QHBoxLayout(self.main_layout)
        self.layout_v1 = QtWidgets.QVBoxLayout()

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
