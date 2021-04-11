import sys

from PySide2 import QtCore, QtGui, QtWidgets
import matplotlib.backends.backend_qt5agg as beqt5agg
import matplotlib.pyplot as plt
import numpy as np

from . import core
from .algorithms import bubble_sort, heap_sort, insertion_sort, top_down_merge_sort


class ArrayGraph(beqt5agg.FigureCanvasQTAgg):
    """Class containing random array sorting display.

    Args:
        beqt5agg (object): Matplotlib backend.
    """

    def __init__(self, algorithm_value, default_density):
        """Class init.

        Args:
            algorithm_value (str): Selected algorithm name.
            default_density (int): Default graph X density.
        """
        self.fig, self.ax = plt.subplots(figsize=(1, 1), dpi=1, constrained_layout=True)
        plt.ioff()
        super(ArrayGraph, self).__init__(self.fig)
        self.algorithm_value = algorithm_value
        self.input_array = core.create_array_random(10)
        self.algorithm = None
        self.bars = None
        self.signals = None
        self.density = default_density
        self.current = None
        self.set_graph_density(self.density)
        self.set_algorithm(self.algorithm_value)

    def update_signal_source(self):
        """Update signal source when algorithm changed."""
        self.signals = self.algorithm.signals
        self.signals.signal_sort_array.connect(self.update_bars)
        self.signals.signal_current.connect(self.update_current)

    def set_graph_density(self, density):
        """Set graph X axis density.

        Args:
            density (int): Length of X data array.
        """
        self.input_array = core.create_array_random(density)
        x_data = self.input_array[:, 0]
        y_data = self.input_array[:, 1]
        self.ax.clear()
        self.bars = self.ax.bar(x_data, y_data, color="b")
        self.ax.axis("off")
        self.draw()
        self.update()

    @QtCore.Slot(np.ndarray)
    def update_bars(self, sort_array):
        """Update graph bars by changing the Y data.

        Args:
            sort_array (np.ndarray): Numpy array sent from algorithm module.
        """
        if not self.bars:
            return
        y_data = sort_array[:, 1]
        for i, elem in enumerate(self.bars):
            elem.set_height(y_data[i])
            # Update color of bar currently switched
            if i == self.current:
                elem.set_color("r")
            if i != self.current:
                elem.set_color("b")

        # Update GUI display by flushing any GUI events and redrawing canvas
        self.flush_events()
        self.draw()

    @QtCore.Slot(int)
    def update_current(self, x_data):
        """Signal method to update current bar variable/

        Args:
            x_data (int): Current bar's X position.
        """

        self.current = x_data

    def set_algorithm(self, value):
        """Set selected algorithm for sorting.

        Args:
            value (str): Selected algorithm name.
        """
        self.algorithm_value = value
        algorithm_arg = self.input_array
        if self.algorithm_value == "Top Down Merge Sort":
            self.algorithm = top_down_merge_sort.MergeSort(algorithm_arg)
        if self.algorithm_value == "Bubble Sort":
            self.algorithm = bubble_sort.BubbleSort(algorithm_arg)
        if self.algorithm_value == "Heap Sort":
            self.algorithm = heap_sort.HeapSort(algorithm_arg)
        if self.algorithm_value == "Insertion Sort":
            self.algorithm = insertion_sort.InsertionSort(algorithm_arg)

        self.update_signal_source()

    def solve_algorithm(self):
        """Solve currently represented array with selected algorithm."""
        self.algorithm.solve()


