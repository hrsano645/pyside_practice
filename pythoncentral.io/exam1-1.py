# coding: utf-8
from __future__ import division, print_function, absolute_import, unicode_literals

__author__ = 'hiroshi'

# Allow access to command-line arguments
import sys

# Import the core and GUI elements of Qt
from PySide.QtCore import *
from PySide.QtGui import *


def main():
    # Every Qt application must have one and only one QApplication object;
    # it receives the command line arguments passed to the script, as they
    # can be used to customize the application's appearance and behavior
    qt_app = QApplication(sys.argv)

    # Create a widget
    widget = QWidget()
    widget.setMinimumSize(QSize(800, 600))
    widget.setWindowTitle('I Am A Window!')

    label2 = QLabel('日本語行ける？!', widget)
    label2.setAlignment(Qt.AlignCenter)
    # Show it as a standalone widget
    widget.show()

    # Run the application's event loop
    qt_app.exec_()


if __name__ == '__main__':
    main()


