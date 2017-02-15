# coding: utf-8

from PyQt5 import QtWidgets, QtCore, QtGui, QtPrintSupport
from Diagnost import Diagnost




if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Diagnost()
    window.setWindowTitle('Диагност 1.0')
    window.setWindowOpacity(0.95)  # Задали небольшую прозрачность главного экрана
    pal = window.palette()
    pal.setColor(QtGui.QPalette.Normal, QtGui.QPalette.Window,
                 QtGui.QColor("#98FF98"))  # задали background-color (Зеленая мята)
    window.setPalette(pal)
    window.resize(913, 722)
    window.show()
    sys.exit(app.exec_())