class SortVisualizer(QtWidgets.QDialog):
    """Main Class for Sort Visualizer program.

    Args:
        QtWidgets (obj): Inheriting Pyside2.QtWidgets.QDialog.
    """

    def __init__(self):
        """Sort Visualizer class init."""
        super(SortVisualizer, self).__init__()
        self.algorithms_list = [
            "Top Down Merge Sort",
            "Bubble Sort",
            "Heap Sort",
            "Insertion Sort",
            "Tim Sort",
        ]
        # self.algorithms_list = core.ALGORITHMS

        self.algorithm_value = self.algorithms_list[0]
        print(self.algorithm_value)
        self.algorithm = None
        self.init_ui()
        self.setGeometry(300, 300, self.app_size[0], self.app_size[1])
        self.setWindowTitle("Sort Visualizer")
        self.center_window()
        self.update_signal_source()

    def init_ui(self):
        """Init UI widgets and parameters."""
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
        self.array_length_label = QtWidgets.QLabel()
        self.iterations_label = QtWidgets.QLabel()
        self.time_complexity_label = QtWidgets.QLabel()
        self.space_complexity_label = QtWidgets.QLabel()

        self.set_array_length_label(default_density)
        self.set_time_complexity_label(self.array_graph.algorithm.time_complexity)
        self.set_space_complexity_label(self.array_graph.algorithm.space_complexity)
        self.set_iterations_label()

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
        self.density_slider.setMaximum(100)
        self.density_slider.setValue(default_density)

        # Signals
        # self.algorithm_list.currentTextChanged.connect(self.array_graph.set_algorithm)
        self.algorithm_list.currentTextChanged.connect(self.update_infos_on_change)
        self.sort_button.clicked.connect(self.array_graph.solve_algorithm)
        self.reset_button.clicked.connect(self.reset_graph)

        self.density_slider.valueChanged.connect(self.slider_changed)
        self.density_slider.sliderPressed.connect(self.slider_disconnect)
        self.density_slider.sliderReleased.connect(self.slider_reconnect)

    def update_infos_on_change(self):
        """Merge methods required to change infos labels on algorithm change"""
        self.reset_graph()
        self.set_time_complexity_label(self.array_graph.algorithm.time_complexity)
        self.set_space_complexity_label(self.array_graph.algorithm.space_complexity)

    def update_signal_source(self):
        """Update signal variable when algorithm is change and reconnect signals."""
        self.signals = self.array_graph.signals
        self.signals.signal_iterations.connect(self.set_iterations_label)

    @QtCore.Slot(int)
    def set_iterations_label(self, iteration=0):
        """Set value to iterations label."""
        self.iterations_label.setText("Iterations: {}".format(iteration))

    def set_array_length_label(self, array_length):
        """Set value to array length label."""
        self.array_length_label.setText("Array Length: {}".format(array_length))

    def set_time_complexity_label(self, time_complexity):
        """Set value to time complexity label."""
        self.time_complexity_label.setText(
            "Time Complexity: {}".format(time_complexity)
        )

    def set_space_complexity_label(self, space_complexity):
        """Set value to space complexity label."""
        self.space_complexity_label.setText(
            "Space Complexity: {}".format(space_complexity)
        )

    def slider_disconnect(self):
        """Disconnect slider signal when button is pressed."""
        self.sender().valueChanged.disconnect()

    def slider_reconnect(self):
        """Reconnect slider signal when button is released to"""
        """Graph isn't cooked at every slider scroll."""
        self.sender().valueChanged.connect(self.slider_changed)
        self.sender().valueChanged.emit(self.sender().value())

    def slider_changed(self, value):
        """Merge operations when slider button in released.

        Args:
            value (int): Slider value to feed graph X density.
        """
        if self.array_graph.algorithm.solving == 1:
            return
        self.array_graph.set_graph_density(value)
        self.array_graph.set_algorithm(self.algorithm_list.currentText())
        self.set_array_length_label(value)
        self.set_iterations_label()
        self.update_signal_source()
        self.signals.signal_iterations.connect(self.set_iterations_label)

    def reset_graph(self):
        """Reset graph array and infos."""
        if self.array_graph.algorithm.solving == 1:
            return
        self.array_graph.set_graph_density(self.density_slider.value())
        self.array_graph.set_algorithm(self.algorithm_list.currentText())
        self.update_signal_source()
        self.set_iterations_label()

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
