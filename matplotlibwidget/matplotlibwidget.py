import matplotlib
import numpy as np
# Use a Qt-compatible backend
matplotlib.use('Qt5Agg') 
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, pyqtProperty, pyqtSignal

class MatplotlibWidget(QtWidgets.QWidget):
    # x-axis init
    _x_data = None

    def __init__(self, parent=None):
        super().__init__(parent)

        self._x_data = 0

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.axes = self.figure.add_subplot(111)
       
        self.toolbar = NavigationToolbar(self.canvas, self)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

    def plot(self, x_data, y_data):
        self.axes.clear()
        self.axes.plot(x_data, y_data)
        self.axes.set_ylabel('Some numbers')
        self.axes.set_title('Matplotlib Plot in PyDM')
        self.canvas.draw()

    def getXData(self):
        return self._x_data

    def setXData(self, value):
        self._x_data = value

    # Define the property using the Property decorator
    _x_data = pyqtProperty(int, getXData, setXData) 


# Make the widget runnable for testing
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    widget = MatplotlibWidget()
    widget.show()
    app.exec_()
